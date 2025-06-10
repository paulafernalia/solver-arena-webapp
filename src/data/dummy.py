import numpy as np
import pandas as pd

from utils.solvers import names as solvernames

# List of solver names

# Number of solvers
n = len(solvernames)

# Create sample data (reasonable random values)
data = {
    "solvers": solvernames,
    "time": np.round(
        np.random.uniform(10, 300, n), 2
    ),  # Time in seconds (10s to 5 mins)
    "ub": np.round(np.random.uniform(1000, 5000, n), 1),  # Objective values
    "lb": np.round(
        np.random.uniform(900, 4800, n), 1
    ),  # Bound values, slightly less than best solution
    "gap": np.round(np.random.uniform(0, 0.1, n), 4),  # Gap between 0% and 10%
    "nodes": np.random.randint(1000, 50000, n),  # Number of nodes explored
}

# Create DataFrame with solvers as index
summary_df = pd.DataFrame(data)
