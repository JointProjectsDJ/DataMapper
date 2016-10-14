class MapperEntity:

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value

    @property
    def query_type(self):
        return self.__query_type

    @query_type.setter
    def query_type(self, value):
        self.__query_type = value
