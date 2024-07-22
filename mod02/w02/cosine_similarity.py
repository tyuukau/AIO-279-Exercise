import numpy as np


def compute_cosine(v1: list[float], v2: list[float]) -> float:
    """Calculate the eigenvalues and eigenvectors of a matrix."""
    # Convert the input lists to numpy arrays
    v1_np = np.array(v1)
    v2_np = np.array(v2)

    # Calculate the dot product of the vectors
    dot_product = np.dot(v1_np, v2_np)

    # Calculate the norms (lengths) of the vectors
    norm_v1 = np.linalg.norm(v1_np)
    norm_v2 = np.linalg.norm(v2_np)

    # Calculate the cosine similarity
    cos_sim = dot_product / (norm_v1 * norm_v2)

    return cos_sim
