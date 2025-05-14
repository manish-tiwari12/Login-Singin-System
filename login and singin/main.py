print("Welcome to Python Project..!")

user_choice = input("Choose  One (Login/Singin): ")

def singIn():
        print("USER SINGIN.")
        user_name = input("Enter Your FullName: ")
        email = input("Enter Your Email Id:")
        mobail = int(input("Enter Your Mobail Number:"))
        passwrd = input("Please Enter a Stong Password :")

        deta = f"Name : {user_name}, \nEmail : {email}, \nMobail Number : {mobail}, \nPassword : {passwrd}\n"

        with open("user_deta.txt" , "a") as f:
            deta = f.write(deta)
        
        print("You SingIn SuccessFully ✅ ")


def LogIn():
        user_name = input("Enter Your User Name Or Mobail NO. : ")
        Password = input("Enter Your Password")
        found  = False 
    
        try:
             with open("user_deta.txt", "r") as f:
                 for line in f:
                     line = line.split()
                     if line == f"{user_name},{Password}":
                         found  = True
                         break       
                          
        except FileNotFoundError:
           print("❌ User file not found. Please create users.txt first.")
           return
        
        
        if found:
           print("✅ Login successful! Welcome,", user_name)
        else:
           print("❌ Login failed! Email or password is incorrect.")
 
       
if user_choice.lower() == "singin":
               singIn()
elif user_choice.lower() == "login":
               LogIn()
else:
    print("❌ Invalid choice. Please type Login or Signin.")