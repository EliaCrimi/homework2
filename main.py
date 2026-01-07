# hw03_demo.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import your C++ pybind11 module
import cpp_toolbox

# -------------------------------
# 1) Interpolation (C++ backend)
# -------------------------------
nodes = {0.0: 0.0, 1.0: 1.0, 2.0: 4.0}
li = cpp_toolbox.LinearInterpolation(nodes)
pi = cpp_toolbox.PolynomialInterpolation(nodes)

x_values = np.linspace(0, 2, 100)
y_linear = np.array([li(x) for x in x_values])
y_poly = np.array([pi(x) for x in x_values])

# -------------------------------
# 2) Statistics from CSV (C++ backend)
# -------------------------------
stats = cpp_toolbox.LoadStatistics()
stats.loadCSV("data.csv")  # Replace with your CSV file

# Convert first column to pandas Series for analysis
col0 = [x if isinstance(x, float) else np.nan for x in stats.getColumn(0)]
col0_series = pd.Series(col0)

# NumPy / SciPy analysis
mean0 = np.nanmean(col0)
std0 = np.nanstd(col0)
median0 = np.nanmedian(col0)

print(f"Column 0 stats: mean={mean0:.2f}, std={std0:.2f}, median={median0:.2f}")

# -------------------------------
# 3) Visualization
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(x_values, y_linear, label="Linear Interpolation")
plt.plot(x_values, y_poly, label="Polynomial Interpolation")
plt.scatter(list(nodes.keys()), list(nodes.values()), color='red', label="Nodes")
plt.title("Interpolation Example")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# seaborn histogram of column 0
sns.histplot(col0_series.dropna(), bins=20, kde=True)
plt.title("Column 0 Distribution")
plt.show()

