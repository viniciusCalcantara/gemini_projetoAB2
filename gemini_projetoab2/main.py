base_conhecimento = {
    "fatos": {"dor_de_cabeca": "sim", "garganta_inflamada": "sim", "tosse": "sim"},
    "regras": [
        [["dor_de_cabeca=sim", "garganta_inflamada=sim", "tosse=sim"], "diagnostico=gripe"],
        # ... outras regras
    ]
}


def motor_inferencia(base_conhecimento):
    while True:
        novas_conclusoes = []
        for regra in base_conhecimento["regras"]:
            antecedentes, consequente = regra
            if all(fato in base_conhecimento["fatos"] and base_conhecimento["fatos"][fato] == "sim" for fato in antecedentes):
                novas_conclusoes.append(consequente)
        if not novas_conclusoes:
            break
        for conclusao in novas_conclusoes:
            base_conhecimento["fatos"][conclusao] = "sim"
    # Retornar o diagnóstico (último consequente adicionado) ou "Indeterminado"