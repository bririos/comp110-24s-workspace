__author__ = "730576067"

import matplotlib.pyplot as plt
#exercises.ex07.
from runtime_analysis_functions import evaluate_runtime

from runtime_analysis_functions import evaluate_memory_usage

START_SIZE: int = 0


END_SIZE: int = 1000


usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - bririos")
plt.show()