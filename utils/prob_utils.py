import numpy as np


def normalise_to_unity(probs) -> np.array:
    probs = np.array(probs)
    if np.sum(probs) == 0:
        return 1 / len(probs) * np.array([1]*len(probs))
    return 1 / np.sum(probs) * probs
