import numpy as np
import math
def w_a_dbm(p_w):
    return 10*math.log10(p_w)
def dbm_a_w(p_dbm):
    return 10*math.log10(p_dbm)
