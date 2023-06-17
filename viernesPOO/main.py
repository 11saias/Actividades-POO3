from cosas import *

def main():
    per1 = Persona("Jose", 22)
    print(per1)
    print(per1.descripcion())

    print("----Herencia-------")
    al1 = Alumno("Jose", 22, "223344", "ICO")
    print(al1)
    print(al1.descripcion())

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("----Herencia profe-------")
    profe1 = Profesor("Jesus", 30+16,35353, "Ing. de software")
    print(profe1)
    profe1.dormir()

    print("----Herencia AyudanteProfe-------")
    ayudante = AyudanteProfesor("Adrian", 20, "3234322", "ICO", 23223, "Ing.software", 4)
    ayudante.dormir()
    ayudante.nombre ="Abraham"
    ayudante.dar_clase("Matemáticas")

main()

