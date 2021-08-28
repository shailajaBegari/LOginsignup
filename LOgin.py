import json
f1=open("users.json","r")
data=json.load(f1)
def user_exit(data,password,username):

    for i in data:
        if data[i]["password"]==password and data[i]["name"]==username:
            return True

def signup(data):
    Name=input("enter u r name:")
    print(Name,"WELLCOME TO LOGIN/SIGNUP")
    user=int(input("if you want signup enter 1 and if you want to login enter 2:"))
    if user==1:
        name=input("enter name:")
        n=input("enter password must be Caps and @ and num and small:")
        c_pas=input("enter confirm password:")
        if ("a" in n or "b" in n or "c" in n or "d" in n or "e" in n or "f" in n or "g" in n or "h" in n or "i" in n or "j" in n or "k" in n or "l" in n or "m" in n or "n" in n or "o" in n or "p" in n or "q" in n or "r" in n or "s" in n or "t" in n or "u" in n or "v" in n or "w" in n or "x" in n or "y" in n or "z" in n) and ("A" in n or "B" in n or "C" in n or "D" in n or "E" in n or "D" in n or "E" in n or "F" in n or "G" in n or "H" in n or "I" in n or "J" in n or "K" in n or "L" in n or "M" in n or "N" in n or "O" in n or "P" in n or "Q" in n or "R" in n or "S" in n or "T" in n or "U" in n or "V" in n or "W" in n or "X" in n or "Y" in n or "Z" in n) and ("0" in n or "1" in n or "2" in n or "3" in n or "4" in n or "5" in n or "6" in n or "7" in n or "8" in n or "9" in n) and ("@" in n or "#" in n or "$" in n or "&" in n):
            if n==c_pas:
                print("ur  password is valid")
                dob=input("enter u r date of birth:")
                gender=input("enter the male/female:")
                descrip=input("enter the description:")
                hob=input("enter u r hobbies:")
        else:
            print("your typing password is not correct")
        data[name]={"name":name,"password":n,"confirmpass":c_pas,"date of birth":dob,"gender":gender,"descripition":descrip,"hobbies":hob}
        with open("users.json","w") as f:
            data=json.dump(data,f,indent=4)
    if user==2:
        username=input("enter user name:")
        password=input("enter the pasdsword:")
        check=user_exit(data,password,username)
        if check==True:
            print("login sucessfully")
        else:
            print("not valid username and password")

    
signup(data)


