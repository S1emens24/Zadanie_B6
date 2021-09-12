class Rectangle:

    def __init__(self, w, l):
        self.width = w
        self.length = l

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(15, 4)
print(newRectangle.rectangle_area())