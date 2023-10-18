PDF to Excel Converter
This Python program allows you to convert tables from a PDF file into separate Excel files.

Requirements
Python 3.x
Required Python libraries: tabula-py, pandas
Install the necessary libraries using the following command:

bash
Copy code
pip install tabula-py pandas
Usage
Clone this repository to your local machine:
bash
Copy code
git clone 
Navigate to the project directory:
bash
Copy code
cd pdf-to-excel-converter
Run the program:
bash
Copy code
python PDF_to_Excel.py
When prompted, provide the path to the PDF file you want to convert.
Notes
If no tables are found in the PDF, the program will indicate so.

The extracted tables will be saved as separate Excel files, each named output_0.xlsx, output_1.xlsx, and so on.

