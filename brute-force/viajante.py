from input import DateInput
from permutation import permut
from time import process_time

def menor(routes, r):
    minim, rt = 0, ''
    
    for x in range(len(routes)):
        route = ['R']
        distanci = [r.distant(routes[x][0])]
        for y in range(len(routes[x])):
            route.append(routes[x][y].name)
            
            if (y < len(routes[x])-1):
                distanci.append(routes[x][y].distant(routes[x][y+1]))
        
        route.append('R')
        distanci.append(r.distant(routes[x][-1]))
        if minim == 0 or minim > sum(distanci):
            minim = sum(distanci)
            rt = route
        
    return 'A menor rota é %s com exatos %d dronômetros'%(rt, minim)
    


        

def menor_distancia_file(url):
    datas = DateInput(url)
    
    routes = datas.create_router(datas.read_file())
    
    r = list(filter(lambda el: el.name in 'R', routes))[0]
    routes = permut(list(filter(lambda el: not el.name in 'R', routes)))
    
    return menor(routes, r)
""" 
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0

A 0 0 0 L 0
0 E 0 0 0 0
0 0 0 K 0 R
Y 0 0 0 0 0
G 0 0 I 0 Z

0 J 0 0 L
U 0 N M 0
Y H 0 0 0
A B T 0 0
0 0 0 0 R
"""
a = process_time()
print(menor_distancia_file('route.txt'))
b = process_time()
print('%.90f'%(b-a))