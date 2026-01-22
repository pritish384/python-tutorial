t1 = ("Samiksha", [10,20,30,40])
t2 = ("Pritish", [20,304,45045])

my_list = [t1,t2]

my_dict = {
    "team": my_list
}


for item in my_dict["team"]:
    print(item[0])