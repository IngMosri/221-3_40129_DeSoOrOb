class viaje:
    
    def __init__(self, id, id_vuelo, id_pasajero):
        self.id = id
        self.id_vuelo = id_vuelo
        self.id_pasajero = id_pasajero
    
    def __str__(self):
        return f" Vaije: {self.id}, Vuelo{self.id_vuelo}, Pasajero registrado { self.id_pasajero} "
    
    
viaje_uno = viaje(876, 1234, 1456)
print(viaje_uno)
    