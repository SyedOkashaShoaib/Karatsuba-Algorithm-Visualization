import streamlit as st

st.title("Karatsuba Algorithm Implementation in Python")

code = '''def karatsuba_function(num1,num2):
        if num1 < 10 or num2 < 10: 
            return num1*num2
        n = max(len(str(abs(num1))), len(str(abs(num2))))
        m = n // 2 
        power = 10 ** m
        a = num1 // power
        b = num1 % power
        c = num2 // power
        d = num2 % power
        p1 = karatsuba_function(a,c)
        p2 = karatsuba_function(b,d)
        p3 = karatsuba_function((a+b),(c+d))    
        product = p1*pow(10,(2*m)) + (p3- p1 - p2)*pow(10,m)   + p2
        return product'''
with st.container():
   st.code(code,language="python")
