class task:
    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category
        # default 1 hour
        self.time = 1
        # default 10 (cannot be modified)
        self.difficulty = 10
    
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def setTime(self, time):
        self.time = time