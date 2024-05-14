from ass_3.day import StartDay
from ass_3.engine import Engine
from ass_3.penalty import EnginePenalty
from ass_3.team import Team


class EngineGene:
    maintenance_type_a = [4 if 1 <= j <= 20 else 3 if 21 <= j <= 55 else 2 if 56 <= j <= 80 else 8 for j in range(1, 100+1)]
    maintenance_type_b = [t + 1 if 1 <= j <= 25 else t + 2 if 26 <= j <= 70 else t + 1 for j, t in enumerate(maintenance_type_a, start=1)]

    def __init__(self, engine_id:int, bits:list[int]) -> None:
        self.engine_id = engine_id
        self.bits = bits
        self.decode_bits()
        self.get_maintenance_time()
        self.get_penalty()

    def decode_bits(self) -> None:
        self.start_day = StartDay(self.bits[2:])
        self.team = Team(self.bits[:2])
        self.engine = Engine(engine_id=self.engine_id)


    def get_maintenance_time(self):
        team_kind = self.team.kind
        engine_id = self.engine.engine_id

        if team_kind == "a":
            self.maintenance_time = self.maintenance_type_a[engine_id-1]

        else:
            self.maintenance_time = self.maintenance_type_b[engine_id-1]


    def get_penalty(self) -> None:
        if self.start_day.start_day == 0:
            self.start_day.start_day = 9999999999
            
        self.penalty = EnginePenalty(self.start_day, self.engine)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}(engine_id={self.engine_id!r}, bits={self.bits!r}, start_day={self.start_day!r}, team={self.team!r})"