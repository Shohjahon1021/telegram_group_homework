from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    list1 = []
    list2 = []
    list_1 = []
    messages = data["messages"]
    for i in messages:
        list1.append(i.get("actor",0))
        list1.append(i.get("from",0))
    for k in list1:
        if k != 0:
            if k not in list_1:
                list_1.append(k)

    return list_1

a = read_data("data/result.json")
find_all_users_name(a)
