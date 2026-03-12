"""
Archivo de demostración - Muestra cómo usar todas las clases
Ejecutar con: python demo.py
"""

from entidades import *
from persistencia.RepositorioHabito import RepositorioHabito
from servicios.ServiciosHabitos import ServiciosHabitos


def demo_validacion():
    """Demostración de validación de datos"""
    print("\n" + "="*60)
    print("1️⃣ DEMOSTRACIÓN DE VALIDACIÓN")
    print("="*60)
    
    # Validación correcta
    try:
        Validador.validar_nombre("Estudiar")
        print("✓ Nombre válido: 'Estudiar'")
    except HabitoInvalidoError as e:
        print(f"✗ Error: {e}")
    
    # Validación con error
    try:
        Validador.validar_nombre("Xyz")
        print("✓ Nombre válido: 'Xyz'")
    except HabitoInvalidoError as e:
        print(f"✗ Error: {e}")
    
    # Validar frecuencia
    try:
        Validador.validar_frecuencia("diario")
        print("✓ Frecuencia válida: 'diario'")
    except FrecuenciaInvalidaError as e:
        print(f"✗ Error: {e}")


def demo_habitos(servicios: ServiciosHabitos):
    """Demostración de crear hábitos"""
    print("\n" + "="*60)
    print("2️⃣ DEMOSTRACIÓN DE CREACIÓN DE HÁBITOS")
    print("="*60)
    
    try:
        # Crear hábito check
        h1 = servicios.crear_habito_check("h1", "Meditar", "diario")
        print(f"✓ Creado: {h1}")
        
        # Crear hábito de cantidad
        h2 = servicios.crear_habito_cantidad("h2", "Beber agua", "diario", objetivo=2.0)
        print(f"✓ Creado: {h2}")
        
        # Crear otro hábito
        h3 = servicios.crear_habito_check("h3", "Hacer ejercicio", "semanal")
        print(f"✓ Creado: {h3}")
        
        h4 = servicios.crear_habito_cantidad("h4", "Leer páginas", "diario", objetivo=30.0)
        print(f"✓ Creado: {h4}")
        
    except HabitoInvalidoError as e:
        print(f"✗ Error: {e}")


def demo_operaciones(servicios: ServiciosHabitos):
    """Demostración de operaciones sobre hábitos"""
    print("\n" + "="*60)
    print("3️⃣ DEMOSTRACIÓN DE OPERACIONES")
    print("="*60)
    
    # Marcar un check como completado
    if servicios.marcar_completado("h1"):
        print("✓ Hábito h1 marcado como completado")
    
    # Agregar cantidad
    if servicios.agregar_cantidad("h2", 0.5):
        print("✓ Agregados 0.5 litros al hábito h2")
    
    if servicios.agregar_cantidad("h2", 1.5):
        print("✓ Agregados 1.5 litros al hábito h2 (TOTAL: 2.0 - CUMPLIDO ✓)")
    
    if servicios.agregar_cantidad("h4", 20):
        print("✓ Agregadas 20 páginas al hábito h4")
    
    if servicios.agregar_cantidad("h4", 10):
        print("✓ Agregadas 10 páginas al hábito h4 (TOTAL: 30.0 - CUMPLIDO ✓)")


def demo_consultas(servicios: ServiciosHabitos):
    """Demostración de consultas"""
    print("\n" + "="*60)
    print("4️⃣ DEMOSTRACIÓN DE CONSULTAS")
    print("="*60)
    
    # Obtener todos
    print("\n📋 Todos los hábitos:")
    for h in servicios.obtener_todos():
        print(f"  {h}")
    
    # Obtener por tipo
    print("\n✓ Hábitos tipo CHECK:")
    for h in servicios.obtener_por_tipo("check"):
        print(f"  {h}")
    
    print("\n📊 Hábitos tipo CANTIDAD:")
    for h in servicios.obtener_por_tipo("cantidad"):
        print(f"  {h}")
    
    # Obtener por frecuencia
    print("\n📅 Hábitos DIARIOS:")
    for h in servicios.obtener_por_frecuencia("diario"):
        print(f"  {h}")


def demo_notificadores():
    """Demostración de notificadores polimórficos"""
    print("\n" + "="*60)
    print("5️⃣ DEMOSTRACIÓN DE NOTIFICADORES (POLIMORFISMO)")
    print("="*60)
    
    # Crear gestor
    gestor = GestorNotificadores()
    
    # Registrar diferentes notificadores
    gestor.registrar_notificador(NotificadorConsola())
    
    email = NotificadorEmail()
    email.agregar_destinatario("usuario@example.com")
    gestor.registrar_notificador(email)
    
    sms = NotificadorSMS()
    sms.agregar_numero("+34600123456")
    gestor.registrar_notificador(sms)
    
    # Enviar a todos
    gestor.notificar_a_todos("Recordatorio de Hábito", "¡No olvides tu hábito diario!")


def demo_estadisticas(servicios: ServiciosHabitos):
    """Demostración de estadísticas"""
    print("\n" + "="*60)
    print("6️⃣ DEMOSTRACIÓN DE ESTADÍSTICAS")
    print("="*60)
    
    stats = servicios.obtener_estadisticas_rapidas()
    
    print(f"\n📊 Estadísticas Rápidas:")
    print(f"  • Total de hábitos: {stats['total_habitos']}")
    print(f"  • Activos: {stats['habitos_activos']}")
    print(f"  • Checks completados: {stats['checks_completados']}/{stats['checks_totales']}")
    print(f"  • Cantidades cumplidas: {stats['cantidades_cumplidas']}/{stats['cantidades_totales']}")


def demo_encapsulamiento():
    """Demostración de encapsulamiento"""
    print("\n" + "="*60)
    print("7️⃣ DEMOSTRACIÓN DE ENCAPSULAMIENTO (PROPIEDADES)")
    print("="*60)
    
    try:
        habito = HabitoCheck("test1", "Test Hábito", "diario")
        
        # Acceso mediante propiedades
        print(f"✓ Nombre (property): {habito.nombre}")
        print(f"✓ Frecuencia (property): {habito.frecuencia}")
        print(f"✓ Activo (property): {habito.activo}")
        
        # Cambiar mediante setters con validación
        habito.nombre = "Nuevo nombre"
        print(f"✓ Nombre actualizado: {habito.nombre}")
        
        # Intento de asignación inválida
        try:
            habito.nombre = "xy"  # Muy corto
        except HabitoInvalidoError as e:
            print(f"✗ Validación de setter: {e}")
        
        # Recordatorio con encapsulamiento
        print(f"✓ Tiene recordatorio: {habito.tiene_recordatorio}")
        habito.activar_recordatorio(1, 8)  # Lunes a las 8am
        print(f"✓ Recordatorio activado - Día: {habito.dia_recordatorio}, Hora: {habito.hora_recordatorio}")
        
    except Exception as e:
        print(f"✗ Error: {e}")


def demo_persistencia(servicios: ServiciosHabitos, repo: RepositorioHabito):
    """Demostración de persistencia"""
    print("\n" + "="*60)
    print("8️⃣ DEMOSTRACIÓN DE PERSISTENCIA")
    print("="*60)
    
    print(f"\n💾 Guardando {repo.contar()} hábitos en archivo...")
    repo.guardar()
    print("✓ Hábitos guardados en 'datos/habitos.json'")
    
    print("\n📂 Contenido del repositorio:")
    for h in repo.obtener_todos():
        print(f"  - {h}")


def main():
    """Función principal de demostración"""
    print("\n" + "🎯 "*20)
    print("DEMOSTRACIÓN COMPLETA DEL SISTEMA DE HÁBITOS")
    print("Criterios de Evaluación: Clases, Encapsulamiento, Herencia, ABC")
    print("🎯 "*20)
    
    # Crear repositorio y servicio
    repo = RepositorioHabito("datos/habitos.json")
    servicios = ServiciosHabitos(repo)
    
    # Ejecutar demostraciones
    demo_validacion()
    demo_habitos(servicios)
    demo_operaciones(servicios)
    demo_consultas(servicios)
    demo_notificadores()
    demo_estadisticas(servicios)
    demo_encapsulamiento()
    demo_persistencia(servicios, repo)
    
    # Mostrar resumen final
    print("\n" + servicios.obtener_resumen_completo())
    
    print("✓ Demostración completada exitosamente")


if __name__ == "__main__":
    main()

