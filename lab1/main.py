import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from scipy.stats import pearsonr
import warnings

warnings.filterwarnings("ignore")

data = pd.read_csv('imports-85.data', header=None)[[10, 11]].rename(columns={10: 'length', 11: 'width'})
x = data['length']
y = data['width']

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot()
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.scatter('length', 'width', data=data)
ax1.set_title('Length Vs. Width')

root.mainloop()

# Корреляция Пирсона и Статистическая гипотеза
alpha = 0.05
cor, p = pearsonr(x, y)
print(f'Корреляция Пирсона = {cor}')
if p > alpha:
    print(f'Признаки некоррелированы на уровне значимости = {alpha}, p = {p}')
else:
    print(f'Признаки коррелированы на уровне значимости = {alpha}, p = {p}')
