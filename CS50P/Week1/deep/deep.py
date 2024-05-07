answer = ["42" , "forty two" , "forty-two"]
x=str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
y= x.lower()
if any(item in y for item in answer):
    print("yes")
else:
    print("no")


