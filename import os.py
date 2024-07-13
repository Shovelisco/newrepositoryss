import os   
import time
import random
import json

os.system("cls")
modelos=["rio", "Forte", "optima", "stinger", "soul", "Seltos", "sportage", "sorento", "telluride", "carnival"]
ModeloPrecio=[]





def error():
    os.system("cls")
    print("Opcion no valida, Ingrese una nuevamente.")
    time.sleep(1)

def asignarprecios(modelos):
    for modelo in modelos:
        PrecioModelo = random.choice(range(7000000,12500000,100000))
        auto = {
            "modelo": modelo,
            "precio": PrecioModelo,
        }
        ModeloPrecio.append(auto)
    guardar_json("ModeloPrecio.json", ModeloPrecio)
    os.system("cls")
    print("se ah creado correctamente")
    time.sleep(2)
    
        
def guardar_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def ClasificarPrecios(ModeloPrecio):
    ModelosMenorPrecio=[]
    ModelosMayorPrecio=[]
    ModelosEntrePrecio=[]

    for modelo in ModeloPrecio:
        if modelo["precio"] < 9000000:
            ModelosMenorPrecio.append(modelo)
        elif modelo["precio"] >= 9000000 and modelo["precio"] <= 11000000:
            ModelosEntrePrecio.append(modelo)
        elif modelo["precio"] > 11000000:
            ModelosMayorPrecio.append(modelo)

 
def menu():
    print("1. Asignar precios aleatorios")
    print("2. Clasificar precios")
    print("3. Ver estadisticas")
    print("4. report de precios")
    print("5. Salir del programa")

def main():
    while True:
        opcmenu=0
        menu()
        try:
            opcmenu=int(input("ingrese la opcion:  "))
        except:
            error()
        if opcmenu < 1 or opcmenu > 5:
            error()
        else:  
            if opcmenu == 1:
                asignarprecios(modelos)
            elif opcmenu == 2:
                ClasificarPrecios(ModeloPrecio)
            elif opcmenu == 3:
                print("3. Ver estadisticas")
            elif opcmenu == 4:
                print("4. report de precios")
            elif opcmenu == 5:
                os.system("cls")
                print("cerrando el progama...")
                time.sleep(3)
                break

                
            


if __name__ == "__main__":
    main()  