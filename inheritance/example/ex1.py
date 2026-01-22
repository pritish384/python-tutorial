class MyString(str):

    def reverse(self):
        return self[::-1]
    
    
    
print(MyString("This is a string").reverse())