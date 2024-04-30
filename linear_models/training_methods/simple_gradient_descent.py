import numpy as np


def compute_cost(x, y, theta, b):
    m = x.shape[0]
    f_x = (x * theta) + b
    square_diff = np.square(f_x - y)
    return np.sum(square_diff) / (2 * m)


def compute_gradient(x, y, theta, b):
    m = x.shape[0]
    ftheta_x = (x * theta) + b
    df_theta = np.multiply((ftheta_x - y), x)
    df_b = ftheta_x - y
    return [np.sum(df_theta) / m, np.sum(df_b) / m]


def gradient_descent(x, y, theta_ini, b_ini, iterations, learning_rate):
    b = b_ini
    theta = theta_ini

    for i in range(iterations):
        df_theta, df_b = compute_gradient(x, y, theta, b)
        theta = theta - learning_rate * df_theta
        b = b - learning_rate * df_b
    return theta, b
