def train_test(data, test_size:float, random_state:int)->tuple:
    if test_size > 0.0 and test_size < 1.0:
        raise ValueError('test_size must be between 0.-1.')
    import random
    random.seed(random_state)
    from gendbox.utils import _DataConverter, _is_matrix
    dc = _DataConverter(data)
    data_ = dc._convert_to_list()
    train_data = []
    test_data = []
    test_length = int(len(data_) * test_size)
    counter = 0
    if _is_matrix(data_):
        while len(data_) > 0:
            index = random.randint(0, len(data_))
            if counter < test_length:
                test_data.append(data_[index])
                counter = counter + 1
            else:
                train_data.append(data_[index])
            del data_[index]