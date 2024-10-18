class BooleanExtension:
    @staticmethod
    def to_boolean(value):
        return value in ['true', 'True', '1', 1, True]

    @staticmethod
    def to_integer(value: bool):
        return 1 if BooleanExtension.to_boolean(value) else 0
