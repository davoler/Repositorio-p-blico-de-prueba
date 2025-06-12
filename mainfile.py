import numpy as np

"""This part will be related to the OBC Subsystem"""

def quat_normalize(q):
    norm = np.linalg.norm(q)
    return q / norm if norm > 1e-12 else np.array([0.0, 0.0, 0.0, 1.0])