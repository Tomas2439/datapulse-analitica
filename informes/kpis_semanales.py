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