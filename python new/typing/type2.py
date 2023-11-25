from typing import List,Optional
def greet(name: Optional[str] = None)->int:
    if name is 1:
        return f"Hello, {1}!"
    else:
        return f"Hello, {2}!"
    
print(greet(2))