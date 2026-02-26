# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 17:01:47 2026

@author: vvall
"""

#Present Value
def present_value(cf:float, r: float, t:float) -> float:
    """
    Compute the present value of a cash flow. Let's say to keep it simple,
    that it's compounded once annually
    cf: cash flow
    r: interest rate
    t: number of periods
    >>> present_value(1000, 0.07, 5)
    712.98
    >>> present_value(1000, 0.07, 10)
    508.35
    >>> present_value(1000, 0.07, 15)
    362.45
    """
    pv = cf/(1 + r)**t
    return pv
    
    present_value(1000, 0.07, 5)
    present_value (1000, 0.07, 10)
    present_value(1000, 0.07, 15)
 
#Future Value
def future_value(pv: float, r: float, t: float) -> float:
    """
    Compute the future value of a cash flow. Again, let's say to keep it
    simple, that it's compunded once annually
    pv: present value
    r: interest rate
    t: number of periods
    >>> future_value(5000, 0.07, 5)
    7012.76
    >>> future_value(5000, 0.07, 10)
    9835.76
    >>> future_value(5000, 0.07, 15)
    13795.16
    """
    fv = pv*(1 + r)**t
    return fv

    future_value(5000, 0.07, 5)
    future_value(5000, 0.07, 10)
    future_value(5000, 0.07, 15)
    
#Total Revenue
def total_revenue(x: float, p:float) -> float:
    """
    Find the total revenue earned by a firm selling a product at a fixed price
    x: number of units sold
    p: price
    >>> total_revenue(100, 10)
    1000
    >>> total_revenue(500, 3)
    1500
    >>> total_revenue(250, 5)
    1250
    """
    tr = x*p
    return tr

    total_revenue(100,10)
    total_revenue(500, 3)
    total_revenue(250, 5)
    
#Total Cost
def total_cost(x: float, b: float, a: float) -> float:
    """
    Find the total cost incurred by a firm to produce a product
    x: number of units sold
    b: fixed cost
    a: constant
    >>> total_cost(50, 100, 5)
    12600
    >>> total_cost(100, 100, 5)
    50100
    >>> total_cost(25, 100, 5)
    3225
    """
    tc = a*x**2 + b
    return tc

    total_cost(50, 100, 5)
    total_cost(100, 100, 5)
    total_cost(25, 100, 5)

#Constant Elasticity of Substitution
def CESutility(x:float, y:float, r:float) -> float:
    """
    Calculate the value of the constant elasticity of substitution
    utility function, which measures the theoretical degree of
    satisfcation a consumer may get from two goods.
    x: good one
    y: good 2
    r: degree to which goods are complements or substitutes
    >>> CESutility(5, 5, 2)
    7.07
    >>> CESutility(10, 10, 3)
    12.6
    >>> CESutility(15, 15, 1)
    30
    """
    ces = (x**r + y**r)**(1/r)
    return ces

    CESutility(5, 5, 2)
    CESutility(10, 10, 3)
    CESutility(15, 15, 1)
    
    