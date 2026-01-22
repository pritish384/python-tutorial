file = open("data.txt",'r')

data = file.read()
modified_data = data.replace("donkey", '@#$@@$')
file.close()

file = open("data.txt", 'w')
file.write(modified_data)
