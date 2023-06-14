from cosas import Alumno

def main():
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("-----------------------")
    # OJO
    #Alumno.facultad = "FES Aragón EDOMEX"
    al1.facultad = "FES Aragón EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("----un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print("----modificar atributos publicos")
    al1.edad = 999


    al1 = Alumno("Diego", 19, "ICO")
    al2 = Alumno("Montse", 20, "Derecho")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))




main()