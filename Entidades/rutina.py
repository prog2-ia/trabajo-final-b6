
class Rutina:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitos = []  # Lista de objetos Habito

    def agregar_habito(self, habito):
        self.habitos.append(habito)

    def __add__(self, otra_rutina):  # Unir rutinas
        nueva = Rutina(f"{self.nombre} + {otra_rutina.nombre}")
        nueva.habitos = self.habitos + otra_rutina.habitos
        return nueva

    def __lt__(self, otra_rutina):  # Comparar progreso (menor si menos hábitos completados)
        self_completados = sum(1 for h in self.habitos if h.cumplido())
        otra_completados = sum(1 for h in otra_rutina.habitos if h.cumplido())
        return self_completados < otra_completados

    def __iadd__(self, valor):  # Ajustar rachas en todos los hábitos
        for h in self.habitos:
            if hasattr(h, 'racha'):
                h.racha += valor
        return self

    def exportar_resumen(self):
        resumen = f"Resumen de {self.nombre}:\n"
        for h in self.habitos:
            completado = "Sí" if h.cumplido() else "No"
            resumen += f"- {h.nombre}: Completado: {completado}, Racha: {getattr(h, 'racha', 0)}\n"
        return resumen