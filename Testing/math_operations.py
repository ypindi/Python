def divide(a: int, b: int) -> int:
    if b==0:
        raise ValueError("Cannot divide by 0")
    return a//b