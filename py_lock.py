import pyfiglet, getpass, os, string, random, hashlib

welcome_text = pyfiglet.figlet_format(text="PY-LOCK", font="isometric3",width=120)
print(welcome_text)

var = "     "  # Pwd for opening logs

def details_to_text():
    """To store user_name and passwords in a text file"""
    with open("log.txt", "a") as f:
        f.write(f"{description} ---> User-ID is '{user_name}'' and Password is {pwd}\n")

def open_logs():
    """Function to read the log contents"""
    try:
        with open("log.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("\nFile does not exist!\n")

def pass_generator(length_of_pass):  # Random key generating Function
    char = string.ascii_letters + string.punctuation + string.digits
    key = "".join(random.choice(char) for i in range(length_of_pass))
    print(f"\nKey Generated: '{key}'\n")

def encode_decode_str(your_str):  # Creating md5 hash using hashlib module
    result = hashlib.md5(your_str.strip().encode())   # Encoding and sending this to md5
    print(f"\nEncrypted Key: {result.hexdigest()}")
    hex_equivalent = result.hexdigest()
    return hex_equivalent

print(84*"#")
print("\n[1] New\n")
print("\n[2] Key Generator\n")
print("\n[3] Encrypt a Key [md5]\n")
print("\n[4] Read Saved Logs\n")
print("\n[5] Delete all logs\n")
print("\n[6] Quit\n")
print(84*"#")

while True:  # Continously prompt for choice
    while True:
        try:
            user_choice = int(input("\nInput a choice: "))
            break
        except ValueError:
            print("\nOnly Integer Allowed!")

    if user_choice==1 or user_choice==0o1:
        print("\n84*'#'\n")
        description = input("\nEnter a Description: ")
        user_name = input("\nEnter Your User ID: ")
        pwd = getpass.getpass("\nEnter your Password: ")
        print(f"\nYour ID is '{user_name}' and password is {len(pwd)} ;)")
        details_to_text()
        print("\nLOG SAVED SUCCESSFULLY!\n")
        print("\n84*#\n")
    elif user_choice == 2 or user_choice == 0o2:
        print("\n84*'#'\n")
        len_pass = int(input("\nEnter the maximum length of your key: "))
        pass_generator(len_pass)
        print("\n84*'#'\n")

    elif user_choice == 3 or user_choice == 0o3:
        print("\n84*'#'\n")
        key = input("\nEnter the string to be encrypted: ")
        encode_decode_str(key)
        print("\n84*'#'\n")

    elif user_choice==4 or user_choice==0o4:
        print("\n84*'#'\n")
        log_pwd = getpass.getpass("Enter Password: " + "\n")
        if log_pwd == var:
            open_logs()
        else:
            print("\nIncorrect!")
        print("\n84*'#'\n")

    elif user_choice == 5 or user_choice ==0o5:
        print("\n84*'#'\n")
        if os.path.exists("log.txt"):
            os.remove("log.txt")
            print("\nDeleted all saved logs!")
        else:
            print("\nFile does not exist.")
        print("\n84*'#'\n")

    elif user_choice==0o6 or user_choice == 6:
        print("\nVAULT LOCKED!!!\U0001F512\n")
        break
    else:
        print("\nEnter a valid option!!!")




