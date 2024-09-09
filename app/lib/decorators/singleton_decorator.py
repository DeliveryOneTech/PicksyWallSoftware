def Singleton(cls):
    """
        Bu dekoratör, Singleton Design Pattern'ini uygulamak için kullanılır.
        Bu dekoratörü bir sınıfa uygulayarak, o sınıfın bir örneğinin sadece bir kez oluşturulmasını sağlayabilirsiniz.
    """
    if not isinstance(cls, type):
        raise TypeError("Singleton decorator must be applied to a class.")

    instances = {}  # Bu sözlük, her sınıf için bir örneğin saklanmasını sağlar.

    # get_instance fonksiyonu, sınıfın bir örneğini oluştururken, o sınıfın daha önce oluşturulup oluşturulmadığını kontrol eder.
    def get_instance(*args, **kwargs):
        # Eğer sınıfın örneği daha önce oluşturulmamışsa, yeni bir örnek oluşturur.
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        # Eğer sınıfın örneği daha önce oluşturulmuşsa, o örneği döndürür.
        return instances[cls]

    return get_instance
