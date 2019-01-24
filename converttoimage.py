import argparse
import win32clipboard
from binascii import a2b_base64


def converttoimage(filepath):
    # get clipboard data - ref: https://stackoverflow.com/a/101167
    print('Job started')
    print('Get clipboard data ...')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    print('length of data is: %s'%len(data))
    if data == '' or len(data) < 100:
        print('Error: data is empty or very low')
        return

    print('The first 100 character of the clipboard data is: ')
    print(data[0:100])

    ans = input('\r\nAceepted? [y/n] ')

    if ans == 'y':
        # convert to just base64 part
        data = data.replace('data:image/png;base64,', '')

        # convert to a png file
        binary_data = a2b_base64(data)

        print('generating image...')
        fd = open('%s.png'%filepath, 'wb')
        fd.write(binary_data)
        fd.close()

        print('image generated successfully.')
        print('Clearing clipboard data...')
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        print('All things are processed successfully')

    else:
        print('Exiting...')


parser = argparse.ArgumentParser("converttoimage")
parser.add_argument("filepath", help="file path to save the clipboard data as an png file.")
args = parser.parse_args()

converttoimage(args.filepath)
