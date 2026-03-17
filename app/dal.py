from mongo_db import get_data

def get_shifting_quality_goals():
    query = {
         'priority_level': { '$in': [1, 2] },
          'distance': { '$gt': 5 }
            },{'_id': 0, 'entity_id': 1, 'target_name': 1, 'priority_level': 1, 'distance': 1}
    return get_data(query)

def get_analysis_of_collection_sources():
    pass

def get_finding_new_targets():
    pass


def get_identifying_sleeping_cells():
    pass

def get_visualization_track(entity_id):
    pass


