#stack--principle
#last in first out-LIFO
class stack:
    def __init__(self):
        self.container=[]#intilization of array or list
        
    def push(self,data):#to add the element in container 
        return self.container.append(data)
        
    def peek(self):#to see the last element in container(array)
        print(self.container[-1])
        return self.container[-1]
        
    def pop(self):#to remove the last element in container or array
        if self.length==0:
            print("there is no elements to pop")
            return 
        return self.container.pop()
        
    def length(self):#length
        return len(self.container)
        
'''---------------------checking-----------------------''' 
a=stack()
a.push(2)
a.push(3)
a.pop()
a.peek()
a.push(5)
a.push(4)
print(a.container)
a.pop()
print(a.container)