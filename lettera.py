class Letter:
    def __init__(self, letterFrom, letterTo, subject, body=""):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self._subject = subject
        self._body = body

    def addLine(self, line):
        self._body += line + "\n"
        return self._body

    def getText(self):
        return f"{self._letterFrom}\n{self._subject}\n{self._body}\n{self._letterTo}"


lettera = Letter(" \nJhon", "Mary","\nI am sorry we must part \nI whish you all the best \n  \nSincerely, ")
print(lettera.getText())
