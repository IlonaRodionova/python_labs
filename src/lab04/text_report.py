from lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    txt = tokenize(normalize(read_text("data/input.txt")))
    a = [("word",len(txt))]
    for el in top_n(count_freq(txt)):
        a.append((el[0],el[1]))
    write_csv(a, "data/report.csv")

if __name__ == "__main__":
    main()
