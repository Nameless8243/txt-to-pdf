from fpdf import FPDF
import pandas as pd
from pathlib import Path
import glob
import pyarrow

pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("texts/*.txt")

for filepath in filepaths:
    df = pd.read_fwf(filepath)
    print(filepath)                                  #

    pdf.add_page()
    filename = Path(filepath).stem
    animal_name = filename.split("-")[0]
    print(animal_name)                              #

    # Set the header

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=animal_name, align="L", ln=1)

    # Set the text



pdf.output("output.pdf")
