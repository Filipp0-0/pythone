class Person:
    def __init__(self, nome, anno_di_nascita):
        self.nome = nome
        self.anno_di_nascita = anno_di_nascita

    def __repr__(self):
        return f"ID: ({self.nome}, {self.anno_di_nascita})"


class Student(Person):

    def __init__(self,nome, anno_di_nascita, iscrizione):
        super().__init__(nome, anno_di_nascita)
        self.iscrizione = iscrizione
        

    def __repr__(self):
        return f"Studente {super().__repr__()} iscritto a: ({self.iscrizione})"
    

class Instructor(Person):
    def __init__(self, nome, anno_di_nascita, salario):
        super().__init__(nome, anno_di_nascita)
        self.salario = salario

    def __repr__(self):
        return f"Istruttore {super().__repr__()} salario di: {self.salario} euro"
    

def main():
    person = Person("Mario Rossi","1990-2-4")
    print(person)
    student = Student("Luca Bianchi", "1995-3-15", "Informatica")
    print(student)
    instructor = Instructor("Mauro Marroni", "1976-2-6", 50000)
    print(instructor)

if __name__ == "__main__":
    main()
