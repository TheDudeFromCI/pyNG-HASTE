from Algorithm import DataType, Function, Axiom
from StandardLibrary import NumberDataType, IntegerDataType
import math


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
        if inputs[0] >= 999999 or inputs[1] >= 9999:
            raise ValueTooLargeError

        return [inputs[0] ** inputs[1]]


class ExponentIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self, inputs):
        if inputs[0] >= 999999 or inputs[1] >= 9999:
            raise ValueTooLargeError

        return [inputs[0] ** inputs[1]]


class ValueTooLargeError(SystemError):
    pass
