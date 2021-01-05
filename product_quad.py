import numpy as np
import math

def prod_quad(N):
    """Compute ordinates and weights for product quadrature
    Inputs:
        N:               Order of Legendre or Chebyshev quad
    Outputs:
        w:               weights
        eta,xi,mu:       direction cosines (x,y,z)
    """
    assert (N % 2 == 0)
    #get legendre quad
    MUL, WL = np.polynomial.legendre.leggauss(N)
    #get chebyshev y's
    Y, WC = np.polynomial.chebyshev.chebgauss(N)

    #get all pairs
    place = 0
    eta = np.zeros(N*N*2)
    xi = np.zeros(N*N*2)
    mu = np.zeros(N*N*2)
    w = np.zeros(N*N*2)
        
    for i in range(N):
        for j in range(N):
            mul = MUL[i]
            y = Y[j]
            mu[place] = mul
            mu[place+1] = mul
            gamma = np.arccos(y)
            gamma2 = -gamma
            sinTheta = np.sqrt(1-mul*mul)
            eta[place] =   sinTheta*np.cos(gamma)
            eta[place+1] = sinTheta*np.cos(gamma2)
            xi[place] =   sinTheta*np.sin(gamma)
            xi[place+1] = sinTheta*np.sin(gamma2)
            w[place] = WL[i]*WC[j]
            w[place+1] = WL[i]*WC[j]
            place += 2

    # print(mu)
    # print(eta)
    # print(xi)
    # print(w)

    return w[mu>0]/np.sum(w[mu>0]), eta[mu>0],xi[mu>0]
print(prod_quad(4))
w, eta, xi = prod_quad(4)
print(np.sum(w))