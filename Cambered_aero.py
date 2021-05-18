import math
import matplotlib.pyplot as plt
import csv



def Cambered_aero(Chord_len, thickness, M, P):
    # Chord_len = 120
    # thickness =  30
    t = thickness / Chord_len
    Points_per_length = 0.3
    # M = 0.04 # Max camber
    # P = 0.4 # location of max camber (0 < p < 1)
    

    Suffix = 'NACA'
    xx = int(Chord_len/thickness)
    Suffix += str(round(M * 100))
    Suffix += str(round(P * 10))

    Suffix += str(xx)
    print(Suffix)

    X = [0] * int(Chord_len * Points_per_length)
    Y = [0] * int(Chord_len * Points_per_length)
    Z = [0] * int(Chord_len * Points_per_length * 2)


    for p in range(1, len(X)):
        X[p] = (p/Points_per_length) / Chord_len

    Y_C = [0] * len(Y)

    P_point = int(P * len(Y))

    #Calculate camber line
    for pp in range(1, P_point):
        X_perc = X[pp]
        Y_C[pp] = M / P ** 2 * (2 * P * X_perc - X_perc ** 2)

    for qq in range(P_point, len(Y)):
        X_perc = X[qq]
        Y_C[qq] = (M / (1 - P) ** 2) * ((1 - 2 * P) + 2 * P * X_perc - X_perc ** 2)

    # Calculate gradient at each point

    dy_dx = [0] * len(X)
    for x in range(0, P_point):
        X_perc = X[x]
        dy_dx[x] = ((2 * M) / P ** 2) * (P - X[x])

    for xx in range(P_point, len(X)):
        dy_dx[xx] = ((2 * M) / (1 - P) ** 2) * (P - X[xx]) 
    
    theta = [(math.atan(ang)) for ang in dy_dx]

    for q in range(1, len(Y)):
        X_perc = X[q] 
        Y[q] = 5 * t * (0.2969 * math.sqrt(X_perc) - (0.1260 * X_perc) - (0.3516 * X_perc ** 2) + (0.2843 * X_perc ** 3) - (0.1036 * X_perc ** 4))

    Y_T = Y
    #Calculate upper and lower values from X, Y, theta
    X_U = [0] * len(X)
    X_L = [0] * len(Y)
    for r in range(1, len(X)):
        X_U[r] = X[r] - (Y_T[r] * math.sin(theta[r]))
        X_L[r] = X[r] + (Y_T[r] * math.sin(theta[r]))

    Y_U = [0] * len(Y)
    Y_L = [0] * len(Y)
    for y in range(1, len(Y)):
        Y_U[y] = Y_C[y] + (Y_T[y] * math.cos(theta[y]))
        Y_L[y] = (Y_C[y] - (Y_T[y] * math.cos(theta[y])))



    X_true = [(x * Chord_len - Chord_len/2) for x in X] 
    
    # Y_neg = [0] * len(Y_true)
    # for t in range(len(Y_true)):
    #     Y_neg[t] = Y_true[t] * -1

    X_tot = X_U
    X_tot.extend(X_L[::-1])
    Y_tot = Y_U
    Y_tot.extend(Y_L[::-1])

    X_tot = [x * Chord_len - Chord_len/2 for x in X_tot]
    Y_tot = [y * Chord_len for y in Y_tot]


    # plt.plot(X_tot,Y_tot)
    # plt.plot(X_L, Y_L)
    # plt.show()

    
    # plt.show()
    # X_coords = X_true

    # X_coords.extend(X_true[::-1])
    # Y_coords = Y_true
    # Y_coords.extend(Y_neg[::-1])
    # Y_coords.append(0)
    # X_coords.append(0)
    # Z.append(0)

    True_coords = zip(X_tot,Y_tot,Z)
    # plt.plot(X_coords,Y_coords)
    # # ymax = plt.ylim()
    # # plt.ylim(0, 0.2)
    # plt.show()

    with open('Aero_coords.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(True_coords)

if __name__ == '__main__':
    Cambered_aero(100, 10, 0.2, 0.4)


