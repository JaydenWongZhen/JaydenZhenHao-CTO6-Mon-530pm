# print("Hello from lesson 9")

# print("Hello, welcome to the libary.")
# days=int(input("How many days have you borrowed this book? "))
# if days >= 25:
#     print("Remember to return your book, this book is due in 5 days!")
# else:
#     print("Alright, you're clear! Have a nice day!")

# import random
# answer=random.randint(1,50)
# guess=int(input("Guess "))
# if guess == answer:
#     print("conguratulation")
# else:
#     print("try agin")

# aplle=60
# orangutan=90

# numap=int(input("how much aplle you buy "))
# numor=int(input("how much orangutan you buy "))

# if numap*aplle >= aplle*5:
#     priceapple=numap*aplle*0.9
# else:
#     priceapple=numap*aplle

# if numor*orangutan >= orangutan*5:
#     priceorangutan=numor*orangutan*0.9
# else:
#     priceorangutan=numor*orangutan

# totalrpice=(priceorangutan+priceapple)/100
# print("you have to pay $" + str(totalrpice))

A=100
numA=int(input("how much apples you wanna buy? ")) #THIS IS AN INPUT

if numA*A >= A*10: #THIS IS A DECISION
    print("here you go a deal, 10 for the price of 9 or 10% discount") #THIS IS AN OUTPUT
    TotA=numA*A*0.9/100
else: #ALSO A DECISION
    TotA=numA*A/100
print("please insert cash or card to pay $" + str(TotA)) #ALSO AN OUTPUT