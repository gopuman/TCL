import pandas as pd

file = "AIR_RATE.xlsx"

df1 = pd.read_excel(file,header=[0,1])

def getRateCardAIR(i):
    print("="*80)
