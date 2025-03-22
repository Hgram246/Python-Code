import pandas as pd

df = pd.read_excel('/Users/henryg/Documents/Business_Spreadsheets/KorCompList.xlsx')

filterdf = df[(df["분류"] == "화장품 제조업")]

filterdf.to_excel("/Users/henryg/Documents/Business_Spreadsheets/KorCompListFilteredCosmeticsMan.xlsx")

print("done")