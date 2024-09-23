import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.title("Interactive Math Solver")
st.write("Solve quadratic equations, compute derivatives, or evaluate integrals!")

# Sidebar for choosing operation
operation = st.sidebar.selectbox(
    "Choose the operation:",
    options=["Solve Quadratic Equation", "Find Derivative", "Evaluate Integral"]
)

if operation == "Solve Quadratic Equation":
    st.header("Solve Quadratic Equation")
    
    a = st.number_input("Enter coefficient a:", value=1)
    b = st.number_input("Enter coefficient b:", value=0)
    c = st.number_input("Enter coefficient c:", value=0)

    if st.button("Solve"):
        # Solve quadratic equation ax^2 + bx + c = 0
        x = sp.symbols('x')
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        solutions = sp.solve(equation, x)
        st.write(f"Solutions: {solutions}")

elif operation == "Find Derivative":
    st.header("Find Derivative")
    
    expression = st.text_input("Enter a mathematical expression:")
    
    if expression:
        expr = sp.sympify(expression)
        x = sp.symbols('x')
        derivative = sp.diff(expr, x)
        st.write(f"The derivative of {expression} is:")
        st.latex(sp.latex(derivative))

elif operation == "Evaluate Integral":
    st.header("Evaluate Integral")
    
    expression = st.text_input("Enter a mathematical expression to integrate:")
    
    if expression:
        expr = sp.sympify(expression)
        x = sp.symbols('x')
        integral = sp.integrate(expr, x)
        st.write(f"The integral of {expression} is:")
        st.latex(sp.latex(integral))

# Optionally plot quadratic function
if operation == "Solve Quadratic Equation" and st.checkbox("Plot the quadratic function?"):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a * x_vals ** 2 + b * x_vals + c
    
    plt.plot(x_vals, y_vals)
    plt.title(f"Quadratic Function: {a}x^2 + {b}x + {c}")
    st.pyplot(plt)
