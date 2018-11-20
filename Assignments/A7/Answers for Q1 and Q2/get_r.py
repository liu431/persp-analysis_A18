# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:04:52 2018

@author: LI LIU
"""

def get_r(K, L, alpha, Z, delta):
    '''This function generates the interest rate or vector of interest rates
    '''
    r=alpha*Z*((L/K)**(1-alpha))-delta
    return r