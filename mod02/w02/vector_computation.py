import numpy as np


def compute_vector_length(vector: list[float]) -> float:
    """Calculate the length of the vector."""
    len_of_vector = np.sqrt(np.sum(np.square(vector)))
    return len_of_vector


def compute_dot_product(vector1: list[float], vector2: list[float]) -> float:
    """Calculate the dot product of the two vectors."""
    result = np.dot(vector1, vector2)
    return result


def matrix_multi_vector(
    matrix: list[list[float]], vector: list[float]
) -> list[float]:
    """Calculate the dot product of a matrix and a vector."""
    # Convert the inputs to numpy arrays
    matrix_np = np.array(matrix)
    vector_np = np.array(vector)

    # Calculate the result of the matrix-vector multiplication
    result = np.dot(matrix_np, vector_np)

    # Convert the result back to a list and return
    return result.tolist()


def matrix_multi_matrix(
    matrix1: list[list[float]], matrix2: list[list[float]]
) -> list[list[float]]:
    """Calculate the dot product of two matrices."""
    # Convert the inputs to numpy arrays
    matrix1_np = np.array(matrix1)
    matrix2_np = np.array(matrix2)

    # Calculate the result of the matrix-matrix multiplication
    result = np.dot(matrix1_np, matrix2_np)

    # Convert the result back to a list and return
    return result.tolist()


def inverse_matrix(matrix: list[list[float]]) -> list[list[float]] | None:
    # Convert the input to a numpy array
    matrix_np = np.array(matrix)

    # Calculate the inverse of the matrix
    try:
        result = np.linalg.inv(matrix_np)
        # Convert the result back to a list and return
        return result.tolist()
    except np.linalg.LinAlgError:
        # Handle cases where the matrix is not invertible
        return None
