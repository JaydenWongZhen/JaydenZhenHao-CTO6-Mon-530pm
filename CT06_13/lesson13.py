print("IM TIRED CAN I HAVE A BREAK PLEASE")

# balance=1000
# print("Welcome to the ATM.")
# print("Choose the 4 following. | Withdraw || Deposit || Check Balance || Exit ||")
# reply = input(" ")
# if reply == "Exit":
#     print("Thank you for using the ATM.")
#     break
# elif reply == "Withdraw":
#     answer= input("How much to withdraw? ")
#     answer= int(answer)
#     break

shoping_lise =["apples","bread","carrots","dates","eggs","flour","grapes","honey"]
shoping_lise[7]= "herbs"
print(shoping_lise[0])
shoping_lise.append("Ice")
del(shoping_lise[1])
shoping_lise.insert(1, "bananas")
for item in shoping_lise:
    print(item)
    if item == "apples":
        print(item + ": i need 5 of them big juicys")
    if item == "carrots":
        print(item + ": i need 3 of those small ones")
    if item == "grapes":
        print(item + ": buy from the FarmFresh brand, i like that rband")