print("Hello to Student program")
print("_"*60)
print("1. Insert student")
print("2. Search for Student")
print("3. Print Count Of Student")
print("4. Remove Student ")
print("5. Exit")

students=[
            {"fullName":"lamyaa altuwairqi", 
             "mobile":"0551245966",
             "address":"Riyadh",
             "email":"lamya.altuwairqi@gmail.com"}
            ]
w=True
while w==True:

        
    x=int(input("choose one number: "))
    if x == 1:
        name=input("Please enter the name of the Student: ")
        mobile=input("Please enter the mobile of the Student: ")
        address=input("Please enter the address of the Student: ")
        email=input("Please enter the email of the Student: ")
        students.append({"fullName":name, "mobile":mobile, "address":address, "email":email})
        
        for x in students:
            for i, y in x.items():
                print(i,y)
            print("-"*50)

    elif x==2:
        name=input("Please enter the name of the Student: ")
        
        def search(z):
            for p in students:
                if p['fullName'] == z:
                    return p
                    
        print(search(name))

    elif x==3:
        print(len(students))

    elif x==4:
        name=input("Please enter the name of the Student: ")
        
        def delete(z):
            for p in students:
                if p['fullName'] == z:
                    students.remove(p)
                    return "data deleted"
                else:
                    return "there is no student in that name"
                    
        print(delete(name))

    elif x==5:
        w=False

    else: #when the user choose number more than 5
        print("please choose from 1 to 5 ")