import os.path
from cryptography.fernet import Fernet
import random, string


print("="*30,"PWD Manager","="*30)
print(' '*30,"ver:b.1.0")
logp = os.path.isfile("log.txt")
if logp ==True:
    usrn = input("Username:")
    usrp = input("Password:")
    with open('Titan.txt', 'rb') as file:
        key = file.readline().strip()
    f = Fernet(key)
    with open('log.txt', 'rb') as file:
        encrypted_username = file.readline().strip()
        encrypted_password = file.readline().strip()
        username = f.decrypt(encrypted_username).decode()
        password = f.decrypt(encrypted_password).decode()
    if usrn == username:
        if usrp == password:
            print("successuly logged in")
            dop = input("Display Passowrd  Generate Password or Save Password D/G/S")


            def get_specific_line(file_path, line_number):
                line_data = ""
                try:
                    with open('PwdList.txt', "r") as file:
                        lines = file.readlines()
                        if 1 <= line_number <= len(lines):
                            line_data = lines[line_number - 1]
                        else:
                            print("Line number is out of range.")
                except FileNotFoundError:
                    print("File not found.")
                except IOError:
                    print("An error occurred while reading the file.")
                return line_data


            if dop == 'd' or dop == 'D':
                # Display Passwords
                taglist_path = "taglist.txt"
                with open(taglist_path, "r") as taglist:
                    lines = taglist.readlines()

                    j = 1
                    for line in lines:
                        fileline = line.strip()
                        print(j, ":", fileline)
                        j += 1

                selection = input("Choose password (eg. 1, 2, 3...): ")
                try:
                    selected_line_number = int(selection)
                    if 1 <= selected_line_number <= len(lines):
                        selected_line = get_specific_line(taglist_path, selected_line_number)
                        dpwd = selected_line.strip()
                        pwdd = f.decrypt(dpwd).decode()
                        print("Selected password:", pwdd)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")


            elif dop == 's' or dop == 'S':
                # Save Password
                tag = input("input tag for the password")
                cpwd = input("input Password")
                encrypted_cpwd = f.encrypt(cpwd.encode())
                with open('PwdList.txt', 'ab') as file:
                    file.write(encrypted_cpwd + b'\n')
                with open('taglist.txt', 'a') as file:
                    file.write(tag + '\n')


            elif dop == 'g' or dop == 'G':
                gtag = input("make a tag for your password")
                with open('taglist.txt', 'a') as file:
                    file.write(gtag + '\n')
                plength = int(input("How long should the password be"))
                s = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
                genpass = (''.join(random.sample(s, plength)))
                print("your password is:\n",genpass)
                encrypted_genpass = f.encrypt(genpass.encode())
                with open('PwdList.txt', 'ab') as file:
                    file.write(encrypted_genpass + b'\n')





        else:
            print("wrong password or username")

else:
    key = Fernet.generate_key()

    print("Please make some login credentials")
    susrn = input("Username:")
    susrp = input("Password:")

    # Create a Fernet object with the key
    f = Fernet(key)
    # Encrypt the username and password
    encrypted_username = f.encrypt(susrn.encode())
    encrypted_password = f.encrypt(susrp.encode())
    # Write the encrypted username and password to a file
    with open('log.txt', 'wb') as file:
        file.write(encrypted_username + b'\n')
        file.write(encrypted_password)

    with open('Titan.txt', 'wb') as file:
        file.write(key)

    print('Login details successfully saved!(restart program and login)')
