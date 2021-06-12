class Vuelos:
    
    def __init__(self, id, origen, destino):
        self.id = id
        self.origen = origen
        self.destino = destino
        
    def __str__(self):
        return f"vuelo id: {self.id}, origen: {self.origen}, y destino {self.destino }"
    
vuelo_uno = Vuelos(1234, "Jalisco", "New York")
print(vuelo_uno)
    
        
        
    