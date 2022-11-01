from prettytable import PrettyTable
from tempfile import NamedTemporaryFile
import shutil
import csv
import sys

#*********************Stored CSV file**************************
FinalFile = "address.csv"
Header = "FirstName,LastName,Address,City,State,Zip,ContactNumber,EmailAddress"

#*******************Add Entry from Terminal*********************
def addEntry(val):
    dataLineAdd=val[0]+","+val[1]+","+val[2]+","+val[3]+","+val[4]+","+val[5]+","+val[6]+","+val[7]
    try:
            f = open("address.csv", "a")
            f.write("\n")
            f.write(dataLineAdd)
            f.close()
    except Exception as ep:
        print("Exception error: {}".format(ep))
    else:
        print("Entry"+ " Successfully"+ " Added!! ")

#*********************Add Entry From CSV File************************
def AddEntryFromCSV(val):
    field=[]
    try:
        with open(val[0]) as csvfile:
            reader=csv.reader(csvfile)
            field=next(reader)
            cat=','.join(field)
            present="FirstName,LastName,Address,City,State,Zip,ContactNumber,EmailAddress"
            if (cat!=present):
                raise ValueError("Header of the csv file should be exactly 'FisrtName,LastName,Address,City,State,Zip,ContactNumber,EmailAddress")
            f = open("address.csv", "a")
            for row in reader:
                f.write("\n")
                f.write(','.join(row))
            f.close()    
    except ValueError as er:
        print("Exception error: {}".format(ep))
    else:
        print("Data from CSV"+" file entered "+" into address directory"+" successfully!!")

#**********************Display Whole Data************************
def Display():
    attri=PrettyTable(Header.split(','))
    attri.align='l'
    attri.border=True
    try:
        f = open("address.csv")
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            attri.add_row(row)
        f.close()        
    except Exception as ep:
        print("Exception error: {}".format(ep))
    else:
        tableValue=str(attri)
        print(tableValue)                

#************************Filter Rows*******************************
def filterTuple(val,att):
    ret=False
    firstName,lastName,address,city,state,zipcode,contactNumber,emailAddress = val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7]
    if att.get("FirstName", 0) != 0 and firstName!= att["FirstName"]:
        return ret
    elif att.get("LastName", 0) != 0 and lastName != att["LastName"]:
        return ret
    elif att.get("Address", 0) != 0 and address!= att["Address"]:
        return ret
    elif att.get("City", 0) != 0 and city != att["City"]:
        return ret
    elif att.get("State", 0) != 0 and state!= att["State"]:
        return ret
    elif att.get("Zip", 0) != 0 and zipcode!= att["Zip"]:
        return ret
    elif att.get("ContactNumber", 0) != 0 and contactNumber != att["ContactNumber"]:
        return ret
    elif att.get("EmailAddress", 0) != 0 and emailAddress!= att["EmailAddress"]:
        return ret
    return True

#****************************Divide Function*****************************
def divide(val):
    att = {}
    i=0
    arr=[]
    while i<len(val):
        arr = val[i].split('=')
        att[arr[0]] = arr[1]
        i+=1
    return att

#***************************Search Entries*****************************
def search(val):
    att = divide(val)
    ans = []
    try:
        reader = csv.reader(open("address.csv"))
        next(reader)
        for row in reader:
            presentValue=filterTuple(row, att)
            if presentValue:
                ans.append(row)            
        x = Header.split(',')
        attri=PrettyTable(x)
        attri.align='l'
        attri.border=True
        for row in ans:
            attri.add_row(row)
        tableValue=str(attri)    
        print(tableValue)
    except Exception as ep:
        print("Exception error: {}".format(ep))

def dividingSub1(val):
    idx = val.index('where')
    p= val[0: idx]
    return divide(p) 
def dividingSub2(val):
    idx = val.index('where')
    q = val[idx + 1:]
    return divide(q)
#******************************Update Entries in the CSV File****************************
def update(val):
    dividedNewArr = dividingSub1(val)
    divideOldArr = dividingSub2(val)
    count = 0
    try:
        head = NamedTemporaryFile(mode='w', delete=False)
        with open("address.csv", 'r') as c, head:
            reader = csv.DictReader(c, fieldnames=Header.split(','))
            writer = csv.DictWriter(head, fieldnames=Header.split(','))
            for row in reader:
                val = [row[x] for x in row.keys()]
                cmpvalue=filterTuple(val, divideOldArr)
                if cmpvalue:
                    count+= 1
                    for key in dividedNewArr.keys():
                        row[key] = dividedNewArr[key]
                id1,id2,id3,id4,id5,id6,id7,id8= 'FirstName','LastName','Address','City','State','Zip','ContactNumber','EmailAddress'       
                row = {
                    id1: row[id1],
                    id2: row[id2],
                    id3: row[id3],
                    id4: row[id4],
                    id5: row[id5],
                    id6: row[id6],
                    id7: row[id7],
                    id8: row[id8],
                }
                writer.writerow(row)
            head.truncate()
        shutil.move(head.name, FinalFile)
        x=open("address.csv")    
        r = x.readlines()
        lengthR=len(r)-1
        r[lengthR] = r[lengthR].rstrip()
        x.close()    

        x=open("address.csv","w") 
        x.writelines(r)
        x.close()
    except Exception as e:
        print("Exception error: {}".format(e))
    else:
        print("Successfully updated enties...\n {} entries updated".format(count))

#*************************Delete Entry From Table****************************
def delete(val):
    dividedArray = divide(val)
    count = 0
    try:
        head = NamedTemporaryFile(mode='w', delete=False)
        with open("address.csv", 'r') as x, head:
            reader = csv.DictReader(x, fieldnames=Header.split(','))
            writer = csv.DictWriter(head, fieldnames=Header.split(','))
            for row in reader:
                val = [row[x] for x in row.keys()]
                cmpvalue=filterTuple(val, dividedArray)
                if cmpvalue:
                    count+=1
                    continue
                id1,id2,id3,id4,id5,id6,id7,id8= 'FirstName','LastName','Address','City','State','Zip','ContactNumber','EmailAddress'       
                row = {
                    id1: row[id1],
                    id2: row[id2],
                    id3: row[id3],
                    id4: row[id4],
                    id5: row[id5],
                    id6: row[id6],
                    id7: row[id7],
                    id8: row[id8],
                }
                writer.writerow(row)
            head.truncate()
        shutil.move(head.name, "address.csv")

        f=open("address.csv")    
        li = f.readlines()
        lengthLI=len(li) - 1
        li[lengthLI] = li[lengthLI].rstrip()
        f.close()

        f=open("address.csv","w")    
        f.writelines(li)
        f.close()
    except Exception as e:
        print("Exception error: {}".format(e))
    if(count==0):
        print("No such entires present...")    
    else:
        print("Successfully deleted entry...\n {} entries deleted".format(count))

#************************Address Directory Funcion*********************
def AddressDirectory(arguments):
    detail=arguments[2:]
    if (arguments[1]=="addentry"):
        if(len(detail)==8):
            addEntry(detail)
        else:
            raise ValueError('Please provide FirstName,LastName,Address,City,State,Zip,ContactNumber,EmailAddress')

    elif arguments[1]=="addentryfromCSV":
        if(len(detail)==1):
            AddEntryFromCSV(detail)
        else:
            raise ValueError('Please provide only csv file as an argument')
    elif arguments[1]=="display":
        if(len(detail)==0):
            Display()
        else:
            raise ValueError('Please provide only display command')
    elif arguments[1]=="update":
        if(len(detail)<2):
            raise ValueError('Please provide correct values for updation')
        else:
            update(detail)
    elif arguments[1]=="delete":
        if(len(detail)<1):
            raise ValueError('Please provide correct attribute for deletion')
        else:
            delete(detail)
    elif arguments[1]=="search":
        if(len(detail)!=0):
            search(detail)
        else: 
            raise ValueError('Please provide correct search parameters')
    else:
        print("Invalid Command... Try Again!!!")

#*********************Main Function************************
if __name__=="__main__":
    if(len(sys.argv))<2:
        raise ValueError("Incorrect Number of Arguments!!")
    else:
        AddressDirectory(sys.argv)        