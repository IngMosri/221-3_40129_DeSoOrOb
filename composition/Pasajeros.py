class Pasajeros:
    
    def __init__(self, id, first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"id del pasajero {self.id}, nombre del pasajero : {self.first_name}, Apellido {self.last_name}"
pasajeros_uno = Pasajeros(7, "Juana de arco")
print(pasajero_uno)
viaje_uno =viaje(876, vuelo_uno.id, pasajeros_uno.id)
print(viaje_uno)