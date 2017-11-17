import sys
import zipfile
from pathlib import Path

wrd_fp = Path(__file__).parent / Path("dictionary.txt")
zip_fp = Path(__file__).parent / Path("locked.zip")
file_n = "picture.jpg"

pws = []
with wrd_fp.open("rb") as f:
    for pw in f.read().split(b"\n"):
        pws.append(pw)

print("Wordlist:", pws)

with zipfile.ZipFile(zip_fp) as z:
    for pw in pws:
        try:
            with z.open(file_n, pwd=pw) as zc:
                of = Path(__file__).parent / Path(f"{file_n}")
                with of.open("wb") as f:
                    print(f"The password is '{pw}' - writing file to disk...")
                    f.write(zc.read())
                break
        except RuntimeError:
            print(f"The password is not '{pw}'")
            continue
