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
    list_2 = []
    messages = data["messages"]
    for i in messages:
        list1.append(i.get("actor",0))
    for k in list1:
        if k != 0:
            if k not in list_1:
                
                list_1.append(k)

    for j in messages:
        list2.append(j.get("from",0))
    for s in list2:
        if s != 0:
            if s not in list_1:
                list_1.append(s)

    return list_1

a = read_data("data/result.json")
print(find_all_users_name(a))
