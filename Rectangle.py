class Rectangle:
  def __init__(self,x,y,h,w):
    self.x = x
    self.y = y
    self.height = h
    self.width = w

    if x<0:
      self.x = 0
    if y<0:
      self.y = 0
    if h<0:
      self.height = 0
    if w<0:
      self.width = 0
      

  def __str__(self):
    return "(x:" + str(self.x) + ",y:" + str(self.y) + ")" + " width:" + str(self.width) + " height:" + str(self.height)
  