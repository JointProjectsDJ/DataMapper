class MapMySql:
    server = None

    def __init__(self, pool):
        global server
        server = pool.get_mysql()

    def __del__(self):
        server.close()
