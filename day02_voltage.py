# 1. Create day02_voltage.py. Make a time array from 0 to 2 seconds with np.linspace(0, 2, 201).
# 2. Calculate voltage = 12 + 2 * np.sin(2 * np.pi * 2 * time). Print the first five values and the minimum, maximum and mean using NumPy.
# 3. Plot voltage against time. Label both axes, add a title and grid, and save the figure as day02_voltage.png.
# 4. In two sentences, explain what the 12 V baseline, 2 V amplitude and 2 Hz frequency mean on your plot.
import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 2, 201)
voltage = 12 + 2 * np.sin(2 * np.pi * 2 * time)
plt.plot(time, voltage, label='Voltage Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Signal with 12 V Baseline, 2 V Amplitude, and 2 Hz Frequency')
plt.grid(True)
plt.legend()
plt.ylim(0, 20)
plt.savefig('day02_voltage.png', dpi=200, bbox_inches='tight')
plt.show()
