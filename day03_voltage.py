# 1. In the Python environment you set up on Day 1, create day03_current.py. Import numpy and matplotlib.pyplot. If either is missing, run python -m pip install numpy matplotlib.
# 2. Set voltage V = 12 volts and resistance R = 6 ohms. Create a NumPy time array from 0 to 2 seconds using np.linspace(0, 2, 201).
# 3. Calculate steady current I_final = V / R. Then model a gradual rise with I = I_final * (1 - np.exp(-t / 0.4)). Plot I against t, label both axes with units, add a title, and save the figure as day03_current.png.
# 4. Print the first and last current values. In a short comment or README, explain what V / R means and why the plotted current starts near zero and approaches 2 A.

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 2, 201)
voltage = 12
resistance = 6
I_final = voltage / resistance
I = I_final * (1 - np.exp(-time / 0.4))
plt.plot(time, I, label='Current vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Current (A)')
plt.title('Current Rise Over Time')
plt.grid(True)
plt.legend()
plt.savefig('day03_current.png', dpi=200, bbox_inches='tight')
plt.show()
