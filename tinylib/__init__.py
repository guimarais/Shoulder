import h5py
import numpy as np

def eqildatah5py(fname):        
    hf = h5py.File(fname, 'r')
    
    shotnr = np.array(hf['shotnr'])
    R = np.array(hf['R'])
    Z = np.array(hf['Z'])
    t = np.array(hf['t'])
    pfm = np.array(hf['pfm'])
    psi0 = np.array(hf['psi0'])
    psix = np.array(hf['psix'])
    
    hf.close()
    
    class objview(object):
        def __init__(self, d):
            self.__dict__=d
        
    return objview({'shotnr':shotnr,
                    'R':R,
                    'Z':Z,
                    't':t,
                    'pfm':pfm,
                    'psi0':psi0,
                    'psix':psix})