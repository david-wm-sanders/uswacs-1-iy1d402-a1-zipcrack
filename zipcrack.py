import sys
import zipfile
from pathlib import Path

wrd_fp = Path(__file__).parent / Path("dictionary.txt")
zip_fp = Path(__file__).parent / Path("locked.zip")

def read_word_list(wrd_fp):
    pws = []
    with wrd_fp.open("rb") as f:
        for pw in f.read().split(b"\n"):
            pws.append(pw)
    return pws

def crack_zip(zip_fp, word_list):
    with zipfile.ZipFile(zip_fp) as z:
        for pw in pws:
            try:
                z.extractall(path="extracted", pwd=pw)
                print(f"The password is '{pw}' - writing file to disk...")
                break
            except RuntimeError:
                print(f"The password is not '{pw}'")
                continue

if __name__ == '__main__':
    pws = read_word_list(wrd_fp)
    print("Wordlist:", pws)
    crack_zip(zip_fp, pws)
