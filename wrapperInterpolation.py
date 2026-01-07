from statistics import LinearInterpolation, PolynomialInterpolation

class PyInterpolation:
    def __init__(self, cpp_obj):
        self._cpp = cpp_obj

    def __call__(self, x):
        return self._cpp(x)

    def __repr__(self):
        return f"{self.__class__.__name__}(C++ backend)"


class PyLinearInterpolation(PyInterpolation):
    def __init__(self, nodes: dict):
        cpp_obj = LinearInterpolation(nodes)
        super().__init__(cpp_obj)

class PyPolynomialInterpolation(PyInterpolation):
    def __init__(self, nodes: dict):
        cpp_obj = PolynomialInterpolation(nodes)
        super().__init__(cpp_obj)


