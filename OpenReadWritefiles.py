
with open("text_file.txt", mode='a') as file:
    file.write("hi i am zoya")

file = open("text_file.txt")
contents = file.read()
print(contents)
file.close()

with open("text_file.txt", mode='a') as file:
    file.write("\ni am a cutie pie")

with open("text_file.txt") as file:
    contents = file.read()
    print(contents)

with open("text_file.txt", mode='w') as file:
    contents = file.write("i am a cutie pie")
    print(contents)



