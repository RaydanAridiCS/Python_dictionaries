# 1st program 
# Merge function for dictionaries
firstDictionary = {"a": 3, "b": 7, "c": 3, "d": 3, "e": 3}
secondDictionary = {"b": 10, "d": 4 }

def merge_dictionaries(dict1, dict2):
    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    return merged_dict

print(merge_dictionaries(firstDictionary, secondDictionary))
