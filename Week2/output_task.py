print("What type of book is this?")
book_name=input()
if book_name == "adventure":
    print(f"I like {book_name} books")
print("Finished reading book.")

print("Please enter the activity to be performed.")
activity=input()
if activity == "calculate":
    print(f"Performing: {activity}")
else:
    print("Activity completed")