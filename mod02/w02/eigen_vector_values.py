import numpy as np


def compute_eigenvalues_eigenvectors(
    matrix: list[list[float]],
) -> tuple[list[float], list[list[float]]]:
    """Calculate the eigenvalues and eigenvectors of a matrix."""
    # Convert the input to a numpy array
    matrix_np = np.array(matrix)

    # Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix_np)

    # Convert the results back to lists and return
    return eigenvalues.tolist(), eigenvectors.tolist()
