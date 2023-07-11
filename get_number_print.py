#promt a user for a number and it use to print the miau
def main():
    number = get_number()
    miau(number)

def get_number():
    while True:
        n = (int(input("Whats n? ")))
        if n > 0:
            break
        return n

def miau(n):
    for _ in range(n):
        print("Miau")

main()