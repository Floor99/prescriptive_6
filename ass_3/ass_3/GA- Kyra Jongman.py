######################################### IMPORT PACKAGES ########################################################################
import pandas as pd
import numpy as np

######################################### INITIALIZE VARIABLES ########################################################################
# Total number of engines
M = 100 

# Planning Horizon
T = 30

# Team A maintenance days
maint_type_A = [4 if 1 <= j <= 20 else 3 if 21 <= j <= 55 else 2 if 56 <= j <= 80 else 8 for j in range(1, M+1)]

# Team B maintenance days
maint_type_B = [t + 1 if 1 <= j <= 25 else t + 2 if 26 <= j <= 70 else t + 1 for j, t in enumerate(maint_type_A, start=1)]

# Penalty costs
cj = [4 if 1 <= j <= 20 else 3 if 21 <= j <= 30 else 2 if 31 <= j <= 45 else 5 if 46 <= j <= 80 else 6 for j in range(1, M+1)]

# Four different teams
G = ["T1", "T2", "T3", "T4"]

# Teams with type A
teams_with_type_A = ["T1", "T3"]
print(f"Teams {G[0]} and {G[2]} are of type A")

# Team with type B
teams_with_type_B = ["T2", "T4"]
print(f"Teams {G[1]} and {G[3]} are of type B")

# Load the provided prediction data
prediction_data = pd.read_csv("ass_3/data/RUL_consultancy_predictions_A3-2.csv", sep= ";")

# Identify engines requiring maintenance in the next 30 days
df = prediction_data[prediction_data['RUL'] <= 29]
maint_engines = df['id'].tolist()

######################################### FITNESS FUNCTION ########################################################################
# Function to calculate penalties for a team
def calculate_team_penalty(team, engines, safety_due_dates_engines, max_penalty=250, T=30):
    total_penalty = 0
    start_day = 1
    
    for engine in engines:
        maint_days = maint_type_A[engine - 1] if team in teams_with_type_A else maint_type_B[engine - 1]
        end_day = start_day + maint_days - 1
        
        safety_due_date = safety_due_dates_engines[engine]
        if end_day > safety_due_date:
            days_after_safety_due_date = end_day - safety_due_date
            penalty_costs = cj[engine - 1] * (days_after_safety_due_date ** 2)
            penalty_costs = min(penalty_costs, max_penalty)
            total_penalty += penalty_costs

        if end_day > T:
            extra_days = end_day - T
            exceed_planning_horizon = 400 * extra_days  
            total_penalty += exceed_planning_horizon
        
        start_day = end_day + 1
    return total_penalty
    
def fitness(population, safety_due_dates_engines):
    penalties_whole_population = []
    # Process each solution in the population
    for solution in population:
        team_engines = {}  # Use a standard dictionary

        # Aggregate engines by teams for each solution
        for team_engine_schedule in solution:
            for engine, team in team_engine_schedule.items():
                if team not in team_engines:
                    team_engines[team] = []
                team_engines[team].append(engine)
        
        # Calculate penalties for each team and sum for the whole solution
        total_solution_penalty = 0
        for team, engines in team_engines.items():
            team_penalty = calculate_team_penalty(team, engines, safety_due_dates_engines)
            total_solution_penalty += team_penalty
        penalties_whole_population.append(total_solution_penalty)
    return penalties_whole_population

######################################### INITIALIZING THE POPULATION ########################################################################
def initialize_population(population_size: int, G: list, maint_engines: list):
    maint_schedule_for_whole_population = []
    for _ in range(population_size):
        maint_schedule_engines = []

        for engine in maint_engines:
            chosen_team = np.random.choice(G)
            maint_schedule_engines.append({engine: (chosen_team)})
        
        maint_schedule_for_whole_population.append(maint_schedule_engines)
    return maint_schedule_for_whole_population

population = initialize_population(5, G, maint_engines)
print(population)
######################################### SELECTION ########################################################################
def selection_roulette_wheel(population, fitness_values):
    inverted_values = [1.0 / value for value in fitness_values]
    probabilities = np.array(inverted_values) / sum(inverted_values)
    id = np.random.choice(len(population), size=2, p=probabilities, replace=False)
    return population[id[0]], population[id[1]]

############################################# CROSSOVER #############################################################################
def crossover(parent1, parent2):
    # Calculate the crossover point
    crossover_point = np.random.randint(1, len(parent1) - 1)

    # Create offspring by combining parts from both parents
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

############################################# MUTATE #############################################################################

def mutate(child, mutation_rate=0.2):
    # Assuming possible teams are from T1 to T4
    possible_teams = G
    
    # Iterate through each dictionary in the list
    for engine in child:
        if np.random.rand() < mutation_rate:
            engine, current_team = list(engine.items())[0]
            # Choose a new team different from the current one
            new_teams = [team for team in possible_teams if team != current_team]
            new_team = np.random.choice(new_teams)
            # Update the team for the engine
            engine[engine] = new_team
    return child 

############################################################################################

def genetic_algorithm(population, num_generations, elitism_size, safety_due_dates_engines):
    for generation in range(num_generations):
        fitness_scores = fitness(population, safety_due_dates_engines)
        paired_population = sorted(zip(population, fitness_scores), key=lambda x: x[1])
        new_population = [indiv for indiv, _ in paired_population[:elitism_size]]

        while len(new_population) < len(population):
            parent1, parent2 = tournament_selection(population, fitness_scores)[0], tournament_selection(population, fitness_scores)[1]
            if random.random() < 0.8:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
            
        population = new_population
        print(f"Generation {generation + 1}: Best Penalty = {paired_population[0][1]}")

    return population

# Initialize and run the genetic algorithm
population_size = 100
num_generations = 150
elitism_size = 5
population = initialize_population(population_size, G, maint_engines)
final_population = genetic_algorithm(population, num_generations, elitism_size, safety_due_dates_engines)