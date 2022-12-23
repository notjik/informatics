import os
import sys
import argparse

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

parser = argparse.ArgumentParser(prog='HtmlToPdf', description='Convert HTML files to PDF')
parser.add_argument('-I', '--input', nargs='*', type=str, help='path or url to html file', required=True)
parser.add_argument('-O', '--output', nargs='*', type=str, help='path to pdf file', required=False)
parser.add_argument('-M', '--mode', help='local file or url', choices=['local', 'L', 'url', 'U'], required=True)


def html_to_pdf(html: str, pdf: str, mode:str):
    app = QtWidgets.QApplication(sys.argv)
    page = QtWebEngineWidgets.QWebEnginePage()

    def handle_print_finished(filename, status):
        print("\033[32mSuccessfully converted to «{}»!\033[0m".format(filename))
        QtWidgets.QApplication.quit()

    def handle_load_finished(status):
        if status:
            page.printToPdf(pdf)
        else:
            print("\033[31mFailed!\033[0m")
            QtWidgets.QApplication.quit()

    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    if mode in ['local', 'L']:
        page.load(QtCore.QUrl.fromLocalFile(html))
    else:
        page.load(QtCore.QUrl.fromUserInput(html))
    app.exec_()


if __name__ == "__main__":
    parser = parser.parse_args()
    if parser.mode in ['local', 'L']:
        dir = os.path.abspath(os.curdir)
        html = os.path.join(dir, ' '.join(parser.input))
        isdir = True
    else:
        html = ' '.join(parser.input)
        isdir = False
    print('\033[34mConverting from «{}» to PDF.\n\033[0m'.format(html))
    if parser.output:
        pdf = ' '.join(parser.output)
    else:
        if isdir:
            pdf = os.path.splitext(html)[0] + '.pdf'
        else:
            pdf = html.rsplit('/', 1)[-1] + '.pdf'
    html_to_pdf(html, pdf, mode=parser.mode)
