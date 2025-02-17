from gemini_client import GeminiClient
from utils import setup_logger, save_to_markdown
import os

logger = setup_logger()

def process_pdf(pdf_path: str, api_key: str) -> str:
    """Process PDF file using Gemini API for OCR and return markdown text"""
    try:
        client = GeminiClient(api_key)

        # Simple prompt that lets Gemini handle formatting naturally
        prompt = """Convert this PDF to markdown format. Please:
1. Preserve all LaTeX equations exactly as they appear
2. Keep tables properly formatted with markdown table syntax
3. Maintain proper question numbering and indentation
4. Format options with proper line breaks between them
5. Preserve the original document structure"""

        # Get OCR text from Gemini
        ocr_text = client.get_ocr_text(pdf_path, prompt)
        if not ocr_text:
            raise Exception("Failed to extract text from PDF")

        # Save the extracted text
        output_file = f"{os.path.splitext(pdf_path)[0]}_ocred.md"
        save_to_markdown(output_file, ocr_text)

        return output_file

    except Exception as e:
        logger.error(f"Error processing PDF: {str(e)}")
        raise