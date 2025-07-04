import fitz

def extract_text_from_pdf(pdf_path, max_pages=5):
    doc = fitz.open(pdf_path)  # OPEN FROM PATH
    text = ""
    for page_num in range(min(len(doc), max_pages)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text
