
class A:
    def __init__(self):
        self.string=input("enter string:")

    def fill(self):
        self.vowel_list=[]
        self.consonant_list=[]

        for i in range(len(self.string)):
            if(self.string[i]in'aioue'):
                self.vowel_list.append(self.string[i])
            else:
                self.consonant_list.append(self.string[i])

        print("vowel list:",self.vowel_list)
        print("consonant list:",self.consonant_list)

c=A()
c.fill()