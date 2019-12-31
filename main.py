from typing import List
from werkzeug.datastructures import FileStorage


def a6_sort_list(a: List[int]):
    print("type of a = ", type(a), " => ", a)
    return sorted(a)

def a6_add(a: int, b: int):
    return a+b 

def a6_sey_hello(name): 
    return "hello " + name 

def a6_read_file(file: FileStorage):
    print(file.stream.read())
    return 0
