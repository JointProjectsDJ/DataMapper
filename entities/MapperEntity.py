class MapperEntity:
    def __init__(self):
        self.source = None
        self.payload = None
        self.query_type = None

    @property
    def source(self):
        return self.source

    @source.setter
    def source(self,value):
        self.source = value

    @property
    def payload(self):
        return self.payload

    @payload.setter
    def payload(self,value):
        self.payload = value

    @property
    def query_type(self):
        return self.query_type

    @query_type.setter
    def query_type(self,value):
        self.query_type = value