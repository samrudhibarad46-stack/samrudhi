with open("1.txt","r") as src:
    data = src.read()

with open("2.txt","w") as dst:
    dst.write(data)
    print("data copied successfully")   
