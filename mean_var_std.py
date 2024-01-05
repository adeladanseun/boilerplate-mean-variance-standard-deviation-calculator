import numpy as np

def calculate(list):
    a = np.array(list)
    if len(a)!=9:
        raise ValueError("List must contain nine numbers.")
    else: 
        flatMin = a.min()
        flatMax = a.max()
        flatVar = a.var()
        flatStd = a.std()
        flatSum = a.sum()
    a=a.reshape((3,3))
    calculations = {'min':[], 'max':[], 'variance':[], 'standard deviation':[], 'sum':[]}
    for i in range(2):
        newMin=[]
        newMax=[]
        var=[]
        std=[]
        sum=[]
        for j in range(a):
            if i==1:
                row = a[j]
            else:
                row = a[: ,j]
            newMin.append(row.min())
            newMax.append(row.max())
            var.append(row.var())
            std.append(row.std())
            sum.append(row.sum())
        calculations['min'].append(newMin)
        calculations['max'].append(newMax)
        calculations['variance'].append(var)
        calculations['standard deviation'].append(std)
        calculations['sum'].append(sum)
    calculations['sum'].append(flatSum)
    calculations['standard deviation'].append(flatStd)
    calculations['variance'].append(flatVar)
    calculations['min'].append(flatMin)
    calculations['max'].append(flatMax)

    return calculations













