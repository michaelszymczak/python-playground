from matplotlib import animation, pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys


def update(frame_number, rolls, faces, frequencies):
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1


rolls = 10_000
frequencies = {score: 0 for score in range(6)}
update(0, rolls, 0, frequencies)
scores_x = [k for k in frequencies.keys()]
frequencies_y = [v for v in frequencies.values()]

sns.set_style('whitegrid')
axes = sns.barplot(x=scores_x, y=frequencies_y, palette='bright')
axes.set_title(f'Rolled {rolls:,} times')
axes.set(xlabel='score', ylabel='frequency')
axes.set_ylim(top=max(frequencies_y) * 1.20)
for bar, frequency in zip(axes.patches, frequencies_y):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    axes.text(text_x, text_y, f'{frequency / rolls:.4}', fontsize=11, ha='center', va='bottom')
