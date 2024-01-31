from fpdf import FPDF
import pandas as pd
from pathlib import Path
import glob
import pyarrow

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    animal_name = filename.title()

    # Set the header
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=animal_name, ln=1)

    # Set the text
    ######################

# Produce the PFD
pdf.output("output.pdf")
