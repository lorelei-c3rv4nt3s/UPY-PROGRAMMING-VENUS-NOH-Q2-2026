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
        print("Error: El archivo de configuración contiene valores que no son números válidos.")
    finally:
        archivo.close()
claves_requeridas = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]

if not config or not all(k in config for k in claves_requeridas):
    print("Error crítico: Faltan parámetros en config.txt o el diccionario está vacío. Proceso abortado.")
    exit()

try:
    ancho = int(config["ancho"])
    alto = int(config["alto"])
    max_iter = int(config["max_iter"])
except ValueError:
    print("Error: 'ancho', 'alto' o 'max_iter' no se pueden convertir a enteros.")
    exit()

try:
    salida = open("clase.csv", 'w')
except IOError:
    print("Error: No se pudo crear o escribir en el archivo 'clase.csv'.")
else:
    try:
        salida.write("fila, colunma, iteraciones\n")

        for fila in range(alto):
            for columna in range(ancho):
                real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
                imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
                c = complex(real, imag)
                
                z = 0 + 0j
                iteraciones = 0
                
                while (abs(z) <= 2) and (iteraciones < max_iter):
                    z = z * z + c
                    iteraciones += 1
                    
                salida.write(f"{fila},{columna},{iteraciones}\n")
                
        print("DONE")
        
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el procesamiento matemático: {e}")
    finally:
        
        salida.close()