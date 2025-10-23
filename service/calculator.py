import json
from fastapi.responses import JSONResponse # Still needed if you use it outside this class, but not in it

class Calculator:
    def __init__(self, data: dict) -> None:
        # Note: You might want to validate that 'a' and 'b' are numbers here
        self.a = data.get('a')
        self.b = data.get("b")
        self.operator = data.get("operator")

    def calculate_add(self) -> int | float:
        # No change needed
        sum_val = self.a + self.b
        return sum_val
    
    def calculate_subtract(self) -> int | float:
        # No change needed
        sub = self.a - self.b
        return sub
    
    def calculate_multiply(self) -> int | float:
        # No change needed
        multiply = self.a * self.b
        return multiply
    
    def calculate_divide(self) -> int | float:
        # 🟢 CORRECTION 1: Check for value 0, and RAISE an exception on error
        if self.b == 0:
            # Raise a native Python exception. The calling FastAPI route will catch this.
            raise ZeroDivisionError(f"Cannot divide by zero. Denominator is {self.b}.")
            
        divide = self.a / self.b
        return divide
    
    def calculate_(self) -> int | float:
        # Removed the inner try/except block. It's better to let errors propagate 
        # to the FastAPI router, which can handle them with a 500 status code.
        
        if self.operator == "add":
            return self.calculate_add()
            
        elif self.operator == "subtract":
            return self.calculate_subtract()
            
        elif self.operator == "multiply":
            return self.calculate_multiply()
            
        elif self.operator == "divide":
            return self.calculate_divide()
            
        else:
            # 🟢 CORRECTION 2: RAISE an exception for an invalid operator
            raise ValueError(f"Invalid operator '{self.operator}'. Must be one of: add, subtract, multiply, divide.")