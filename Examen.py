def Estud():
    tupla = set()
    try:

        with open("Estudiantes.prn") as archivo:
            for line in archivo:
                tupla.add((line[0:8], line[8:-1]))
    except:
        print("No se pudo abrir el archivo estudiantes")
    else:
        return tupla


def Kardex():
    lista = []
    tupla = set()
    try:
        with open("Kardex.txt") as archivo:
            for line in archivo:
                lista = line.split("|")
                tupla.add((int(lista[0]), str(lista[1]), int(lista[2])))
    except:
        print("No se pudo abrir el archivo Kardex")
    else:
        return tupla

import json
def RegresarAlumnos(controles):


    estudiantes = Estud()
    listadicc = []
    listanombres = []
    listamaterias = []
    materias = Kardex()
    if len(controles) > 0:
        for control in controles:  # trae la lista de números de control
            # print(f"control es {control}")
            for e in estudiantes:  # trae el número de control y nombres. De aquí tengo que sacar el nombre
                # print(e[0])
                if (control == e[0]):
                    listanombres.append(e[1])
        for control in controles:
            mate = []
            print(f"control es {control}")
            for m in materias:
                c, m, p = m
                if int(control) == c:
                    print("Se encontro", m)
                    mate.append(m)
            listamaterias.append(mate)
        i = 0
        for nombre in listanombres:
            dicc = {}
            dicc["Nombre"] = nombre
            dicc["Materias"] = listamaterias[i]
            i += 1
            listadicc.append(dicc)

    else:
        for e in estudiantes:
            dicc ={}
            mate = []
            for m in materias:
                c, m, p = m
                if int(e[0]) == c:
                    mate.append(m)
            listamaterias.append(mate)
            dicc["Nombre"] = e[1]
            dicc["Materias"] = mate
            listadicc.append(dicc)



    return json.dumps(listadicc, indent=4)
    #dicc["Materias"] = mate
    #return json.dumps(dicc, indent=3)





lista = ["18420493"]
print(RegresarAlumnos(lista))
