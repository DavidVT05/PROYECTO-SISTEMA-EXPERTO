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
    "Pasos_Inmovilizacion": (
        "PASOS DE AUXILIOS (TRAUMATISMOS):\n"
        "1. Inmovilizar la extremidad en la posición encontrada.\n"
        "2. Colocar férula abarcando una articulación arriba y una abajo de la lesión.\n"
        "3. Fijar el vendaje sin apretar (dejar espacio de 1 dedo)."
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
    
    # R5: Compromiso neurovascular en traumatismos
    {
        "id": "R5",
        "condiciones": {"Traumatismo": True, "Compromiso_neurovascular": True},
        "conclusiones": ["Urgencia_Hospitalaria"]
    },
    
    # R6: Quemadura de 1er Grado
    {
        "id": "R6",
        "condiciones": {"Quemadura": True, "Enrojecimiento": True, "Ampollas": False},
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
    
    # R8: Corte con requerimiento de sutura
    {
        "id": "R8",
        "condiciones": {"Corte": True, "Separacion_Bordes": True},
        "conclusiones": ["Requiere_Sutura", "Pasos_Corte"]
    },
    
    # R9: Sospecha de Fractura Cerrada Leve
    {
        "id": "R9",
        "condiciones": {
            "Traumatismo": True, 
            "Dolor_Oseo_Agudo": True, 
            "Incapacidad_Funcional": True,
            "Compromiso_neurovascular": False
        },
        "conclusiones": ["Sospecha_Fractura", "Pasos_Inmovilizacion", "Prohibir_Reordenar_Hueso"]
    }
]
