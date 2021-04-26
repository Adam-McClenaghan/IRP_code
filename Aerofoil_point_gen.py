import math
import matplotlib.pyplot as plt
import csv

def Aero_create(Chord_len, thickness):
    # Chord_len = 120
    # thickness =  30
    t = thickness / Chord_len
    Points_per_length = 0.5


    Suffix = 'NACA00'
    xx = int(Chord_len/thickness)
    if xx < 10:
        Suffix += '0'

    Suffix += str(xx)
    print(Suffix)

    X = [0] * int(Chord_len * Points_per_length)
    Y = [0] * int(Chord_len * Points_per_length)
    Z = [0] * int(Chord_len * Points_per_length * 2)


    for p in range(1, len(X)):
        X[p] = (p/Points_per_length) / Chord_len


    for q in range(1, len(Y)):
        X_perc = X[q] 
        Y[q] = 5 * t * (0.2969 * math.sqrt(X_perc) - (0.1260 * X_perc) - (0.3516 * X_perc ** 2) + (0.2843 * X_perc ** 3) - (0.1036 * X_perc ** 4))

    X_true = [(x * Chord_len - Chord_len/2) for x in X] 
    Y_true = [x * Chord_len for x in Y]
    Y_neg = [0] * len(Y_true)
    for t in range(len(Y_true)):
        Y_neg[t] = Y_true[t] * -1



    X_coords = X_true

    X_coords.extend(X_true[::-1])
    Y_coords = Y_true
    Y_coords.extend(Y_neg[::-1])
    # Y_coords.append(0)
    # X_coords.append(0)
    # Z.append(0)

    True_coords = zip(X_coords,Y_coords,Z)
    # plt.plot(X_coords,Y_coords)
    # # ymax = plt.ylim()
    # # plt.ylim(0, 0.2)
    # plt.show()

    with open('Aero_coords.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(True_coords)
# with open('Aero_coords.csv', 'wb'), delimiter=",", newline="" as f:
    # write = csv.writer(f)
# write.writerows(True_coords)
    # write.writerow(X_true)
    # write.writerow(Y_true)

if __name__ == '__main__':
    Aero_create(100, 10)