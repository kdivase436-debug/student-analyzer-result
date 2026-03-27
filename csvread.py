#import the csv module
import csv
#create a empty list
students=[]
#string variable create to store top student
top=''
#these var. store the highest avg marks
high_avg=0
#open the csv file
with open('csv.csv','r')as file:
      #reads the csv file 
      reader=csv.DictReader(file)
      #these loop convert the row in dictionary format
      for row in reader:
        #add each row
        students.append(row)  
for student in students:
    #calculate total marks
    total=int(student['Math'])+int(student['Science'])+int(student['English'])+int(student['Physics'])+int(student['Chemistry'])+int(student['Marathi'])
    #calculate avg marks     
    #length=6
    length = len(student) - 1
    avg=round(total/length,2)
    #stores avg in dictionary
    student['avg']=avg
    if avg>high_avg:
        high_avg=avg
        top= student['Name']

#open text file 
with open('csv.txt','w')as file:
    file.write("\nstudent Result")
    file.write(f"\ntop student: {top}")

    for student in students:
        #print the name and avg
        file.write(f"\n{student['Name']}-Avg:{student['avg']}")
        #print name of top student
        print("report successfully")
                