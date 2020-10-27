import random
import math
import time
import numpy as np
from generator_problem import GeneratorProblem



class Solve:

    def __init__(self, n_generator, n_device, seed):

        self.n_generator = n_generator
        self.n_device = n_device
        self.seed = seed

        self.instance = GeneratorProblem.generate_random_instance(self.n_generator, self.n_device, self.seed)

    def solve_naive(self):

        print("Solve with a naive algorithm")
        print("All the generators are opened, and the devices are associated to the closest one")

        opened_generators = [1 for _ in range(self.n_generator)]

        assigned_generators = [None for _ in range(self.n_device)]

        for i in range(self.n_device):
            closest_generator = min(range(self.n_generator),
                                    key=lambda j: self.instance.get_distance(self.instance.device_coordinates[i][0],
                                                                      self.instance.device_coordinates[i][1],
                                                                      self.instance.generator_coordinates[j][0],
                                                                      self.instance.generator_coordinates[j][1])
                                    )

            assigned_generators[i] = closest_generator

        self.instance.solution_checker(assigned_generators, opened_generators)
        total_cost = self.instance.get_solution_cost(assigned_generators, opened_generators)
        self.instance.plot_solution(assigned_generators, opened_generators)

        print("[ASSIGNED-GENERATOR]", assigned_generators)
        print("[OPENED-GENERATOR]", opened_generators)
        print("[SOLUTION-COST]", total_cost)
        
    def solve_ls(self):

        print("Solve with a local search algorithm")
        print("The devices are associated to the closest generator", "\n")
        tps1 = time.time()
        
        # Declaration de constante
        pop_size = 500
        proportion_retenue = 0.5
        nb_solution_gardée = round(pop_size*proportion_retenue)
        nb_generation_max = 100
        
        # Initailisation de la population
        list_of_good_solutions = init_population(pop_size, self, proportion_retenue, nb_solution_gardée)
        
        for i in range(0, nb_generation_max):
            tps3 = time.time()
            list_of_good_solutions = next_generation(list_of_good_solutions, pop_size, nb_solution_gardée, self)    
            tps4 = time.time()
            print("\nTEMPS ITERATION i=", i," : ", round(tps4 - tps3, 2))
        
        # # Affichage du final
        # self.instance.plot_solution(assigned_generators, opened_generators)
        tps2 = time.time()
        # print("[ASSIGNED-GENERATOR]", assigned_generators)
        # print("[OPENED-GENERATOR]", opened_generators)
        # print("[SOLUTION-COST]", total_cost)
        print("\nTEMPS D'EXECUTION : ", round(tps2 - tps1, 2))

def declaration_des_generateur(self):
    
    # Declaration de liste
    opened_generators = []
    list_of_opened_generators = []
            
    # Decision aléatoire de quel générateur est allumé ou éteint
    for i in range(self.n_generator):
                opened_generators.append(random.randint(0, 1))
                if (opened_generators[i]):
                    list_of_opened_generators.append(i)
    
    # Cas ou aucun générateur n'a été allumé
    if (len(list_of_opened_generators) <= 0):
        generateur_solo = random.randint(0, self.n_generator-1)
        opened_generators[generateur_solo] = 1
        list_of_opened_generators.append(generateur_solo)
    
    return(opened_generators, list_of_opened_generators)

def closest_generator_func(self, list_of_opened_generators):
    
    # Association des machines au générateur le plus proche
    assigned_generators = [None for _ in range(self.n_device)]
    for i in range(self.n_device):
        closest_generator = min(list_of_opened_generators,
                                key=lambda j: self.instance.get_distance(self.instance.device_coordinates[i][0],
                                                                     self.instance.device_coordinates[i][1],
                                                                     self.instance.generator_coordinates[j][0],
                                                                     self.instance.generator_coordinates[j][1])
                                        )
        assigned_generators[i] = closest_generator
    return(assigned_generators)
                
def init_population(pop_size, self, proportion_retenue, nb_solution_gardée):
    
    # Declaration de liste
    list_of_good_solutions = []
    
    # Initailisation de la population
    for i in range(0, pop_size):
        
        # Declaration des generateurs allumés
        test_opened_generators, list_of_opened_generators = declaration_des_generateur(self)
        
        # Association des machines au générateur le plus proche
        test_assigned_generators = closest_generator_func(self, list_of_opened_generators)
        
        # Test de la solution et calcul du cout 
        self.instance.solution_checker(test_assigned_generators, test_opened_generators)
        test_cost = self.instance.get_solution_cost(test_assigned_generators, test_opened_generators)
        
        # Mise en mémoire des meilleurs solutions
        #list_of_good_solutions = selection_solution(test_assigned_generators, test_cost, nb_solution_gardée)
        compteur = 0
        if (len(list_of_good_solutions) == 0):
            list_of_good_solutions.append([test_opened_generators, test_cost])
        elif (len(list_of_good_solutions) < nb_solution_gardée):
            ajoute = False
            for solution, cout in list_of_good_solutions:
                if(test_cost < cout):
                    list_of_good_solutions.insert(compteur, [test_opened_generators, test_cost])
                    ajoute = True
                    break
                compteur += 1
            if (not(ajoute)):
                list_of_good_solutions.append([test_opened_generators, test_cost])
        else:
            ajoute = False
            for solution, cout in list_of_good_solutions:
                if(test_cost < cout):
                    list_of_good_solutions.insert(compteur, [test_opened_generators, test_cost])
                    ajoute = True
                    break
                compteur += 1
            if (ajoute):
                list_of_good_solutions.pop()
                     
    print(list_of_good_solutions, "\n")
    return(list_of_good_solutions)
    
def selection_solution(test_opened_generators, test_cost, nb_solution_gardée):
    list_of_good_solutions = []
    compteur = 0
    if (len(list_of_good_solutions) == 0):
        list_of_good_solutions.append([test_opened_generators, test_cost])
    elif (len(list_of_good_solutions) < nb_solution_gardée):
        ajoute = False
        for solution, cout in list_of_good_solutions:
            if(test_cost < cout):
                list_of_good_solutions.insert(compteur, [test_opened_generators, test_cost])
                ajoute = True
                break
            compteur += 1
        if (not(ajoute)):
            list_of_good_solutions.append([test_opened_generators, test_cost])
    else:
        ajoute = False
        for solution, cout in list_of_good_solutions:
            if(test_cost < cout):
                list_of_good_solutions.insert(compteur, [test_opened_generators, test_cost])
                ajoute = True
                break
            compteur += 1
        if (ajoute):
            list_of_good_solutions.pop()
    return (list_of_good_solutions)

def next_generation(list_of_solutions, pop_size, nb_solution_gardée, self):
    # Declaration de constante
    proportion_cross = 0.6
    proportion_mutat = 0.3
    
    # Declaration de liste
    list_of_new_solutions = []
    list_of_good_solutions = []
    
    # Crossover et mutation
    list_of_new_solutions += handle_crossover(pop_size, proportion_cross, nb_solution_gardée, list_of_solutions, self)
    list_of_new_solutions += handle_mutations(pop_size, proportion_mutat, nb_solution_gardée, list_of_solutions, self)
    
    # Un peu de aléatoire
    while (len(list_of_new_solutions) < pop_size):
        new_random_generators, garboge = declaration_des_generateur(self)
        list_of_new_solutions.append(new_random_generators)  
    #print(list_of_new_solutions)    
    
    # Crealtion de la list of open generators
    for solution in list_of_new_solutions:
        open_generators = []
        for generator in range(0, len(solution)):
            if (solution[generator]):
                open_generators.append(generator)
                
        # Association des machines au générateur le plus proche
        
        assigned_generators = closest_generator_func(self, open_generators)
        
        # Test de la solution et calcul du cout 
        self.instance.solution_checker(assigned_generators, solution)
        test_cost = self.instance.get_solution_cost(assigned_generators, solution)      
        
        # Mise en mémoire des meilleurs solutions
        compteur = 0
        if (len(list_of_good_solutions) == 0):
            list_of_good_solutions.append([solution, test_cost])
        elif (len(list_of_good_solutions) < nb_solution_gardée):
            ajoute = False
            for solution, cout in list_of_good_solutions:
                if(test_cost < cout):
                    list_of_good_solutions.insert(compteur, [solution, test_cost])
                    ajoute = True
                    break
                compteur += 1
            if (not(ajoute)):
                list_of_good_solutions.append([solution, test_cost])
        else:
            ajoute = False
            for solution, cout in list_of_good_solutions:
                if(test_cost < cout):
                    list_of_good_solutions.insert(compteur, [solution, test_cost])
                    ajoute = True
                    break
                compteur += 1
            if (ajoute):
                list_of_good_solutions.pop()
                
    print(list_of_good_solutions[0:4], "\n\n")
    return(list_of_good_solutions)

def handle_mutations(pop_size, proportion_mutat, nb_solution_gardée, list_of_solutions, self):
    
    list_of_mutated = []
    for i in range(0, round(pop_size*proportion_mutat)):
        # Choix des solution a muter       
        chosen_solution = nb_solution_gardée - round(nb_solution_gardée*random.betavariate(1, 0.3))
        while (chosen_solution >= nb_solution_gardée):
            chosen_solution = nb_solution_gardée - round(nb_solution_gardée*random.betavariate(1, 0.3))
        list_of_mutated.append(list_of_solutions[chosen_solution][0])
        
        # Choix des mutations
        p_mutation = random.random()
        mutated_generators = []
        if(p_mutation < 0.6):
            mutated_generators.append(random.randint(0, self.n_generator-1))
        elif (p_mutation < 0.9):
            mutated_generators.append(random.randint(0, self.n_generator-1))
            mutated_generators.append(random.randint(0, self.n_generator-1))
        else:
            mutated_generators.append(random.randint(0, self.n_generator-1))
            mutated_generators.append(random.randint(0, self.n_generator-1))
            mutated_generators.append(random.randint(0, self.n_generator-1))
        
        # Application des mutations
        #print("avant changement", list_of_mutated[i], "\nliste de changement", mutated_generators)
        for m_generator in mutated_generators:
            if (list_of_mutated[i][m_generator]):
                list_of_mutated[i][m_generator] = 0
            else:
                list_of_mutated[i][m_generator] = 1
        #print("apres changement", list_of_mutated[i])
    #print(list_of_mutated)
    return (list_of_mutated)

def handle_crossover(pop_size, proportion_cross, nb_solution_gardée, list_of_solutions, self):
    list_of_cross = []
    for i in range(0, round(pop_size*proportion_cross)):
        
        # Setup des parametre
        chosen_parent1 = nb_solution_gardée - round(nb_solution_gardée*random.betavariate(1, 0.3))
        while(chosen_parent1 >= nb_solution_gardée):
            chosen_parent1 = nb_solution_gardée - round(nb_solution_gardée*random.betavariate(1, 0.3))
        chosen_parent2 = chosen_parent1
        while (chosen_parent1 == chosen_parent2 and chosen_parent1 >= nb_solution_gardée):
            chosen_parent2 = nb_solution_gardée - round(nb_solution_gardée*random.betavariate(1, 0.3))
        #print("p1", chosen_parent1)
        #print("p2", chosen_parent2)
        parent1 = list_of_solutions[chosen_parent1][0]
        parent2 = list_of_solutions[chosen_parent2][0]
        borne_inf = random.randint(0, self.n_generator-1)
        borne_sup = borne_inf
        while (borne_inf == borne_sup):
            borne_sup = random.randint(0, self.n_generator-1)
        if (borne_sup < borne_inf): 
            temp = borne_inf
            borne_inf = borne_sup
            borne_sup = temp
        
        # Gestion enfant
        enfant = parent1[0:borne_inf] + parent2[borne_inf:borne_sup] + parent1[borne_sup:self.n_generator]
        #print(enfant)
        list_of_cross.append(enfant)
    return (list_of_cross)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))