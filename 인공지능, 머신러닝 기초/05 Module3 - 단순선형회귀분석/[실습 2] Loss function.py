import elice_utils
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
eu = elice_utils.EliceUtils()

def loss(x, y, beta_0, beta_1):
    N = len(x)
    ans=0
    for i in range(N):
        ans=ans+(y[i]-(beta_0*x[i]+beta_1))**2
    return ans

X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

beta_0 = 1 # ����
beta_1 = 0.5 # ����

print("Loss: %f" % loss(X, Y, beta_0, beta_1))

plt.scatter(X, Y) # (x, y) ���� �׸��ϴ�.
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r') # y = beta_0 * x + beta_1 �� �ش��ϴ� ���� �׸��ϴ�.

plt.xlim(0, 10) # �׷����� X���� �����մϴ�.
plt.ylim(0, 10) # �׷����� Y���� �����մϴ�.
plt.savefig("test.png") # ���� �� �������� �̹����� ǥ���մϴ�.
eu.send_image("test.png")