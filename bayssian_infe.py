# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

thetas = np.linspace(0,1,1001)
#print(thetas)

likelihood = lambda r : thetas if r else (1-thetas)

#print(likelihood(0))
def posterior(r, prior):
	lp = likelihood(r) * prior
	return lp/lp.sum()

p = np.array([1/ len(thetas) for _ in thetas])
#print(p)

p = posterior(1,p)
#print(p)

plt.plot(thetas, p)
plt.xlabel(r'$\theta$')
plt.ylabel('r$p(\ theta)$')
plt.show()

clicks = 2
noclicks = 38

p = np.array([1/len(thetas) for theta in thetas])
for _ in range(clicks):
	p = posterior(1,p)
for _ in range(noclicks):
	p = posterior(0,p)
plt.plot(thetas, p)
plt.xlabel('r$\ theta$')
plt.ylabel('$p(\ theta)')
plt.show()


