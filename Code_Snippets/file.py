value = 'Hacking'
with open("password.txt", "a+") as file:
    file.seek(0) 
    lines = file.read().splitlines() 
    if value in lines:
        print('value is in file')
    else:
        file.write(value + " ")


f = open("pass.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("pass.txt", "r")
print(f.read())