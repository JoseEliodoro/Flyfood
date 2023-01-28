from house import House
class DateInput():
    
    def __init__(self, url):
        self.url = url
        
    def read_file(self):
        with open(self.url, 'r') as obj:
            line = obj.readlines()
        return line
    
    def create_matriz(self, text):
        matriz = [x.replace('\n','').split(' ') for x in text]
        return matriz
    
    
    def create_routes(self, matriz):
        position = []
        for x in range(len(matriz)):
            for y in range(len(matriz[x])):
                if matriz[x][y] != '0': position.append(House(x, y, matriz[x][y]))
        return position
    
    def create_router(self, text):
        x = 0
        position = []

        for line in text:
            ln = line.replace('\n', '').split(' ')
            for y in range(len(ln)):
                if ln[y] != '0': position.append(House(x, y, ln[y]))
            x += 1
        return position
    
""" test = DateInput('route.txt')
print(test.create_routes(test.create_matriz(test.read_file())))
print(test.create_router(test.read_file()))
test.read_file() """