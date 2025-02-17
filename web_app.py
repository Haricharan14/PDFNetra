from flask import Flask, render_template, request, jsonify, send_file
import os
from pdf_ocr import process_pdf
from utils import setup_logger
import markdown
import io

app = Flask(__name__)
logger = setup_logger()

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Please upload a PDF file'}), 400

    try:
        # Save uploaded file
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Process PDF using existing OCR function
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            return jsonify({'error': 'API key not configured'}), 500

        process_pdf(filepath, api_key)

        # Read the output file
        output_file = f"{os.path.splitext(filepath)[0]}_ocred.md"
        with open(output_file, 'r', encoding='utf-8') as f:
            output_text = f.read()

        # Store the output text in session for downloads
        original_filename = os.path.splitext(file.filename)[0]

        return render_template('index.html', 
                             output_text=output_text,
                             filename=original_filename)

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(output_file):
            os.remove(output_file)

@app.route('/download/<filename>/<format>')
def download_file(filename, format):
    if not filename or 'output_text' not in request.args:
        return jsonify({'error': 'No content available'}), 400

    content = request.args.get('output_text')

    if format == 'md':
        output = content
        mime_type = 'text/markdown'
        ext = '.md'
    elif format == 'txt':
        # Convert markdown to plain text by removing markdown syntax
        output = content.replace('#', '').replace('*', '')
        mime_type = 'text/plain'
        ext = '.txt'
    elif format == 'pdf':
        # For PDF, we'll return markdown for now
        # TODO: Add PDF conversion
        output = content
        mime_type = 'text/markdown'
        ext = '.md'
    else:
        return jsonify({'error': 'Invalid format'}), 400

    # Create in-memory file
    buffer = io.BytesIO()
    buffer.write(output.encode('utf-8'))
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype=mime_type,
        as_attachment=True,
        download_name=f"{filename}{ext}"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)