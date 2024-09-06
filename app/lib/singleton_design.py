class SingletonDesign(type):
    def __init__(cls, name, bases, attrs):
        super(SingletonDesign, cls).__init__(name, bases, attrs)
        cls._instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonDesign, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
