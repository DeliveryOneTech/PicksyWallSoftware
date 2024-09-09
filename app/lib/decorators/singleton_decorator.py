def Singleton(cls):
    """
        Bu dekoratör, Singleton Design Pattern'ini uygulamak için kullanılır.
        Bu dekoratörü bir sınıfa uygulayarak, o sınıfın bir örneğinin sadece bir kez oluşturulmasını sağlayabilirsiniz.
    """
    if not isinstance(cls, type):
        raise TypeError("Singleton decorator must be applied to a class.")

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
