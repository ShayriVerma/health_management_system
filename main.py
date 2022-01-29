import datetime
def getdate() :
    return datetime.datetime.now()

def log(k) :
    if k == 1 :                                                   #1st person - shayri
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1 :
            ex_name = input ("type here \n")
            with open ("Shayri_ex.txt" , "a") as f :
                f.write (str([str(getdate())]) + ":" + ex_name + "\n")
            print ("successfully logged")
        if a == 2 :

            food_name = input ("type here \n")
            with open ("Shayri_food.txt" , "a") as f :
                f.write (str([str(getdate())]) + ":" + food_name + "\n")
            print ("successfully logged")
    elif k == 2 :                                             #2nd person - saransh
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1 :
            ex_name = input("type here \n")
            with open("Saransh_ex.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + ex_name + "\n")
            print("successfully logged")
        if a == 2:
            food_name = input("type here \n")
            with open ("Saransh_food.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + food_name + "\n")
            print("successfully logged")
    elif k == 3 :                                             #3rd person - Archana
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1:
            ex_name = input("type here \n")
            with open("Archana_ex.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + ex_name + "\n")
            print("successfully logged")
        if a == 2:
            food_name = input("type here \n")
            with open ("Archana_food.txt" , "a") as f:
                f.write(str([str(getdate())]) + ":" + food_name + "\n")
            print("successfully logged")
    else :
        print ("Enter a valid input")

def retrieve(t) :
    if t == 1 :
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1:
            with open("Shayri_ex.txt") as f :
                for i in f :
                    print (i , end="")
        else :
            with open("Shayri_food.txt") as f :
                for i in f :
                    print (i , end="")
    elif t == 2 :
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1:
            with open("Saransh_ex.txt") as f :
                for i in f :
                    print (i , end="")
        else :
            with open("Saransh_food.txt") as f :
                for i in f :
                    print (i , end="")
    elif t == 3 :
        a = int(input("enter 1 for excercise and 2 for food"))
        if a == 1:
            with open("Archana_ex.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            with open("Archana_food.txt") as f:
                for o in f:
                    print(o, end="")
    else :
        print ("enter a valid input")

print ("Health Management System")
s = int(input(print("Enter 1 to log the value and 2 to retrieve the value")))
if s == 1 :
    r = int(input("enter 1 for Shayri, 2 for Saransh and 3 for Archana"))
    log(r)
else :
    r = int(input("enter 1 for Shayri, 2 for Saransh and 3 for Archana"))
    retrieve(r)

