import pandas as pd

file = "/Users/gopuman/Documents/TCL_backend/LCL_RATE.xlsx"

df1 = pd.read_excel(file,header = [0,1])

def getRateCardLCL(i):
    print("="*80)
    print("Agent: ",df1.iloc[i]["Overseas Agent"]["Agent"])

    if(pd.isnull(df1.iloc[i]["Port of Discharge Port Code (5 digit)"]["Via_POD"])):
        print(df1.iloc[i]["Origin Port Code (5 digit)"]["Origin"],"\t -------> \t",df1.iloc[i]["Destination Port Code (5 digit)"]["Destination"])
    else:
        print(df1.iloc[i]["Origin Port Code (5 digit)"]["Origin"],"\t -------> \t",df1.iloc[i]["Port of Discharge Port Code (5 digit)"]["Via_POD"],"\t -------> \t",df1.iloc[i]["Destination Port Code (5 digit)"]["Destination"])
    print("\n")

    print("CHARGE HEAD\t\t\t\tCOLUMN\t\t\t BASIS")
    print("- Ocean Freight\t\t\t\t",df1.iloc[i]["Basic Ocean Freight"]["ocean_freight"],"\t\t\t",df1.iloc[i]['Basic Ocean Freight']["ocean_freight_basis"])
    print("\n")

    print("ORIGIN LOCAL CHARGES\t\t\tCOLUMN\t\t\t BASIS")
    print("- Inland Haulage Charge\t\t\t",df1.iloc[i]["Origin Local Charge"]["INLAND HAULAGE CHARGE"],"\t\t\t",df1.iloc[i]["Origin Local Charge"]["Basis"])
    print("- Handling Charge\t\t\t",df1.iloc[i]["Origin Local Charge"]["HANDLING CHARGE"],"\t\t\t",df1.iloc[i]["Origin Local Charge"]["Basis.1"])
    print("- Pickup Charge\t\t\t\t",df1.iloc[i]["Origin Local Charge"]["PICK UP CHARGE"],"\t\t\t",df1.iloc[i]["Origin Local Charge"]["Basis.2"])
    print("- Loading/Unloading Charge\t\t",df1.iloc[i]["Origin Local Charge"]["Loading/Unloading Charge"],"\t\t\t",df1.iloc[i]["Origin Local Charge"]["Basis.3"])
    print("\n")

    print("ORIGIN CLEARANCE CHARGES\t\tCOLUMN\t\t\t BASIS")
    print("- Origin Customs Clearance Charge  \t",df1.iloc[i]["Origin Customs clearance charge  "]["Destination Customs clearance charge  "],"\t\t\t",df1.iloc[i]["Origin Customs clearance charge  "]["Basis"])
    print("\n")

    print("DESTINATION LOCAL CHARGES\t\tCOLUMN\t\t\t BASIS")
    print("- LCL Charge\t\t\t\t",df1.iloc[i]["Destination Local Charge"]["LCL CHARGES"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis"])
    print("- TSA Charge\t\t\t\t",df1.iloc[i]["Destination Local Charge"]["TSA_Value"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis.1"])
    print("- Inland Haulage Charge\t\t\t",df1.iloc[i]["Destination Local Charge"]["Inland Haulage - Import"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis.3"])
    print("- Delivery Order Fee\t\t\t",df1.iloc[i]["Destination Local Charge"]["Delivery order fee"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis.4"])
    print("- Loading/Unloading Charge\t\t",df1.iloc[i]["Destination Local Charge"]["Loading/Unloading Charge"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis.5"])
    print("- Delivery Charge\t\t\t",df1.iloc[i]["Destination Local Charge"]["Delivery charge"],"\t\t\t",df1.iloc[i]["Destination Local Charge"]["Basis.6"])
    print("\n")

    print("DESTINATION CLEARANCE CHARGES\t\tCOLUMN\t\t\t BASIS")
    print("- Destination Customs Clearance Charge \t",df1.iloc[i]["Destination Customs clearance charge  "]["Destination Customs clearance charge  "],"\t\t\t",df1.iloc[i]["Destination Customs clearance charge  "]["Basis"])
    print("="*80)
    print("\n")

origin = input("Enter Origin: ")
destination = input("Enter Destination: ")

row = df1[(df1["Origin Port Code (5 digit)"]["Origin"]==origin) & (df1["Destination Port Code (5 digit)"]["Destination"]==destination)].index

for i in row:
    getRateCardLCL(i)
