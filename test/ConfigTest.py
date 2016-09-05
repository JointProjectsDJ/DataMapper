from config.GetConfig import get_configs

data = {'Redis': {'port': 6379, 'user': None, 'host': 'laptop', 'pass': None},
        'Cassandra': {'port': 9042, 'user': None, 'host': 'laptop,pc', 'pass': None},
        'MongoDB': {'port': None, 'user': None, 'host': 'laptop', 'pass': None},
        'MySQL': {'port': 3306, 'user': None, 'host': 'laptop', 'pass': None}}

data_config = get_configs()

assert data == data_config
