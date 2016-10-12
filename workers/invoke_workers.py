from multiprocessing import Pool, cpu_count
from entities.MapperEntity import MapperEntity
from data_store_factory.wrapper_object_factory import WrapperFactory

class Workers:
    def __init__(self):
        self.num_workers = cpu_count()
        self.pool = Pool(processes=self.num_workers)

    def invoke(self,MapperEntity):
        with self.pool as p:
            wrapper_factory = WrapperFactory()
            p.apply(wrapper_factory.set_server_object(MapperEntity.source))
            p.apply(wrapper_factory.invoke_mapper_action(MapperEntity.payload,MapperEntity.query_type))
