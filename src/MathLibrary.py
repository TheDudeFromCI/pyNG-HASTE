from Algorithm import DataType, Function, Axiom


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

    def run(self):
        pass


class AddFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class MultiplyFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class DivideFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class SubtractFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class AddIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self):
        pass


class MultiplyIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self):
        pass


class DivideIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self):
        pass


class SubtractIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self):
        pass


class ExponentFunction(Function):
    def __init__(self):
        super().__init__(
            [NumberDataType(), NumberDataType()], [NumberDataType()])

    def run(self):
        pass


class ExponentIntFunction(Function):
    def __init__(self):
        super().__init__(
            [IntegerDataType(), IntegerDataType()], [IntegerDataType()])

    def run(self):
        pass


class InputNumberFunction(Function):
    def __init__(self):
        super().__init__([], [NumberDataType()])

    def run(self):
        pass


class InputIntegerFunction(Function):
    def __init__(self):
        super().__init__([], [IntegerDataType()])

    def run(self):
        pass
