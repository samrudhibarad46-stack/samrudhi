# Append data to file

message = input("Enter a message: ")

with open("notes.txt", "a") as file:
    file.write(message + "\n")

print("Message added successfully!")

# Show updated content
with open("notes.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())