import os
import argparse
import pdfkit

from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(prog='HtmlToPdf', description='Convert HTML files to PDF')
parser.add_argument('-I', '--input', nargs='*', type=str, help='path to html file')
parser.add_argument('-O', '--output', nargs='*', type=str, help='path to pdf file')
parser = parser.parse_args()

try:
    with open(parser.input[0], encoding='utf8') as f:
        data = f.read()

    if '<meta charset="utf-8">' not in data:
        with open(parser.input[0], 'w', encoding='utf8') as f:
            f.write(data[:data.find('<head>') + 6] + '<meta charset="utf-8">' + data[data.find('<head>') + 6:])
    pdfkit.from_file(parser.input[0], parser.output[0],
                     configuration=pdfkit.configuration(wkhtmltopdf=os.getenv('path_to_wkhtmltopdf')))
except TypeError:
    print('Enter the path\n\nTo learn more, enter tag -h\n')
except FileNotFoundError:
    print('Enter the correct path\n\nTo learn more, enter tag -h\n')
