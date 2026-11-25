# ==============================================================================
# INTERFAZ PRINCIPAL (Flujo en Embudo sin condicionales + Resultados)
# ==============================================================================
from Base_Conocimiento import HECHOS, MAPA_SI_NO, OPCIONES_LESION, PREGUNTAS_POR_LESION
from Motor_inferencia import motor_inferencia


def preguntar_booleano(clave_hecho):
    entrada = ""
    while entrada not in MAPA_SI_NO:
        entrada = input(f"\n{HECHOS[clave_hecho]} (s/n): ").strip().lower()
    return MAPA_SI_NO[entrada]


def preguntar_detalle_lesion(memoria):
    print("\nSeleccione el tipo de lesión:")
    print("  1. Quemadura")
    print("  2. Corte")
    print("  3. Traumatismo")
    opcion = ""
    while opcion not in OPCIONES_LESION:
        opcion = input("Opción (1/2/3): ").strip()

    memoria.update(dict.fromkeys(OPCIONES_LESION.values(), False))
    lesion_elegida = OPCIONES_LESION[opcion]
    memoria[lesion_elegida] = True

    for sintoma in PREGUNTAS_POR_LESION[lesion_elegida]:
        memoria[sintoma] = preguntar_booleano(sintoma)


def recolectar_hechos():
    memoria = {}
    memoria["Existen_Heridos"] = preguntar_booleano("Existen_Heridos")

    # Selección por índice booleano: False -> tupla vacía (), True -> signos vitales
    preguntas_vitales = ((), ("Persona_Respirando", "Perdida_Consciencia"))[memoria["Existen_Heridos"]]
    for hecho_vital in preguntas_vitales:
        memoria[hecho_vital] = preguntar_booleano(hecho_vital)

    estable = (
        memoria.get("Existen_Heridos") is True
        and memoria.get("Persona_Respirando") is True
        and memoria.get("Perdida_Consciencia") is False
    )
    (lambda _: None, preguntar_detalle_lesion)[estable](memoria)
    return memoria


def mostrar_resultados(resultado):
    print("\n" + "=" * 60)
    print("Reglas activadas:", resultado["reglas_disparadas"])
    print("=" * 60)
    conclusiones = resultado["conclusiones"]
    aviso = ("No se cumplió ninguna regla completa con los datos ingresados.", "")[bool(conclusiones)]
    print(aviso)
    for clave in conclusiones:
        print(f"\n{HECHOS[clave]}")


# Ejecución principal
if __name__ == "__main__":
    hechos_usuario = recolectar_hechos()
    resultado_final = motor_inferencia(hechos_usuario)
    mostrar_resultados(resultado_final)