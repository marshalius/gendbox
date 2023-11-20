from koru.preprocessing.normalization import MinMax as __minmax
import pandas as __dep_pd
import numpy as __dep_np

def mean(data):
    mean = sum(data) / len(data)
    return mean


def med(data):
    sorted_data = sorted(data)
    median = 0.0
    if len(sorted_data) % 2 == 0:
        median = (sorted_data[int(len(sorted_data)/2-1)] + sorted_data[int(len(sorted_data)/2)]) / 2
    else:
        median = sorted_data[int((len(sorted_data)-1)/2)]
    return median

def std(data):
    if len(data) == 1:
        return 0.0
    std = 0.0
    mean_ = mean(data)
    total = 0.0
    for value in data:
        total = total + (value-mean_)**2
    std = (total/(len(data)-1))**0.5
    return std

def cor(data):
    _data = None
    if isinstance(data, __dep_pd.DataFrame):
        _data = data.copy()
        data_type = 'pandas_dataframe'
        data = data.values.tolist()
    if isinstance(data, __dep_pd.Series):
        _data = data.copy()
        data_type = 'pandas_series'
        data = data.tolist()
    if isinstance(data, __dep_np.Matrix):
        _data = data.copy()
        data_type = 'numpy_matrix'
        data = data.tolist()
    if isinstance(data, __dep_np.ndarray()):
        _data = data.copy()
        data_type = 'numpy_ndarray'
        data = data.tolist()
    if is_matrix(data):
        cor_data = []
        for i in range(0, len(data[0])):
            cor_row = []
            for j in range(0, len(data[0])):
                corr = __cor([row[i] for row in data], [row[j] for row in data])
                cor_row.append(corr)
            cor_data.append(cor_row)
        if data_type == 'pandas_df':
            cor_data = __dep_np.DataFrame(data=cor_data, columns=_data.columns, index=_data.columns)
        return cor_data
    else:
        raise TypeError('The type data is not compatible.')
        return None

def __cor(x, y):
    if is_matrix(x) and is_matrix(y):
        if len(x) == len(y):
            if not all(len(row) == 1 for row in x):
                raise ValueError('The x and y matrix should be in the shape (n, 1), but the shape of x is ​​not compatible.')
                return None
            if not all(len(row) == 1 for row in y):
                raise ValueError('The x and y matrix should be in the shape (n, 1), but the shape of y is ​​not compatible.')
                return None
            length = len(x)
            if length > 0:
                r = 0.0
                sumx = 0.0
                sumy = 0.0
                sumxy = 0.0
                sumx2 = 0.0
                sumy2 = 0.0
                
                normalizer = __minmax()
                x = normalizer.fit_transform(x)
                y = normalizer.transform(y)
                for i in range(0,len(x)):
                    sumx += x[i][0]
                    sumy += y[i][0]
                    sumxy += x[i][0] * y[i][0]
                    sumx2 += x[i][0] ** 2
                    sumy2 += y[i][0] ** 2
                try:
                    r = (length*sumxy-sumx*sumy)/((length*sumx2-sumx**2)*(length*sumy2-sumy**2))**0.5
                except ZeroDivisionError:
                    r = 0
                    pass
                return r
            else:
                raise ValueError('x and y are empty.')
        else:
            raise ValueError('x and y are not equal in length.')
    elif not is_matrix(x) and not is_matrix(y):
        if isinstance(x, list) and isinstance(y, list):
            if len(x) == len(y):
                length = len(x)
                if length > 0:
                    r = 0.0
                    sumx = 0.0
                    sumy = 0.0
                    sumxy = 0.0
                    sumx2 = 0.0
                    sumy2 = 0.0
                    for i in range(0,len(x)):
                        sumx += x[i]
                        sumy += y[i]
                        sumxy += x[i] * y[i]
                        sumx2 += x[i] ** 2
                        sumy2 += y[i] ** 2
                    try:
                        r = (length*sumxy-sumx*sumy)/((length*sumx2-sumx**2)*(length*sumy2-sumy**2))**0.5
                    except ZeroDivisionError:
                        r = 0
                        pass
                    return r
                else:
                    raise ValueError('x and y are empty.')
            else:
                raise ValueError('x and y are not equal in length.')
        else:
            raise ValueError('The format of x and y is not compatible.')
    else:
        raise ValueError('x and y have different shapes.')
    
    
def is_matrix(data):
    if not isinstance(data, list):
        return False
    elif not data:
        return False
    elif not all(isinstance(row, list) and len(row) == len(data[0]) for row in data):
        return False
    else:
        return True
