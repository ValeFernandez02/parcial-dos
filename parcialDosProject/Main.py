salario_base = int(input("Ingrese el salario base mensual: "))
cargo = input("Ingrese el cargo del empleado: ")
desempeno = input("Ingrese el desempeño del empleado: ")


def calcular_bonificacion(salario_base, cargo, desempeno):
    # Inicializar la bonificación
    bonificacion = 0

    # Normalizar el cargo y desempeño
    cargo = cargo.capitalize()
    desempeno = desempeno.capitalize()

    # Calcular bonificación según cargo y desempeño
    if cargo.lower() == "directivo":
        if desempeno.lower() == "alto":
            bonificacion = salario_base * 0.20
        elif desempeno.lower() == "medio":
            bonificacion = salario_base * 0.10
    elif cargo.lower() == "operativo":
        if desempeno.lower() == "alto":
            bonificacion = salario_base * 0.15
        elif desempeno.lower() == "medio":
            bonificacion = salario_base * 0.05

    # Calcular el total a recibir
    total_a_recibir = salario_base + bonificacion

    return (cargo, desempeno, salario_base, bonificacion, total_a_recibir)


# Calcular y mostrar resultados
resultado = calcular_bonificacion(salario_base, cargo, desempeno)
print("-----Resumen del Pago-----")
print(f"Cargo: {resultado[0]}")
print(f"Nivel de Desempeño: {resultado[1]}")
print(f"Salario Base: ${resultado[2]:,.2f}")
print(f"Bonificación: ${resultado[3]:,.2f}")
print(f"Total a Recibir: ${resultado[4]:,.2f}")
print("------------------------------------")

