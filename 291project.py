import sys
def enter_prescription():
    print("entered prescription")
    main()
def medical_test():
    main()
def edit_patients():
    main()
def search():
    main()
    
def main():
    print("########welcome to 291 mini project menu########")
    print("###please enter 1 for entering a prescription###")
    print("###please enter 2 for entering a medical test###")
    print("###please enter 3 for editing a patients info###")
    print("###please enter 4 for entering a search query###")
    print("####please enter 5 to terminate this program####")
    choice =int(input("enter your choice:"))
    if (choice == 1):
        enter_prescription()
    elif (choice == 2):
        medical_test()
    elif (choice == 3):
        edit_patients()
    elif (choice == 4):
        search()
    elif (choice == 5):
        sys.exit()
    else:
        main()

main()