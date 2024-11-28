import threading
import time

# Crear un lock global para sincronizar las tareas
lock = threading.Lock()

# Función para tomar la orden
def tomar_orden(cliente):
    with lock:
        print(f"[{cliente}] Está tomando la orden...")
        time.sleep(2)  # Simulando el tiempo para tomar la orden
        print(f"[{cliente}] Orden tomada.")

# Función para preparar el café
def preparar_cafe(cliente):
    with lock:
        print(f"[{cliente}] Está preparando el café...")
        time.sleep(3)  # Simulando el tiempo para preparar el café
        print(f"[{cliente}] Café preparado.")

# Función para servir el pedido
def servir_pedido(cliente):
    with lock:
        print(f"[{cliente}] Está sirviendo el pedido...")
        time.sleep(1)  # Simulando el tiempo para servir el pedido
        print(f"[{cliente}] Pedido servido.")

# Función principal que coordina el flujo de trabajo
def proceso_cliente(cliente):
    tomar_orden(cliente)
    preparar_cafe(cliente)
    servir_pedido(cliente)

# Crear hilos para varios clientes
def main():
    clientes = ["Cliente 1", "Cliente 2", "Cliente 3"]

    # Crear y lanzar los hilos
    hilos = []
    for cliente in clientes:
        hilo = threading.Thread(target=proceso_cliente, args=(cliente,))
        hilos.append(hilo)
        hilo.start()

    # Esperar que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Todos los pedidos han sido procesados.")

if __name__ == "__main__":
    main()
