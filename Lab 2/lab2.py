##############################
# APS106 Winter 2021 - Lab 2 #
# Student Name: Chiung-Ting (Bella) Huang
# PRA Section: PRA0104
##############################

###########################################
# PART 1 - Cartesian to Polar Coordinates #
###########################################
import math

def magnitude(x,y):
    """
    (float,float) -> float
    
    Function calculate the magnitude of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the magnitude of the vector as a float.
    
    >>> magnitude(10.0,25.5)
    27.390691849604675
    
    >>> magnitude(0,0)
    0.0
    
    >>> magnitude(10.2,63.2)
    64.01781002189938
    
    >>> magnitude(-11.3, -3.9)
    11.954078801814886
    
    """
    
    magnitude = math.sqrt(x**2 + y**2)          # body
    return magnitude                            # return statement


def phase(x,y):
    """
    (float,float) -> float
    
    Function calculates the phase angle of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the phase angle in radians as a float.   
    
    >>> phase(10.0,25.5)
    1.197069506829343
    
    >>> phase(0,0)
    0.0
    
    >>> phase(10.2,63.2)
    1.4107837110492034
    
    >>> phase(-11.3, -3.9)
    -2.8092604835720754
    
    """
    
    phase = math.atan2(y,x)                     # body
    return phase                                # return statement


#########################################
# PART 2 - Particle Height Calculation  #
#########################################

def particle_height(q,E,m,t,L):
    """
    (float,float,float,float,float) -> float
    
    Function calculates the vertical height of a charged particle
    within a electrostatic precipitator.
    Input parameters:
        q - charge of the particle in nanocoulombs
        E - electric field strength in kilonewtons/coulomb
        m - mass of particle in nanograms
        t - time since the particle entered the precipitator in microseconds
        L - the distance between the parallel plate electrodes in centimetres
        
    Returns the height of the particle in centimetres
    
    >>> particle_height(0,150,9.2,3.6,5.0)
    2.5
    
    >>> particle_height(2.3,150,9.2,26.8,5.0)
    1.1532999999999998
    
    >>> particle_height(-2.3,160,9.2,36.8,5.0)
    5.0
    
    """
    
    particle_height = -(1/20000)*(q * E/m)*(t ** 2) + (L/2)  # body
    return float(max(min(particle_height, 5), 0))            # return statement

if __name__ == '__main__':
    import doctest
    doctest.testmod()