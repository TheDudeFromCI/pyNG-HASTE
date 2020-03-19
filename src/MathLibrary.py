from Algorithm import DataType, Function, Axiom
import math


class NumberDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, NumberDataType)


class IntegerDataType(DataType):
    def connectsTo(self, dataType):
        return isinstance(dataType, NumberDataType) \
            or isinstance(dataType, IntegerDataType)


class OutputNumberFunction(Function):
    def __init__(self):
        super().__init__([NumberDataType()], [])

    def run(self, inputs):
        pass


class OutputIntegerFunction(Function):
    def __init__(self):
        super().__init__([IntegerDataType()], [])

    def run(self, inputs):
        pass


class AddFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self, inputs):
        return [inputs[0] + inputs[1]]


class MultiplyFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self, inputs):
        return [inputs[0] * inputs[1]]


class DivideFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self, inputs):
        return [inputs[0] / inputs[1]]


class SubtractFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self, inputs):
        return [inputs[0] - inputs[1]]


class AddIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        return [inputs[0] + inputs[1]]


class MultiplyIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        return [inputs[0] * inputs[1]]


class DivideIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        return [math.floor(inputs[0] / inputs[1])]


class SubtractIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        return [inputs[0] - inputs[1]]


class ExponentFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self, inputs):
        return [inputs[0] ** inputs[1]]


class ExponentIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        return [inputs[0] ** inputs[1]]


class InputNumberFunction(Function):
    def __init__(self):
        super().__init__([], [NumberDataType()])

    def run(self, inputs):
        pass


class InputIntegerFunction(Function):
    def __init__(self):
        super().__init__([], [IntegerDataType()])

    def run(self, inputs):
        pass
