# Name should be str, piece and score should be int
class Player:
    def __init__(self, name, piece, score):
        self.name = name
        self.piece = piece
        self.score = score
    
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score

    def get_name(self):
        return self.name

    def get_piece(self):
        return self.piece