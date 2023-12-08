import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("\nEnter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for password length.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    generated_password = generate_password(length)

    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()