from pypdf import PdfReader

def extract_text_from_pdf_pypdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Example usage
pdf_file_path = "./pdf/test.pdf"  # Replace with your PDF file path
extracted_text = extract_text_from_pdf_pypdf(pdf_file_path)
print(extracted_text)