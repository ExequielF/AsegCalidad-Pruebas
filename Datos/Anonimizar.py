import pandas as pd     #pip install pandas
from faker import Faker #pip install Faker
import random           #pip install random

#Largo de contraseña para fake.password()
largo_pass = random.randint(12,30)

# Función para anonimizar los datos
def anonimizar_datos(row):
    fake = Faker()

    anonimizado = {
        'Nombre': fake.first_name(),
        'Apellido Paterno': fake.last_name(),
        'Apellido Materno': fake.last_name(),
        
        'Contraseña': fake.password(length=largo_pass),
        
        'Mes': fake.month(),
        'Dia': fake.day_of_month(),

        'Correo': fake.free_email(),
    }

    # Mantener el RUT sin cambios
    if 'RUT' in row.index:
        anonimizado['Rut'] = row['Rut']

    return anonimizado

# Ruta del archivo Excel de entrada y salida
archivo_entrada = 'datos_originales.xlsx'
archivo_salida = 'datos_anonimizados.xlsx'

# Cargar datos desde el archivo Excel
datos_originales = pd.read_excel(archivo_entrada)

# Aplicar la función de anonimización a cada fila, excluyendo la columna 'RUT'
columnas_anonimizar = [col for col in datos_originales.columns if col != 'Rut']
datos_anonimizados = datos_originales[columnas_anonimizar].apply(anonimizar_datos, axis=1, result_type='expand')

# Unir la columna 'RUT' con los datos anonimizados
datos_anonimizados['Rut'] = datos_originales['Rut']

# Guardar los datos anonimizados en un nuevo archivo Excel
datos_anonimizados.to_excel(archivo_salida, index=False, engine='openpyxl')

print(f'Datos anonimizados guardados en: {archivo_salida}')
