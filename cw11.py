import random

#crear csv
archivo = open("archivo,csv","w")

#escribir encabezados
archivo.write ("x, y, COLOR\n")

for _ in range (1000):     #cuando la variable auxiliar no se usa en loop usamos _
    x=random.uniform(-10,10)
    y=random.uniform(-10,10)      #uniform para que sea de forma uniforme o lo mas amplio posible
    
    distancia=(x*x + y*y)**0.5
    iteraciones = 0
    color = 0
    
    while (distancia < 1) and (iteraciones <100):
        distancia = distancia * distancia
        iteraciones+= 1
        
    if distancia > 1:
        color= 255
        
    archivo.write(f"{x},{y},{color}\n")
archivo.close()
print("done")
    