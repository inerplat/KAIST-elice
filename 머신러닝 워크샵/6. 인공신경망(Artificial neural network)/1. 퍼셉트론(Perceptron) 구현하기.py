def activation(weight, x):
    p=0
    for i in range(len(weight)):
        p=p+weight[i]*x[i]
    return p
    
def output(weight, x):
    b=1+activation(weight, x)
    if b<=0 :
        return 0
    else :
        return 1

def main():
    weight = [1, 0.5, -0.7, 0.1]
    x = [0, 1, 1, 0]

    if output(weight, x) == 1:
        print("My neuron fired a signal")
    else:
        print("My neuron did not fire a signal")

if __name__ == "__main__":
    main()
