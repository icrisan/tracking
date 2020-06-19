def is_found(obj_to_find, objects_list):
    """
    Search object in list of objects
    :param obj_to_find: object to be found
    :param objects_list: list of objects
    :return:
    """
    found = False
    items = obj_to_find.__dict__.items()

    for obj in objects_list:
        if found:
            break
        for attr, value in items:
            if obj[attr] == value:
                found = True
            if obj[attr] != value and value is not None:
                found = False
                break

    return found
