def get_floor(**kwargs):
    floor = kwargs.get("floor")
    if floor not in [0,1,2,3]:
        return None
    match floor:
        case 0:
            return {"room_id":"00_wr_00"}
        case 1:
            return {"room_id":"01_wr_00"}
        case 2:
            return {"room_id":"02_wr_00"}
        case 3:
            return {"room_id":"03_wr_00"}
    return None

