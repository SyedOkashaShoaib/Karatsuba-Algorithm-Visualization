import math
import os   
import streamlit as st
import random
import string 
from io import StringIO

if "generated" not in st.session_state:
    st.session_state.generated = False


def karatsuba_function(num1,num2):
    if num1 < 10 or num2 < 10: 
        container.markdown(f"Since either *input 1* ({num1}) or *input 2* ({num2}) is less than 10 (*or perhaps both of them are* ), we can finally say we have reached the base case:")
        container.latex(rf'''input 1 \cdot input 2''')
        container.latex(rf'''{num1}  \cdot  {num2} = {num1*num2}''')
        container.markdown(f"Returning {num1*num2}...")
        return num1*num2
    n = max(len(str(abs(num1))), len(str(abs(num2))))
    m = n // 2 
    power = 10 ** m
    a = num1 // power
    b = num1 % power
    c = num2 // power
    d = num2 % power
    container.markdown(f"Representing **{num1}** as the following equation:")
    container.latex(r'''X = a \cdot 10^m + b   ''')
    container.markdown("Where,")
    container.latex(rf'''a = {a} \\ b = {b}''')
    container.markdown(f"Similarly, we are going to represent **{num2}** by the following equation: ")
    container.latex(r'''Y = c \cdot 10^m + d''')
    container.markdown("Where,")
    container.latex(rf'''c = {c} \\ d = {d}''')
    container.markdown("For both equations, the value of m must be the same: ")
    container.latex(rf'''m = {m}''')
    
    
    # p1=1
    container.markdown(f"In order to find the value of p1 for **{num1}** and **{num2}** , we are going to recursively call the function again and set the values for input 1 and input 2 as the values of the variables a and c respectively:")
    container.latex(rf'''input 1={a}\\input2={c}''')
    
    p1 = karatsuba_function(a,c)
    container.markdown(f"We have found the value of p1 for {num1} and {num2}:")
    container.latex(rf'''p_1 = {p1}''')
    container.markdown(f"In order to find the value of p2 for **{num1}** and **{num2}** , we are going to recursively call the function again and set the values for input 1 and input 2 as the values of the variables b and d respectively:")
    container.latex(rf'''input 1={b}\\input2={d}''')
    p2 = karatsuba_function(b,d)
    container.markdown(f"We have found the value of p2 for {num1} and {num2}:")
    container.latex(rf'''p_2 = {p1}''')
    container.markdown(f"In order to find the value of p3 for **{num1}** and **{num2}** , we are going to recursively call the function again and set the values for input 1 and input 2 as the values (a + b) and (c + d) respectively:")
    container.latex(rf'''input 1={a+b}\\input2={c+d}''')
    p3 = karatsuba_function((a+b),(c+d))    
    
    

    

    product = p1*pow(10,(2*m)) + (p3- p1 - p2)*pow(10,m)   + p2
    # container.markdown(f"We have found the values of p1, p2, and p3 for {num1} and {num2} successfully.Plugging them in the following formula:")
    # container.latex(r'''Product = p1 \cdot 10^{2m} + (p3 - p1 - p2 ) \cdot 10^{m} + p2''') 
    # container.latex(rf'''Product= {p1} \cdot 10^{2*m} + ({p3} - {p2} - {p1}) \cdot 10^{m} + {p2} 
    #                     \\Product ={product}''')

    
    container.latex(rf'''
        \begin{{aligned}}
        &\text{{Product}} = p_1 \cdot 10^{{2m}} + (p_3 - p_1 - p_2) \cdot 10^m + p_2 \end{{aligned}}''')
    container.markdown("Plugging in the aquired values:")
    container.latex(rf'''
        \begin{{aligned}}
        &= {p1} \cdot 10^{{2*m}} + ({p3} - {p1} - {p2}) \cdot 10^{{m}} + {p2} \\
        &= {p1} \cdot {10**(2*m)} + ({p3 - p1 - p2}) \cdot {10**m} + {p2} \\
        &= {p1 * (10**(2*m))} + {(p3 - p1 - p2) * (10**m)} + {p2} \\
        &= {product}
        \end{{aligned}}
        ''')
    return product

def generate_inputs():
    characters = '123456789'
    for i in range(0,10):
        length1 = random.randint(0,10)
        length2 = random.randint(0,10)
        input_1 = ''.join(random.choices(characters,k= length1 + 1))
        input_2 = ''.join(random.choices(characters, k=length2 + 1)) 
        with open (f"./inputfiles/file{i}.txt", "w") as file_obj:
            file_obj.write(input_1 + ' ' + input_2)

    st.session_state.generated = True

st.title("Karatsuba's Algorithm with a very nice UI")

col1,col2 = st.columns([1,3])
with col1:
    st.button("Generate Input files",key="generate", on_click=generate_inputs)
if st.session_state.generated: 
    epstein_list = [ f for f in os.listdir("./inputfiles") if f.endswith(".txt")]
    with st.form("input_selection_form"):
        file_name = st.selectbox("Choose an input file",epstein_list,index=None)
        st.form_submit_button("Visualize")
        
    if file_name:
        with open(f"./inputfiles/{file_name}","r") as file_obj:
            content = file_obj.read()
            # st.write(content)
            numbers = content.split(' ')  
            st.write("Working")
            num1 = int(numbers[0])
            st.write(" NOt Working")
            num2 = int(numbers[1])
        #ima add checks for ensuring a random file is not iserted later on
            with st.container():
                st.title("Visualization")
        container = st.container(border=True)
        container.markdown("The integers that we have to multiply are: ")
        container.latex(rf'''Input 1 = {num1} \\ input 2 = {num2}''')
        karatsuba_function(num1,num2)

def visualize():
    """God knows"""


    # print(f"{n1} {n2} {m} {a} {b} {c} {d}")

# product = karatsuba_function(5141827774193825,1763612285207119)
# print(f"{product}")
    

#maybe use markdown to differentiate with colors or something?
#st.badge as well.




