import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the spreadsheet
# Key: Number of Paper Clips (0 to 4)
# Value: Recorded flight times across all trials
data = {
    0: [2.10, 2.18, 2.40, 1.19, 1.73, 1.59, 1.34, 1.96, 1.93, 2.14, 2.13, 2.11, 1.46, 1.46, 1.63, 1.71, 1.65, 1.44, 2.17, 2.09, 2.50],
    1: [1.86, 1.93, 2.10, 1.53, 1.31, 1.28, 1.73, 2.11, 2.04, 1.63, 1.80, 1.81, 1.45, 1.46, 1.52, 1.44, 1.52, 1.50, 2.39, 1.75, 1.90],
    2: [1.85, 1.75, 1.78, 1.36, 1.11, 1.19, 1.84, 1.71, 1.74, 2.20, 2.10, 2.03, 1.59, 1.45, 1.52, 1.39, 1.46, 1.45, 1.87, 1.71, 1.62],
    3: [1.71, 1.75, 1.63, 1.20, 1.00, 1.06, 1.76, 1.71, 1.53, 1.71, 1.85, 1.83, 1.52, 1.52, 1.26, 1.25, 1.32, 1.45, 1.94, 1.66, 1.50],
    4: [1.56, 1.71, 1.61, 1.14, 0.98, 1.06, 1.73, 1.19, 1.39, 1.55, 1.78, 1.95, 1.32, 1.25, 1.58, 0.99, 1.38, 1.13, 1.53, 1.50, 1.60]
}

# Flatten data for scatterplot
x_vals = []
y_vals = []
paper_clip_counts = list(data.keys())
mean_times = []

for clips, times in data.items():
    x_vals.extend([clips] * len(times))
    y_vals.extend(times)
    mean_times.append(np.mean(times))

# Plot configuration
plt.figure(figsize=(10, 6))

# Individual data points (Scatterplot)
plt.scatter(x_vals, y_vals, color='steelblue', alpha=0.6, edgecolors='w', s=60, label='Trial Data Points')

# Mean flight times for each paper clip count
plt.plot(paper_clip_counts, mean_times, color='crimson', marker='D', linestyle='-', linewidth=2, label='Mean Flight Time')

# Trendline (Linear Regression)
m, b = np.polyfit(x_vals, y_vals, 1)
x_line = np.linspace(0, 4, 100)
plt.plot(x_line, m * x_line + b, color='black', linestyle='--', linewidth=1.5, label=f'Trendline (y = {m:.3f}x + {b:.3f})')

# Formatting and Labels
plt.title('Whirlybird Flight Time vs. Number of Paper Clips', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Number of Paper Clips', fontsize=12)
plt.ylabel('Flight Time (seconds)', fontsize=12)
plt.xticks(paper_clip_counts)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show() 