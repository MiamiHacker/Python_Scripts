'''
coding example of a perceptron by MiamiHacker

x0 * w0 = 0.2 * 0.6 = 0.12
x1 * w1 = 0.4 * 0.3 = 0.12
x2 * w2 = 0.3 * 0.5 = 0.15
x3 * w3 = 0.5 * 0.2 = 0.10

total                 0.49

treshold = 0.5 

return will be 0 

https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590#
'''

x_input = [0.2, 0.4, 0.3, 0.5]
w_weights = [0.6, 0.3, 0.5, 0.2]
treshold = 0.5

def step(weighted_sum):
    if weighted_sum > treshold:
        return 1
    else:
        return 0

def perceptron():
    weighted_sum = 0
    for x,w in zip(x_input, w_weights):
        weighted_sum += x*w
        print(weighted_sum)
    return step(weighted_sum)

output = perceptron()
print(f"output: {output}")


