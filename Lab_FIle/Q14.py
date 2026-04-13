import matplotlib.pyplot as plt
import numpy as np

# Get input from user - 12 months of profits
print("Enter profits for 12 months (in thousands):")
profits = []
for i in range(12):
    profit = float(input(f"Month {i+1}: "))
    profits.append(profit)

# Month numbers (1-12) for x-axis
months = np.arange(1, 13)

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(months, profits, marker='o', linewidth=2.5, markersize=8, color='#1f77b4')

# Set EXACT axis labels as specified
plt.xlabel("Month Number")
plt.ylabel("Total profit")

# Formatting
plt.title("Company ABC - Monthly Profits Over a Year", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(months)

# Show the plot
plt.tight_layout()
plt.show()

print("\n✓ Line plot generated successfully with specified axis labels!")