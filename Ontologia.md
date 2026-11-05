```mermaid
graph TD
    %% Filtros de Urgencia Crítica (Hechos a Escalamiento)
    Consciencia[Pérdida de consciencia] --> Urgencia((Urgencia Hospitalaria))
    Sangrado[Sangrado persistente] --> Urgencia
    LlenadoCapilar[Llenado capilar lento / Cianosis] --> Urgencia

    %% Hechos a Categoría: Quemadura
    Enrojecimiento[Enrojecimiento y Piel Seca] --> Quemadura(Quemadura)
    Ampollas[Presencia de Ampollas] --> Quemadura
    DolorQuemadura[Dolor al contacto con el aire] --> Quemadura

    %% Categoría Quemadura a Conclusiones
    Quemadura -->|Sin ampollas + Dolor localizado| QG1((Quemadura Grado 1))
    Quemadura -->|Con ampollas + Lecho húmedo| QG2((Quemadura Grado 2))

    %% Hechos a Categoría: Corte
    Bordes[Separación de bordes > 5mm] --> Corte(Corte / Hemorragia)
    Tejido[Tejido adiposo o músculo visible] --> Corte
    Hemorragia[Sangrado activo tras 15 min de presión] --> Corte

    %% Categoría Corte a Conclusiones
    Corte -->|Cumple profundidad o sangrado continuo| Sutura((Requiere Sutura))
    Corte -->|Sangrado controlado superficial| Gasa((Estabilización Local))

    %% Hechos a Categoría: Traumatismo
    DolorOseo[Dolor óseo agudo a la palpación] --> Traumatismo(Traumatismo)
    Deformidad[Deformidad anatómica visible] --> Traumatismo
    Incapacidad[Incapacidad funcional total] --> Traumatismo

    %% Categoría Traumatismo a Conclusiones
    Traumatismo -->|Inflamación + dolor articular| Esguince((Esguince / Contusión))
    Traumatismo -->|Crepitación + deformidad| Fractura((Sospecha de Fractura))

    %% Reglas de Oro / Contraindicaciones Globales
    Remedios[Aplicación de hielo, huevo, pasta dental] --> Contraindicacion((Contraindicación Absoluta))
    Reordenar[Intento de reordenar o alinear hueso] --> Contraindicacion
