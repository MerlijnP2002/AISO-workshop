import cmath
import math

CONSTANTS: dict[str, float] = {
    "pi":    math.pi,
    "e":     math.e,
    "tau":   math.tau,
    "phi":   (1 + math.sqrt(5)) / 2,
    "sqrt2": math.sqrt(2),
    "sqrt3": math.sqrt(3),
    "inf":   math.inf,
}


def _resolve(value: float | str) -> complex:
    if isinstance(value, str):
        key = value.strip().lower()
        if key in CONSTANTS:
            return CONSTANTS[key]
        try:
            return complex(value)
        except ValueError:
            raise ValueError(f"Unknown constant or value: '{value}'")
    return value


def _fmt(value: complex) -> str:
    if value.imag == 0:
        real = value.real
        if isinstance(real, float) and real.is_integer():
            return str(int(real))
        return str(real)
    if value.real == 0:
        return f"{value.imag}j"
    return str(value)


def calculator(operation: str, a: float | str, b: float | str = 0.0) -> str:
    """Perform arithmetic, logarithmic, trigonometric, and complex calculations.

    Operations: add, subtract, multiply, divide, modulo, power, abs, floor,
    ceil, round, sqrt, log (base b, default 10), ln, log2, exp, sin, cos, tan,
    asin, acos, atan, atan2, deg2rad, rad2deg, sinh, cosh, tanh, csqrt, cexp, cabs.
    Constants for a/b: "pi", "e", "tau", "phi", "sqrt2", "sqrt3", "inf".
    """
    operation = operation.strip().lower()

    try:
        a_val = _resolve(a)
        b_val = _resolve(b)

        if operation == "add":
            result = a_val + b_val
        elif operation == "subtract":
            result = a_val - b_val
        elif operation == "multiply":
            result = a_val * b_val
        elif operation == "divide":
            if b_val == 0:
                return "Error: division by zero."
            result = a_val / b_val
        elif operation == "modulo":
            if b_val == 0:
                return "Error: modulo by zero."
            result = a_val % b_val
        elif operation == "power":
            result = a_val ** b_val
        elif operation == "abs":
            result = abs(a_val)
        elif operation == "floor":
            result = math.floor(a_val.real)
        elif operation == "ceil":
            result = math.ceil(a_val.real)
        elif operation == "round":
            decimals = int(b_val.real) if b_val != 0 else 0
            result = round(a_val.real, decimals)
        elif operation == "ln":
            result = cmath.log(a_val)
        elif operation == "log2":
            result = cmath.log(a_val, 2)
        elif operation == "log":
            base = b_val if b_val != 0 else 10
            result = cmath.log(a_val, base)
        elif operation == "exp":
            result = cmath.exp(a_val)
        elif operation == "sin":
            result = cmath.sin(a_val)
        elif operation == "cos":
            result = cmath.cos(a_val)
        elif operation == "tan":
            result = cmath.tan(a_val)
        elif operation == "asin":
            result = cmath.asin(a_val)
        elif operation == "acos":
            result = cmath.acos(a_val)
        elif operation == "atan":
            result = cmath.atan(a_val)
        elif operation == "atan2":
            result = math.atan2(a_val.real, b_val.real)
        elif operation == "deg2rad":
            result = math.radians(a_val.real)
        elif operation == "rad2deg":
            result = math.degrees(a_val.real)
        elif operation == "sinh":
            result = cmath.sinh(a_val)
        elif operation == "cosh":
            result = cmath.cosh(a_val)
        elif operation == "tanh":
            result = cmath.tanh(a_val)
        elif operation in ("sqrt", "csqrt"):
            result = cmath.sqrt(a_val)
        elif operation == "cexp":
            result = cmath.exp(complex(a_val.real, b_val.real))
        elif operation == "cabs":
            result = abs(complex(a_val.real, b_val.real))
        else:
            return f"Error: unknown operation '{operation}'."

    except Exception as exc:
        return f"Error: {exc}"

    if isinstance(result, complex):
        real = 0.0 if abs(result.real) < 1e-12 else result.real
        imag = 0.0 if abs(result.imag) < 1e-12 else result.imag
        result = complex(real, imag)
    elif isinstance(result, float) and abs(result) < 1e-12:
        result = 0.0

    return _fmt(complex(result) if not isinstance(result, complex) else result)
