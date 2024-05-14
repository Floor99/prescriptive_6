# from ass_3.engine import Engine, EngineGene
# from ass_3.team import Team



# class MaintenanceTime:
#     maintenance_type_a = [4 if 1 <= j <= 20 else 3 if 21 <= j <= 55 else 2 if 56 <= j <= 80 else 8 for j in range(1, 100+1)]
#     maintenance_type_b = [t + 1 if 1 <= j <= 25 else t + 2 if 26 <= j <= 70 else t + 1 for j, t in enumerate(maintenance_type_a, start=1)]
    
#     def __init__(self, team: Team, engine: Engine) -> None:
#         self.engine = engine
#         self.team = team
#         self.get_maintenance_time()


#     def get_maintenance_time(self):
#         team_kind = self.team.kind
#         engine_id = self.engine.engine_id 
        
#         if team_kind == "a":
#             self.maintenance_time = self.maintenance_type_a[engine_id-1]
#         else:
#             self.maintenance_time = self.maintenance_type_b[engine_id-1]
    
#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         return f"{class_name}(engine_gene={self.engine_gene!r}, maintenance_time={self.maintenance_time!r})"
        
