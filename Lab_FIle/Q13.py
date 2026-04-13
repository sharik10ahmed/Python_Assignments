import numpy as np
import matplotlib.pyplot as plt

def plot_math_curves():
    # Create x values from -2π to 2π
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    
    # Calculate different functions
    sine = np.sin(x)
    cosine = np.cos(x)
    polynomial = x**3 - 3*x  # Cubic polynomial
    exponential = np.exp(-x**2 / 2)  # Gaussian (bell curve)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    plt.plot(x, sine, label='sin(x)', linewidth=2, color='blue')
    plt.plot(x, cosine, label='cos(x)', linewidth=2, color='red')
    plt.plot(x, polynomial, label='x³ - 3x', linewidth=2, color='green')
    plt.plot(x, exponential, label='e^(-x²/2)', linewidth=2, color='purple')
    
    plt.title('Mathematical Curves: Sine, Cosine, Polynomial, and Exponential', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()

# Call the function
plot_math_curves()
