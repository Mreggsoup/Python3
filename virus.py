
import time
mylist = ["MUSIC", "BURGER"]

one = input("MUSIC y/n:")

two = input("BURGER y/n:")

view = input("View Survey Results y/n:")

if view == "y":
    mylist.insert(1, one)
    mylist.insert(2, two)

    print(mylist)


for i in mylist:
    mylist.append(one)
    mylist.append(two)
    time.sleep(0)
    print("Final results", mylist)
    time.sleep(0)
    with open('your_file.txt', 'w') as f:
        for item in mylist:
            f.write("%s\n" % item)

