import numpy as np
import cv2


def compute_difference(
    bg_img: np.ndarray, input_img: np.ndarray
) -> np.ndarray:
    # Compute the absolute difference between the background image and the input image
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype("uint8")

    return difference_single_channel


def compute_binary_mask(difference_single_channel: np.ndarray) -> np.ndarray:
    # Apply a binary threshold to the single channel difference image
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,) * 3, axis=-1)
    return difference_binary


def replace_background(
    bg1_image: np.ndarray, bg2_image: np.ndarray, ob_image: np.ndarray
) -> np.ndarray:
    """
    Extracts the foreground object from `ob_image` using background subtraction with `bg1_image`
    and overlays it onto `bg2_image`.
    """
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


def main():
    bg1_image = cv2.imread("./data/GreenBackground.png", 1)
    bg1_image = cv2.resize(bg1_image, (678, 381))

    ob_image = cv2.imread("./data/Object.png", 1)
    ob_image = cv2.resize(ob_image, (678, 381))

    bg2_image = cv2.imread("./data/NewBackground.jpg", 1)
    bg2_image = cv2.resize(bg2_image, (678, 381))

    output = replace_background(bg1_image, bg2_image, ob_image)
    cv2.imwrite("./data/Output.png", output)


if __name__ == "__main__":
    main()
