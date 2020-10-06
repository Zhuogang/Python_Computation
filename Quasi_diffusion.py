import numpy as np

def quasi_diffusion_1D(x, dx, T, name, cl = 0, graph=False)
    """Find the scalar flux with quasi-diffusion method
    Args:
        x: computational domain
        dx: spatial resolution
        T: simulation time
        name: name of the test problem
        cl: closure term
        
    Returns:
        scalar flux at T
        
    """
    if (name == "plane source"):
        







