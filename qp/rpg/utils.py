
def get_score(rpg):
    result = 0
    if not rpg.is_active:
        return 0
    if rpg.caption != "": result += 1
    if rpg.description != "": result += 1
    if rpg.icon: result += 1
    if rpg.is_public: result += 1
    return result
