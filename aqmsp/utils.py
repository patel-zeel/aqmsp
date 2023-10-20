import numpy as np


def get_calibration(test_y: np.ndarray, pred_proba_y: np.ndarray, n_bins: int):
    """Get calibration curve

    Args:
        test_y (np.ndarray): Test labels (0 or 1)
        pred_proba_y (np.ndarray): Predicted probabilities of class 1 between 0 and 1
        n_bins (int): Number of bins

    Returns:
        x (np.ndarray): Mean predicted probabilities of class 1 in each bin
        y (np.ndarray): Mean true labels in each bin
    """
    if isinstance(test_y, list):
        test_y = np.array(test_y)
    if isinstance(pred_proba_y, list):
        pred_proba_y = np.array(pred_proba_y)
    if not isinstance(test_y, np.ndarray):
        raise TypeError("test_y must be a numpy array or a list")
    if not isinstance(pred_proba_y, np.ndarray):
        raise TypeError("pred_proba_y must be a numpy array or a list")
    bins = np.linspace(0, 1, n_bins + 1)
    x = []
    y = []
    for start, end in zip(bins, bins[1:]):
        idx = (pred_proba_y >= start) & (pred_proba_y < end)
        if idx.sum() > 0:
            x.append(np.mean(pred_proba_y[idx]))
            y.append(np.mean(test_y[idx]))
        else:
            x.append(np.nan)
            y.append(np.nan)
    return np.array(x), np.array(y)


def expected_calibration_error(test_y: np.array, pred_proba_y: np.array, n_bins: int):
    """Get expected calibration error

    Args:
        test_y (np.ndarray): Test labels (0 or 1)
        pred_proba_y (np.ndarray): Predicted probabilities of class 1 between 0 and 1
        n_bins (int): Number of bins

    Returns:
        ece (float): Expected calibration error
    """
    x, y = get_calibration(test_y, pred_proba_y, n_bins)
    ece = np.abs(x - y).mean()
    return ece
