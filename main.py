from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Data.estudiantes import estudiantes
import uvicorn
from clases.estudiante import Estudiante

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/obtener_todos")
def obtener_alumno():
    return estudiantes

@app.post("/registrar")
def my_function(estudiante: Estudiante):
    estudiantes.append(estudiante)
    return "!registrado correctamente"




@app.get("/obtener_por_identificacion/")
def obtener_por_identificacion(identificacion: str):
    for estudiante in estudiantes:
        if estudiante.identificacion == identificacion:
            return estudiante


@app.delete("/Eliminar_por_identificacion/")
def obtener_por_identificacion ( identificacion: str):
    for estudiante in estudiantes:
       if estudiante.identificacion == identificacion:
            estudiantes.remove(estudiante)
    return "Eliminado correctamente"



@app.get("/Promedio del Estudiante por identificacion/")
def promedio_del_estudiante ( identificacion : str):
    for estudiante in estudiantes :
        if estudiante.identificacion == identificacion:
            return sum(estudiante.notas) / len(estudiante.notas)


@app.get("/aprobaste_por_identificacion/")
def aprobaste_por_identificacion(identificacion: str):
    for estudiante in estudiantes:
        if estudiante.identificacion == identificacion:
            promedio = sum(estudiante.notas) / len(estudiante.notas)

            if promedio >= 3.0:
                return "Aprobo"
            else:
                return "reprobo"


@app.delete("/Eliminar_por_identificacion/")
def obtener_por_identificacion ():
    lista = estudiantes.copy()
    for estudiante in estudiantes:
           promedio = sum(estudiante.notas) / len(estudiante.notas)
           if promedio >= 3.0 :
            lista.remove(estudiante)
    return lista




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
