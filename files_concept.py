# file = open("poem.txt",'a')
# file.write()
# file.close()


# Syntax 2

# with open("poem.txt","r+") as f:
#     print(f.read())
#     f.write("Help")

n = 5
for i in range(1,11):
    with open('table.txt', 'a') as f:
        f.write(f"{n} x {i} = {n*i}\n")