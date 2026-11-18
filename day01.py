# 1. Create a virtual environment and install numpy and matplotlib.
# 2. Write day01.py that creates time values from 0 to 5 seconds, models a simple voltage step (0 V before 1 s, 12 V afterward), and plots voltage versus time with labelled axes and a title.
# 3. Save the graph as day01_voltage.png.
import numpy as np
import matplotlib.pyplot as plt

time=np.linspace(0,5,501)
voltage=np.where(time < 1, 0, 12)

plt.plot(time, voltage, label='Input Voltage')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('12 V step input ar 1 second')
plt.grid(True)
plt.legend()
plt.ylim(-1, 13)
plt.savefig('day01_voltage.png', dpi=200, bbox_inches='tight')
plt.show()
