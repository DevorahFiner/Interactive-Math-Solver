import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Interactive Math Solver", page_icon="📐")

# Title and description
st.title("🌟 Interactive Math Solver 🌟")
st.write("Solve quadratic equations, compute derivatives, or evaluate integrals with interactive visualizations!")

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
    
    a = st.number_input("Enter coefficient a:", value=1, format="%.2f")
    b = st.number_input("Enter coefficient b:", value=0, format="%.2f")
    c = st.number_input("Enter coefficient c:", value=0, format="%.2f")

    if st.button("Solve"):
        # Solve quadratic equation ax^2 + bx + c = 0
        x = sp.symbols('x')
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        solutions = sp.solve(equation, x)
        st.write(f"### Solutions: {solutions}")
        
        # Display step-by-step solution
        st.write("### Step-by-step solution:")
        st.write(f"1. Identify the coefficients: a = {a}, b = {b}, c = {c}.")
        st.write("2. Use the quadratic formula: x = (-b ± √(b² - 4ac)) / (2a).")
        
        # Plot the quadratic function
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a * x_vals ** 2 + b * x_vals + c
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f"{a}x² + {b}x + {c}", color='blue')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
        plt.title(f"Quadratic Function: {a}x² + {b}x + {c}", fontsize=16)
        plt.xlabel("x", fontsize=14)
        plt.ylabel("f(x)", fontsize=14)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
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
        
        # Plot the function and its derivative
        x_vals = np.linspace(-10, 10, 400)
        f_vals = [expr.subs(x, val) for val in x_vals]
        df_vals = [derivative.subs(x, val) for val in x_vals]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, f_vals, label=f"f(x) = {expression}", color='blue')
        plt.plot(x_vals, df_vals, label=f"f'(x) = {derivative}", color='red', linestyle='--')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
        plt.title("Function and Its Derivative", fontsize=16)
        plt.xlabel("x", fontsize=14)
        plt.ylabel("y", fontsize=14)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        st.pyplot(plt)

elif operation == "Evaluate Integral":
    st.header("➕ Evaluate Integral")
    
    expression = st.text_input("Enter a mathematical expression to integrate:")
    
    if expression:
        expr = sp.sympify(expression)
        x = sp.symbols('x')
        integral = sp.integrate(expr, x)
        st.write(f"The integral of {expression} is:")
        st.latex(sp.latex(integral))
        
        # Plot the function and its integral
        x_vals = np.linspace(-10, 10, 400)
        f_vals = [expr.subs(x, val) for val in x_vals]
        F_vals = [sp.integrate(expr, (x, 0, val)).evalf() for val in x_vals]  # Definite integral from 0 to x
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, f_vals, label=f"f(x) = {expression}", color='blue')
        plt.plot(x_vals, F_vals, label=f"F(x) = ∫f(x)dx", color='green', linestyle='--')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
        plt.title("Function and Its Integral", fontsize=16)
        plt.xlabel("x", fontsize=14)
        plt.ylabel("y", fontsize=14)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        st.pyplot(plt)

