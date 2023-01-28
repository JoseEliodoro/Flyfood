class House():
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
    def distant(self, house):
        return abs(self.x - house.x) + abs(self.y - house.y)
    
    def a(self):
        return self.name

""" a = House(1, 1, 'A')
b = House(3, 2, 'B')
c = House(2, 4, 'C')
d = House(0, 4, 'D') """

""" 
A -> B = 3 
A -> C = 4   B -> C = 3
A -> D = 4   B -> D = 5   C -> D = 2 
"""


""" print('A -> B =', a.distant(b))
print('A -> C =', a.distant(c))
print('A -> D =', a.distant(d))
print('B -> C =', b.distant(c))

print('B -> D =', b.distant(d))
print('C -> D =', c.distant(d))
 """