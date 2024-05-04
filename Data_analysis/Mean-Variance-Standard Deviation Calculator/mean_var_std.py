import numpy as np

def calculate(list):
    try:
        var = np.array(list).reshape(3,3)
        print(var)
        calculations={}
        calculations['mean'] = [var.mean(axis=0).tolist(),var.mean(axis=1).tolist(),var.mean()]
        calculations['variance'] = [var.var(axis=0).tolist(),var.var(axis=1).tolist(),var.var()]
        calculations['standard deviation'] = [var.std(axis=0).tolist(),var.std(axis=1).tolist(),var.std()]
        calculations['max'] = [var.max(axis=0).tolist(),var.max(axis=1).tolist(),var.max()]
        calculations['min'] = [var.min(axis=0).tolist(),var.min(axis=1).tolist(),var.min()]
        calculations['sum'] = [var.sum(axis=0).tolist(),var.sum(axis=1).tolist(),var.sum()]
        
        return calculations
    
    except  ValueError:
        raise ValueError("List must contain nine numbers.") from None