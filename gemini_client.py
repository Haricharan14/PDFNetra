import google.generativeai as genai
import time
from random import uniform
from typing import Optional

class GeminiClient:
    def __init__(self, api_key: str, max_retries: int = 3):
        self.api_key = api_key
        self.max_retries = max_retries
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')

    def get_ocr_text(self, pdf_path: str, prompt: str) -> Optional[str]:
        """
        Send PDF to Gemini API for OCR processing
        Returns:
            str: The extracted text if successful
            None: If the API response is invalid
        """
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                # Read PDF file
                with open(pdf_path, 'rb') as f:
                    pdf_content = f.read()

                # Generate content
                response = self.model.generate_content([
                    prompt,
                    {"mime_type": "application/pdf", "data": pdf_content}
                ], generation_config={
                    "temperature": 0.1,
                    "top_p": 1,
                    "top_k": 32
                })

                # Extract text from response
                if response and hasattr(response, 'text'):
                    return response.text.strip()
                return None

            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "quota" in error_msg.lower() or "resource exhausted" in error_msg.lower():
                    retry_count += 1
                    if retry_count >= self.max_retries:
                        raise Exception("API quota exceeded. Please try again later.")
                    # Exponential backoff with jitter
                    wait_time = (2 ** retry_count) + uniform(0, 1)
                    time.sleep(wait_time)
                    continue
                elif "payload too large" in error_msg.lower():
                    raise Exception("PDF file is too large for direct processing")
                elif "bad credentials" in error_msg.lower():
                    raise Exception("Invalid API key or authentication error")
                else:
                    raise Exception(f"Gemini API error: {error_msg}")