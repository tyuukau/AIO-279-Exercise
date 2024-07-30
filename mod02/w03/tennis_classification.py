import numpy as np
import pandas as pd


def create_train_data() -> np.ndarray:
    """Create data"""
    df = pd.read_csv("./data/PlayTennis.csv")
    data = df.to_numpy()
    return np.array(data)


def compute_prior_probability(train_data: np.ndarray) -> np.ndarray:
    """Calculate prior probability"""
    y_labels = ["no", "yes"]
    prior_probability = np.zeros(len(y_labels))
    for num in range(0, len(y_labels)):
        prior_probability[num] = np.sum(
            train_data[:, -1] == y_labels[num]
        ) / len(train_data)
    return prior_probability


def compute_conditional_probability(
    train_data: np.ndarray,
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Calculates the conditional probability P(feature|class) for each feature in the dataset"""
    y_labels = ["no", "yes"]
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_labels), len(x_unique)))

        for rows in range(0, len(y_labels)):
            for cols in range(0, len(x_unique)):
                x_conditional_probability[rows, cols] = np.sum(
                    (train_data[:, -1] == y_labels[rows])
                    & (train_data[:, i] == x_unique[cols])
                ) / np.sum(train_data[:, -1] == y_labels[rows])

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


def get_index_from_value(feature_name: str, list_features: np.ndarray) -> int:
    """Return the index of the feature name"""
    return np.nonzero(list_features == feature_name)[0][0]


def train_naive_bayes(
    train_data: np.ndarray,
) -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    """Train a Naive Bayes model"""
    # Step 1: Caculate Prior Probability
    prior_probablity = compute_prior_probability(train_data=train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data=train_data
    )

    return prior_probablity, conditional_probability, list_x_name


def prediction_play_tennis(
    x: list[str],
    list_x_name: list[np.ndarray],
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
            x_i = get_index_from_value(
                x[feature_idx], list_x_name[feature_idx]
            )
            p *= conditional_probability[feature_idx][class_idx, x_i]

        list_p.append(p)

    return np.argmax(list_p)


def main():
    x = ["Sunny", "Cool", "High", "Strong"]
    data = create_train_data()
    prior_probablity, conditional_probability, list_x_name = (
        train_naive_bayes(data)
    )
    pred = prediction_play_tennis(
        x, list_x_name, prior_probablity, conditional_probability
    )

    if pred:
        print("Ad should go!")
    else:
        print("Ad should not go!")


if __name__ == "__main__":
    main()
