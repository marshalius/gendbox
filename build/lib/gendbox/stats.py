def mean(data:list):
    try:
        mean = sum(data) / len(data)
        return mean
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f'An unexcepted error has occured: {e}')

def med(data:list):
    try:
        sorted_data = sorted(data)
        median = 0.0
        if len(sorted_data) % 2 == 0:
            median = (sorted_data[int(len(sorted_data)/2-1)] + sorted_data[int(len(sorted_data)/2)]) / 2
        else:
            median = sorted_data[int((len(sorted_data)-1)/2)]
        return median
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f'An unexpected error has occured: {e}')

def lowerq(data:list):
    if len(data) < 4:
        raise ValueError('The length of the list must be at least 4 to lower quartile calculation.')
        return None
    try:
        sorted_data = sorted(data)
        lowerset = None
        if len(data) % 2 == 0:
            lowerset = sorted_data[:len(data)/2]
        else:
            lowerset = sorted_data[:len(data)//2]
        q1 = None
        if len(lowerset) % 2 == 0:
            q1 = mean(lowerset[len(lowerset)/2-1, len(lowerset)/2])
        else:
            q1 = lowerset[len(lowerset)//2]
        return q1
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f'An unexpected error has occured: {e}')

def upperq(data:list):
    if len(data) < 4:
        raise ValueError('The length of the list must be at least 4 to upper quartile calculation.')
        return None
    try:
        sorted_data = sorted(data)
        upperset = None
        if len(data) % 2 == 0:
            upperset = sorted_data[len(data)/2:]
        else:
            upperset = sorted_data[len(data)//2+1:]
        q3 = None
        if len(upperset) % 2 == 0:
            q3 = mean(upperset[len(upperset)/2-1, len(upperset)/2])
        else:
            q3 = upperset[len(upperset)//2]
        return q3
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f'An unexpected error has occured: {e}')
            
def iqr(data:list):
    if len(data) < 4:
        raise ValueError('The length of the list must be at least 4 to Interquartile Range calculation.')
        return None
    try:
        q1 = lowerq(data)
        q3 = upperq(data)
        return q3 - q1
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f'An unexpected error has occured: {e}')

def std(data:list, sample:bool=True):
    try:
        std = 0.0
        mean_ = mean(data)
        total = 0.0
        for value in data:
            total = total + (value-mean_)**2
        if sample == True:
            if len(data) == 1:
                return 0.0
            std = (total/(len(data)-1))**0.5
        else:
            if len(data) == 0:
                raise ValueError('The list cannot be empty.')
                return None
            std = (total/len(data))**0.5
        return std
    except ValueError:
        print("A list consisting of only numbers must be entered as a parameter.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

def cor(data):
    try:
        _data = data.copy()
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data = data.values.tolist()
        if(str(type(data)) == "<class 'pandas.core.series.Series'>" or 
           str(type(data)) == "<class 'numpy.matrix'>" or 
           str(type(data)) == "<class 'numpy.ndarray'>"):
            data = data.tolist()
        if __is_matrix(data):
            cor_data = []
            for i in range(0, len(data[0])):
                cor_row = []
                for j in range(0, len(data[0])):
                    corr = __cor([row[i] for row in data], [row[j] for row in data])
                    cor_row.append(corr)
                cor_data.append(cor_row)
            if str(type(_data)) == "<class 'pandas.core.frame.DataFrame'>":
                import pandas as __dep_pd
                cor_data = __dep_pd.DataFrame(data=cor_data, columns=_data.columns, index=_data.columns)
            if str(type(_data)) == "<class 'pandas.core.series.Series'>":
                import pandas as __dep_pd
                cor_data = __dep_pd.Series(cor_data)
            if str(type(_data)) == "<class 'numpy.matrix'>":
                import numpy as __dep_np
                cor_data = __dep_np.matrix(cor_data)
            if str(type(_data)) == "<class 'numpy.ndarray'>":
                import numpy as __dep_np
                cor_data = __dep_np.array(cor_data)
            return cor_data
        else:
            raise TypeError('A matrix must be entered as a parameter.')
    except TypeError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

def __cor(x, y):
    try:
        if __is_matrix(x) and __is_matrix(y):
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
                    from gendbox.preprocessing.normalization import MinMax as __minmax
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
        elif not __is_matrix(x) and not __is_matrix(y):
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
                    raise TypeError('x and y are not equal in length.')
            else:
                raise TypeError('The format of x and y is not compatible.')
        else:
            raise TypeError('x and y have different shapes.')
    except ValueError or TypeError as e:
        print(e)
    except Exception as e:
        print(f'An unexcepted error has occured: {e}')
    
    
def __is_matrix(obj):
    try:
        if not isinstance(obj, list):
            return False
        elif not obj:
            return False
        elif not all(isinstance(row, list) and len(row) == len(obj[0]) for row in obj):
            return False
        else:
            return True
    except Exception as e:
        print(f'An unexcepted error has occured: {e}')
