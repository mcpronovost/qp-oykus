
def get_score(project):
    result = 0
    if not project.is_active:
        return 0
    if project.caption != "": result += 1
    if project.description != "": result += 1
    if project.icon: result += 1
    if project.is_public: result += 1
    return result
