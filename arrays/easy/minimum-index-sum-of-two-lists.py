def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    list1_set = {}
    index = 0
    for word in list1:
        list1_set[word] = index
        index += 1
    min_value = 999999999
    output_word = ""
    index = 0
    for word in list2:
        if word in list1_set:
            if min_value > list1_set[word] + index:
                min_value = list1_set[word] + index
                output_word = word
        index += 1
    return [str(output_word)]


print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
               ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
