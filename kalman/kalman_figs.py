import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.stats import norm
%matplotlib inline

m1 = np.linspace(50, 0, 100)
m2 = m1 + 2
m1 += np.array([(np.random.normal() - 0.5)*1 for x in m1])
m2 += np.array([(np.random.normal() - 0.5)*1 for x in m1])

df = pd.DataFrame([m1, m2]).T
df.columns = ['measurment1', 'measurment2']
plt.figure(figsize = (15, 3))

plt.subplot(1, 2, 1)
df.measurment1.plot(kind = 'line', label='measurement 1')
df.measurment2.plot(kind = 'line', label='measurement 2')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('distance (m)')
plt.title('Radar Measurements - Distance from Wall')

plt.subplot(1, 2, 2)

x = np.linspace(50, -50, 1000)
m1 = norm.pdf(x)
m2 = norm.pdf(x+2)
est = (m1*m2)
est = ((m1.sum() + m2.sum()) / 2.0) * (est.astype(float) / est.astype(float).sum())

plt.ylim(0.0,0.9)
plt.xlim(-6.0,5.0)
plt.plot(x, m1, label = 'measurement 1')
plt.plot(x, m2, label = 'measurement 2')
plt.plot(x, est, label = 'combined estimated')
plt.legend()
plt.xlabel('distance (m)')
plt.ylabel('probablity')
plt.title('Update Esimate of Two Measurments, time t=100')

plt.show()