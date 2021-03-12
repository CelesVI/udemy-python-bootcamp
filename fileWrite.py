f = open("test.txt", "w")
f.write("pink\n")
f.write("white\n")
x = ["red","blue","green","yellow"]
for i in x:
    f.write(i + "\n")
f.close()
