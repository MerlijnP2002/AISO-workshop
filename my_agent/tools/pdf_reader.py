import pathlib

import fitz  # PyMuPDF

TEST_PDF = pathlib.Path("benchmark/attachments/7.pdf")


def read_pdf(file_path: str) -> str:
    """Extract and return all text from a PDF file, page by page.
    Use this whenever a question refers to an attached PDF file.
    """
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        return f"Error: could not open PDF '{file_path}': {e}"

    pages_text = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            pages_text.append(f"--- Page {page_num} ---\n{text.strip()}")

    doc.close()

    if not pages_text:
        return f"Error: no text could be extracted from '{file_path}'. The PDF may be image-only."

    return "\n\n".join(pages_text)

