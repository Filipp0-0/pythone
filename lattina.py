import math

class Soda_Can:
    def __init__(self, altezza, raggio):
       
        self._altezza = altezza 
        self._raggio = raggio
       
    def getSurfaceArea(self):
     
        circonferenza = 2 * math.pi * self._raggio
        base_area = 2 * math.pi * self._raggio**2  
        area_laterale = circonferenza * self._altezza
        return area_laterale + 2 * base_area

    def getVolume(self):
        
        base_area = math.pi * self._raggio**2  
        return self._altezza * base_area

mini_lattina = Soda_Can(10, 2)
lattina = Soda_Can (9.24, 3.37)


print(mini_lattina.getSurfaceArea())
print(lattina.getSurfaceArea())
print(mini_lattina.getVolume())
print(lattina.getVolume())
