import ply.lex as lex

tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'PAR_APERTURA',
    'PAR_CIERRE',
    'LLAVE_APERTURA',
    'LLAVE_CIERRE',
    'PUNTO_Y_COMA',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'UMINUS',
    'PAR_IZQ',
    'PAR_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'CORIZQ',
    'CORDER',
    'COMILLA_DOBLE',
    'ENTERO',
    'AND',
    'OR',
    'NOT',
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'IGUAL',
    'DISTINTO',
    'FLOTANTE',
]

reservadas = {
    'main': 'MAIN',
    'for': 'FOR',
    'if': 'IF',
    'while': 'WHILE',
    'return': 'RETURN',
}

tipos_dato = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void': 'VOID'
}

tokens = list(tokens) + list(reservadas.values()) + list(tipos_dato.values())

t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_UMINUS = r'-'
t_PAR_IZQ = r'\('
t_PAR_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_CORIZQ = r'\{'
t_CORDER = r'\}'
t_COMILLA_DOBLE = r'\"'
t_ENTERO = r'\d+'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_FLOTANTE = r'\d+\.\d+[eE][+-]?\d+|\d+\.\d+'

t_ignore = ' \t'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  
    return t

def t_NUMERO(t):
    r'\d+|\d+\.\d+[eE][+-]?\d+|\d+\.\d+'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_error(t):
    print(f"Caracter inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_codigo(codigo):
    lineas = codigo.splitlines()
    resultado = []
    
    for i, linea in enumerate(lineas, start=1):
        lexer.input(linea)
        tokens_por_linea = []
        
        for token in lexer:
            tipo_token = token.type
            valor_token = token.value
            
            if tipo_token in tipos_dato.values():
                tokens_por_linea.append(("<Tipo de dato>", valor_token))
            elif tipo_token in reservadas.values():
                tokens_por_linea.append(("<Palabra reservada>", valor_token))
            else:
                tokens_por_linea.append((f"<{tipo_token}>", valor_token))
        
        resultado.append((f"LINEA {i}", tokens_por_linea))
    
    return resultado