# file = open("poem.txt",'a')
# file.write()
# file.close()


# Syntax 2

with open("poem.txt","r+") as f:
    print(f.read())
    f.write("Help")

# for j in range(1,101):
#     for i in range(1,11):
#         with open(f'table/table_of_{j}.txt', 'a') as f:
#             f.write(f"{j} x {i} = {j*i}\n")


# str().replace()