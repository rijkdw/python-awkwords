def list_to_count_map(the_list) -> dict:
    return_dict = {}
    for item in the_list:
        if item not in return_dict.keys():
            return_dict[item] = 0
        return_dict[item] += 1
    return return_dict
