def caso_who(ruta_archivo_csv: str) -> dict:
    extencion = ruta_archivo_csv.split(".")[-1]
    if ruta_archivo_csv[-3:] != 'csv':
        return 'Extensión inválida.'
    try:
        import pandas as pd
        datos = pd.DataFrame(pd.read_csv(ruta_archivo_csv))
    except:
        return 'Error al leer el archivo de datos.'
    datos['razon'], datos['date'] = (datos.total_cases_per_million * datos.population / 1000) / (datos.hospital_beds_per_thousand * datos.population),  pd.to_datetime(datos['date'])
    return datos.groupby(['date', 'continent']).razon.mean().unstack().plot()


print(caso_who('owid-covid-data.csv'))
