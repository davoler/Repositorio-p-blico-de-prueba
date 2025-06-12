"""
This will be the main file for VSCODE / Github lab
Here we will be creating a call for spacecraft and their subsystems

"""
# Libraries
import numpy as np
import pandas as pd

# Class Creation

class Satellite:
    """
    Represents a class to create a spacecraft
    """
    def __init__(self, name, altitude, orbit_type="LEO"):
        """_summary_

        Args:
            name (_type_): _Name of the spacecraft_
            altitude (_type_): _description of the spacecraft_
            orbit_type (str, optional): _description for the type of orbit_. Defaults to "LEO".
        """
        
        self.name = name
        self.altitude = altitude  # in kilometers
        self.orbit_type = orbit_type
        self.status = "Idle"
        self.data_collected = 0 # in GB

"""This part will be related to the OBC Subsystem"""

def quat_normalize(q):
    norm = np.linalg.norm(q)
    return q / norm if norm > 1e-12 else np.array([0.0, 0.0, 0.0, 1.0])