import numpy as np

def calculate(list):
  if (len(list) < 9):
    raise ValueError ("List must contain nine numbers.")

  else:
      numpyArray = np.reshape(list, (3,3))
  
      mean = [np.mean(numpyArray, axis = 0).tolist(), 
              np.mean(numpyArray, axis = 1).tolist(),
              np.mean(numpyArray).tolist()
      ]
    
      variance = [np.var(numpyArray, axis = 0).tolist(), 
              np.var(numpyArray, axis = 1).tolist(),
              np.var(numpyArray).tolist()
      ]
    
      stdDeviation = [np.std(numpyArray, axis = 0).tolist(), 
              np.std(numpyArray, axis = 1).tolist(),
              np.std(numpyArray).tolist()
      ]
    
      max = [np.max(numpyArray, axis = 0).tolist(), 
              np.max(numpyArray, axis = 1).tolist(),
              np.max(numpyArray).tolist()
      ]
      
      min = [np.min(numpyArray, axis = 0).tolist(), 
              np.min(numpyArray, axis = 1).tolist(),
              np.min(numpyArray).tolist()
      ]
    
      sum = [np.sum(numpyArray, axis = 0).tolist(), 
              np.sum(numpyArray, axis = 1).tolist(),
              np.sum(numpyArray).tolist()
      ]
      
      calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': stdDeviation,
        'max': max,
        'min': min,
        'sum': sum
      }
      return calculations