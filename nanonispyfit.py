#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:57:34 2016

@author: jack
"""

import numpy as _np

from scipy import optimize as _optimize


def _plane(a0, a1, b1, x0, y0):
    return lambda x,y: a0 +a1*(x-x0) +b1*(y-y0)
    
def _planemoments(data):
    a0 = _np.abs(data).min()
    index = (data-a0).argmin()
    x, y = data.shape
    x0 = float(index / x)
    y0 = float(index % y)
    a1 = 0.0
    b1 = 0.0
    return a0, a1, b1, x0, y0
 
def _fitplane(data):
    params = _planemoments(data)
    errorfunction = lambda p: _np.ravel(_plane(*p)(*_np.indices(data.shape)) - data)
    p, success = _optimize.leastsq(errorfunction, params)
    return p
    
def _return_plane(params, data):
    _fit_data = _plane(*params)
    return _fit_data(*_np.indices(data.shape))
    
def plane_fit_2d(scan_image):
    return scan_image - _return_plane(_fitplane(scan_image),scan_image)
    
def no_filter(scan_image):
    return scan_image