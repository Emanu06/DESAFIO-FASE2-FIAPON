
import collections 



modulos_iniciais = [
    {
        "nome": "HAB-01",
        "tipo": "Habitação",
        "prioridade": 1,
        "combustivel": 72,
        "massa": 18.5,
        "criticidade": 5,
        "horario": 8,
    },
    {
        "nome": "ENER-01",
        "tipo": "Energia",
        "prioridade": 2,
        "combustivel": 55,
        "massa": 12.0,
        "criticidade": 4,
        "horario": 9,
    },
    {
        "nome": "LAB-01",
        "tipo": "Laboratório Científico",
        "prioridade": 3,
        "combustivel": 88,
        "massa": 9.5,
        "criticidade": 3,
        "horario": 11,
    },
    {
        "nome": "LOG-01",
        "tipo": "Logística",
        "prioridade": 4,
        "combustivel": 30,
        "massa": 22.0,
        "criticidade": 2,
        "horario": 14,
    },
    {
        "nome": "MED-01",
        "tipo": "Suporte Médico",
        "prioridade": 2,
        "combustivel": 91,
        "massa": 7.8,
        "criticidade": 5,
        "horario": 10,
    },
    {
        "nome": "ENER-02",
        "tipo": "Energia",
        "prioridade": 2,
        "combustivel": 45,
        "massa": 11.5,
        "criticidade": 4,
        "horario": 13,
    },
    {
        "nome": "LOG-02",
        "tipo": "Logística",
        "prioridade": 5,
        "combustivel": 20,
        "massa": 25.0,
        "criticidade": 1,
        "horario": 16,
    },
]


fila_pouso = collections.deque()


lista_pousados = []

pilha_alertas = []

lista_espera = []

CONDICOES_ATMOSFERICAS = True

AREA_POUSO_DISPONIVEL = True

SENSORES_OK = True



def verificar_combustivel_minimo(modulo):
    
    return modulo["combustivel"] >= 40


def verificar_massa_maxima(modulo):
 
    return modulo["massa"] <= 24.0


def autorizar_pouso(modulo, atm_ok, area_ok, sensores_ok):

    combustivel_ok = verificar_combustivel_minimo(modulo)
    massa_ok = verificar_massa_maxima(modulo)

  
    seguranca_modulo = combustivel_ok and massa_ok


    condicoes_externas = atm_ok and area_ok

    decisao_final = seguranca_modulo and condicoes_externas and sensores_ok

    return decisao_final, combustivel_ok, massa_ok



def carregar_fila(modulos):
    """Insere todos os módulos na fila principal de pouso."""
    for m in modulos:
        fila_pouso.append(m)
    print(f"[INIT] {len(fila_pouso)} módulos carregados na fila de pouso.\n")



def busca_linear_por_tipo(estrutura, tipo_buscado):
    resultado = []
    for modulo in estrutura:
        if modulo["tipo"].lower() == tipo_buscado.lower():
            resultado.append(modulo)
    return resultado


def busca_menor_combustivel(estrutura):
    if not estrutura:
        return None
    menor = estrutura[0]
    for modulo in estrutura[1:]:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor


def busca_maior_prioridade(estrutura):
    if not estrutura:
        return None
    mais_prioritario = estrutura[0]
    for modulo in estrutura[1:]:
        if modulo["prioridade"] < mais_prioritario["prioridade"]:
            mais_prioritario = modulo
    return mais_prioritario


def busca_binaria_por_horario(lista_ordenada, horario_alvo):
    esquerda = 0
    direita = len(lista_ordenada) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        h = lista_ordenada[meio]["horario"]

        if h == horario_alvo:
            return meio         
        elif h < horario_alvo:
            esquerda = meio + 1  
        else:
            direita = meio - 1   

    return -1  




def bubble_sort_por_prioridade(lista):
  
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["prioridade"] > lista[j + 1]["prioridade"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def selection_sort_por_combustivel(lista):

    n = len(lista)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if lista[j]["combustivel"] < lista[idx_min]["combustivel"]:
                idx_min = j
        lista[i], lista[idx_min] = lista[idx_min], lista[i]
    return lista


def insertion_sort_por_horario(lista):

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["horario"] > chave["horario"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def simular_pouso():

    print("=" * 60)
    print("   SIMULAÇÃO DE POUSO - MISSÃO AURORA SIGER")
    print("=" * 60)
    print(f"Condições atmosféricas : {'✔ Favoráveis' if CONDICOES_ATMOSFERICAS else '✘ Desfavoráveis'}")
    print(f"Área de pouso          : {'✔ Disponível' if AREA_POUSO_DISPONIVEL else '✘ Ocupada'}")
    print(f"Sensores               : {'✔ Operacionais' if SENSORES_OK else '✘ Com falha'}")
    print("=" * 60 + "\n")

    numero_modulo = 1

    while fila_pouso:
    
        modulo = fila_pouso.popleft()

        print(f"[{numero_modulo:02d}] Processando: {modulo['nome']} ({modulo['tipo']})")
        print(f"     Prioridade: {modulo['prioridade']} | "
              f"Combustível: {modulo['combustivel']}% | "
              f"Massa: {modulo['massa']}t | "
              f"Horário: {modulo['horario']}h")

        autorizado, comb_ok, massa_ok = autorizar_pouso(
            modulo, CONDICOES_ATMOSFERICAS, AREA_POUSO_DISPONIVEL, SENSORES_OK
        )

        if autorizado:
            lista_pousados.append(modulo)
            print(f"     ✔ POUSO AUTORIZADO — {modulo['nome']} pousou com sucesso.\n")
        else:
  
            if not comb_ok:
                pilha_alertas.append(modulo)
                print(f"     ⚠ ALERTA DE COMBUSTÍVEL — {modulo['nome']} "
                      f"({modulo['combustivel']}% < 40%) empilhado para intervenção urgente.\n")
            else:
                lista_espera.append(modulo)
                motivo = []
                if not massa_ok:
                    motivo.append(f"massa {modulo['massa']}t > 24t")
                if not CONDICOES_ATMOSFERICAS:
                    motivo.append("atmosfera desfavorável")
                if not AREA_POUSO_DISPONIVEL:
                    motivo.append("área ocupada")
                if not SENSORES_OK:
                    motivo.append("falha nos sensores")
                print(f"     ✘ POUSO BLOQUEADO — {modulo['nome']} em espera. "
                      f"Motivo(s): {'; '.join(motivo)}.\n")

        numero_modulo += 1


def exibir_relatorio_final():

    print("\n" + "=" * 60)
    print("   RELATÓRIO FINAL DE POUSO")
    print("=" * 60)

    print(f"\n✔ MÓDULOS POUSADOS ({len(lista_pousados)}):")
    for m in lista_pousados:
        print(f"   - {m['nome']} ({m['tipo']}), Prioridade {m['prioridade']}")

    print(f"\n⚠ ALERTAS NA PILHA ({len(pilha_alertas)}) [atende o último primeiro]:")
    for m in reversed(pilha_alertas):
        print(f"   - {m['nome']} ({m['tipo']}), Combustível: {m['combustivel']}%")

    print(f"\n✘ MÓDULOS EM ESPERA ({len(lista_espera)}):")
    for m in lista_espera:
        print(f"   - {m['nome']} ({m['tipo']})")


    print("\n" + "─" * 60)
    print("   DEMONSTRAÇÃO DE ALGORITMOS DE BUSCA")
    print("─" * 60)

    todos = lista_pousados + lista_espera + list(pilha_alertas)

    menor_comb = busca_menor_combustivel(todos)
    if menor_comb:
        print(f"\n🔍 Módulo com MENOR combustível: {menor_comb['nome']} "
              f"({menor_comb['combustivel']}%)")

    maior_prior = busca_maior_prioridade(todos)
    if maior_prior:
        print(f"🔍 Módulo com MAIOR prioridade : {maior_prior['nome']} "
              f"(Prioridade {maior_prior['prioridade']})")

    energia = busca_linear_por_tipo(todos, "Energia")
    print(f"🔍 Módulos do tipo 'Energia'   : {[m['nome'] for m in energia]}")

    print("\n" + "─" * 60)
    print("   DEMONSTRAÇÃO DE ALGORITMOS DE ORDENAÇÃO")
    print("─" * 60)

    copia_todos = list(todos)  

    ordenado_prior = bubble_sort_por_prioridade(list(copia_todos))
    print("\n📋 Fila reordenada por PRIORIDADE (Bubble Sort):")
    for m in ordenado_prior:
        print(f"   [{m['prioridade']}] {m['nome']} ({m['tipo']})")

    ordenado_comb = selection_sort_por_combustivel(list(copia_todos))
    print("\n📋 Fila reordenada por COMBUSTÍVEL ↑ (Selection Sort):")
    for m in ordenado_comb:
        print(f"   [{m['combustivel']}%] {m['nome']}")

    ordenado_hora = insertion_sort_por_horario(list(copia_todos))
    print("\n📋 Fila reordenada por HORÁRIO (Insertion Sort):")
    for m in ordenado_hora:
        print(f"   [{m['horario']}h] {m['nome']}")


    horario_busca = 10
    idx = busca_binaria_por_horario(ordenado_hora, horario_busca)
    if idx != -1:
        print(f"\n🔍 Busca Binária por horário {horario_busca}h: "
              f"encontrado '{ordenado_hora[idx]['nome']}' no índice {idx}.")
    else:
        print(f"\n🔍 Busca Binária por horário {horario_busca}h: não encontrado.")

    print("\n" + "=" * 60)
    print("   FIM DA SIMULAÇÃO MGPEB — AURORA SIGER")
    print("=" * 60)



if __name__ == "__main__":
    carregar_fila(modulos_iniciais)  
    simular_pouso()                  
    exibir_relatorio_final()         
