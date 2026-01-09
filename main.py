from password_gen import generate_password
from url_shortener import shorten_url, retrieve_url

def main():
    while True:
        print("1. Generate Password")
        print("2. Shorten URL")
        print("3. Retrieve URL")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print("Generated Password:", password)

        elif choice == "2":
            long_url = input("Enter long URL: ")
            short_code = shorten_url(long_url)
            print(f"Short URL Code: {short_code}")

        elif choice == "3":
            short_code = input("Enter short URL code: ")
            original_url = retrieve_url(short_code)
            print("Original URL:", original_url)

        elif choice == "4":
            print(":(")
            break

if __name__ == "__main__":
    main()
