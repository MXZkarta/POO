import random
import time

class Moneda:
    def lanzar(self):
        print("Lanzando la moneda...")
        time.sleep(2)
        for _ in range(5):
            print(".")
            time.sleep(0.5)
        opciones = ["Cara", "Cruz"]
        resultado = random.choice(opciones)
        print(f"¡La moneda ha caído en {resultado}!")
        return resultado


class Pistola:
    def __init__(self):
        self.recamara = [0] * 7

    def recargar(self, balas):
        if balas < 0:
            self.recamara = [0] * 7
        elif balas > 7:
            self.recamara = [1] * 7
        else:
            self.recamara = [1] * balas + [0] * (7 - balas)

    def girar_recamara(self):
        print("Girando la recámara...")
        random.shuffle(self.recamara)

    def disparar(self):
        if self.recamara:
            if self.recamara[0] == 1:
                print("¡Bang! La bala impactó.")
                self.recamara.pop(0)
            else:
                print("¡Click! No había bala en la recámara.")
                self.recamara.pop(0)
        else:
            print("La recámara está vacía.")


    def obtener_numero_tiros_restantes(self):
        return len(self.recamara)

    def obtener_espacios_vacios(self):
        espacios_vacios = []
        for i, espacio in enumerate(self.recamara, start=1):
            if espacio == 0:
                espacios_vacios.append(i)
        return espacios_vacios

    def __str__(self):
        if any(self.recamara):
            return f"Pistola (Cargada, Tiros restantes: {self.obtener_numero_tiros_restantes()})"
        else:
            return "Pistola (Descargada)"


class Persona:
    def __init__(self, nombre, pistola=None):
        self.nombre = nombre
        if pistola is None:
            self.pistola = Pistola()
        else:
            self.pistola = pistola

    def recargar_pistola(self, balas):
        self.pistola.recargar(balas)
        print(f"{self.nombre} recargó la pistola con {balas} balas.")
        self.pistola.girar_recamara()
        print("La recámara ha sido girada.")

    def lanzar_volado(self):
        resultado_moneda = Moneda().lanzar()
        eleccion = random.choice(["Cara", "Cruz"])
        print(f"{self.nombre} elige: {eleccion}")
        print(f"Resultado de la moneda: {resultado_moneda}")
        return eleccion, resultado_moneda
    
    def jugar_ruleta_rusa(self, eleccion):
        resultado_moneda = Moneda().lanzar()
        print(f"{self.nombre} elige: {eleccion}")
        print(f"Resultado de la moneda: {resultado_moneda}")
        if resultado_moneda == eleccion:
            self.pistola.recargar()
            self.pistola.girar_recamara()
            print(f"Balas en la recámara: {self.pistola.recamara}")
            self.pistola.disparar()
            print("¡Ganador! Disparas primero.")
            return True
        else:
            print(f"Balas en la recámara: {self.pistola.recamara}")
            print("¡Perdiste! Dispara el otro jugador primero.")
            return False
    
    def tomar_decision_disparo(self, otro_jugador):
        decision = random.choice([self.nombre, otro_jugador.nombre])
        if decision == self.nombre:
            print(f"{self.nombre} decide disparar.")
            self.pistola.disparar()
        else:
            print(f"{self.nombre} decide que {otro_jugador.nombre} dispare.")
            otro_jugador.pistola.disparar()

class Arbitro:
    def __init__(self, jugadores):
        self.jugadores = jugadores

    def comprobar_pistolas_cargadas(self):
        pistolas_cargadas = [jugador for jugador in self.jugadores if any(jugador.pistola.recamara)]
        if pistolas_cargadas:
            print("Pistolas cargadas:")
            for jugador in pistolas_cargadas:
                print(f"- {jugador.nombre}")
        else:
            print("Ninguna pistola está cargada en la recámara.")

    def recargar_pistola(self, jugadores, balas):
        for jugador in jugadores:
            if jugador in self.jugadores:
                jugador.pistola.recargar(balas)
                print(f"El árbitro recargó la pistola de {jugador.nombre} con {balas} balas.")
                jugador.pistola.girar_recamara()
                print("La recámara ha sido girada.")
            else:
                print("El jugador no está en la lista de jugadores del árbitro.")


# Crear tres objetos de la clase Persona
juan = Persona("Juan", Pistola())
pepe = Persona("Pepe", Pistola())

# Crear objeto Arbitro
arbitro = Arbitro([juan, pepe])

# Comprobar las pistolas cargadas antes de recargar
arbitro.comprobar_pistolas_cargadas()

# Recargar la pistola de juan y pepe con 1 bala utilizando el árbitro
arbitro.recargar_pistola([juan, pepe], 2)

# Comprobar las pistolas cargadas después de recargar
arbitro.comprobar_pistolas_cargadas()

# Juan elige cara o cruz
decision_juan = random.choice(["Cara", "Cruz"])

# Pepe elige la opción diferente a la de Juan
decision_pepe = decision_juan
while decision_pepe == decision_juan:
    decision_pepe = random.choice(["Cara", "Cruz"])


print(f"Se realiza el Volado...")

print(f"Decisión de Juan: {decision_juan}")
print(f"Decisión de Pepe: {decision_pepe}")

# Decidir quién dispara primero mediante un volado
resultado_volado = Moneda().lanzar()
ganador_volado = None

if resultado_volado == decision_juan:
    ganador_volado = juan
    perdedor_volado = pepe
    print(f"¡{juan.nombre} ganó el volado!")
else:
    ganador_volado = pepe
    perdedor_volado = juan
    print(f"¡{pepe.nombre} ganó el volado!")

# Asignar la decisión de disparo al ganador del volado
ganador_volado.tomar_decision_disparo(perdedor_volado)

# Imprimir la pistola del ganador
print(f"Pistola del ganador: {ganador_volado.pistola}")

# Imprimir la pistola del perdedor
print(f"Pistola del perdedor: {perdedor_volado.pistola}")

# Obtener los espacios vacíos en la recámara del ganador
espacios_vacios_ganador = ganador_volado.pistola.obtener_espacios_vacios()
print(f"Espacios vacíos en la recámara del ganador: {espacios_vacios_ganador}")

# Obtener los espacios vacíos en la recámara del perdedor
espacios_vacios_perdedor = perdedor_volado.pistola.obtener_espacios_vacios()
print(f"Espacios vacíos en la recámara del perdedor: {espacios_vacios_perdedor}")
