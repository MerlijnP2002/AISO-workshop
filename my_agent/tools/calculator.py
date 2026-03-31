import math


def calculator(operation: str, a: float, b: float = 0.0) -> str:
    """Performs arithmetic calculations. Use this tool for any non-trivial
    arithmetic to avoid rounding errors.

    Supported operations:
    - "add"      : a + b
    - "subtract" : a - b
    - "multiply" : a * b
    - "divide"   : a / b  (returns error if b is 0)
    - "power"    : a ** b  (a raised to the power b)
    - "sqrt"     : √a      (b is ignored)
    - "modulo"   : a % b

    Args:
        operation: The arithmetic operation to perform (see above).
        a: The primary operand (or the radicand for sqrt).
        b: The secondary operand (ignored for sqrt). Defaults to 0.

    Returns:
        The result as a string, or an error message if the operation fails.

    Examples:
        calculator("divide", 4782969, 127)   -> "37661.1732283465"
        calculator("power", 2, 47)           -> "140737488355328.0"
        calculator("sqrt", 76384.88)         -> "276.3..."
        calculator("add", 1500, 250.75)      -> "1750.75"
    """
    operation = operation.strip().lower()

    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                return "Error: division by zero."
            result = a / b
        elif operation == "power":
            result = a ** b
        elif operation == "sqrt":
            if a < 0:
                return "Error: square root of a negative number is not real."
            result = math.sqrt(a)
        elif operation == "modulo":
            if b == 0:
                return "Error: modulo by zero."
            result = a % b
        else:
            return (
                f"Error: unknown operation '{operation}'. "
                "Supported: add, subtract, multiply, divide, power, sqrt, modulo."
            )
    except Exception as e:
        return f"Error: {e}"

    # Return an integer string when the result is a whole number,
    # otherwise return a full-precision float string.
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)
