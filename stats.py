def counter(variable):
    list = variable.split()
    return len(list)

def ch_count(filepath):
    dict = {}
    count = 1
    with open(filepath) as f:
        file_contents = f.read()
    lower = str.lower(file_contents)
    
    for ch in lower:
        if ch not in dict:
            dict[ch] = 0
        if ch in dict:
            dict[ch] += count
    return dict
    
def sort(dict):
    new_list = []
    for i in dict:
        