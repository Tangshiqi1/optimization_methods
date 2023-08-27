import numpy as np
import random
import matplotlib.pyplot as plt

def phi(x):
    return 3.0 * x * x - 2.0 * np.tan(x)

def parabola_method(range):
    # parameter
    epsilon = 1e-4
    delta = 1e-5

    # get random inital value
    s0 = 0.0
    h = 0.0
    range_start = range[0]
    range_end = range[1]
    while True: 
        s0 = range_start + random.random() * (range_end - range_start)
        h = random.random() * (range_end - range_start)
        if (s0 + h <= range_end and s0 + 2.0 * h <= range_end \
                and phi(s0 + h) < phi(s0) and phi(s0 + h) < phi(s0 + 2.0 * h)):
            break

    print("The initial value: s0 = ", s0, "h = ", h)

    # solve
    s1 = 0.0
    s2 = 0.0
    max_num_iteration = 100
    iter = 0
    success_flag = False
    s_optimal = 0.0
    while True and iter < max_num_iteration:
        s1 = s0 + h
        s2 = s1 + h
        phi_0 = phi(s0)
        phi_1 = phi(s1)
        phi_2 = phi(s2)

        h_new = (4.0 * phi_1  - 3.0 * phi_0 - phi_2) * h / (2.0 * phi_1  - phi_0 - phi_2) / 2.0
        s_new = s0 + h_new
        if np.abs(s2 - s0) < epsilon and np.abs(phi(s_new) - phi(s1)) < delta:
            success_flag = True
            s_optimal = s_new
            break

        s0 = s_new
        h = h_new
        iter += 1

    if success_flag:
        print("Solve success, s* = ", s_optimal, ", phi(s*) = ", phi(s_optimal), \
                ", |s* - s1| = ", np.abs(s_optimal - s1), ", |phi(s*) - phi(s1)| = ", np.abs(phi(s_optimal) - phi(s1))) 
        print("num of iteration: ", iter)
    else:
        print("solve failed.")

if __name__=="__main__":
    range = [0.0, 1.0]
    parabola_method(range, phi)