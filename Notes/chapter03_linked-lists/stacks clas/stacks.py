class Stack(object):
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit 
    def isEmpty(self):
        return len(self.stk)<=0
    def push(self,item):
        if len (self.stk)>=self.limit:
            print ("Stack Overflow")
        else:
            self.stk.append(item)
        print("Stack afte push:",self.stk)
    def pop (self):
        if (len (self.stk)<= 0):
            print("Stack underflow")
        else: 
            return self.stk.pop()
    def peek(self):
        if (len(self.stk)<=0):
            print ("stack underflow")
        else:
            print (self.stk[-1])
