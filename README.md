# Gestión de Pedidos de Café
## Descripción

Este proyecto es una simulación de la gestión de pedidos en una cafetería utilizando Python y programación multihilo. Se implementan procesos como tomar órdenes, preparar café y servir pedidos para varios clientes.

El objetivo principal es demostrar el uso de hilos en Python y cómo sincronizar tareas concurrentes utilizando un Lock para evitar problemas de acceso simultáneo a recursos compartidos.

## Funcionalidades

    Tomar la orden: Se simula el proceso de registrar la orden de un cliente.
    Preparar el café: Se simula la preparación del café del pedido.
    Servir el pedido: Se simula la entrega del pedido al cliente.

Cada tarea tiene una duración simulada usando la función time.sleep() para mostrar el tiempo que toma cada proceso.
## Estructura del Código

### lock:
    Un objeto global de tipo threading.Lock que asegura que solo un hilo a la vez acceda a las secciones críticas (procesos de orden, preparación o servicio).

### Funciones principales:
        
    tomar_orden(cliente): Simula el registro de la orden del cliente.
    preparar_cafe(cliente): Simula la preparación del café.
    servir_pedido(cliente): Simula el servicio del pedido al cliente.

  Cada una utiliza un bloque with lock para garantizar que solo un cliente sea procesado por vez.

###  proceso_cliente(cliente):
    
    Coordina el flujo completo para un cliente: tomar la orden, preparar el café y servir el pedido.

###    main():
    Define una lista de clientes.
    Crea un hilo por cliente y los ejecuta concurrentemente.
    Espera que todos los hilos terminen antes de finalizar la ejecución del programa.

## Ejecución

Para ejecutar el proyecto:
Asegúrate de tener Python instalado en tu máquina. Ejecuta el archivo desde la línea de comandos:

    python3 cafeteria.py

## Ejemplo de Salida

    [Cliente 1] Está tomando la orden...
    [Cliente 1] Orden tomada.
    [Cliente 1] Está preparando el café...
    [Cliente 1] Café preparado.
    [Cliente 1] Está sirviendo el pedido...
    [Cliente 1] Pedido servido.
    [Cliente 2] Está tomando la orden...
    [Cliente 2] Orden tomada.
    [Cliente 2] Está preparando el café...
    [Cliente 2] Café preparado.
    [Cliente 2] Está sirviendo el pedido...
    [Cliente 2] Pedido servido.
    [Cliente 3] Está tomando la orden...
    [Cliente 3] Orden tomada.
    [Cliente 3] Está preparando el café...
    [Cliente 3] Café preparado.
    [Cliente 3] Está sirviendo el pedido...
    [Cliente 3] Pedido servido.
    Todos los pedidos han sido procesados.


