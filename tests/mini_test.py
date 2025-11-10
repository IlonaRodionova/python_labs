from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("../data/input.txt")
print(txt)
write_csv([("word","count"),("test",5)], "../data/check.csv")