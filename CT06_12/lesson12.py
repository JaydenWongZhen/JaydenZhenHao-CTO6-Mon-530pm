print("Hello from lesson 12")

# fhrfgt=input("give me a 5 letter word ")
# contains_o= False
# contains_e= False
# for dgufhg in fhrfgt:
#     print(dgufhg)
#     if dgufhg == "o":
#         contains_o = True
#     elif dgufhg == "e":
#         contains_e = True

# if contains_o == True and contains_e == True:
#     print("wow this word has an o and an e good word")
# else:
#     print("needs o and e")

# c=0
# while c <= 50:
#     print(c)
#     c += 1

## - task 3 -  ##



# #take order
# order= "" 
# answer = input("welcome to mcdonal what you wan ")
# while not answer == "no":
#     #inside loop
#     order = order + answer + ","
#     answer= input("anything more? ")
# #outside loop
# print("you have orderd: " + order)

# import random
# n= random.randint(1,10)
# nn= random.randint(1,10)
# ans = n + nn
# guess= "what is " + str(n) + "+" + str(nn) + " "
# youre_adpoted= int(input(guess))
# while not int(youre_adpoted) == ans:
#     print("no")
#     youre_adpoted = input(guess)
#     youre_adpoted = int(youre_adpoted)
# else:
#     print("yes")

import random
TheAdoptionPapers=0
while not TheAdoptionPapers == 4:
    TheAdoptionPapers = random.randint(1,6)