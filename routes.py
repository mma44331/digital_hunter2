from fastapi import APIRouter


route = APIRouter()

@route.get("/shifting_quality_goals")
def shifting_quality_goals():
    res = get_shifting_quality_goals()
    return res

@route.get("/analysis_of_collection_sources")
def analysis_of_collection_sources():
    res = get_analysis_of_collection_sources()
    return res

@route.get("/finding_new_targets")
def finding_new_targets():
    res = get_finding_new_targets()
    return res

@route.get("/identifying_sleeping_cells")
def identifying_sleeping_cells():
    res = get_identifying_sleeping_cells()
    return res

@route.get("/get_Visualization/{entity_id}")
def get_Visualization(entity_id:str):
    res = get_visualization_track(entity_id)
    return res


