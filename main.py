from ColorDetection import openCam
import numpy as np

def run_other_file():
    with open("main.py") as f:
        code = f.read()
        exec(code)

openCam(0,np.array([183, 255, 255]), np.array([170, 100, 60]))
