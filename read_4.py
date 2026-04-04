# Count words in a file

with open("story.txt", "r") as file:
    content = file.read()

words = content.split()
print("Total words:", len(words))