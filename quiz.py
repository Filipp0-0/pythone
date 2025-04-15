class Student:

    def __init__(self,nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self._score = 0.0 
        self._nOfQuiz = 0

    def getNome(self):
        return f"{self._nome} {self._cognome}"

    def addQuiz(self, score):
        self._score += score
        self._nOfQuiz += 1

    def getTotalScore(self):
        return self._score
        
    def getAverageScore(self): 
        raise ValueError (f"Lo studente {self._nome} {self._cognome}" +
                          "non ha sostenuto prove " )
        return self._score / self._nOfQuiz 
    

Studente1= Student("Mario", "Rossi")
Studente2 = Student("Giovanni", "Verdi")
Studente3 = Student("Luigi", "Bianchi")

Studente1.addQuiz(19)
Studente1.addQuiz(17)
Studente1.addQuiz(18)
Studente1.getAverageScore()

Studente2.addQuiz(20) 
Studente2.addQuiz(19)
Studente2.addQuiz(18)
Studente2.getAverageScore()

Studente3.addQuiz(15)
Studente3.addQuiz(17)
Studente3.addQuiz(16)
Studente3.getAverageScore()
    
       
