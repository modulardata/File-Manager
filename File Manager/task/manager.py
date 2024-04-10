import os

# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
def main():
    print("Input the command")
    while True:
        command = input("> ")
        if command == "quit":
            break
        elif command == "pwd":
            print(os.getcwd())
        elif command.startswith("cd"):
            if command == "cd ..":
                print(os.path.basename(os.path.dirname(os.getcwd())))
            elif " " in command:
                path_parts = command.split(" ")
                if len(path_parts) == 2:
                    new_path = os.path.join(os.getcwd(), path_parts[1])
                    if os.path.exists(new_path):
                        os.chdir(new_path)
                        print(os.path.basename(new_path))
                    else:
                        print("No such file or directory")
                else:
                    print("Specify the path to the directory")
            else:
                print("Invalid command")
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
