groupA=[] 
groupB=[] 
groupC=[] 
 
n1=int(input("Enter the student count who play Cricket : ")) 
print("Enter %i student name : "%n1) 
groupA=list(map(str,input().split(" "))) 
 
n2=int(input("Enter the student count who play Badminton : ")) 
print("Enter %i student name : "%n2) 
groupB=list(map(str,input().split(" "))) 
 
n3=int(input("Enter the student count who play Football : ")) 
print("Enter %i student name : "%n3) 
groupC=list(map(str,input().split(" "))) 
 
print(" Group A = ",groupA) 
print(" Group B = ",groupB) 
print(" Group C = ",groupC) 
 
def first(groupA,groupB): 
    newlist=[] 
    lena=len(groupA) 
    lenb=len(groupB) 
     
    for i in range(lena): 
        for j in range(lenb): 
            if(groupA[i]==groupB[j]): 
                newlist.append(groupA[i]) 
                break 
    print(" 1) List of students who play cricket and Badminton : ") 
    print(newlist) 
 
 
def second(groupA,groupB): 
     
    newlist=[] 
    lena=len(groupA) 
    lenb=len(groupB) 
     
    for i in range(lena): 
        for j in range(lenb): 
            if(groupA[i]==groupB[j]): 
                flag=1 
                break 
             
        if(flag==0): 
            newlist.append(groupA[i]) 
        flag=0 
                 
    for i in range(lenb): 
        for j in range(lena): 
            if(groupB[i]==groupA[j]): 
                flag=1 
                break 
             
        if(flag==0): 
            newlist.append(groupB[i]) 
        flag=0 
    print("2) List of students who play either cricket or Badminton but not both : ") 
    print(newlist) 
 
def third(groupA,groupB,groupC): 
     
    newlist=[] 
    lena=len(groupA) 
    lenb=len(groupB) 
    lenc=len(groupC) 
    flag=0 
    for i in range(lenc): 
        for j in range(lena): 
            if(groupC[i]==groupA[j]): 
                flag=1 
                break 
        for var in range(lenb): 
            if(groupC[i]==groupB[var]): 
                flag=1 
                break 
        if(flag==0): 
            newlist.append(groupC[i]) 
        flag=0 
         
    print("3) Number of students who play neither cricket nor Badminton  : ") 
    print(newlist) 
             
def fourth(groupA,groupB,groupC): 
    list1=[] 
    newlist = [] 
    lena = len(groupA) 
    lenb = len(groupB) 
    lenc = len(groupC) 
    flag=0 
    for i in range(lena): 
        for j in range(lenc): 
            if(groupA[i]==groupC[j]): 
                list1.append(groupA[i]) 
                break 
             
    newl=len(list1) 
    for i in range(newl): 
        for j in range(lenb): 
            if(list1[i]==groupB[j]):    
                flag=1 
                break 
        if(flag==0): 
            newlist.append(list1[i]) 
        flag=0 
         
    print("4) Number of students who play cricket and football but not badminton ") 
    print(newlist) 
        
first(groupA,groupB) 
second(groupA,groupB) 
third(groupA,groupB,groupC) 
fourth(groupA,groupB,groupC)
# Initialize empty lists for each sport
group_cricket = []
group_badminton = []
group_football = []

# Input student counts and names for each sport
n_cricket = int(input("Enter the number of students who play Cricket: "))
print(f"Enter {n_cricket} student names: ")
group_cricket = list(map(str, input().split(" ")))

n_badminton = int(input("Enter the number of students who play Badminton: "))
print(f"Enter {n_badminton} student names: ")
group_badminton = list(map(str, input().split(" ")))

n_football = int(input("Enter the number of students who play Football: "))
print(f"Enter {n_football} student names: ")
group_football = list(map(str, input().split(" ")))

# Print the groups
print("Group A (Cricket): ", group_cricket)
print("Group B (Badminton): ", group_badminton)
print("Group C (Football): ", group_football)

# Function to find students who play both cricket and badminton
def find_both_cricket_badminton(group1, group2):
    return [student for student in group1 if student in group2]

# Function to find students who play either cricket or badminton but not both
def find_either_cricket_badminton(group1, group2):
    return [student for student in group1 + group2 if (student in group1) ^ (student in group2)]

# Function to find students who play neither cricket nor badminton
def find_neither_cricket_badminton(group1, group2, group3):
    return [student for student in group3 if student not in group1 and student not in group2]

# Function to find students who play cricket and football but not badminton
def find_cricket_football_not_badminton(group1, group2, group3):
    common_cricket_football = [student for student in group1 if student in group3]
    return [student for student in common_cricket_football if student not in group2]

# Call the functions and print the results
print("1) List of students who play cricket and Badminton: ")
print(find_both_cricket_badminton(group_cricket, group_badminton))

print("2) List of students who play either cricket or Badminton but not both: ")
print(find_either_cricket_badminton(group_cricket, group_badminton))

print("3) List of students who play neither cricket nor Badminton: ")
print(find_neither_cricket_badminton(group_cricket, group_badminton, group_football))

print("4) List of students who play cricket and football but not badminton: ")
print(find_cricket_football_not_badminton(group_cricket, group_badminton, group_football))
