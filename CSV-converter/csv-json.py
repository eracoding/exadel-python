import re

from CSVClass import CsvFile
from JSONClass import JsonFile


def main():
    filename = str(input("Enter File Name: "))
    outputFileName = str(input("Enter Desired FileName Output: "))
    if re.search(r'[^A-Za-z0-9_\-\\]', outputFileName):
        raise SystemExit("Invalid File Output Name: Terminating...")

    if filename.find('json') != -1:
        json_file = JsonFile(filename, outputFileName)
        print(json_file)
    elif filename.find('csv') != -1:
        csv = CsvFile(filename, outputFileName)
        print(csv)
    else:
        raise SystemExit("Invalid File Name: Please, specify the File Type (.json, .csv)")


if __name__ == "__main__":
    main()
