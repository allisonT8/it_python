from banner import banner
banner("HTML Tag Counter", "Allison.T")
print("Welcome to the HTML tag counter /\.")

def file_name(tags):
    filename = input("Please enter the name of an HTML file: ")
    file_name = str(tags)
    count = 0
    for file in tags:
        if file in file_name:
            count += 1
    return count
    another = False
    if input("Would you like to enter another HTML file (Y/N)? ") == "Y":
        print("")
        another = True

print("Thanks you for using the HTML Tag counter. Goodbye!")