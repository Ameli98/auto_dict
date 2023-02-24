from pathlib import Path
import csv

class auto_dict():
    def __init__(self, text_file:Path, WebDict_File:Path="EN_DefaultDict.csv") -> None:
        # text_file : txt file with target words which is split with "/n"
        # WebDict_File : csv file with root path of the website dictionary which is split with "/n"
        # e.g. For apple in Cambridge dictionary : https://dictionary.cambridge.org/dictionary/english-chinese-traditional/apple
        # Use https://dictionary.cambridge.org/dictionary/english-chinese-traditional/ as root path in your file
        self.wordset = self.get_word(text_file)
        self.dictname, self.dictroot = self.get_dict(WebDict_File)
        self.result_file = Path(f"{text_file.stem}.html")
        self.write_result()
        print(self.dictname, self.dictroot)

    # Get words in the txt file
    def get_word(self, text_file:Path) -> list:
        with open(text_file, "r") as tf:
            content = tf.read()
        return content.split("\n")

    # Get dictionaries in the csv file
    def get_dict(self, csv_file:Path) -> tuple:
        with open(csv_file, "r") as df:
            reader = csv.DictReader(df)
            dictname, dictroot = [], []
            for row in reader:
                dictname.append(row["dictname"])
                dictroot.append(row["dictroot"])
        return dictname, dictroot


    # Assemble result
    def write_result(self) -> None:
        result_file = Path()
        with open(self.result_file, "w") as rf:
            html_begin = ["<!DOCTYPE html>\n", "<html>\n", "  <head>\n", f"    <title>{self.result_file.stem}</title>\n", "  </head>\n", "  <body>\n"]
            rf.writelines(html_begin)
            for word in self.wordset:
                rf.write(f"  <h1>{word}</h1>\n  <p>")
                for dictname, dictroot in list(zip(self.dictname, self.dictroot)):
                    rf.write(f"<a href={dictroot+word}>{dictname}</a> ")
                rf.write("</p>\n")
            html_end = ["  </body>\n", "</html>"]
            rf.writelines(html_end)

if __name__ == "__main__":
    from sys import argv
    try:
        text_file, WebDict_File = Path(argv[1]), Path(argv[2])
        Dictionary = auto_dict(text_file, WebDict_File)
    except IndexError:
        print("Except a target txt file and a dictionary csv file")
        print("try: Python3 auto_dict.py <target txt> <dictionary csv>")