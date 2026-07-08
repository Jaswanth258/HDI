import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import pickle
import os
import warnings
warnings.filterwarnings("ignore")

print("All libraries imported successfully")
print(f"NumPy:     {np.__version__}")
print(f"Pandas:    {pd.__version__}")
print(f"Matplotlib: {plt.matplotlib.__version__}")
print(f"Seaborn:   {sns.__version__}")
print(f"Scikit-learn: installed")
