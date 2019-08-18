

majors = ("CIS" , "Interior Architecture" , "Product Design" , "Mathematics")

print("Majors:")
for name in majors:
    if name == "CIS":
        print( name , " - In great demand")
for name in majors:
    if name is not "CIS":
        print(name)
