# A slightly more complex example
x = 3
y = 10
z = None

if x < y:
    z = 13
print(f"Variable z is now {z}.")


# What happens here?
x = 3
y = 10

if x > y:
    print("x is greater than y.")

# x is equal to y with elif statement
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
elif x == y:
    print("x is equal to y.")
else:
    print("x is greater than y.")

tomorrow = "warm"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")




