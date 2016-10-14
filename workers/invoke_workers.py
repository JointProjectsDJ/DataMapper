from multiprocessing import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from data_store_factory.wrapper_object_factory import WrapperFactory

class Workers:
    def __init__(self):
        self.num_workers = cpu_count()
        self.pool = Pool(nodes=self.num_workers)

    def invoke(self, MapperEntity):
        wrapper_factory = WrapperFactory()
        return self.pool.map(wrapper_factory.process,[MapperEntity])[0]
