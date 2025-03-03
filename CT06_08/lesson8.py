print("Hello from lesson 8")

#ask for 5 numbers using a forvloop

pd=1
for c in range(5):
    num = int(input("Give me a number "))
    pd = pd*num

if pd >= 1000000000000:
    pd="beyond my feeble brain to comprehend"

print("final res: " + str(pd))