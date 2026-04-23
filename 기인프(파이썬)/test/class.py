class Myclass:
    def __init__(self,name): ####초기화###
        self.name=name
    
    def f(self):
        return 'hello world',name
    

name='kim'
a=Myclass(name)
print(a.f())
print(a)