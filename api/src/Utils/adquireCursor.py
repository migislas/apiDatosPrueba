class adquireConnection():
    
    def __init__(self, object):
        self.object = object
        
    def __enter__(self):
        self.conection = self.object.getconn()
        self.cursor = self.conection.cursor()
        return self.cursor

    def __exit__(self, *exc) -> None:
        self.object.putconn(self.conection)
        
class OnlyConection():
    
    def __init__(self, object):
        self.object = object
        
    def __enter__(self):
        self.conection = self.object.getconn()
        return self.conection

    def __exit__(self, *exc) -> None:
        self.object.putconn(self.conection)