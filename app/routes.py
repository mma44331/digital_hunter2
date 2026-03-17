from fastapi import APIRouter
import dal

route = APIRouter()

@route.get("/shifting_quality_goals")
def shifting_quality_goals():
    res = dal.get_shifting_quality_goals()
    return res

@route.get("/analysis_of_collection_sources")
def analysis_of_collection_sources():
    res = dal.get_analysis_of_collection_sources()
    return res

@route.get("/finding_new_targets")
def finding_new_targets():
    res = dal.get_finding_new_targets()
    return res

@route.get("/identifying_sleeping_cells")
def identifying_sleeping_cells():
    res = dal.get_identifying_sleeping_cells()
    return res

@route.get("/get_Visualization/{entity_id}")
def get_Visualization(entity_id:str):
    res = dal.get_visualization_track(entity_id)
    return res


