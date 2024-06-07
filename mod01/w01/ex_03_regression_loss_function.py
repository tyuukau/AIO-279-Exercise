from typing import Dict, Callable
from math import sqrt
import random


def mae(pred: float, true: float) -> float:
    return abs(pred - true)


def mse(pred: float, true: float) -> float:
    return (pred - true) ** 2


def rmse(pred: float, true: float) -> float:
    return mse(pred, true)


def exercise3() -> None:
    """
    Calculates the regression loss function.

    Raises:
        TypeError: If the number of samples is not an integer.
    """
    # Dictionary to map loss function names to their respective functions
    func_dict: Dict[str, Callable[[float, float], float]] = {
        "mae": mae,
        "mse": mse,
        "rmse": rmse,
    }

    # Get user input for the number of samples
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        raise TypeError("The number of samples must be an integer number.")

    num_samples = int(num_samples)

    # Get user input for the loss function name
    loss_func_name = input("Input loss name: ")

    # Initialize final_loss variable to accumulate the total loss
    final_loss = 0
    # Loop through the specified number of samples
    for i in range(num_samples):
        true = random.uniform(0, 10)
        pred = random.uniform(0, 10)
        loss = func_dict[loss_func_name](pred=pred, true=true)
        print(
            f"Loss name: {loss_func_name}, sample: {i}, pred: {pred}, target: {true}, loss: {loss}"
        )
        # Accumulate the loss for all samples
        final_loss += loss

    # Average the total loss over the number of samples
    final_loss /= num_samples

    # If the selected loss function is RMSE, take the square root of the final loss
    if loss_func_name == "rmse":
        final_loss = sqrt(final_loss)

    print(f"final {loss_func_name}: {final_loss}")


if __name__ == "__main__":
    try:
        exercise3()
    except Exception as e:
        print(e)
