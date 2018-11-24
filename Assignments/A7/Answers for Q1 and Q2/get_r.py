# -*- coding: utf-8 -*-

import numpy as np
def get_r(K, L, alpha, Z, delta):
    '''This function generates the interest rate or vector of interest rates'''
    assert alpha>0 and alpha<1,"outside the range of capital share of income"
    assert delta>=0 and delta<1,"outside the range of depreciation rate"
    assert Z>0,"outside the range of total factor productivity"
    r=alpha*Z*((L/K)**(1-alpha))-delta
    if type(K)==float and type(L)==float:
        assert type(r)==float, "Doesn't satisfy this condition: if K and L are both scalars,this function should return a scalar interest rate"
    if not np.isscalar(K) and not np.isscalar(L) :
        assert not np.isscalar(r), "Doesn't satisfy this condition: if K and L are both vectors, this function should return a corresponding vector of interest rates"
    return r