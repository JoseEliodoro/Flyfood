from random import randint, random
from typing import Tuple, List
from math import cos, radians

from house import House

# Função de fatorial
def fat(n: int):
  if n == 0:
    return 1
  return fat(n-1) * n

# Função que gera a população inicial do algoritmo
def create_initial_population(arr: List[object], n_individual: int) -> List[list]:
  
  if (n_individual > fat(len(arr))): 
    n_individual=fat(len(arr))
    
  permuts = [None] * n_individual
  count = 0
  
  while (count < n_individual):
    permut_generacto = sorted(arr, key=lambda x: random())[:len(arr)]
    if not permut_generacto in permuts:
      permuts[count] = permut_generacto
      count += 1
  return permuts


# Função de roleta que escolhe um individuo através de porcentagem
def roulette(lista: List[float]) -> int:
  rand = random() * sum(lista)
  soma = 0
  for i, apt in enumerate(lista):
    soma += apt
    if soma >= rand:
      return i
  return len(lista)-1

# Função de torneio dando chances iguais a todos individuos
def tournament(lista: List[float]) -> int:
  return randint(0, len(lista)-1)


# Função que calcula a distancia de uma rota
def calc_distances(router: List[object], r: object) -> float:
  d= r.distant(router[0])
  for i, el in enumerate(router):
    if i != len(router)-1:
      d += el.distant(router[i+1])
  d += r.distant(router[-1])
  return d

# Função que calcula a distancia de todas as rotas em uma lista
def calc_all_distances(list_city: List[object]) -> List[float]:
  routes = [None] * len(list_city)
  for i, route in enumerate(list_city):
    routes[i] =  calc_distances(route[1:], route[0])
  return routes

# Função que escalona uma lista de números
def scale_list(lst: list[float]) -> float:
  min_val = min(lst)
  max_val = max(lst)
  scaled_lst = [(x - min_val +1) / (max_val - min_val +1) for x in lst]
  return scaled_lst

# Função que calcula a apitidão dos indivíduos
def fitness(pop_list: List[float]) -> List[float]:
  fitness_list = [None] * len(pop_list)
  for index, el in enumerate(pop_list):
    fitness_list[index] = cos(el*radians(90))
  return fitness_list

# Função de cruzamento de genes
def cx(parent1, parent2):
  size = len(parent1)
  index = randint(0, size - 1)
  child = [None] * size
  temp1, temp2 = parent1[index:], parent2[index:] + parent2[:index]
  for i in range(size):
    if parent1[i] in temp2:
      child[i] = parent1[i]
    else:
      child[i] = temp1.pop(0)
  return child

# Função de cruzamento de genes
def PMX(father1, father2):
  cutpoint1 = randint(0, len(father1) - 1)
  cutpoint2 = randint(0, len(father1) - 1)
  if cutpoint1 > cutpoint2:
    cutpoint1, cutpoint2 = cutpoint2, cutpoint1
  
  sons = father1[:]
  
  for i in range(cutpoint1, cutpoint2):
    if father2[i] not in sons[cutpoint1:cutpoint2]:
      j = father1.index(father2[i])
      sons[i], sons[j] = sons[j], sons[i]
  
  for i in range(cutpoint1, cutpoint2):
    if father2[i] not in sons[cutpoint1:cutpoint2]:
      j = father1.index(father2[i])
      sons[j], sons[i] = sons[i], sons[j]

  return sons

# Função de cruzamento de dois pais
def crossover_fathers(father1: List[object], father2: List[object], crossover_rate: float)-> Tuple[list, list] :
  if random() < crossover_rate:
    return cx(father1, father2), cx(father2, father1)
  return father1, father2

# Função de cruzamento de todos os pais
def crossover(fathers_list: List[List[object]], crossover_rate: float) -> List[List[object]]:
  children_list = [None] * len(fathers_list)
  for i in range(0, len(fathers_list), 2):
    son1, son2 = crossover_fathers(fathers_list[i], fathers_list[i + 1], crossover_rate)
    children_list[i], children_list[i + 1] = son1, son2
  return children_list

# Função que retorna uma lista com o nome de cada ponto de entrega em sequência
def Name_route(route: List[List[object]]):
  name = [None] * len(route)
  for i, el in enumerate(route):
    house = []
    for z in el:
      house.append(z.name)
    name[i] = '-'.join(house)
  return name

# Função que imprime uma população
def print_pop(pop_list: List[List[object]], distance_list: List[float], generation: int):
  route_name = Name_route(pop_list)
  better_ind = distance_list.index(min(distance_list))
  """ for i, el in enumerate(route_name):
    print('Rota: %s Distancia: %.3f' %('-'.join(el+el[0]), distance_list[i])) """
  #graph([pop_list[better_ind]], generation)
  print('Melhor solução da %sº geracao é %s e sua distancia foi %.3f.'
    %(generation,(route_name[better_ind]+'-' + route_name[better_ind].split('-')[0]), distance_list[better_ind])
  )

# Função que seleciona um pai
def select_fathers(pop_list: List[List[object]], sel_func):
  staggered_distance = scale_list(calc_all_distances(pop_list))
  fitness_list = fitness(staggered_distance)
  fathers_list = [None] * len(pop_list)
  for count in range(0, len(fathers_list), 2):
    father1 = sel_func(fitness_list)
    father2 = sel_func(fitness_list[:father1]+fitness_list[father1+1:])
    fathers_list[count],fathers_list[count+1] = pop_list[father1], pop_list[father2]
  return fathers_list

# Função de mutação de genes
def mutation(pop_list: List[List[object]], mutation_rate: float):
  for i, el in enumerate(pop_list):
    if random() <= mutation_rate:
      a = randint(0, len(el)-1)
      b = randint(0, len(el)-1)
      pop_list[i][a], pop_list[i][b] = pop_list[i][b], pop_list[i][a]
  return pop_list

# Função de elitismo
def elitismo(population: List[List[object]]) -> List[List[object]]:
  distances_list = calc_all_distances(population)
  fitness_list = fitness(distances_list)
  new_pop = [None] * int(len(fitness_list)/2)
  for i, el in enumerate(new_pop):
    index = roulette(fitness_list)
    new_pop[i] = population.pop(index)
    fitness_list.pop(index)
  #print(new_pop, len(new_pop), )
  return new_pop
    
# Função de evolução que cuida de controlar todas as gerações
def evolution(
  data: List[object], n_individuals: int, n_generations: int, 
  crossover_rate: float, mutation_rate: float, sel_func
) -> Tuple[List[List[object]], List[float]]:
  
  initial_population = create_initial_population(data, n_individuals)
  
  for generation in range(n_generations):
    distances = calc_all_distances(initial_population)
    print_pop(initial_population, distances, generation)
    parents = select_fathers(initial_population, sel_func)
    sons = crossover(parents, crossover_rate)
    mutated_sons = mutation(sons, mutation_rate)
    
    #initial_population = mutated_sons
    initial_population = elitismo(initial_population + mutated_sons)
    
  distances=calc_all_distances(initial_population)
  print_pop(initial_population, distances, generation)
  return initial_population, distances


# Entrada dos dados das cidades
lista = []
a = 'berlin52.tsp'
b ='d198.tsp'
c = 'burma14.tsp'
with open (a) as obj_file:
  text =obj_file.readlines()
  
for i, el in enumerate(text[6:-1]):
  line = []
  for index, x in enumerate(el.replace('\n', ' ').split(' ')):
    if (x != ''):
      line.append(float(x))

  lista.append(House(line[1], line[2], str(int(line[0]))))


p, d = evolution(
  data= lista,
  n_individuals= 20,
  n_generations= 1000,
  crossover_rate=0.8,
  mutation_rate= 0.1,
  sel_func=roulette
)

