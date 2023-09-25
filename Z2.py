import math
def process(arg):
    if isinstance(arg, list):
        unique_elements = list(set(arg))
        geometric_mean = math.prod(unique_elements) ** (1.0 / len(unique_elements))
        return unique_elements, geometric_mean
    elif isinstance(arg, dict):
        return list(arg.keys())
    elif isinstance(arg, int):
        return len(str(arg))
    elif isinstance(arg, str):
        words = arg.split()
        palindromes = [word for word in words if word == word[::-1]]
        return len(palindromes)
def z2():
    print(process([1, 2, 2, 3, 3, 3]))
    print(process({"a": 1, "b": 2}))
    print(process(12345))
    print(process("Odin Dva Tri"))