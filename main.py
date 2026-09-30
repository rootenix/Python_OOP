class Students:
        def __init__(self, name: str, age: int, score:int):
            self.name=name
            self.age=age
            self.score=score
        def get_status(self):
            if self.score>60:
                    print(f"utding hurmatli {self.name}")
            else:
                  print("Ensheyinlardan so'rab o'rganing, yiqildingiz")

Students("ali",20,80).get_status()