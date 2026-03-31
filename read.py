src=open("one.txt","r")
data=src.read()
src.close()

dst=open("bit.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")
