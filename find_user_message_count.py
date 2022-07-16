from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    list1 = []
    list2 = []
    list_1 = []
    messages = data["messages"]
    for i in messages:
        list1.append(i.get("text",0))
        list1.append(i.get("answers",0))
        list1.append(i.get("members",0))
        for k in list1:
            if k != 0:
            
                list_1.append(k)
    return list_1
a = read_data("data/result.json")
print(find_user_message_count(a))