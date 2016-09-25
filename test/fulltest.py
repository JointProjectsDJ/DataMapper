# First call to startup.
# Create MapRedis, MapMySql, MapMongo and MapCassandra objects
# Create test payloads
# Pass objects created above with payloads created above to MapActions and hopefully shit works
# If it works and data is CRUDed as expected, then HURRAH!! else back to the drawing board.
from startup import Startup
from datasources import MapRedis, MapMySql, MapCassandra, MapMongo, MapActions

# First call to startup.
pool = Startup.pool

# Create MapRedis, MapMySql, MapMongo and MapCassandra objects
# mr = MapRedis.MapRedis(pool).server
# ms = MapMySql.MapMySql(pool).server
mc = MapCassandra.MapCassandra(pool).server
# mm = MapMongo.MapMongo(pool).server

# Create test payloads
# prc = {'key': 'testkey', 'value': 'test value'}
# prr = {'command': 'get', 'key': 'testkey'}
# pru = {}
# prd = {'command': 'del', 'key': 'testkey'}
# psc = {'query': 'insert into test values(45, \'test text 3\');'}
# psr = {'query': 'select * from test where test = 45;'}
# psu = {'query': 'update test set value = \'new test text\' where test = 45;'}
# psd = {'query': 'delete from test where test = 45;'}
pcc = {
    'query': 'insert into test(test, value) values(4, \'test text\');'}
pcr = {'query': 'select * from test;'}
pcu = {'query': 'update test set value = \'new test text\' where test = 4;'}
pcd = {'query': 'delete from test where test = 4;'}
# pmc = {'doc': {'test': 'test'}, 'collection': 'test'}
# pmr = {'collection': 'test', 'filter': {}}
# pmu = {'doc': {'$set': {'test': 'new test'}}, 'collection': 'test', 'filter': {}}
# pmd = {'collection': 'test', 'filter': {}}

# Pass objects created above with payloads created above to MapActions and hopefully shit works
# MapActions.create(mr, prc)
# MapActions.create(ms, psc)
MapActions.create(mc, pcc)
# MapActions.create(mm, pmc)
# print(MapActions.read(mr, prr))
# print(MapActions.read(ms, psr))
print(MapActions.read(mc, pcr))
# print(MapActions.read(mm, pmr))
# MapActions.update(mr, pru)
# MapActions.update(ms, psu)
MapActions.update(mc, pcu)
# MapActions.update(mm, pmu)
# MapActions.delete(mr, prd)
# MapActions.delete(ms, psd)
MapActions.delete(mc, pcd)
# MapActions.delete(mm, pmd)
