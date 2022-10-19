import random 

secret_number = random.randint(1,100)
print("The Secret number is", secret_number)

while True:
    guess = int(input("Enter your number: "))
    if guess > secret_number:
        print("Yor number is higher, please try again")
    
    elif guess < secret_number:
        print("Yor number is lower, please try again") 

    else:
        print("You won!")

