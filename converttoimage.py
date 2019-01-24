import argparse
import win32clipboard
from binascii import a2b_base64


def converttoimage(filepath):
    # get clipboard data - ref: https://stackoverflow.com/a/101167
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if data == '':
        print('Error: data is empty')

    # convert to just base64 part
    data = data.replace('data:image/png;base64,', '')

    # convert to a png file
    binary_data = a2b_base64(data)

    fd = open('%s.png'%filepath, 'wb')
    fd.write(binary_data)
    fd.close()


parser = argparse.ArgumentParser("converttoimage")
parser.add_argument("filepath", help="file path to save the clipboard data as an png file.")
args = parser.parse_args()

converttoimage(args.filepath)
