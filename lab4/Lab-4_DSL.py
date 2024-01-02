import ply.lex as lex
import ply.yacc as yacc
import streamlit as st

# Lexer tokens
tokens = (
    'OPERATION',
    'NUMBER',
)

t_OPERATION = r'SUM|STRSUM'
t_NUMBER = r'\d+'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Invalid character: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression_operation(p):
    '''expression : OPERATION NUMBER NUMBER'''
    if p[1] == 'SUM':
        p[0] = int(p[2]) + int(p[3])
    elif p[1] == 'STRSUM':
        p[0] = p[2] + p[3]

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

def main():
    st.title("OnePiece DSL Calculator")
    
    operation_input = st.text_input("Enter operation (e.g., SUM 2 3 or STRSUM 2 3):")
    
    if st.button("Evaluate"):
        result = parser.parse(operation_input)
        st.success(f"Result: {result}")

if __name__ == '__main__':
    main()
