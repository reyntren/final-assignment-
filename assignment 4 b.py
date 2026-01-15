# assignment 4 part b

names = []  # list to store names

# keep asking for words until the user enters "quit"
while True:
    word = input("Enter a word (type 'quit' to stop): ")

    # check sentinel value
    if word == "quit":
        break

    # validate input (do not allow empty strings)
    if word != "":
        names.append(word)

# display all words entered
print("\nWords entered:")
for name in names:
    print(name)

# ask if the user wants to check a name
choice = input("\nDo you want to check if a name exists in the list? (yes/no): ")

if choice == "yes":
    check_name = input("Enter the name to check: ")

    # check if the name is in the list
    if check_name in names:
        print(check_name, "is in the list!")
    else:
        print(check_name, "is not in the list!")
