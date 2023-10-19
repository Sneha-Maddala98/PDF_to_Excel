# PDF to Excel Conversion Program

This Python program leverages the Tabula library to convert tables from a PDF file into Excel format. It's a straightforward tool that allows you to quickly and easily extract tabular data from PDF documents and save it as Excel files.

## Prerequisites

Before running the program, make sure you have the following prerequisites:

- Python

- Tabula-Py

## Usage
. The program will prompt you to enter the path of the PDF file you want to convert. Please provide the full path to the PDF file.

. The program will analyze the PDF and check for tables on all pages. If tables are found, it will convert them into Excel files. The resulting Excel files will be saved in the same directory as the PDF.

. If no tables are found, the program will inform you that no tables were detected.

## Example

Suppose you have a PDF file named `example.pdf`. To convert it to Excel, run the program and provide the full path to the PDF file:

```plaintext
Please enter the path of your PDF file: /path/to/your/example.pdf
```

The program will generate Excel files with the table(s) it finds in the PDF.

