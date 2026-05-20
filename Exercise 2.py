try:
    
    note = input("Enter a short note/message: ")

    file = open("notes.txt", "w")
    file.write(note)
    file.close()

    
    file = open("notes.txt", "r")
    print("\nContent of file:")
    print(file.read())
    file.close()

    
    new_note = input("\nEnter another note: ")

    file = open("notes.txt", "a")
    file.write("\n" + new_note)
    file.close()

    
    file = open("notes.txt", "r")
    print("\nUpdated content:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("An error occurred:", e)