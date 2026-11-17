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
