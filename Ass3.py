def modify_content(content):
    return content.upper()  

def read_and_write_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read() 
            modified_content = modify_content(content)  
        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)  

        print(f"Modified content saved in {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read/write the file. Check file permissions.")

read_and_write_file()