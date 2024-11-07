class ScoreTracker:
    def __init__(self):
        self.scores = {"X": {"win": 0, "loss": 0, "draw": 0},
                       "O": {"win": 0, "loss": 0, "draw": 0}}

    def update_score(self, result):
        if result == "X":
            self.scores["X"]["win"] += 1
            self.scores["O"]["loss"] += 1
        elif result == "O":
            self.scores["O"]["win"] += 1
            self.scores["X"]["loss"] += 1
        elif result == "draw":
            self.scores["X"]["draw"] += 1
            self.scores["O"]["draw"] += 1

    def reset_scores(self):
        self.scores = {"X": {"win": 0, "loss": 0, "draw": 0},
                       "O": {"win": 0, "loss": 0, "draw": 0}}
