import numpy as np
from typing import Optional

def aggregated_curve(y1, y2, x, tolerance=1e-1):
    
    y_range = np.sort(np.concatenate((y1, y2)))[::-1]

    x_range = []

    for y in y_range:

        index1 = np.where(np.isclose(y1, y, atol=tolerance))[0]
        x1 = x[index1][0] if index1.size > 0 else np.nan

        index2 = np.where(np.isclose(y2, y, atol=tolerance))[0]
        x2 = x[index2][0] if index2.size > 0 else np.nan

        if not np.isnan(x1) and not np.isnan(x2):
            x_range.append(x1 + x2)
        elif not np.isnan(x1):
            x_range.append(x1)
        elif not np.isnan(x2):
            x_range.append(x2)
        else:
            x_range.append(np.nan)

    return x_range, y_range