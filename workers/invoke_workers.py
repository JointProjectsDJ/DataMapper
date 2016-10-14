from multiprocessing import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from data_store_factory.wrapper_object_factory import WrapperFactory

class Workers:
    def __init__(self):
        self.num_workers = cpu_count()
        self.pool = Pool(processes=self.num_workers)

    def invoke(self, MapperEntity):
        with self.pool as p:
            wrapper_factory = WrapperFactory()
            return p.map(wrapper_factory.process,[MapperEntity])[0]
