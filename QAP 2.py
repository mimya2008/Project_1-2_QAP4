# Description: Program for The St. John’s Marina and Yacht Club to help with their paperwork.
# Author: Mimya Hafiz
# Dates:   May 26, 2024- May 30, 2024


# Define Program Constants.
EVEN_SITE_COST = 80.00
ODD_SITE_COST = 120.00
ALT_MEM_COST_MON = 5.00
SITE_CLEAN_RATE = 50.00
VIDEO_SURVEY_RATE = 35.00
HST_RATE = .15

MEM_TYPE_S = 75.00
MEM_TYPE_E = 150.00
PROCESS_FEE = 59.99
CANCEL_RATE = .60

# Gather user inputs:
CurrYear = input("Enter the Current Year(YYYY): ")
CurrMon = input("Enter the Current Month(MM): ")
CurrDay = input("Enter the Current Day(DD): ")

SiteNum = input("Enter the Site Number(###): ")
SiteNum = int(SiteNum)
MemName = input("Enter the Member Name: ")

StAdd= input("Enter the Street Address: ")
City = input("Enter the City: ")
Prov = input("Enter the Province Name (XX): ").upper()
Postal = input("Enter the Postal Code (X9X9X9): ").upper()
PhoneNum = input("Enter the Phone Number (999-999-9999): ")
CellNum = input("Enter the Cell Number (999-999-9999): ")

MemType = input("Enter the Member Type(S/E): ").upper()
AltMemNum = input("Enter the Alternate Member Number(##): ")
AltMemNum = int(AltMemNum)
SiteClean = input("Enter the Site Clean Status(Y/N): ").upper()
VideoSurvey = input("Enter the Video Surveillance Status(Y/N): ").upper()


# Perform Required Calculation:

if SiteNum % 2 == 0:
    PerSiteCost = EVEN_SITE_COST
else: 
    PerSiteCost = ODD_SITE_COST

# Calculate the SiteCharge:
SiteCharge = PerSiteCost + (ALT_MEM_COST_MON * AltMemNum)
SiteCleanStatus = ""
VideoSurveyStatus = ""
MemTypeStatus = ""
if SiteClean == "Y":
    SiteCleanCost = SITE_CLEAN_RATE
    SiteCleanStatus = "Yes"
else: 
    SiteCleanCost = 0
    SiteCleanStatus = "No"

if VideoSurvey == "Y":
    VideoSurveyCost = VIDEO_SURVEY_RATE
    VideoSurveyStatus = "Yes"
else: 
    VideoSurveyCost = 0
    VideoSurveyStatus = "No"

# Calculate the ExtraCharge:
ExtraCharge = SiteCleanCost + VideoSurveyCost

# Calculate the SubTotal:
SubTotal = SiteCharge + ExtraCharge

# Calculate the HST:
HST = SubTotal * HST_RATE

# Calculate the TotMonCharge:
TotMonCharge = SubTotal + HST


if MemType == "S":
    MonthlyDues = MEM_TYPE_S
    MemTypeStatus = "Standard"
else: 
    MonthlyDues = MEM_TYPE_E
    MemTypeStatus = "Executive"

# Calculate the TotMonthlyFees:
TotMonthlyFees = TotMonCharge + MonthlyDues

# Calculate the TotYearlyFees:
TotYearlyFees = TotMonthlyFees * 12

# Calculate the MonthlyPayment:
MonthlyPayment = (TotYearlyFees + PROCESS_FEE) / 12

if SiteNum % 2 == 0:
    CancelFee = (SiteCharge * 12) * CANCEL_RATE
else: 
    CancelFee = (SiteCharge * 12) * CANCEL_RATE



# Display user outputs:
print()
print(f"     St. John’s Marina & Yacht Club")
print(f"          Yearly Member Receipt")
print(f"________________________________________")
print()

print(f"Client Name and Address:")
print()
print(f"{MemName:<26s}")
print(f"{StAdd:<26s}")
print(f"{City:<15s}              , {Prov:<2s} {Postal:<6s} ")

print()
print(f"Phone: {PhoneNum:>10s}(H)")
print(f"       {CellNum:>10s}(C)")

print()
print(f"Site#:{SiteNum:>3d} Member type: {MemTypeStatus:<9s}")
print()
print(f"Alternate members:                    {AltMemNum:>2d}")
print(f"Weekly site cleaning:                {SiteCleanStatus:>3s}")
print(f"Video surveillance:                  {VideoSurveyStatus:>3s}")

print()
SiteChargeDsp = "${:,.2f}".format(SiteCharge)                               #When you format, result is a string
print(f"Site charges:                  {SiteChargeDsp:>9s}")

ExtraChargeDsp = "${:.2f}".format(ExtraCharge)                              #When you format, result is a string
print(f"Extra charges:                   {ExtraChargeDsp:>7s}")
print(f"                             -----------")


SubTotalDsp = "${:,.2f}".format(SubTotal)                                   #When you format, result is a string
print(f"Subtotal:                      {SubTotalDsp:>9s}")

HSTDsp = "${:.2f}".format(HST)                                              #When you format, result is a string
print(f"Sales tax (HST):                 {HSTDsp:>7s}")
print(f"                             -----------")

TotMonChargeDsp = "${:,.2f}".format(TotMonCharge)                           #When you format, result is a string
print(f"Total monthly charges:         {TotMonChargeDsp:>9s}")

MonthlyDuesDsp = "${:.2f}".format(MonthlyDues)                              #When you format, result is a string
print(f"Monthly dues:                    {MonthlyDuesDsp:>7s}")
print(f"                             -----------")

TTotMonthlyFeesDsp = "${:,.2f}".format(TotMonthlyFees)                      #When you format, result is a string
print(f"Total monthly fees:            {TTotMonthlyFeesDsp:>9s}")

TotYearlyFeesDsp = "${:,.2f}".format(TotYearlyFees)                         #When you format, result is a string
print(f"Total yearly fees:            {TotYearlyFeesDsp:>10s}")
print()

MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)                       #When you format, result is a string
print(f"Monthly payment:               {MonthlyPaymentDsp:>9s}")

print(f"________________________________________")
print()

print(f"Issued: {CurrYear:<4s}-{CurrMon:<2s}-{CurrDay:<2s}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()

CancelFeeDsp = "${:,.2f}".format(CancelFee)                                 #When you format, result is a string
print(f"Cancellation fee:              {CancelFeeDsp:>9s}")
print()


