# Write a function is_even that will return true if the passed-in number is even.


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(2))
print(is_even(3))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even_tho(n):
    if n % 2 == 0:
        return "Even!"
    else:
        return "Odd"
print(is_even_tho(num))