from housepy import util, log, config, strings
from ingest import ingest_json_file, ingest_data

def parse(request):
    log.info("databoat.parse")
    data = ingest_json_file(request)
    try:
        t_local = strings.as_numeric(data['t_local'])
        data = data['data']        
        data['FeatureType'] = "sensor"
        data['FeatureSubType'] = "hybrid"
        data['SensorName'] = "DataBoat"
        data['LocationUpdate'] = False
        data['t_utc'] = util.delocalize_timestamp(t_local, tz=config['local_tz'])
    except Exception as e:
        log.error("--> failed: %s" % log.exc(e))
        return None        
    return data



"""
{ t_local: '1429805254',
 data: 
  { dissolved_oxygen: '9.79',
    orp: '202.2',
    salinity: '0.00',
    ph: '3.747',
    conductivity: '0',
    'water temp': '0' },
 t_utc: 1429805257 }

"""