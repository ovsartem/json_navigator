import json


def get_info(path):
    """
    Reads json file
    """
    with open("frienfs_list_Obama.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def dictionary(element):
    """
    Function to work with dictionary
    """
    all_elements = list(element.keys())
    print("This object is a dictionary. Here are all keys.")
    for i in range(len(all_elements)):
        print(f"{i+1}) {all_elements[i]}")
    choice = int(input("Type the humber of the key: "))
    if isinstance(element[all_elements[choice-1]], list):
        return element[all_elements[choice-1]][0]
    return element[all_elements[choice-1]]


def _list(element):
    """
    Function to work with list
    """
    print("This object is a dictionary. Here are all elements.")
    for i in range(len(element)):
        print(f"{i+1}) {element[i]}")
    choice = int(input("Type the humber of the element: "))
    return element[choice-1]


def other_elements(element):
    """
    Function to work with str,int,float
    """
    print(element)
    return 111


def main(element):
    """
    Main function to organize all types
    """
    if isinstance(element, dict):
        return dictionary(element)
    elif isinstance(element, list):
        return _list(element)
    elif isinstance(element, tuple):
        return _list(element)
    else:
        return other_elements(element)


def _work():
    """
    Cycles the main function. Here you can change the path of json file.
    """
    print("This is json file navigator. You can leave whenever you want.")
    data = get_info("frienfs_list_Obama.json")
    stop = False
    while stop != True:
        data = main(data)
        if data == 111:
            stop = True


if __name__ == '__main__':
    start = True
    while start != False:
        _work()
        move = input("Do you want to repeat? +/: ")
        if move == "-":
            start = False
