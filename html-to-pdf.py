import os
import sys
import argparse

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

parser = argparse.ArgumentParser(prog='HtmlToPdf', description='Convert HTML files to PDF')
parser.add_argument('-I', '--input', nargs='*', type=str, help='path or url to html file', required=True)
parser.add_argument('-M', '--mode', help='local file or url', choices=['local', 'url'], required=True)


def html_to_pdf(html: str, pdf: str, mode: str):
    app = QtWidgets.QApplication(sys.argv)
    page = QtWebEngineWidgets.QWebEnginePage()
    print("\033[34m" + "\033[1m" + "Converting from «{}» to PDF.\n".format(html) + "\033[0m" + "\033[2m")

    def handle_print_finished(filename, status):
        print(
            "\033[0m" + "\033[1m" + "\033[32m" + "\nSuccessfully converted to «{}»!\n\n\n".format(filename) + "\033[0m")
        app.quit()

    def handle_load_finished(status):
        if status:
            page.printToPdf(pdf)
        else:
            print("\033[31m" + "\033[1m" + "Failed!\n\n\n" + "\033[0m")
            QtWidgets.QApplication.quit()

    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    if mode == 'local':
        page.load(QtCore.QUrl.fromLocalFile(html))
    else:
        page.load(QtCore.QUrl.fromUserInput(html))
    app.exec_()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    parser = parser.parse_args()
    if parser.mode == 'local':
        dir = os.path.abspath(os.curdir)
        html = os.path.join(dir, ' '.join(parser.input).replace('/', '\\'))
        isdir = True
        if html[-1] == '\\':
            pull_html = [os.path.join(walk[0], file) for walk in os.walk(html)
                         for file in walk[2] if file.endswith('.html')]
        else:
            pull_html = [html]
    else:
        html = ' '.join(parser.input)
        isdir = False
        pull_html = [html]
    for doc in pull_html:
        if isdir:
            html_to_pdf(doc, os.path.splitext(doc)[0] + '.pdf', mode=parser.mode)
        else:
            html_to_pdf(doc, doc.rsplit('/', 1)[-1] + '.pdf', mode=parser.mode)
