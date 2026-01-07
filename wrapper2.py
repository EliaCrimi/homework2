from statistics import LoadStatistics, mean, median, variance, standardDeviation

class PyStatistics:
    def __init__(self):
        self._cpp = LoadStatistics()

    def load_csv(self, file_name: str):
        self._cpp.loadCSV(file_name)

    def save_txt(self, file_name: str):
        self._cpp.printTXT(file_name)

    def get_column(self, index: int):
        return self._cpp.getColumn(index) 

    def __len__(self):
        """Number of rows"""
        return self._cpp.getRowsNumber()

    def __getitem__(self, index):
        """Allows iteration like stats[0]"""
        column = self._cpp.getColumn(index)
        return column

    def __repr__(self):
        return f"PyStatistics(rows={len(self)})"


def mean_py(v):
    return mean(v)

def median_py(v):
    return median(v)

def variance_py(v):
    return variance(v)

def stddev_py(v):
    return standardDeviation(v)



