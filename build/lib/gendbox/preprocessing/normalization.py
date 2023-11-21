class MinMax:
    def __init__(self):
        self.min_value = None
        self.max_value = None
    
    def fit(self, data):
        try:
            self.min_value = min(data)
            self.max_value = max(data)
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def transform(self, data):
        try:
            new_list = []
            for value in data:
                normalized_value = (value - self.min_value) / (self.max_value - self.min_value)
                new_list.append(normalized_value)
            return new_list
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

class ZScore:
    def __init__(self):
        self.mean = None
        self.std = None
    
    def fit(self, data):
        try:
            import gendbox.stats as __sts
            self.mean = __sts.mean(data)
            self.std = __sts.std(data)
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def transform(self, data):
        try:
            new_list = []
            for value in data:
                normalized_value = (value - self.mean) / self.std
                new_list.append(normalized_value)
            return new_list
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

class Robust:
    def __init__(self):
        self.median = None
        self.iqr = None
    
    def fit(self, data):
        try:
            import gendbox.stats as __sts
            self.median = __sts.median(data)
            self.iqr = __sts.iqr(data)
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def transform(self, data):
        try:
            new_list = []
            for value in data:
                normalized_value = (value - self.median) / self.iqr
                new_list.append(normalized_value)
            return new_list
        except Exception as e:
            print(f'An unexcepted error has occured: {e}')
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)