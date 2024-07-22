# Description: Program for The One Stop Insurance Company to enter and calculate new insurance policy
# information for its multiple customers.
# Author: 
# Date(s):
 
 
# Define required libraries.



 
# Define program constants.
NEXT_POLICY_NUM = 1944
BASIC_PREMIUM = 869.00
DIS_ADD_CARS = .25
COST_EX_LIA_COVERAGE = 130.00
COST_GLASS_COVERAGE = 86.00
COST_LOANER_CAR_COVERAGE = 58.00
HST= .15
PROCESS_FEE_MONTH_PAYMENTS = 39.99


# Open the defaults file and read the values into variables
# The file must be created first since it is being read, it must exits. 




# Define program functions.
# From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c



 
# Main program starts here.
while True:
   
    # Gather user inputs.
    CustFirstName = input("Enter the Customer First Name: ")
    CustLastName = input("Enter the Customer Last Name: ")
    StAdd= input("Enter the Street Address: ")
    City = input("Enter the City: ")
    

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MN", "SK", "AB", "BC", "YT", "NW", "NT"]
    while True:
        Prov = input("Enter the Province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be Blank - Please Reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 Digit Code - Please Reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a Valid Province - Please Reenter.")
        else:
            break

    Postal = input("Enter the Postal Code (X9X9X9): ").upper()
    PhoneNum = input("Enter the Phone Number (999-999-9999): ")
    CellNum = input("Enter the Cell Number (999-999-9999): ")

    InsCarsNum = input("Enter the Number of Cars Being Insured: ")
    ExtLiability = input("Enter the Extra Liability Status up to $1,000,000(Y/N): ").upper()
    GlassCoverage = input("Enter the Optional Glass Coverage Status(Y/N): ").upper()
    LoanerCar = input("Enter the Optional Loaner Car Status(Y/N): ").upper()


    PayOptionLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PayOption = input("Enter the Payment Option: ").upper()
        if Prov == "":
            print("Error - Province cannot be blank - Please reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 digit code - please reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province - please reenter.")
        else:
            break


    # enter a value to indicate if they want to pay in full or monthly (Full or Monthly or Down Pay – use a list to validate). 







    # Perform required calculations.
    
 
 
    # Display results
    
 
    # Write processed data to a file for future use.
    # Steps 1. Open the file, 2. Process the data, 3. Close the file.
   
    
 
    # Any value written to a file must be recognized as a string.
    
 
    # A file is organized into records and fields.
    # A single line in a file is a record - about a single person, place, thing or event.
    # Each record is made up of individual pieces of data known as fields.
    # In every record, the fields are always in the same order.
 
    # 2. Progress Bar - More fancy status bar.  
    # Also needs sys and time imports and the function above.
   
    
 
    # Update any values for the next claim.
    
 

    # Can place the inside to loop to update each time, or in the housekeeping
    # section below to update when the user exists in the program



    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.

    


    # 2. Progress Bar - More fancy status bar.  
    # Also needs sys and time imports and the function above.
   
    
    Continue = input("Do you want to process another claim (Y / N): ").upper()
    if Continue == "N":
        break
 
# Any housekeeping duties at the end of the program.
