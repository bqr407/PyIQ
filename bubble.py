class Bubble():
    """Class for bubble objects"""

    def __init__(self, id, x, y, x2, y2, value):
        """each bubble object has these values associated with it"""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.value = value

    def getX(self):
        """returns x1 of tkinter shape"""
        return self.x

    def getY(self):
        """returns y1 of tkinter shape"""
        return self.y

    def getX2(self):
        """returns x2 pos of tkinter shape"""
        return self.x2

    def getY2(self):
        """returns y2 of tkinter shape"""
        return self.y2

    def getID(self):
        """returns unique object identifier"""
        return self.id

    def getValue(self):
        """returns value of the bubble"""
        return self.value

class Choice():
    """Class for choice objects"""

    def __init__(self, id, x, y, x2, y2, value):
        """each choice object has these values associated with it"""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.value = value

    def getX(self):
        """returns x1 of tkinter shape"""
        return self.x

    def getY(self):
        """returns y1 of tkinter shape"""
        return self.y

    def getX2(self):
        """returns x2 pos of tkinter shape"""
        return self.x2

    def getY2(self):
        """returns y2 of tkinter shape"""
        return self.y2

    def getID(self):
        """returns unique object identifier"""
        return self.id

    def getValue(self):
        """returns answer the object represents"""
        return self.value