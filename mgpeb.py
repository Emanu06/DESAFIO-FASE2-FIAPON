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

# --- ESTRUTURAS DE DADOS ---
fila_pouso = collections.deque()
lista_pousados = []
pilha_alertas = []
lista_espera = []

# --- VARIÁVEIS DE AMBIENTE ---
CONDICOES_ATMOSFERICAS = True
AREA_POUSO_DISPONIVEL = True
SENSORES_OK = True

# --- FUNÇÕES DE VERIFICAÇÃO ---
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
    for m in modulos:
        fila_pouso.append(m)
    print(f"[INIT] {len(fila_pouso)} modulos carregados na fila de pouso.\n")

# --- ALGORITMOS DE BUSCA ---
def busca_linear_por_tipo(estrutura, tipo_buscado):
    resultado = []
    for modulo in estrutura:
        if modulo["tipo"].lower() == tipo_buscado.lower():
            resultado.append(modulo)
    return resultado

def busca_menor_combustivel(estrutura):
    if not estrutura: return None
    menor = estrutura[0]
    for modulo in estrutura[1:]:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor

def busca_maior_prioridade(estrutura):
    if not estrutura: return None
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

# --- ALGORITMOS DE ORDENAÇÃO ---
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

# --- SIMULAÇÃO ---
def simular_pouso():
    print("=" * 60)
    print("   SIMULACAO DE POUSO - MISSAO AURORA SIGER")
    print("=" * 60)
    print(f"Condicoes atmosfericas : {'Favoraveis' if CONDICOES_ATMOSFERICAS else 'Desfavoraveis'}")
    print(f"Area de pouso          : {'Disponivel' if AREA_POUSO_DISPONIVEL else 'Ocupada'}")
    print(f"Sensores               : {'Operacionais' if SENSORES_OK else 'Com falha'}")
    print("=" * 60 + "\n")

    numero_modulo = 1
    while fila_pouso:
        modulo = fila_pouso.popleft()
        print(f"[{numero_modulo:02d}] Processando: {modulo['nome']} ({modulo['tipo']})")
        
        autorizado, comb_ok, massa_ok = autorizar_pouso(
            modulo, CONDICOES_ATMOSFERICAS, AREA_POUSO_DISPONIVEL, SENSORES_OK
        )

        if autorizado:
            lista_pousados.append(modulo)
            print(f"     POUSO AUTORIZADO - {modulo['nome']} pousou com sucesso.\n")
        else:
            if not comb_ok:
                pilha_alertas.append(modulo)
                print(f"     ALERTA DE COMBUSTIVEL - {modulo['nome']} empilhado.\n")
            else:
                lista_espera.append(modulo)
                print(f"     POUSO BLOQUEADO - {modulo['nome']} em espera.\n")
        numero_modulo += 1

def exibir_relatorio_final():
    print("\n" + "=" * 60)
    print("   RELATORIO FINAL DE POUSO")
    print("=" * 60)
    print(f"Pousados: {len(lista_pousados)} | Alertas: {len(pilha_alertas)} | Espera: {len(lista_espera)}")
    
    print("\nDEMONSTRACAO DE ORDENACAO (HORARIO):")
    todos = lista_pousados + lista_espera + list(pilha_alertas)
    for m in insertion_sort_por_horario(list(todos)):
        print(f" - [{m['horario']}h] {m['nome']}")


# BLOCO PARA TESTES INTERATIVOS (OPCIONAL)

#def adicionar_modulo_pelo_usuario():
#    """Permite ao usuario cadastrar um modulo manualmente via console."""
 #   print("\n--- CADASTRO DE NOVO MODULO ---")
  #      nome = input("Nome do modulo (ex: HAB-02): ")
   # try:
    #    tipo = input("Tipo (ex: Energia, Habitacao): ")
     #   prioridade = int(input("Prioridade (1-5): "))
      #  combustivel = float(input("Nivel de combustivel (0-100): "))
       # massa = float(input("Massa em toneladas: "))
        #criticidade = int(input("Nivel de criticidade (1-5): "))
        #horario = int(input("Horario previsto (0-23): "))

        #novo_modulo = {
 #           "nome": nome, "tipo": tipo, "prioridade": prioridade,
  #          "combustivel": combustivel, "massa": massa,
   #         "criticidade": criticidade, "horario": horario,
    #    }
     #   fila_pouso.append(novo_modulo)
      #  print(f"Modulo {nome} adicionado a fila!\n")
    #except ValueError:
     #   print("Erro: Entrada invalida. Use numeros onde solicitado.")

if __name__ == "__main__":
    carregar_fila(modulos_iniciais)

    # CASO QUEIRA TESTAR COM DADOS, APENAS TESTAR LINHAS ABAIXO
    # opcao = input("Deseja inserir um modulo manualmente antes de iniciar? (s/n): ")
    # if opcao.lower() == 's': adicionar_modulo_pelo_usuario()

    simular_pouso()
    exibir_relatorio_final()
