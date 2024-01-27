from pydantic import BaseModel
from datetime import date
from typing import List


class Estudiante(BaseModel):
    nombre: str
    identificacion: str
    sexo: str
    fecha_nacimiento: date
    fecha_ingreso :date
    notas : List[float]

