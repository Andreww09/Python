
# ex1
def intersection(a, b):
    return {el for el in a if el in b}


def union(a, b):
    c = set()
    for el in a:
        c.add(el)
    for el in b:
        c.add(el)
    return c


def difference(a, b):
    return {el for el in a if (el in b) == False}

def all_operations(a,b):
    return [union(a,b),intersection(a,b),difference(a,b),difference(b,a)]

# a={1,3,5,8,9}
# b={2,4,6,8,9}
# print(union(a,b))
# print(intersection(a,b))
# print(difference(a,b))
# print(difference(b,a))

# print(all_operations(a,b))


# ex2
def count_letters(str):
    dict = {}
    for c in str:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict


# print(count_letters("Ana has apples"))

# ex3
def compare(dict1, dict2):
    if len(dict1) != len(dict2): # comparam lungimea
        return False
    for (k, v) in dict1.items():
        if k in dict2:  # daca o cheie se afla in ambele dictionare
            # print(v, dict2[k])
            if type(v) != type(dict2[k]):  # comparam tipul valorii cheilor din cele 2 dictionare
                return False
            elif isinstance(v, dict):   # daca valorile sunt de tip dictionar, comparam recursiv
                if compare(v, dict2[k]) == False:
                    return False
            elif v != dict2[k]: # altfel comparam valoarea celor doua chei
                return False
        else:   # daca o cheie nu se afla in celalalt dictionar
            return False
    return True


a = {
    'k1': 19,
    'k2': 9.0,
    'k3': "String",
    'k4': (1, 2, 3),
    'k5': [12, 1, 8, "abc"],
    'k6': {
        'k11': 'a',
        'k21': [2, "b", 9.0]
    }
}
b = {
    'k1': 19,
    'k2': 9.0,
    'k3': "String",
    'k4': (1, 2, 3),
    'k5': [12, 1, 8, "abc"],
    'k6': {
        'k11': 'a',
        'k21': [2, "b", 9.0]
    }
}
c = {
    'k1': 20,
    'k2': 9.0,
    'k3': "String",
    'k4': (1, 2, 3),
    'k5': [12, 1, 8, "abc"],
    'k6': {
        'k11': 'a',
        'k21': [2, "b", 9.0]
    }
}
# print(compare(a, b))
# print(compare(a, c))

# ex4
def build_xml_element(tag, element, *args):
    xml = "<" + tag
    for i in range(0, len(args)):
        xml += " " + args[i]
    xml += ">" + element + "</" + tag + ">"
    return xml


# print(build_xml_element ("a", "Hello there", 'href =" http://python.org "', '_class =" my-link "',' id= " someid "'))

# ex5
def validate_dict(s, d):
    for (k, v) in d.items():
        found = False
        for i in s:
            if k == i[0]:
                found = True
                if v.startswith(i[1]) is False or v.endswith(i[3]) is False or v.find(i[2]) is False:
                    return False
        if found is False:
            return False

    return True


# s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
# d1={"key1": "come inside, it's too cold out"}
# print(validate_dict(s,d1))


# ex6
def unique_count_duplicates_count(list):
    unique = set()
    for el in list:
        unique.add(el)
    return (len(unique), len(list) - len(unique))


# list = [1, 2, 3, 1, 1, 8, 9, 2]
# print(unique_count_duplicates_count(list))


# ex7
def create_dict(*args):
    dict = {}
    for i in range(0, len(args)):
        for j in range(0, len(args)):
            if i != j:
                dict[str(args[i]) + " & " + str(args[j])] = union(args[i], args[j])
                dict[str(args[i]) + " | " + str(args[j])] = intersection(args[i], args[j])
                dict[str(args[i]) + " - " + str(args[j])] = difference(args[i], args[j])
    return dict


# a = {1, 2}
# b = {2, 3}
# print(create_dict(a, b))


#ex8
def loop(mapping):
    list=[]
    key,value='start',mapping['start']
    while value not in list:
        list.append(value)
        key=value
        value=mapping[key]
    return list

# print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

#ex9
def count_values(*args,**kwargs):
    list=kwargs.values()
    count=0
    for el in args:
        if el in list:
            count+=1
    return count

# print(count_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))