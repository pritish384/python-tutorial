
class MyList(list):
    def append(self):
        return "Main nahi karuga append"
    
    def pop(self):
        return "Main karuga pop"
    
ex_list = MyList([1,3,4,5,5,6,3])
print(ex_list.pop())
print(ex_list)

