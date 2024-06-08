from typing import Any, Dict, Callable
import math


def is_number(x: Any) -> bool:
    """Check if the input can be converted to a float."""
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x: float) -> float:
    """Compute the sigmoid function of the input."""
    return 1 / (1 + math.e ** (-x))


def relu(x: float) -> float:
    """Compute the Rectified Linear Unit (ReLU) of the input."""
    return x if x > 0 else 0


def elu(x: float) -> float:
    """Compute the Exponential Linear Unit (ELU) of the input."""
    return x if x > 0 else 0.01 * (math.e**x - 1)


def calculate_activation_function() -> None:
    """
    Calculate the activation function.

    Raises:
        TypeError: If the input value for x is not a number.
        ValueError: If the selected activation function is not supported.
    """
    # Dictionary to map activation function names to their respective functions
    func_dict: Dict[str, Callable[[float], float]] = {
        "sigmoid": sigmoid,
        "relu": relu,
        "elu": elu,
    }

    # Get user input for the value of x
    x = input("Input x: ")
    if not is_number(x):
        raise TypeError("x must be a number")

    # Get user input for the activation function
    func_name = input("Input activation function (sigmoid|relu|elu): ")
    if func_name not in func_dict:
        raise ValueError(f"{func_name} is not supported")

    # Convert input value to float and apply the selected activation function
    x = float(x)
    print(f"{func_name}: f({x}) = {func_dict[func_name](x)}")


if __name__ == "__main__":
    try:
        calculate_activation_function()
    except Exception as e:
        print(e)
