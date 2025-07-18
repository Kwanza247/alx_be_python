#ask for size
size = int(input("Enter the size of the pattern: "))
 #check if the input is positive
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

row = 0 #start with the first row

while row < size: #repeat until we reach the number of rows
    for col in range(size): #print one line of asterisks
        print("*", end="") #dont move to the next line
    print() #move to the next line after one row is done
    row += 1 #Go to the next row