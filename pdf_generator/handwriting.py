import os
from fpdf import FPDF

def generate_pdf(text, handwriting_style):
    # Create 'output' directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(handwriting_style, size=12)
    pdf.multi_cell(0, 10, text)
    
    output_path = "output/handwritten_text.pdf"
    pdf.output(output_path)
    return output_path
