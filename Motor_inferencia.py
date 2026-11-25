from Base_Conocimiento import REGLAS_PRODUCCION

def motor_inferencia(hechos_iniciales, reglas=REGLAS_PRODUCCION):
    memoria_trabajo = dict(hechos_iniciales)
    reglas_disparadas = ()
    conclusiones_acumuladas = ()
    hubo_cambios = True

    while hubo_cambios:
        cantidad_previa = len(reglas_disparadas)

        for regla in reglas:
            id_regla = regla["id"]
            cumple = (
                id_regla not in reglas_disparadas
                and all(
                    memoria_trabajo.get(hecho) == valor_esperado
                    for hecho, valor_esperado in regla["condiciones"].items()
                )
            )

            nuevos_hechos = ({}, dict.fromkeys(regla["conclusiones"], True))[cumple]
            memoria_trabajo.update(nuevos_hechos)
            reglas_disparadas = reglas_disparadas + ((), (id_regla,))[cumple]
            conclusiones_acumuladas = conclusiones_acumuladas + ((), tuple(regla["conclusiones"]))[cumple]

        hubo_cambios = len(reglas_disparadas) > cantidad_previa

    return {
        "memoria_trabajo": memoria_trabajo,
        "reglas_disparadas": reglas_disparadas,
        "conclusiones": tuple(dict.fromkeys(conclusiones_acumuladas))
    }