# ==============================================================================
# BASE DE CONOCIMIENTO: SISTEMA EXPERTO DE PRIMEROS AUXILIOS
# ==============================================================================

# 1. DICCIONARIO MAESTRO DE HECHOS (Entradas, Diagnósticos, Pasos y Reglas de Oro)
HECHOS = {
    # Hechos de Entrada
    "Existen_Heridos": "¿Existen personas heridas o lesionadas en el lugar del accidente?",
    "Persona_Respirando": "¿La persona accidentada está respirando normalmente?",
    "Perdida_Consciencia": "La persona perdió el conocimiento o se encuentra desorientada",
    "Quemadura": "La lesión fue causada por calor / fuego / agua caliente / vapor",
    "Corte": "La lesión es una herida abierta con sangrado activo / corte",
    "Traumatismo": "La lesión fue por caída, golpe fuerte o posible fractura",
    "Sangrado_Persistente": "El sangrado no se detiene tras 10 minutos de presión continua",
    "Enrojecimiento": "La piel se encuentra roja, seca y presenta dolor localizado",
    "Ampollas": "Hay presencia de ampollas (flictenas) con líquido en la piel",
    "Zona_Critica": "Afecta cara, manos, pies, genitales o articulaciones principales",
    "Gran_Extension": "La quemadura ocupa más de la palma de la mano de la víctima",
    "Separacion_Bordes": "Los bordes del corte están separados por más de 5 mm",
    "Dolor_Oseo_Agudo": "Presenta dolor intenso en el hueso al tocar o intentar mover",
    "Incapacidad_Funcional": "La persona no puede mover o apoyar la extremidad lesionada",
    "Compromiso_neurovascular": "Presenta piel fría, azulada/pálida o pérdida de sensibilidad",

    # Hechos de Conclusión
    "Escena_Sin_Riesgo": "No se detectan heridos. Escena segura, finaliza la evaluación.",
    "Urgencia_Hospitalaria": "¡ATENCIÓN CRÍTICA! Llamar inmediatamente al 911 o trasladar al hospital.",
    "Quemadura_Grado_1": "DIAGNÓSTICO: Quemadura superficial de primer grado.",
    "Quemadura_Grado_2": "DIAGNÓSTICO: Quemadura de segundo grado leve.",
    "Corte_Superficial": "DIAGNÓSTICO: Herida superficial sin compromiso vascular ni requerimiento de sutura.",
    "Traumatismo_Leve": "DIAGNÓSTICO: Contusión o esguince leve sin signos de fractura.",
    "Requiere_Sutura": "DIAGNÓSTICO: Herida profunda que requiere atención médica para sutura.",
    "Sospecha_Fractura": "DIAGNÓSTICO: Sospecha de fractura cerrada leve o traumatismo.",
    "Pasos_Quemadura": (
        "PASOS DE AUXILIOS (QUEMADURAS):\n"
        "1. Enfriar con agua de la llave (15-25 °C) por 10 a 20 minutos.\n"
        "2. Retirar pulseras o anillos antes de que se inflame la zona.\n"
        "3. Cubrir holgadamente con gasa humedecida."
    ),
    "Pasos_Corte": (
        "PASOS DE AUXILIOS (CORTES):\n"
        "1. Aplicar compresa limpia sobre la herida y presionar firmemente por 10 min.\n"
        "2. SI LA GASA SE EMPAPA: NO retirarla, colocar una nueva compresa ENCIMA."
    ),
    "Pasos_Corte_Leve": (
        "PASOS DE AUXILIOS (CORTE SUPERFICIAL):\n"
        "1. Lavar la herida con agua limpia y jabón neutro.\n"
        "2. Aplicar presión suave con una gasa estéril hasta que ceda el sangrado.\n"
        "3. Cubrir con una curita o apósito limpio."
    ),
    "Pasos_Inmovilizacion": (
        "PASOS DE AUXILIOS (TRAUMATISMOS):\n"
        "1. Inmovilizar la extremidad en la posición encontrada.\n"
        "2. Colocar férula abarcando una articulación arriba y una abajo de la lesión.\n"
        "3. Fijar el vendaje sin apretar (dejar espacio de 1 dedo)."
    ),
    "Pasos_Traumatismo_Leve": (
        "PASOS DE AUXILIOS (CONTUSIÓN / ESGUINCE LEVE):\n"
        "1. Mantener en reposo la zona afectada.\n"
        "2. Aplicar frío local envuelto en un paño limpio durante 15 minutos.\n"
        "3. Evitar masajear o forzar el movimiento de la articulación."
    ),
    "Prohibir_Remedios_Caseros": (
        "¡REGLA DE ORO! NO usar hielo directo, pasta dental, mantequilla ni reventar ampollas."
    ),
    "Prohibir_Reordenar_Hueso": (
        "¡REGLA DE ORO! NO intentar jalar, alinear ni reordenar el hueso."
    )
}

# 2. REGLAS DE PRODUCCIÓN TRANSCRITAS A LISTA DE DICCIONARIOS
REGLAS_PRODUCCION = [
    # R0: Filtro de control de escena
    {
        "id": "R0",
        "condiciones": {"Existen_Heridos": False},
        "conclusiones": ["Escena_Sin_Riesgo"]
    },

    # R1: Descarte de emergencia vital (respiración)
    {
        "id": "R1",
        "condiciones": {"Existen_Heridos": True, "Persona_Respirando": False},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },

    # R2: Alarma por pérdida de conocimiento
    {
        "id": "R2",
        "condiciones": {"Existen_Heridos": True, "Perdida_Consciencia": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },

    # R3: Hemorragia incontrolable
    {
        "id": "R3",
        "condiciones": {"Corte": True, "Sangrado_Persistente": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },

    # R4: Quemaduras de alto riesgo (zonas críticas o extensas)
    {
        "id": "R4",
        "condiciones": {"Quemadura": True, "Ampollas": True, "Zona_Critica": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },
    {
        "id": "R4_B",
        "condiciones": {"Quemadura": True, "Ampollas": True, "Gran_Extension": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },
    {
        "id": "R4_C",
        "condiciones": {"Quemadura": True, "Zona_Critica": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },
    {
        "id": "R4_D",
        "condiciones": {"Quemadura": True, "Gran_Extension": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },

    # R5: Compromiso neurovascular en traumatismos
    {
        "id": "R5",
        "condiciones": {"Traumatismo": True, "Compromiso_neurovascular": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },

    # R6: Quemadura de 1er Grado
    {
        "id": "R6",
        "condiciones": {
            "Quemadura": True,
            "Enrojecimiento": True,
            "Ampollas": False,
            "Zona_Critica": False,
            "Gran_Extension": False
        },
        "conclusiones": ["Quemadura_Grado_1", "Pasos_Quemadura", "Prohibir_Remedios_Caseros"]
    },

    # R7: Quemadura de 2do Grado Leve
    {
        "id": "R7",
        "condiciones": {
            "Quemadura": True,
            "Ampollas": True,
            "Zona_Critica": False,
            "Gran_Extension": False
        },
        "conclusiones": ["Quemadura_Grado_2", "Pasos_Quemadura", "Prohibir_Remedios_Caseros"]
    },

    # R8: Corte con requerimiento de sutura y corte superficial
    {
        "id": "R8",
        "condiciones": {"Corte": True, "Separacion_Bordes": True},
        "conclusiones": ["Requiere_Sutura", "Pasos_Corte"]
    },
    {
        "id": "R8_B",
        "condiciones": {"Corte": True, "Sangrado_Persistente": False, "Separacion_Bordes": False},
        "conclusiones": ["Corte_Superficial", "Pasos_Corte_Leve"]
    },

    # R9: Sospecha de Fractura Cerrada Leve y traumatismo leve
    {
        "id": "R9",
        "condiciones": {
            "Traumatismo": True,
            "Dolor_Oseo_Agudo": True,
            "Incapacidad_Funcional": True,
            "Compromiso_neurovascular": False
        },
        "conclusiones": ["Sospecha_Fractura", "Pasos_Inmovilizacion", "Prohibir_Reordenar_Hueso"]
    },
    {
        "id": "R9_B",
        "condiciones": {
            "Traumatismo": True,
            "Dolor_Oseo_Agudo": False,
            "Incapacidad_Funcional": False,
            "Compromiso_neurovascular": False
        },
        "conclusiones": ["Traumatismo_Leve", "Pasos_Traumatismo_Leve"]
    }
]

# 3. ESTRUCTURAS DE CONTROL PARA EL FLUJO EN EMBUDO SIN CONDICIONALES
MAPA_SI_NO = {
    "s": True, "si": True, "sí": True, "1": True,
    "n": False, "no": False, "0": False
}

OPCIONES_LESION = {
    "1": "Quemadura",
    "2": "Corte",
    "3": "Traumatismo"
}

PREGUNTAS_POR_LESION = {
    "Quemadura": ("Enrojecimiento", "Ampollas", "Zona_Critica", "Gran_Extension"),
    "Corte": ("Sangrado_Persistente", "Separacion_Bordes"),
    "Traumatismo": ("Dolor_Oseo_Agudo", "Incapacidad_Funcional", "Compromiso_neurovascular")
}