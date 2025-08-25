import pandas as pd

df = pd.read_excel("C:\\Source.xlsx", engine="openpyxl") #open excel from source to read, You need to paste Your source!

def gender(name):
    if isinstance(name, str):
        if name == ["Kuba", "Barnaba", "Dyzma"]:
            return "M"
        elif name.endswith("a"):
            return "K"
        else:
            return "M"
    return ""

df["gender"] = df.iloc[:, 0].apply(gender)

df.to_excel("C:\\Source.xlsx", index=False)
print("Done")
