```
we can easy solve this problem using python in built functions such that append,pop()
```


class MinStack(object):
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        if self.stack:
            val=self.stack.pop()
        
    def top(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]
    def getMin(self):
        if not self.stack:
            return None
        else:
            return min(self.stack)
