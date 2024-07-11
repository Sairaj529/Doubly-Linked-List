class node:
  def __init__(self,data):
    self.next = None
    self.prev = None
    self.data = data

class dll:
  def __init__(self):
    self.null = None
    self.start = None
    self.end = None

  def insertBeg (self, data):
    newnode = node(data)

    if (self.start == None):
      self.start = newnode
      self.end = newnode

    else:
      newnode.next = self.start
      self.start.prev = newnode
      self.start = newnode

  def insertEnd (self, data):
    newnode = node(data)

    if (self.start == None):
      self.start = newnode
      self.end = newnode
    
    else:
      self.end.next = newnode
      newnode.prev = self.end
      self.end = newnode

  def searchNode (self, data):
    temp = self.start

    while(temp != None):
      if (temp.data == data):
        return temp
      temp = temp.next

    return None

  def insertAfter (self, data, prev_data):
    a = self.searchNode(prev_data)

    if (a == self.null):
      return self.null 

    if(a == self.end):
      self.insertEnd(data)

    else:
      b = node(data)

      c = a.next
      c.prev = b
      b.next = c
      a.next = b
      b.prev = a 

  def insertBefore (self, data, next_data):
    c = self.searchNode(next_data)

    if (c == self.null):
      return self.null 

    if(c == self.start):
      self.insertBeg(data)

    else:
      b = node(data)
      a = c.prev
      a.next = b
      b.prev = a
      b.next = c
      c.prev = b

  def forwardTraversal(self):
    temp = self.start
    while(temp != self.null):
      print(f"{temp.data}",end ="")
      if(temp.next != None):
        print(" -> ",end="")
      temp = temp.next
    print()
    
      

  def deleteBeg(self):
    if(self.start == None):
      return None
    if(self.start == self.end):
      x = self.start
      self.start = None
      self.end = None
      return x

    else:
      y = self.start
      self.start = self.start.next
      self.start.prev = None

      return y

  def deleteEnd(self):
    if(self.start == None):
      return None
    if(self.start == self.end):
      x = self.start
      self.start = None
      self.end = None
      return x
    else:
      y = self.end
      self.end = self.end.prev
      self.end.next = None
      return y

  def delSearch(self,x):
    a = self.searchNode(x)
    if(a == None):
      return None
    if(a == self.start):
      y = self.deleteBeg()
      return y
    if(a == self.end):
      y = self.deleteEnd()
    else:
      a.prev.next = a.next
      a.next.prev = a.prev

      return a
      
      

def main():
  ll = dll()
  ll.insertBeg(1)
  ll.insertBeg(2)
  ll.insertBefore(-1,2)
  ll.forwardTraversal()
  
      
      
    



main()