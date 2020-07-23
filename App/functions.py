import numpy as np
from pathlib import Path

# DICIONARIO CONTENDO A QUANTIDADE DE SIMBOLOS POR TIPO DO PREFIXO CILICO (NORMAL OU EXTENDIDO)
CYCLIC_PREFIX = {
    'Normal': {'SYMBOLS': 7},
    'Extendido': {'SYMBOLS': 6}
}

# DICIONARIO CONTENDO QUANTIDADE DE RESOURCE BLOCKS POR LARGURA DE BANDA UTILIZADA
PRB_PER_BW = {
    '1.4': (1.4, 6),
    '3': (3, 15),
    '5': (5, 25),
    '10': (10, 50),
    '15': (15, 75),
    '20': (20, 100),
    '100': (100, 100)

}

# DICIONARIO QUE MAPEIA A QUANTIDADE DE SIMBOLOS DA MODULACAO UTILIZADA, A TAXA DE CODIFICACAO E O INDICE DA TABELA TBS
# PELO VALOR DO MCS INDICAO NA INTERFACE
MODULATION_AND_CODE_RATE = {
    '0': {'MOD': 2, 'CR': 0.1172, 'TBSINDEX': 0}, '1': {'MOD': 2, 'CR': 0.1533, 'TBSINDEX': 1},
    '2': {'MOD': 2, 'CR': 0.1884, 'TBSINDEX': 2}, '3': {'MOD': 2, 'CR': 0.2451, 'TBSINDEX': 3},
    '4': {'MOD': 2, 'CR': 0.3007, 'TBSINDEX': 4}, '5': {'MOD': 2, 'CR': 0.3701, 'TBSINDEX': 5},
    '6': {'MOD': 2, 'CR': 0.4384, 'TBSINDEX': 6}, '7': {'MOD': 2, 'CR': 0.5136, 'TBSINDEX': 7},
    '8': {'MOD': 2, 'CR': 0.5879, 'TBSINDEX': 8}, '9': {'MOD': 2, 'CR': 0.6630, 'TBSINDEX': 9},
    '10': {'MOD': 4, 'CR': 0.3320, 'TBSINDEX': 9}, '11': {'MOD': 4, 'CR': 0.3691, 'TBSINDEX': 10},
    '12': {'MOD': 4, 'CR': 0.4238, 'TBSINDEX': 11}, '13': {'MOD': 4, 'CR': 0.4785, 'TBSINDEX': 12},
    '14': {'MOD': 4, 'CR': 0.5400, 'TBSINDEX': 13}, '15': {'MOD': 4, 'CR': 0.6015, 'TBSINDEX': 14},
    '16': {'MOD': 4, 'CR': 0.6425, 'TBSINDEX': 15}, '17': {'MOD': 6, 'CR': 0.4277, 'TBSINDEX': 15},
    '18': {'MOD': 6, 'CR': 0.4550, 'TBSINDEX': 16}, '19': {'MOD': 6, 'CR': 0.5049, 'TBSINDEX': 17},
    '20': {'MOD': 6, 'CR': 0.5537, 'TBSINDEX': 18}, '21': {'MOD': 6, 'CR': 0.6015, 'TBSINDEX': 19},
    '22': {'MOD': 6, 'CR': 0.6503, 'TBSINDEX': 20}, '23': {'MOD': 6, 'CR': 0.7021, 'TBSINDEX': 21},
    '24': {'MOD': 6, 'CR': 0.7540, 'TBSINDEX': 22}, '25': {'MOD': 6, 'CR': 0.8027, 'TBSINDEX': 23},
    '26': {'MOD': 6, 'CR': 0.8525, 'TBSINDEX': 24}, '27': {'MOD': 6, 'CR': 0.8886, 'TBSINDEX': 25},
    '28': {'MOD': 6, 'CR': 0.9257, 'TBSINDEX': 26}
}

# DICIONARIO QUE CONTEM O VALOR DO MIMO
MIMO = {'1': 1, '2': 2, '4': 4, '8': 8}

# PEGA O CAMINHO DO ARQUIVO QUE CONTEM A TABELA DE MCSxPRBs
data_folder = Path("assets/")
csv_file = data_folder / "tbs_size_table.csv"

# CONVERTE A TABELA ACIMA EM UM ARRAY PARA FACIL ACESSO.
tbs_size_table = np.genfromtxt(csv_file, delimiter=",", skip_header=1, dtype=int)


def calc_lte_troughtput(bandwidth, mcs, mimo_type, cyclic_prefix_type, component_carriers):

    """
    Funcao que realiza o calculo do throughput usando a tabela da norma e a equacao.

    :param bandwidth: Largura de banda
    :param mcs: MSC
    :param mimo_type: Tipo do mimo utilizado
    :param cyclic_prefix_type: Prefixo ciclico
    :param component_carriers: Carrier Agregation
    :return: dict()
    """
    num_prbs = PRB_PER_BW[bandwidth][1]
    tbs_index = MODULATION_AND_CODE_RATE[mcs]['TBSINDEX']
    bits_from_tbs_size_table = tbs_size_table[tbs_index, int(num_prbs)]
    mimo = MIMO[mimo_type]
    cyclic_prefix = CYCLIC_PREFIX[cyclic_prefix_type]['SYMBOLS']
    ca = int(component_carriers)
    nre = 12 * cyclic_prefix

    # Calculo pela tabela
    troughput_table = (bits_from_tbs_size_table * ca * mimo * cyclic_prefix) / 7e3

    # Calculo pela equacao
    troughput_equation = (nre * MODULATION_AND_CODE_RATE[mcs]["MOD"] * mimo * 2 * num_prbs * 0.75 * ca) / 1_000

    return {
        'TROUGHPUT_TABLE': float(f'{troughput_table:.2f}'),
        'TROUGHPUT_EQUATION': float(f'{troughput_equation:.2f}'),
        'PRBS': num_prbs,
        'TBSINDEX': tbs_index,
        'TBSVALUE': bits_from_tbs_size_table,
        'MODULATION': 2 ** MODULATION_AND_CODE_RATE[mcs]["MOD"],
        'NRE': nre,
        'SYMBOLSQTD': cyclic_prefix
    }
