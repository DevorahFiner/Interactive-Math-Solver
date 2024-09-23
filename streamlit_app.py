import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Interactive Math Solver", page_icon="📐")

# Title and description
st.title("🌟 Interactive Math Solver 🌟")
st.write("Solve quadratic equations, compute derivatives, or evaluate integrals!")

# Sidebar for choosing operation
operation = st.sidebar.selectbox(
    "Choose the operation:",
    options=["Solve Quadratic Equation", "Find Derivative", "Evaluate Integral"]
)

# Add a colorful sidebar header
st.sidebar.header("Math Operations")
st.sidebar.markdown("Choose an operation from the dropdown menu.")

if operation == "Solve Quadratic Equation":
    st.header("🔍 Solve Quadratic Equation")
    
    a = st.number_input("Enter coefficient a:", value=1)
    b = st.number_input("Enter coefficient b:", value=0)
    c = st.number_input("Enter coefficient c:", value=0)

    if st.button("Solve"):
        # Solve quadratic equation ax^2 + bx + c = 0
        x = sp.symbols('x')
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        solutions = sp.solve(equation, x)
        st.write(f"### Solutions: {solutions}")

        # Plot the quadratic function
        x_vals = np.linspace(-15, 15, 400)  # Adjusted x range
        y_vals = a * x_vals ** 2 + b * x_vals + c
        
        plt.figure(figsize=(12, 8))  # Increased figure size
        plt.plot(x_vals, y_vals, label=f"{a}x² + {b}x + {c}", color='blue')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
        plt.title(f"Quadratic Function: {a}x² + {b}x + {c}", fontsize=20)
        plt.xlabel("x", fontsize=16)
        plt.ylabel("f(x)", fontsize=16)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend(fontsize=14)
        plt.xlim(-15, 15)  # Adjusted x limits
        plt.ylim(min(y_vals) - 10, max(y_vals) + 10)  # Adjusted y limits
        plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.3)  # Fill area under curve
        st.pyplot(plt)

elif operation == "Find Derivative":
    st.header("🔢 Find Derivative")
    
    expression = st.text_input("Enter a mathematical expression:")
    
    if expression:
        expr = sp.sympify(expression)
        x = sp.symbols('x')
        derivative = sp.diff(expr, x)
        st.write(f"The derivative of {expression} is:")
        st.latex(sp.latex(derivative))

elif operation == "Evaluate Integral":
    st.header("➕ Evaluate Integral")
    
    expression = st.text_input("Enter a mathematical expression to integrate:")
    
    if expression:
        expr = sp.sympify(expression)
        x = sp.symbols('x')
        integral = sp.integrate(expr, x)
        st.write(f"The integral of {expression} is:")
        st.latex(sp.latex(integral))
