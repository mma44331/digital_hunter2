from mongo_db import get_data_find, get_data_aggr
from maps_data.DigitalHunter_map import plot_map_with_geometry
def get_shifting_quality_goals():
    query = ({
         'priority_level': { '$in': [1, 2] },
          'distance': { '$gt': 5 }
            },{'_id': 0, 'entity_id': 1, 'target_name': 1, 'priority_level': 1, 'distance': 1})
    return get_data_find(query)

def get_analysis_of_collection_sources():
    query = [{"$group": {"_id": "signal_type", "count": {"$sum": 1}}},
             {'$project': {'_id': 0, 'signal_type': '$_id', 'count': 1}},
             {"$sort": {"count": -1}}]
    return get_data_aggr(query)


def get_finding_new_targets():
    query =[{"$match": {'priority_level': 99}},{"$group": {"_id": "$entity_id","count":{"$sum":1}}},{"$sort":{"count": -1}},{"$limit": 3}]
    return get_data_aggr(query)


def get_identifying_sleeping_cells():
    pass


def get_visualization_track(entity_id):
    query = [{"$match": {'entity_id': entity_id}},{"$sort": {'timestamp': -1}}]
    res = get_data_aggr(query)
    cords = []
    for item in res:
        cord = (item['reported_lat'],item['reported_lon'])
        cords.append(cord)
    plot_map_with_geometry(cords)


