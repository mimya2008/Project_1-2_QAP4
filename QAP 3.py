# Description: Program for Honest Harry to keep track of his sales for his car lot.
# Author: Mimya Hafiz, QAP 3
# Date(s): June 7, 2024 - June 11, 2024

 
# Define required libraries.
import datetime 
 
 
# Define program constants.
LICENCE_FEE_LOW = 75.00
LICENCE_FEE_HIGH = 165.00
TRANS_RATE = .01
ADD_TRANS_RATE = .016
HST_RATE = .15
FIN_FEE_RATE = 39.99
 

 
# Main program starts here.
while True:
   
    # Gather user inputs.
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'")     # Customer First Name
    while True:
        CustFirst = input("Enter the customer first name (END to quit): ").title()
        if CustFirst == "":
            print("   Data Entry Error - customer name cannot be blank.")
        elif set(CustFirst).issubset(allowed_char) == False:
            print("   Data Entry Error - customer name contains invalid characters.")
        else:
            break 

    if CustFirst.upper() == "END":
        break



    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'")       # Customer Last Name
    while True:
        CustLast = input("Enter the customer last name: ").title()
        if CustLast == "":
            print("   Data Entry Error - customer name cannot be blank.")
        elif set(CustLast).issubset(allowed_char) == False:
            print("   Data Entry Error - customer name contains invalid characters.")
        else:
            break


    FullName = CustFirst[0] + ". " + CustLast                                           # Customer Full Name
    


    allowed_char = set("0123456789")
    while True:
        PhoneNum = input("Enter the phone number (9999999999): ")

        if PhoneNum == "":
            print("   Data Entry Error - phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("   Data Entry Error - phone number must be 10 digits.")
        elif set(PhoneNum).issubset(allowed_char) == False:                                # PhoneNum.isdigit for num, .alpha is for alphabet
            print("   Data Entry Error - phone number contains invalid characters.")
        else:
            PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
            break   

    
    
    while True:
        PlateNum = input("Enter the car plate number (XXX999): ").upper()
    
        if PlateNum == "":
            print("    Data Entry Error - Plate Number cannot be blank.")
        elif len(PlateNum) != 6:
            print("    Data Entry Error - Plate Number must be 6 digits.")
        elif PlateNum[0:3].isalpha() == False:
            print("    Data Entry Error - Plate Number must start with 3 letters.")
        elif PlateNum[3:6].isdigit() == False:
            print("    Data Entry Error - Plate Number must end with 3 numbers.")
        else:
            break



    SellPrice = input("Enter the Selling Price: ")
    SellPrice = float(SellPrice)
    if SellPrice > 50000.00: 
        print("Data Entry Error - Selling price does not exceed $50,000.00 ")
    

    TradeAmt = input("Enter the Trading Amount: ")
    TradeAmt = float(TradeAmt)
    if TradeAmt > SellPrice: 
        print("Data Entry Error - Trading amount does not exceed the Selling price ")



    SalesPerName = input("Enter the Sales Persons Name: ")


    CurDate = datetime.datetime.now()
    InvoiceDateUp= CurDate.strftime("%B %d, %Y")
    InvoiceDateDown= CurDate.strftime("%d-%b-%y")



    # 30 days to the Current date
    CurDatePlus30 = CurDate + datetime.timedelta(days = 30)
    FirstPaymentDate = CurDatePlus30.strftime("%d-%b-%y")


    CarYear = input("Enter the year of car made(YYYY): ")
    CarMake = input("Enter the car make company: ").capitalize()
    CarModel = input("Enter the car model: ").capitalize()



    # Perform required calculations.
    PriceAftTrade = SellPrice - TradeAmt


    if SellPrice <= 5000.00:
        LicenceFee = LICENCE_FEE_LOW
    else:
        LicenceFee = LICENCE_FEE_HIGH


    if SellPrice <= 20000.00:
        TransFee = SellPrice * TRANS_RATE
    else:
        TransFee = (SellPrice * TRANS_RATE) + (SellPrice * ADD_TRANS_RATE)



    Subtotal = PriceAftTrade + LicenceFee + TransFee

    HST = Subtotal * HST_RATE

    TotSalesPrice = Subtotal + HST



    # Display results
    print()
    print()
    print(f"Honest Harry Car Sales                            Invoice Date: {InvoiceDateUp:>14s}")
    ReceiptID = CustFirst[0] + CustLast[0] + "-" + PlateNum[3:] + "-" + PhoneNum[10:]
    print(f"Used Car Sale and Receipt                         Receipt No:      {ReceiptID:>11s}")
    print()
    


    SellPriceDsp = "${:,.2f}".format(SellPrice)                               #When you format, result is a string
    print(f"                                            Sale price:             {SellPriceDsp:>10s}")



    TradeAmtDsp = "${:,.2f}".format(TradeAmt)                                 #When you format, result is a string
    print(f"Sold to:                                    Trade Allowance:        {TradeAmtDsp:>10s}")
    print(f"                                            ----------------------------------")



    PriceAftTradeDsp = "${:,.2f}".format(PriceAftTrade)                        #When you format, result is a string
    print(f"     {FullName:<29s}          Price after Trade:      {PriceAftTradeDsp:>10s}")



    LicenceFeeDsp = "${:,.2f}".format(LicenceFee)
    print(f"     {PhoneNum:<14s}                         License Fee:            {LicenceFeeDsp:>10s}")



    TransFeeDsp = "${:,.2f}".format(TransFee)                               #When you format, result is a string
    print(f"                                            Transfer Fee:           {TransFeeDsp:>10s}")
    print(f"                                            ----------------------------------")



    SubtotalDsp = "${:,.2f}".format(Subtotal)                                 #When you format, result is a string
    print(f"Car Details :                               Subtotal:               {SubtotalDsp:>10s}")



    HSTDsp = "${:,.2f}".format(HST)                               #When you format, result is a string
    print(f"                                            HST:                    {HSTDsp:>10s}")



    print(f"     {CarYear:<4s} {CarMake:<13s} {CarModel:<10s}          ----------------------------------")
    TotSalesPriceDsp = "${:,.2f}".format(TotSalesPrice)                               #When you format, result is a string
    print(f"                                            Total sales price:      {TotSalesPriceDsp:>10s}")
    print()



    print(f"------------------------------------------------------------------------------")
    print()
    print(f"                                    Financing      Total         Monthly")



    print(f"     # Years      # Payments           Fee         Price         Payment      ")
    print(f"     -------------------------------------------------------------------      ")



    for Years in range (1,5):
        Payments = Years * 12
        FinFee = FIN_FEE_RATE * 4
        Totprice = TotSalesPrice + FinFee
        TotMonths = 12 * 4
        MonPay = Totprice / TotMonths

        FinFeeDsp = "${:.2f}".format(FinFee)
        TotpriceDsp = "${:,.2f}".format(Totprice)
        MonPayDsp = "${:,.2f}".format(MonPay)
            



        print(f"        {Years:>d}             {Payments:>2d}             {FinFeeDsp:>7s}     {TotpriceDsp:>10s}    {MonPayDsp:>9s}")
    print(f"     -------------------------------------------------------------------      ")    




    print(f"     Invoice date: {InvoiceDateDown:<9s}               First payment date: {FirstPaymentDate:>9s}")
    print()
    print(f"------------------------------------------------------------------------------")




    # Any housekeeping duties at the end of the program.
    print(f"                      Best used cars at the best prices!                      ")
    print()
    print()