config = {}


try:
    archivo = open("config.txt", 'r')
except FileNotFoundError:
    print("Error: El archivo 'config.txt' no existe.")
except IOError:
    print("Error: No se pudo leer el archivo 'config.txt'.")
else:
    try:
        for linea in archivo:
            if "=" in linea:
                clave, valor = linea.strip().split("=")
                config[clave.strip()] = float(valor.strip())
    except ValueError:
        print("Error: Uno de los valores en 'config.txt' no es un número válido.")
    finally:
        archivo.close()

required_keys = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]
if not config or not all(k in config for k in required_keys):
    print("Error: Configuración incompleta o vacía. Revisa tu archivo.")
    exit()

for clave, valor in config.items():
    print(f"{clave}={valor}")

ancho = int(config["ancho"])
alto = int(config["alto"])
max_iter = int(config["max_iter"])

try:
    salida = open("clase.csv", 'w')
except IOError:
    print("Error: No se pudo crear o escribir en 'clase.csv'.")
else:
    try:
        salida.write("fila,columna,iteraciones\n")

        for fila in range(alto):
            for columna in range(ancho):
                real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
                imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
                
                c = complex(real, imag)
                z = 0 + 0j
                iteraciones = 0
                
                while (abs(z) <= 2) and (iteraciones < max_iter):
                    z = z**2 + c
                    iteraciones += 1
                
                salida.write(f"{fila},{columna},{iteraciones}\n")
        print("done")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el cálculo: {e}")
    finally:
        salida.close()