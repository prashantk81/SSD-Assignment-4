# SSD-Assignment-4

## Q1-> File Name is pattern.py

    to run this file  `python3 pattern.py`
    pattern will show on the command prompt

## Q2-> File Name is address.py

    In this question we used `prettytable` module to print in tabular format...
    for question 2 there is address.csv file which is main file where all the entries are stored and one more test.csv file which is used during adding entries from a CSV file.

#### Header of file is

`FirstName,LastName,Address,City,State,Zip,ContactNumber,EmailAddress`

=> To add a new user from command prompt
run this command `python3 address.py addentry prashant kumar IIITH Hyderabad Telangana 500032 8178169444 prashant.k@students.iiit.ac.in`

=>Loading Entries from .csv file
run this command `python3 address.py addentryfromCSV test.csv`

=>Display the data on terminal
run this command `python3 address.py display`

=>Remove the entry from directory
run this command `python3 address.py delete FirstName=Virat LastName=Kohli`

=>Update the entry
run this command `python3 address.py update Zip=12344 where FirstName=Prashant`

=>Search entry in the address directory
run this command `python3 address.py search FirstName=Prashant LastName=Kumar`

All the operations are case-sensitive

## Q3-> File Name is map.py

    In this part of question we used matplotlib, numpy,pandas library...
    I take input from directionData.csv file which contains set of lengths and directions.
    I take all the length in (millimeter)mm unit.

I assumed, initial location of Person P is origin(0,0)

=> to run this file `python3 map.py`
We print direction and distance on the command prompt at each and every step with respect to initial position.
we also print total distance on command prompt.
