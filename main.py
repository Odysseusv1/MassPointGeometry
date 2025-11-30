import matplotlib.pyplot as plt

mA = float(input("Mass at A: "))
mB = float(input("Mass at B: "))
mC = float(input("Mass at C: "))

# place triangle ABC at nice coords
# A = (0, 0)
# B = (1, 0)
# C = (0, 1)

A = (0, 0)
B = (1, 0)
C = (0, 1)

# D on BC such that BD : DC = mC  mB
# E on CA such that CE : EA = mA : mC
# F on AB such that AF : FB = mB : mA

def divide(P, Q, ratioPQ):
    # Divide segment PQ in ratio P->X : X->Q = ratioPQ (P-weight : Q-weight)
    (x1, y1), (x2, y2) = P, Q
    r1, r2 = ratioPQ
    x = (r2*x1 + r1*x2) / (r1 + r2)
    y = (r2*y1 + r1*y2) / (r1 + r2)
    return (x, y)

# Compute points D, E, F
D = divide(B, C, (mC, mB))
E = divide(C, A, (mA, mC))
F = divide(A, B, (mB, mA))

# Compute concurrency point G (weighted centroid)
Gx = (mA*A[0] + mB*B[0] + mC*C[0]) / (mA + mB + mC)
Gy = (mA*A[1] + mB*B[1] + mC*C[1]) / (mA + mB + mC)
G = (Gx, Gy)

plt.figure(figsize=(6,6))

# triangle
plt.plot([A[0], B[0], C[0], A[0]],
         [A[1], B[1], C[1], A[1]], 'k-')

# cevian segments
plt.plot([A[0], D[0]], [A[1], D[1]], 'r--')
plt.plot([B[0], E[0]], [B[1], E[1]], 'g--')
plt.plot([C[0], F[0]], [C[1], F[1]], 'b--')


for name, P in zip(["A","B","C","D","E","F","G"],
                   [A,B,C,D,E,F,G]):
    plt.scatter(P[0], P[1], s=60)
    plt.text(P[0]+0.02, P[1]+0.02, name)

plt.title("Mass Point Geometry Triangle")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()

print("\n--- Computed Points ---")
print("A =", A)
print("B =", B)
print("C =", C)
print("D on BC =", D)
print("E on CA =", E)
print("F on AB =", F)
print("Concurrency point G =", G)
