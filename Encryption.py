import random

def encryption():
    print("""---------------------------------------------------
            Welcome to PyEncryption
---------------------------------------------------""")

    # Generate a dynamic encryption dictionary for all characters in BMP (0-65535)
    chars = [chr(i) for i in range(65536)]  # All characters in Unicode BMP
    shuffled_chars = chars.copy()
    random.seed(1234)  # Fixed seed for consistent encryption/decryption mapping
    random.shuffle(shuffled_chars)

    dict_char = {c: shuffled_chars[i] for i, c in enumerate(chars)}
    r_dict = {v: k for k, v in dict_char.items()}

    # Reply list
    reply = ["yea", "yes", "y", "yo", "ye"]

    # Rating Function
    def rating():
        rate = input("Do you want to rate this? (Yes/No): ")
        if rate.lower() in reply:
            rated = input("Rate (1-5): ")
            if rated in ["1", "2", "3", "4", "5"]:
                print(f"Thank you for rating, you rated {rated}.")
            else:
                print("Thank you for rating, you rated 5.")
        else:
            print("")

    # Encryption function
    def encryption_t():
        user_text = input("\nEnter encrypting text: ")
        new = ''.join(dict_char.get(char, char) for char in user_text)
        print(f"\nEncrypted form is: {new}")

    # Decryption function
    def decryption():
        user_text = input("\nEnter decrypting text: ")
        decrypted = ''.join(r_dict.get(char, char) for char in user_text)
        print(f"Decrypted form is: {decrypted}")

    # Main loop
    while True:
        intro = input("\nPress '1' for encryption or Press '2' for decryption (or 'q' to quit): ").strip().lower()

        if intro == 'q':
            print("\nThank you for using")
            rating()
            break

        elif intro == '1':
            encryption_t()

        elif intro == '2':
            decryption()

        else:
            print("\nPlease enter a valid choice.")
if  __name__ == "__main__":
    encryption()