#Read a File and Display Content
with open("user_1.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)