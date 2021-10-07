# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

thetas = np.linspace(0,1,1001)
#print(thetas)

likelihood = lambda a, N : thetas ** a * (1-thetas)**(N -a)

#print(likelihood(0))
def posterior(a, N, prior):
	lp = likelihood(a,N) * prior
	return lp/lp.sum()


prior = 1/len(thetas)
plt.subplot(2,1,1)
plt.plot(thetas, posterior(2,40,prior), label = 'alice -a')
plt.plot(thetas, posterior(4,50,prior), label = 'alice -b')
plt.xlabel('thetas')
plt.ylabel('probability')
plt.xlim(0,0.2)
plt.legend()
plt.subplot(2,1,2)
plt.plot(thetas, posterior(64,1280,prior), label = 'bob -a')
plt.plot(thetas, posterior(128,1600,prior), label = 'bob -b')
plt.xlabel('thetas')
plt.ylabel('probability')
plt.xlim(0,0.2)
plt.legend()
plt.tight_layout()
plt.show()

