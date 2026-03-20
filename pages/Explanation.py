import streamlit as st


st.title("Karatsuba Algorithm")
    
st.markdown("""
    ## Overview
    The **Karatsuba algorithm** is a fast multiplication algorithm that uses a divide-and-conquer approach 
    to multiply two numbers. It was discovered by Anatoly Karatsuba in 1960 and has a time complexity of 
    **O(n^log₂³) ≈ O(n¹⋅⁵⁸⁵)**, which is significantly faster than the traditional O(n²) schoolbook multiplication 
    for large numbers.
    """)
    

    
st.header("How It Works")
    
st.subheader("Traditional vs Karatsuba")
st.markdown("""
    - **Traditional**: Requires 4 multiplications for n-digit numbers
    - **Karatsuba**: Requires only 3 multiplications through mathematical optimization
    """)
    
st.subheader("The Key Insight")
st.markdown("For two n-digit numbers x and y, we can split them as:")
    
st.latex(r'''
    \begin{aligned}
    &x = a \cdot 10^m + b \\
    &y = c \cdot 10^m + d
    \end{aligned}
    ''')
    

    
st.subheader("The Mathematical Trick")
st.markdown("Instead of computing:")
    
st.latex(r'''x \cdot y = a \cdot c \cdot 10^{2m} + (a \cdot d + b \cdot c) \cdot 10^m + b \cdot d \quad \text{(4 multiplications)}''')
    
st.markdown("Karatsuba computes:")
    
st.latex(r'''x \cdot y = a \cdot c \cdot 10^{2m} + [(a + b) \cdot (c + d) - a \cdot c - b \cdot d] \cdot 10^m + b \cdot d \quad \text{(3 multiplications)}''')
    
    
st.header("Algorithm Steps")
    
steps = [
        "**Base Case**: If numbers are small (typically < 10 digits), use direct multiplication",
        "**Split**: Divide each number into two halves",
        "**Recurse**: Compute three products recursively:",
        "   $z₀ = b * d$",
        "   $z₁ = a * c$", 
        "  - $z₂ = (a + b) * (c + d)$",
        "**Combine**: Use the Karatsuba formula"
    ]
    
for step in steps:
    st.markdown(f"- {step}")
    
st.latex(r'''\text{result} = z_1 \cdot 10^{2m} + (z_2 - z_1 - z_0) \cdot 10^m + z_0''')
    

    