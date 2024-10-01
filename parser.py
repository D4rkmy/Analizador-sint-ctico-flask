import ply.yacc as yacc
from lexer import tokens

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion'''
    pass

def p_instruccion(p):
    '''instruccion : asignacion
                   | condicion
                   | ciclo'''
    pass

def p_asignacion(p):
    'asignacion : IDENTIFICADOR ASIGNAR expresion PUNTO_Y_COMA'
    pass

def p_condicion(p):
    'condicion : IF PAR_APERTURA expresion PAR_CIERRE instrucciones'
    pass

def p_ciclo(p):
    'ciclo : WHILE PAR_APERTURA expresion PAR_CIERRE instrucciones'
    pass

def p_expresion(p):
    '''expresion : IDENTIFICADOR
                 | NUMERO
                 | expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

def analizar_sintaxis(codigo):
    parser = yacc.yacc()
    errores = []
    try:
        parser.parse(codigo)
    except Exception as e:
        errores.append(f"Error: {str(e)}")
    return errores
