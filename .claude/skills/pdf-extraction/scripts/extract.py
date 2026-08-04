#!/usr/bin/env python3
"""
PDF extraction helper for VaultDiligence pdf-extraction skill.
Requires: pip install pdfplumber --break-system-packages

Usage:
  python3 extract.py path/to/audit.pdf
  python3 extract.py path/to/audit.pdf --pages 1-10
"""
import sys
import os

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Run: pip install pdfplumber --break-system-packages")
    sys.exit(1)

def extract_pdf(path, page_range=None):
    with pdfplumber.open(path) as pdf:
        pages = pdf.pages
        if page_range:
            start, end = page_range
            pages = pages[start-1:end]

        for i, page in enumerate(pages):
            page_num = (page_range[0] + i) if page_range else (i + 1)
            text = page.extract_text()
            if text:
                print(f"\n--- Page {page_num} ---")
                print(text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 extract.py <pdf_path> [--pages START-END]")
        sys.exit(1)

    path = sys.argv[1]
    page_range = None

    if '--pages' in sys.argv:
        idx = sys.argv.index('--pages')
        parts = sys.argv[idx + 1].split('-')
        page_range = (int(parts[0]), int(parts[1]))

    extract_pdf(path, page_range)
