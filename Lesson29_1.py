# Description: Program for The One Stop Insurance Company to enter and calculate new insurance policy
# information for its multiple customers.
# Author: 
# Date(s):
 
 
# Define required libraries.
import datetime
CurDate = datetime.datetime.now()


import time
import sys
 
# Define program constants.
# CLAIM_NUM = 34
# HST_RATE = .15
# Open the defaults file and read the values into variables
# The file must be created first since it is being read, it must exits. 

f = open('Def.dat', 'r')
# Values are stored as strings, covert according
CLAIM_NUM = int(f.readline())
HST_RATE = float(f.readline())
f.close()


# Define program functions.
# From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
 
 
# Main program starts here.
while True:
   
    # Gather user inputs.
    EmpNum = input("Enter the employee number: ")
    EmpName = input("Enter the employee name: ")
    Location = input("Enter the location: ")
    StartDate = input("Enter the start date (YYYY-MM-DD): ")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    EndDate = input("Enter the end date (YYYY-MM-DD): ")
    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    OwnRent = input("Did you rent or use own car (O / R): ").upper()
    Kms = 0
    if OwnRent == "O":
        Kms = input("Enter the total kilometers travelled: ")
        Kms = int(Kms)
   
 
    # Perform required calculations.
    NumDays = (EndDate - StartDate).days
   
    if NumDays <= 3:
        PerDiem = 85.00 * NumDays
    else:
        PerDiem = 100.00 * NumDays
   
    if OwnRent == "O":
        MilAmt = Kms * .10
    else:
        MilAmt = 56.00 * (NumDays - 1)
   
    ClaimAmt = PerDiem + MilAmt
    HST = ClaimAmt * HST_RATE
 
    ClaimTotal = ClaimAmt + HST
 
 
    # Display results
    print(f"Claim number:           {CLAIM_NUM}")
    print(f"Location:               {Location}")
    print(f"Claim total:            {ClaimTotal}")
 
    # Write processed data to a file for future use.
    # Steps 1. Open the file, 2. Process the data, 3. Close the file.
   
    f = open("Claims.dat", "a") #Mode can be 'a' for append, 'w' for overwrite, 'r' to read.
 
    # Any value written to a file must be recognized as a string.
    f.write(f"{str(CLAIM_NUM)}, ")
    f.write(f"{CurDate}, ") # This is the current system date
    f.write(f"{EmpNum}, ")
    f.write(f"{EmpName}, ")
    f.write(f"{Location}, ")
    f.write(f"{StartDate}, ")
    f.write(f"{EndDate}, ")
    f.write(f"{str(NumDays)}, ")
    f.write(f"{str(ClaimTotal)}\n")
 
    f.close()
 
    # A file is organized into records and fields.
    # A single line in a file is a record - about a single person, place, thing or event.
    # Each record is made up of individual pieces of data known as fields.
    # In every record, the fields are always in the same order.
 
    # 2. Progress Bar - More fancy status bar.  
    # Also needs sys and time imports and the function above.
   
    print()
 
    TotalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Movie Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()

    
    print()
    print("Claim date has been sucessfully saved.")
    print()
 
    # Update any values for the next claim.
    CLAIM_NUM += 1
 

    # Can place the inside to loop to update each time, or in the housekeeping
    # section below to update when the user exists in the program



    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.

    f = open('Def.dat', 'w')
    f.write(f"{CLAIM_NUM}\n")
    f.write(f"{HST_RATE}\n")
    f.close()



    # 2. Progress Bar - More fancy status bar.  
    # Also needs sys and time imports and the function above.
   
    print()
 
    TotalIterations = 20 # The more iterations, the more time is takes.
    Message = "Updating default Values ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()


    Continue = input("Do you want to process another claim (Y / N): ").upper()
    if Continue == "N":
        break
 
# Any housekeeping duties at the end of the program.





