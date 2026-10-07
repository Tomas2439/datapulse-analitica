def calcular_kpis(semana):
    """Calcula los KPIs principales de la semana."""
    print(f"Generando KPIs para semana: {semana}")
    kpis = {
        "usuarios_activos": 12450,
        "ingresos_eur": 89200,
        "churn_rate": 0.0335,
        "nps": 72,
    }
    return kpis

def generar_informe(kpis):
    """Formatea los KPIs para el email semanal."""
    lineas = []
    for nombre, valor in kpis.items():
        lineas.append(f"  {nombre}: {valor}")
    return "\n".join(lineas)

if __name__ == "__main__":
    kpis = calcular_kpis("2024-W28")
    print(generar_informe(kpis))

def calcular_kpis(semana):
    """Calcula los KPIs principales de la semana."""
    kpis = {
        "usuarios_activos": 12450,
        "ingresos_eur": 89200,
        "churn_rate": 0.021,  # CORREGIDO: excluir trials
        "nps": 72,
    }
    return kpis

def calcular_churn(mes, excluir_trials=True):
    """Calcula el churn rate mensual.
    Los usuarios en prueba gratuita que no convierten NO son bajas.
    Solo contamos como baja a quien ERA cliente de pago y dejo de serlo.
    """
    clientes_inicio = 8500
    bajas_mes = 178  # Solo clientes de pago que cancelaron
    if not excluir_trials:
        bajas_mes = 285  # Incluiria trials (INCORRECTO)
    return round(bajas_mes / clientes_inicio, 4)

def generar_informe(kpis):
    """Formatea los KPIs para el email semanal."""
def calcular_conversion(semana):
    """Tasa de conversion semanal = compradores / visitantes."""
    visitantes = 45000
    compradores = 1890
    return round(compradores / visitantes, 4)

def generar_informe(kpis):
    lineas = []
    for nombre, valor in kpis.items():
        lineas.append(f"  {nombre}: {valor}")
    return "\n".join(lineas)

if __name__ == "__main__":
    kpis = calcular_kpis("2024-W28")
    kpis["churn_rate"] = calcular_churn("2024-07")
    print(generar_informe(kpis))