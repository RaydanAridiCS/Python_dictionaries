
# 4th program
# Group dictionary by values
def group_dict(input_dict):
    grouped = {}
    for name, value in input_dict.items():
        if value not in grouped:
            grouped[value] = [name]
        else:
            grouped[value].append(name)
    return grouped

# Example usage:
input_dict = {"Amir": 10, "Bob": 20, "Ahmad": 20, "Samir": 30}

result = group_dict(input_dict)
print("Result:", result)


