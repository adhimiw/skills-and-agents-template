---
name: ebook-treasure-chest
description: >-
  Production-grade digital library and academic repository management. Covers dual-server deployment (Calibre-web and Kavita), OPDS feed configuration for e-readers, automated PDF/EPUB educational study material classification, metadata scraping from ISBN/Crossref/arXiv, deduplication, format normalization, and headless ingest pipelines. Triggers: 'calibre', 'calibre-web', 'kavita', 'opds', 'ebook library', 'digital library', 'epub classification', 'study materials', 'book deduplication', 'academic papers', 'ebook-treasure-chest'.
---

# E-Book Treasure Chest & Digital Study Library

Production blueprint for managing self-hosted digital book repositories, educational courseware, and research literature. Unifies Calibre-Web (metadata-rich cataloging and format conversion) and Kavita (high-speed reader for technical docs, comics, and PDFs) with automated ingestion and OPDS synchronization.

## Triggers & Activation Matrix

Activate this skill when:
- Deploying or configuring self-hosted digital library software (Calibre-Web, Kavita, Calibre headless).
- Designing a classification taxonomy for educational materials, textbooks, lecture slides, and papers.
- Building automated ingest pipelines: scraping ISBNs, DOIs, arXiv IDs, and Google Books metadata.
- Detecting duplicate books, normalizing formats (PDF $\leftrightarrow$ EPUB), and repairing corrupted e-books.
- Setting up OPDS catalogs for KOReader, Kobo e-readers, Moon+ Reader, or mobile apps.
- Troubleshooting SQLite database locks, missing covers, or ingestion failures.

---

## 1. System Architecture

```
[ New Books / Lecture Notes / Papers ]
                 │
                 ▼
     ┌────────────────────────┐
     │  Watch Folder / Ingest │
     └───────────┬────────────┘
                 │ Automated Ingestion Script
                 ▼
  ┌────────────────────────────────────────────────────────┐
  │ Pipeline: Deduplication (SHA-256 & Fuzzy)              │
  │           Text/Metadata Scraping (ISBN, Crossref, arXiv)│
  │           Custom Taxonomical Tagging                   │
  │           Format Validation (qpdf, epubcheck)          │
  └──────────────┬──────────────────────────┬──────────────┘
                 │ calibredb add            │ Direct File Link
                 ▼                          ▼
     ┌───────────────────────┐  ┌───────────────────────┐
     │      Calibre-Web      │  │        Kavita         │
     │ (Books, Papers, EPUB) │  │(Comics, Docs, Slides) │
     └───────────┬───────────┘  └───────────┬───────────┘
                 │                          │
                 └───────────┬──────────────┘
                             │ OPDS v1.2 / v2 Feeds
                             ▼
     [ E-Readers: KOReader / Kobo / Moon+ Reader / Tablets ]
```

---

## 2. Docker Compose Deployment

This stack provisions Calibre-Web, Kavita, and an automated headless Calibre ingestion engine sharing a unified library volume.

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  # Calibre headless backend for CLI tools (calibredb, ebook-convert)
  calibre-server:
    image: lscr.io/linuxserver/calibre:latest
    container_name: calibre-core
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /mnt/storage/ebooks/config/calibre:/config
      - /mnt/storage/ebooks/library:/books
      - /mnt/storage/ebooks/ingest:/ingest
    restart: unless-stopped

  # Calibre-Web: Sleek Web UI, metadata editor, and OPDS server
  calibre-web:
    image: lscr.io/linuxserver/calibre-web:latest
    container_name: calibre-web
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - DOCKER_MODS=linuxserver/mods:universal-calibre # Enables ebook-convert inside container
    volumes:
      - /mnt/storage/ebooks/config/calibre-web:/config
      - /mnt/storage/ebooks/library:/books
    ports:
      - "8083:8083"
    depends_on:
      - calibre-server
    restart: unless-stopped

  # Kavita: Lightning-fast reader for manga, comics, and fast PDF rendering
  kavita:
    image: jvmilazz0/kavita:latest
    container_name: kavita
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /mnt/storage/ebooks/config/kavita:/kavita/config
      - /mnt/storage/ebooks/library:/data/books:ro # Read-only access to Calibre library
      - /mnt/storage/ebooks/study_materials:/data/study:ro
    ports:
      - "5000:5000"
    restart: unless-stopped
```

---

## 3. Academic & Educational Material Taxonomy

Educational material requires deeper taxonomy than standard fiction/non-fiction. Implement the following custom columns and tag structures in Calibre:

### Directory & Classification Structure
```
/mnt/storage/ebooks/study_materials/
├── Computer_Science/
│   ├── CS106_Algorithms/
│   │   ├── Textbooks/       # Primary course references
│   │   ├── Lectures/        # Slide decks and transcribed notes
│   │   ├── Problem_Sets/    # Exercises, exams, and answer keys
│   │   └── Research_Papers/ # Foundational reading
│   └── CS224_Deep_Learning/
└── Mathematics/
    ├── Linear_Algebra/
    └── Probability_Statistics/
```

### Calibre Custom Columns Schema
Run inside `calibre-core` or via `calibredb`:

```bash
# Add custom column for academic course code (e.g., CS101, MATH201)
docker exec calibre-core calibredb custom_columns add course "Course Code" string --library-path /books

# Add custom column for material type (Textbook, Lecture, Slides, Exam, Paper)
docker exec calibre-core calibredb custom_columns add material_type "Material Type" enumeration \
  --enum-values "Textbook,Lecture,Slides,Paper,Notes,CheatSheet" --library-path /books

# Add custom column for academic term/semester
docker exec calibre-core calibredb custom_columns add term "Term/Year" string --library-path /books
```

---

## 4. Automated Metadata Scraping & Ingestion Pipeline

The following Python script automates file inspection, extracts ISBN/DOI/arXiv identifiers from the first 3 pages of PDFs, fetches authoritative metadata, and registers the file into Calibre without duplicates.

### `ingest_pipeline.py`

```python
#!/usr/bin/env python3
"""
Automated E-Book & Study Material Ingestion Engine
Extracts identifiers (ISBN, DOI, arXiv), scrapes metadata, and imports to Calibre.
"""

import os
import re
import sys
import json
import hashlib
import subprocess
import urllib.request
from pathlib import Path
from pypdf import PdfReader

LIBRARY_PATH = "/books"
INGEST_DIR = "/ingest"

def compute_sha256(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def extract_identifiers_from_pdf(filepath):
    """Scan first 3 pages of PDF for ISBN, DOI, and arXiv identifiers."""
    identifiers = {"isbn": None, "doi": None, "arxiv": None}
    try:
        reader = PdfReader(filepath)
        sample_text = ""
        for i in range(min(3, len(reader.pages))):
            sample_text += (reader.pages[i].extract_text() or "") + "\n"
        
        # ISBN Regex (ISBN-10 and ISBN-13)
        isbn_match = re.search(r'(?:ISBN(?:-1[03])?:?\s*)?(?=[-0-9 ]{13}|[-0-9X ]{10})(?:97[89][-\s]?)?[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9X]', sample_text)
        if isbn_match:
            clean_isbn = re.sub(r'[^0-9X]', '', isbn_match.group(0))
            if len(clean_isbn) in (10, 13):
                identifiers["isbn"] = clean_isbn

        # DOI Regex
        doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', sample_text)
        if doi_match:
            identifiers["doi"] = doi_match.group(0).rstrip('.')

        # arXiv Regex
        arxiv_match = re.search(r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)', sample_text)
        if arxiv_match:
            identifiers["arxiv"] = arxiv_match.group(1)

    except Exception as e:
        print(f"Warning: Failed to extract text from {filepath}: {e}")
    return identifiers

def fetch_isbn_metadata(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "EbookIngestBot/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            key = f"ISBN:{isbn}"
            if key in data:
                b = data[key]
                return {
                    "title": b.get("title"),
                    "authors": [a.get("name") for a in b.get("authors", [])],
                    "publisher": b.get("publishers", [{}])[0].get("name") if b.get("publishers") else None,
                    "published_date": b.get("publish_date"),
                }
    except Exception as err:
        print(f"Metadata lookup failed for ISBN {isbn}: {err}")
    return None

def import_to_calibre(filepath, meta=None):
    cmd = ["calibredb", "add", filepath, "--library-path", LIBRARY_PATH]
    if meta and meta.get("title"):
        cmd.extend(["--title", meta["title"]])
    if meta and meta.get("authors"):
        cmd.extend(["--authors", ", ".join(meta["authors"])])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully added: {filepath}")
        return True
    else:
        print(f"Calibre error on {filepath}: {result.stderr}")
        return False

def process_ingest_directory():
    ingest_path = Path(INGEST_DIR)
    for file in ingest_path.glob("**/*"):
        if file.suffix.lower() in [".pdf", ".epub", ".mobi"]:
            print(f"Processing: {file.name}")
            identifiers = {}
            if file.suffix.lower() == ".pdf":
                identifiers = extract_identifiers_from_pdf(file)
            
            meta = None
            if identifiers.get("isbn"):
                print(f"Found ISBN: {identifiers['isbn']}, fetching metadata...")
                meta = fetch_isbn_metadata(identifiers["isbn"])

            success = import_to_calibre(str(file), meta)
            if success:
                # Move to archive or delete original
                file.unlink()

if __name__ == "__main__":
    process_ingest_directory()
```

---

## 5. Deduplication & Format Normalization

### Content-Based Deduplication (SHA-256 & Fuzzy Title)
Run this check to find identical files stored under different names:

```bash
# 1. Identify identical file hashes in library
find /mnt/storage/ebooks/library -type f \( -name "*.epub" -o -name "*.pdf" \) -exec sha256sum {} + \
  | sort | uniq -w64 -dD
```

### PDF & EPUB Sanitization and Repair
Corrupt files break e-readers and crash Kavita scanners. Sanitize before importing:

```bash
# Linearize and repair broken PDF cross-reference tables
qpdf --linearize --replace-input input_broken.pdf

# Check and validate EPUB conformity
epubcheck book.epub

# Convert scanned/unreadable PDF to clean, reflowable EPUB
ebook-convert source_text.pdf output.epub \
  --enable-heuristics \
  --remove-paragraph-spacing-indent-size 1.5 \
  --smarten-punctuation
```

---

## 6. OPDS Feeds & E-Reader Client Integration

Both Calibre-Web and Kavita expose OPDS catalogs, enabling direct over-the-air browsing and downloading on devices like Kobo, Kindle, and Android/iOS readers.

### Endpoints
- **Calibre-Web OPDS URL**: `http://<server-ip>:8083/opds`
- **Calibre-Web Kobo Sync URL**: `http://<server-ip>:8083/kobo/<api-token>`
- **Kavita OPDS URL**: `http://<server-ip>:5000/api/opds/<user-api-key>`

### Client Configuration Guide
1. **KOReader (Kindle / Kobo / Android)**:
   - Go to **Search** $\rightarrow$ **OPDS Catalog** $\rightarrow$ **Add New Catalog**.
   - Set Name: `Homelab Calibre-Web`.
   - Set URL: `http://192.168.1.50:8083/opds`.
   - Enter HTTP Basic Auth username & password configured in Calibre-Web.
2. **Kobo Native Sync (Calibre-Web)**:
   - In Calibre-Web $\rightarrow$ Edit User $\rightarrow$ Check **Enable Kobo Sync**.
   - Copy the unique sync token.
   - On the Kobo device, edit `Kobo eReader.conf` under `[ApplicationPreferences]` and set:
     ```ini
     api_endpoint=http://192.168.1.50:8083/kobo/<token>
     ```

---

## 7. Error Recovery & Diagnostics Matrix

| Issue / Error | Root Cause | Diagnosis Command | Remediation |
|---|---|---|---|
| `sqlite3.OperationalError: database is locked` | Concurrent writes from `calibredb add` and `calibre-web` | `fuser /mnt/storage/ebooks/library/metadata.db` | 1. Ensure `calibre-web` background metadata writing is set to read-only during bulk batch CLI imports.<br>2. Run `sqlite3 metadata.db "PRAGMA journal_mode=WAL;"` to enable Write-Ahead Logging. |
| Kavita library scan hangs indefinitely | Malformed PDF with deep circular object streams or huge archives | Inspect Kavita container logs: `docker logs kavita --tail 200` | 1. Isolate the offending file reported in logs.<br>2. Repair with `qpdf --check problematic.pdf`.<br>3. Exclude non-book files (e.g., zip files containing nested zips). |
| EPUB missing cover in Calibre-Web | Missing cover image manifest entry in EPUB `content.opf` | `ebook-meta book.epub` | Run `ebook-meta book.epub --cover cover.jpg` to inject cover or regenerate using `ebook-convert`. |
| OPDS returns `401 Unauthorized` in KOReader | Password encryption mismatch or reverse proxy stripping Auth header | Check Nginx / Caddy reverse proxy headers | Ensure reverse proxy passes auth: `proxy_set_header Authorization $http_authorization;`. |
| Calibre metadata database corruption | Sudden power loss or unclean shutdown | `sqlite3 /books/metadata.db "PRAGMA integrity_check;"` | Restore from automatic backup: `calibredb restore_database --really-do-it --library-path /books`. |

---

## 8. Maintenance & Verification

```bash
# Check SQLite library integrity
sqlite3 /mnt/storage/ebooks/library/metadata.db "PRAGMA integrity_check;"

# Optimize and vacuum Calibre database
sqlite3 /mnt/storage/ebooks/library/metadata.db "VACUUM; ANALYZE;"

# Count total books and distinct formats
docker exec calibre-core calibredb list --library-path /books --fields title,authors,formats
```
