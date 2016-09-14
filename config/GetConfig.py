import yaml


# Will have to be run on deployment automatically

def get_configs():
    with open('../resources/config.yaml', 'rb') as f:
        data = yaml.load(f)
        return data


if __name__ == '__main__':
    print(get_configs())
