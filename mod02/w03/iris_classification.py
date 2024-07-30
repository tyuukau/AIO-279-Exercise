import numpy as np


def create_train_data_iris() -> np.ndarray:
    """Create data"""
    data = np.loadtxt("./data/iris_data.txt", delimiter=",", dtype=str)
    return data


def compute_prior_probability_iris(train_data: np.ndarray) -> np.ndarray:
    """Calculate prior probability from train data"""
    y_labels = np.unique(train_data[:, -1])
    prior_probability = np.zeros(len(y_labels))
    for num in range(0, len(y_labels)):
        prior_probability[num] = np.sum(
            train_data[:, -1] == y_labels[num]
        ) / len(train_data)
    return prior_probability


def compute_conditional_probability_iris(
    train_data: np.ndarray,
) -> list[np.ndarray]:
    """Calculate conditional probability from train data"""
    y_labels = np.unique(train_data[:, -1])
    conditional_probability = []
    for rows in range(0, len(train_data[1, :]) - 1):
        x_conditional_probability = np.zeros((len(y_labels), 2))
        for cols in range(0, len(y_labels)):
            mean = np.mean(
                train_data[:, rows][
                    train_data[:, -1] == y_labels[cols]
                ].astype(float)
            )
            sigma = np.std(
                train_data[:, rows][
                    train_data[:, -1] == y_labels[cols]
                ].astype(float)
            )
            variance = sigma**2
            x_conditional_probability[cols] = [mean, variance]

        conditional_probability.append(x_conditional_probability)
    return conditional_probability


def guassian_distribution(x: float, mean: float, variance: float) -> float:
    """Gaussian function"""
    result = (1.0 / np.sqrt(2 * np.pi * variance)) * np.exp(
        -((float(x) - mean) ** 2) / (2 * variance)
    )
    return result


def train_gaussian_naive_bayes(
    train_data: np.ndarray,
) -> tuple[np.ndarray, list[np.ndarray]]:
    """Train a Naive Bayes model"""
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability_iris(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability = compute_conditional_probability_iris(train_data)

    return prior_probability, conditional_probability


def prediction_iris(
    x: list[float],
    prior_probability: np.ndarray,
    conditional_probability: list[np.ndarray],
) -> int:
    """Predict on new data"""
    num_classes = len(prior_probability)
    num_features = len(x)

    list_p = []
    for class_idx in range(num_classes):
        p = prior_probability[class_idx]
        for feature_idx in range(num_features):
            mean = conditional_probability[feature_idx][class_idx][0]
            variance = conditional_probability[feature_idx][class_idx][1]
            p *= guassian_distribution(x[feature_idx], mean, variance)

        list_p.append(p)

    return list_p.index(max(list_p))


def main():
    x = [6.3, 3.3, 6.0, 2.5]

    train_data = create_train_data_iris()
    y_labels = np.unique(train_data[:, 4])
    prior_probability, conditional_probability = train_gaussian_naive_bayes(
        train_data
    )
    pred = y_labels[
        prediction_iris(x, prior_probability, conditional_probability)
    ]
    print(pred)


if __name__ == "__main__":
    main()
