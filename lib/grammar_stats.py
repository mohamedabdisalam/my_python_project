class GrammarStats:
    def __init__(self):
        self.history = []

    def check(self, text):
        if text[0].isupper():
            if text[-1] in '!.?':
                self.history.append(True)
                return True
            else:
                self.history.append(False)
                return False 
        else:
            self.history.append(False)
            return False
    def percentage_good(self):
        # check the history
        return self.history.count(True) / len(self.history) * 100
