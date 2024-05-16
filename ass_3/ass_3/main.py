from ass_3.algorithm import GeneticAlgorithm
from ass_3.constraints import CompletesMaintenanceIn30Days, Day31Constraint, TeamWorksAtOneEngine
from ass_3.cross_over import SingleCrossOver
from ass_3.initialization import Initializer
from ass_3.mutation import UniformCrossMutation
from ass_3.selection import RouletteWheelSelection
from ass_3.termination import TimeTermination
import pandas as pd



CHROMOSOME_LENGTH = 168
POPULATION_SIZE = 200
MAX_DURATION = 5*60
NR_OF_PARENTS = 10
MUTATION_PROBABILITY = 0.1
MATING_PROBABILITY = 0.9

CONSTRAINTS = [
    Day31Constraint(),
    CompletesMaintenanceIn30Days(),
    TeamWorksAtOneEngine(),
]

initializer= Initializer(chromosome_length=CHROMOSOME_LENGTH, population_size=POPULATION_SIZE, constraints=CONSTRAINTS)
termination_strategy= TimeTermination(max_duration=MAX_DURATION)
selection_strategy= RouletteWheelSelection(nr_of_parents=NR_OF_PARENTS)
crossover_strategy= SingleCrossOver()
mutation_strategy= UniformCrossMutation(mutation_probability=MUTATION_PROBABILITY)



def main():
    algo = GeneticAlgorithm(
        initializer=initializer,
        termination_strategy=termination_strategy,
        selection_strategy=selection_strategy,
        crossover_strategy=crossover_strategy,
        mutation_strategy=mutation_strategy,
        mating_probability=MATING_PROBABILITY,
        constraints=CONSTRAINTS
    )
    
    best_chromosome = algo.run_algorithm()
    print(best_chromosome)
    
    engine_ids = best_chromosome.engine_ids
    teams_kind = [engine_gene.team.kind for engine_gene in best_chromosome.engine_genes]
    teams = [engine_gene.team.team + 1 for engine_gene in best_chromosome.engine_genes]
    safety_day = [engine_gene.engine.safety_day for engine_gene in best_chromosome.engine_genes]
    start_day = [engine_gene.start_day.start_day for engine_gene in best_chromosome.engine_genes]
    end_day = [engine_gene.start_day.start_day + engine_gene.maintenance_time for engine_gene in best_chromosome.engine_genes]
    penalty = [engine_gene.penalty.penalty for engine_gene in best_chromosome.engine_genes]
    
    total_cost = best_chromosome.penalty
    
    print(f"{engine_ids= }")
    print("----------")
    print(f"{teams_kind= }")
    print("----------")
    print(f"{teams= }")
    print("----------")
    print(f"{safety_day= }")
    print("----------") 
    print(f"{start_day= }")
    print("----------")
    print(f"{end_day= }")
    print("----------")
    print(f"{penalty= }")
    print("----------")
    print(f"{total_cost= }")
    print("----------")
    
    dict_final = {'engine id' : engine_ids,
                  'team type' : teams_kind,
                  'teams' : teams,
                  'safety day' : safety_day,
                  'start day' : start_day,
                  'end day' : end_day,
                  'penalty' : penalty}
    
    df_final = pd.DataFrame(dict_final).sort_values(["teams", "start day"], axis=0)
    print(df_final)

    
    
    

if __name__ =="__main__":
    main()