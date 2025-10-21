# Exercise 3 — Quick README

A concise, practical guide for `03-Exercise.ipynb` (exercise sheet 3).

## Purpose
This notebook contains the tasks for Exercise 3: Numpy array manipulation, 2D Gaussian point-cloud plotting and rotation, data preprocessing (Titanic), and Seaborn visual analysis. It is designed to be submitted as a group exercise and defended in a short oral session.

## Key files used
- `03-Exercise.ipynb` — the exercise notebook (this file).
- `backup_data_2a.npy` and `backup_data_2b.npy` — backup data for plotting tasks (use if you can't generate samples).
- `titanic.csv` — local CSV used for preprocessing tasks (also available from Seaborn remote URL).

## Submission & defense
- Submission: see top cell in the notebook for the exact deadline and submission format (zip with group name/student number).
- Defense: register one slot in studIP; the whole group must attend. The person who registered will include group info in the submission filename.

## Grading breakdown (as given in the notebook)
- Task 1 — Arrays: 10%
- Task 2 — Plotting (Gaussian): 40%
- Task 3 — Data Preprocessing: 15%
- Task 4 — Seaborn Plotting (Titanic analysis): 35%

## Quick run / setup
1. Recommended: Python 3.8+ and a virtual environment.
2. Install common packages:

```powershell
pip install numpy pandas matplotlib seaborn jupyter
```

3. Open and run the notebook interactively:

```powershell
jupyter notebook  # then open 03-Exercise.ipynb
```

Or run the entire notebook in VS Code's Jupyter interface.

## How to approach the tasks (brief)
- Task 1 (Arrays): Use NumPy vectorized operations (no loops). Check shapes and types. Use boolean masks to select integer entries.
- Task 2 (Plotting): Set a random seed for reproducibility. Use multivariate normal to generate data, build a 2×2 rotation matrix, apply the rotation, and plot with Matplotlib (GridSpec recommended). If stuck, load `backup_data_2a.npy`.
- Task 3 (Preprocessing): Use Pandas to load `titanic.csv`, inspect columns, clean `Sex` and `Name` columns as required, and document your transformations.
- Task 4 (Seaborn): Use the original Titanic dataset (remote URL provided in the notebook) for plotting and answering the questions. Provide plots and short textual conclusions.

## Minimal code snippets
Load data (example):

```python
import numpy as np
import pandas as pd

# Load backup or generate data
data = np.load('backup_data_2a.npy')  # or generate with np.random.multivariate_normal

# Load Titanic
df = pd.read_csv('titanic.csv')
```

Rotation matrix (example):

```python
import numpy as np

def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]])
```

## Deliverables
- One zipped submission per group named with the registering member and their student number.
- Notebook with code cells executed (outputs visible), clear comments, and short answers to the questions.
- Be prepared to explain code and decisions during defense.

## Tips & troubleshooting
- Reproducibility: set `np.random.seed(101)` where required.
- If `numpy.load` or `pd.read_csv` fail, check file paths and that files are not corrupted.
- For plotting layout issues, try `plt.tight_layout()` and explicit figure sizes.

## Extensions (optional)
- Add more diagnostics for Task 2 (covariance ellipse, principal axes).
- Use `sklearn` for additional preprocessing or small models on the Titanic data.

---

If you'd like, I can also:
- Add a short starter script `exercise_3_starter.py` with the minimal code, or
- Insert a ready-to-run summary cell into `03-Exercise.ipynb`.

