import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import elice_utils
import numpy as np
elice = elice_utils.EliceUtils()

def circle(P):
    return np.linalg.norm(P) - 1 # 밑의 코드와 동일하게 동작합니다.
    # return np.sqrt(np.sum(P * P)) - 1
    
def diamond(P):
    return np.abs(P[0]) + np.abs(P[1]) - 1
    
def smile(P):
    def left_eye(P):
        eye_pos = P - np.array([-0.5, 0.5])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1
    
    def right_eye(P):
        eye_pos = P - np.array([0.5, 0.5])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1
    
    def mouth(P):
        if P[1] < 0:
            return np.sqrt(np.sum(P * P)) - 0.7
        else:
            return 1
    
    return circle(P) * left_eye(P) * right_eye(P) * mouth(P)

def checker(P, shape, tolerance):
    return abs(shape(P)) < tolerance

def sample(num_points, xrange, yrange, shape, tolerance):
    accepted_points = []
    rejected_points = []
    
    for i in range(num_points):
        x = np.random.random() * (xrange[1] - xrange[0]) + xrange[0]
        y = np.random.random() * (yrange[1] - yrange[0]) + yrange[0]
        P = np.array([x, y])
        
        if (checker(P, shape, tolerance)):
            accepted_points.append(P)
        else:
            rejected_points.append(P)
    
    return np.array(accepted_points), np.array(rejected_points)

xrange = [-1.5, 1.5] # X축 범위입니다.
yrange = [-1.5, 1.5] # Y축 범위입니다.
accepted_points, rejected_points = sample(
    100000, #  점의 개수를 줄이거나 늘려서 실행해 보세요. 너무 많이 늘리면 시간이 오래 걸리는 것에 주의합니다.
    xrange, 
    yrange, 
    smile, # smile을 circle 이나 diamond 로 바꿔서 실행해 보세요.
    0.005) # Threshold를 0.01이나 0.0001 같은 다른 값으로 변경해 보세요.

plt.figure(figsize=(xrange[1] - xrange[0], yrange[1] - yrange[0]), 
           dpi=150) # 그림이 제대로 로드되지 않는다면 DPI를 줄여보세요.
           
plt.scatter(rejected_points[:, 0], rejected_points[:, 1], c='lightgray', s=0.1)
plt.scatter(accepted_points[:, 0], accepted_points[:, 1], c='black', s=1)

plt.savefig("graph.png")
elice.send_image("graph.png")