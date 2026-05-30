from typing import Optional,Any,Union,List

def get_name(name: Optional[str] = None) ->str:

    if name:
        return name
    return "Anonymous"

print(get_name())


def process_value(value: Union[int,str]) -> str:
    if isinstance(value,int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value(5))


def process_anything(value: Any) -> str:
    return f"Processed {value}"

print(process_anything(1))


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

result = sum_list([1,2,3,4])
print(f"Rezultati: {result}")