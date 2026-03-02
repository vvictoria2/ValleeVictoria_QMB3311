# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:13:18 2026

@author: vvall
"""

#1. a.
def CESutility_valid(x: float, y: float, r: float) -> float:
    """
    Calculates the value of the Constant Elasticity of Subsitution
    but only if x and y are non-negative and r is strictly positive,
    and returns None otherwise.
    >>> CESutility_valid(5, 5, 2)
    7.07
    >>> CESutility_valid(-2, 6, 3)
    Error: x must be non-negative
    >>> CESutility_valid(4, 3, -1)
    Error: r must be strictly positive
    """
    if x < 0:
        print("Error: x must be non-negative")
        return None
    
    if y < 0:
        print("Error: y must be non-negative")
        return None
    
    if r < 0:
        print("Error: r must be strictly positive")
        return None
    
    ces = (x**r + y**r)**(1/r)
    return ces

    CESutility_valid(5, 5, 2)
    CESutility_valid(-2, 6, 3)
    CESutility_valid(4, 3, -1)

#1. b.
def CESutility_in_budget(x: float, y: float, r: float, p_x: float, p_y: float,
                         w: float) -> float:
    """
    Evaluate if the consumer's choice of goods x and y are in budget. That is,
    given prices p_x and p_y the consumer's choice of goods should cost no more
    than their wealth: w >= p_x*x + p_y*y. If any of the prices are negative or
    r is not positive, return None.
    >>> CESutility_in_budget(5, 5, 2, 5, 5, 30)
    Error: consumer's basket of goods should cost no more than their wealth
    >>> CESutility_in_budget(3, 3, 1, 2, 2, 30)
    6.0
    >>> CESutility_in_budget(3, 4, 1, -6, 8, 30)
    Error: price cannot be negative
    """
    if p_x < 0:
        print("Error: price cannot be negative")
        return None
    
    if p_y < 0: 
        print("Error: price cannot be negative")
        return None
    
    if r < 0:
        print("Error: r cannot be negative")
        return None
    
    if w <= p_x*x + p_y*y:
        print("Error: consumer's basket of goods should cost no more than 
              their wealth")
        return None
    
    return CESutility_valid(x, y, r)

    CESutility_in_budget(5, 5, 2, 5, 5, 30)
    CESutility_in_budget(3, 3, 1, 2, 2, 30)
    CESutility_in_budget(3, 4, 1, -6, 8, 30)
    
#1. c.
import math
def logit(x: float, beta_0: float, beta_1: float) -> float:
    """
    Calculate the logit link function
    l(x; beta_0, beta_1) = (e**(beta_0 + x*beta_1))/(1 + e**(beta_0 + x*beta_1))
    >>> logit(1, 1, 1)
    0.88
    >>> logit(2, 2, 4)
    0.999
    >>> logit(-4, 3, 2)
    0.0066
    """
    
    exponent = beta_0 + x*beta_1
    numerator = math.exp(exponent)
    denominator = 1 + numerator
    
    logit = numerator/denominator
    
    return logit

    logit(1, 1, 1)
    logit(2, 2, 4)
    logit(-4, 3, 2)
    
#1.d.
def logit_like(y_i: float, x_i: float, beta_0: float, beta_1: float) -> float:
    """
    The likelihood function of the logistic regression model is used to 
    estimate coefficients in logistic regression, which is used to model binary
    events, i.e. whether an event or not an event occurred. For each observation
    i, the observation y_i equals 1 if the event occurred and 0 if it did not.
    if y_i = 1: l(x; beta_0, beta_1)
    if y_i = 0: 1 - l(x; beta_0, beta_1)
    >>> logit_like(1, 1, 1, 1)
    -0.12
    >>> logit_like(0, 1, 1, 1)
    1.12
    >>> logit_like(2, 2, 3, 4)
    ValueError: y must be 0 or 1
    """
    z = logit(x_i, beta_0, beta_1)
    
    if y_i == 1:
        return math.log(z)
    
    elif y_i == 0:
        return 1 - math.log(z)
    
    else: 
        raise ValueError("y must be 0 or 1")
        
    return logit_like

    logit_like(1, 1, 1, 1)
    logit_like(0, 1, 1, 1)
    logit_like(2, 2, 3, 4)
    
    
    
    

    
