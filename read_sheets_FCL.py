import pandas as pd

file = "/Users/gopuman/Documents/TCL_backend/FCL_RATE.xlsx"

df1 = pd.read_excel(file,header=[3,4,5])

def getRateCardFCL(i):
    print("="*80)
    print("Carrier: ",df1.iloc[i]["General"]["Liner"]["Carrier"])

    orig = df1.iloc[i]["General"]["Origin Port Code (5 digit)"]["Origin"]
    via = df1.iloc[i]["General"]["Port of Discharge Port Code (5 digit)"]["Via_POD"]
    dest = df1.iloc[i]["General"]["Destination Port Code (5 digit)"]["Destination"]

    if(pd.isnull(df1.iloc[i]["General"]["Port of Discharge Port Code (5 digit)"]["Via_POD"])):
        print(orig,"\t -------> \t",dest)
    else:
        print(orig,"\t -------> \t",via,"\t -------> \t",dest)
    print("\n")

    print("CHARGE HEAD\t\t\t\t 20GP\t\t40GP\t\t40HQ")
    ofbof = df1.iloc[i]["Ocean Freight"]['Basic Ocean Freight']
    print("- Ocean Freight\t\t\t\t",ofbof["20GP"],"\t\t",ofbof["40 GP"],"\t\t",ofbof["40 HQ"])
    print("\n")

    print("ORIGIN LOCAL CHARGES\t\t\t 20GP\t\t40GP\t\t40HQ")
    olcs = df1.iloc[i]["Origin Local Charges"]
    print("- Stuffing\t\t\t\t",olcs["Stuffing"]["20GP"],"\t\t",olcs["Stuffing"]["40 GP"],"\t\t",olcs["Stuffing"]["40 HQ"])
    print("- Handling Charge\t\t\t",olcs["Origin Handling Charge"]["20GP"],"\t\t",olcs["Origin Handling Charge"]["40 GP"],"\t\t",olcs["Origin Handling Charge"]["40 HQ"])
    print("- Pickup Charge\t\t\t\t",olcs["Pick Up Charge"]["20GP"],"\t\t",olcs["Pick Up Charge"]["40 GP"],"\t\t",olcs["Pick Up Charge"]["40 HQ"])
    print("- Loading/Unloading Charge\t\t",olcs["Origin Loading/Unloading"]["20GP"],"\t\t",olcs["Origin Loading/Unloading"]["40 GP"],"\t\t",olcs["Origin Loading/Unloading"]["40 HQ"])
    print("- Lift on/Lift off Charge\t\t",olcs["Origin Lift On/lift Off"]["20GP"],"\t\t",olcs["Origin Lift On/lift Off"]["40 GP"],"\t\t",olcs["Origin Lift On/lift Off"]["40 HQ"])
    print("- Documentation Fee\t\t\t",olcs["Origin Documentation fee "]["20GP"],"\t\t",olcs["Origin Documentation fee "]["40 GP"],"\t\t",olcs["Origin Documentation fee "]["40 HQ"])
    print("- Inland Haulage Charge\t\t\t",olcs["Origin Inland Haulage Charges "]["20GP"],"\t\t",olcs["Origin Inland Haulage Charges "]["40 GP"],"\t\t",olcs["Origin Inland Haulage Charges "]["40 HQ"])
    print("\n")

    print("ORIGIN CLEARANCE CHARGES\t\t 20GP\t\t40GP\t\t40HQ")
    occ = df1.iloc[i]["Origin Clearance Charge"]["Origin Customs Clearance"]
    print("- Origin Customs Clearance Charge  \t",occ["20GP"],"\t\t",occ["40 GP"],"\t\t",occ["40 HQ"])
    print("\n")
    
    
    print("DESTINATION LOCAL CHARGES\t\t 20GP\t\t40GP\t\t40HQ")
    dlc = df1.iloc[i]["Destination Local Charges"]
    print("- Equipment Imbalance\t\t\t",dlc["Equipment Imbalance"]["20GP"],"\t\t",dlc["Equipment Imbalance"]["40 GP"],"\t\t",dlc["Equipment Imbalance"]["40 HQ"])
    print("- Peak Season Charge\t\t\t",dlc["Peak Season Charge"]["20GP"],"\t\t",dlc["Peak Season Charge"]["40 GP"],"\t\t",dlc["Peak Season Charge"]["40 HQ"])
    print("- EBS\t\t\t\t\t",dlc["Emergency Bunker Surcharge (EBS)"]["20GP"],"\t\t",dlc["Emergency Bunker Surcharge (EBS)"]["40 GP"],"\t\t",dlc["Emergency Bunker Surcharge (EBS)"]["40 HQ"])
    print("- Low Sulphur Surcharge\t\t\t",dlc["Low Sulphur Surcharge"]["20GP"],"\t\t",dlc["Low Sulphur Surcharge"]["40 GP"],"\t\t",dlc["Low Sulphur Surcharge"]["40 HQ"])
    print("- Inland Haulage Charge\t\t\t",dlc["Destination Inland Haulage Charges "]["20GP"],"\t\t",dlc["Destination Inland Haulage Charges "]["40 GP"],"\t\t",dlc["Destination Inland Haulage Charges "]["40 HQ"])  
    print("- Documentation fee\t\t\t",dlc["Documentation fee - destination"]["20GP"],"\t\t",dlc["Documentation fee - destination"]["40 GP"],"\t\t",dlc["Documentation fee - destination"]["40 HQ"])
    print("- Lift On/lift Off\t\t\t",dlc["Lift On/lift Off"]["20GP"],"\t\t",dlc["Lift On/lift Off"]["40 GP"],"\t\t",dlc["Lift On/lift Off"]["40 HQ"])
    print("- Container cleaning import\t\t",dlc["Container cleaning import"]["20GP"],"\t\t",dlc["Container cleaning import"]["40 GP"],"\t\t",dlc["Container cleaning import"]["40 HQ"])
    print("- Survey Charge\t\t\t\t",dlc["Survey Charge"]["20GP"],"\t\t",dlc["Survey Charge"]["40 GP"],"\t\t",dlc["Survey Charge"]["40 HQ"])
    print("- Administration fee\t\t\t",dlc["Administration fee"]["20GP"],"\t\t",dlc["Administration fee"]["40 GP"],"\t\t",dlc["Administration fee"]["40 HQ"])
    print("- Terminal Handling charges\t\t",dlc["Destination Terminal Handling charges"]["20GP"],"\t\t",dlc["Destination Terminal Handling charges"]["40 GP"],"\t\t",dlc["Destination Terminal Handling charges"]["40 HQ"])
    print("- HBL Fee\t\t\t\t",dlc["HBL Fee"]["20GP"],"\t\t",dlc["HBL Fee"]["40 GP"],"\t\t",dlc["HBL Fee"]["40 HQ"])
    print("- Facility Maintenance\t\t\t",dlc["Facility Maintenance"]["20GP"],"\t\t",dlc["Facility Maintenance"]["40 GP"],"\t\t",dlc["Facility Maintenance"]["40 HQ"])
    print("- CFS Charges\t\t\t\t",dlc["CFS Charges"]["20GP"],"\t\t",dlc["CFS Charges"]["40 GP"],"\t\t",dlc["CFS Charges"]["40 HQ"])
    print("- STORAGE\t\t\t\t",dlc["STORAGE"]["20GP"],"\t\t",dlc["STORAGE"]["40 GP"],"\t\t",dlc["STORAGE"]["40 HQ"])
    print("- Concor\t\t\t\t",dlc["Concor"]["20GP"],"\t\t",dlc["Concor"]["40 GP"],"\t\t",dlc["Concor"]["40 HQ"])
    print("- Container Maintenance Fee\t\t",dlc["Container Maintenance Fee"]["20GP"],"\t\t",dlc["Container Maintenance Fee"]["40 GP"],"\t\t",dlc["Container Maintenance Fee"]["40 HQ"])
    print("- Document stamp tax\t\t\t",dlc["Document stamp tax"]["20GP"],"\t\t",dlc["Document stamp tax"]["40 GP"],"\t\t",dlc["Document stamp tax"]["40 HQ"])
    print("- Union Charge\t\t\t\t",dlc["Union Charge"]["20GP"],"\t\t",dlc["Union Charge"]["40 GP"],"\t\t",dlc["Union Charge"]["40 HQ"])   
    print("- Delivery Order Fee\t\t\t",dlc["Delivery Fee"]["20GP"],"\t\t",dlc["Delivery Fee"]["40 GP"],"\t\t",dlc["Delivery Fee"]["40 HQ"])  
    print("- Loading/Unloading Charge\t\t",dlc["Loading/Unloading"]["20GP"],"\t\t",dlc["Loading/Unloading"]["40 GP"],"\t\t",dlc["Loading/Unloading"]["40 HQ"])  
    print("\n")

    print("DESTINATION CLEARANCE CHARGES\t\t 20GP\t\t40GP\t\t40HQ")
    dcc = df1.iloc[i]["Destination Clearance Charges"]["Customs Clearance"]
    print("- Customs Clearance \t\t\t",dcc["20GP"],"\t\t",dcc["40 GP"],"\t\t",dcc["40 HQ"])
    print("="*80)
    print("\n")

A = input("Enter Origin: ")
B = input("Enter Destination: ")

row = df1[(df1["General"]["Origin Port Code (5 digit)"]["Origin"]==A) & (df1["General"]["Destination Port Code (5 digit)"]["Destination"]==B)].index

for i in row:
    getRateCardFCL(i)


