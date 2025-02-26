import torch
import os
import sys
from contextlib import contextmanager

# Context manager to suppress stdout and stderr
@contextmanager
def suppress_stdout_stderr():
    with open(os.devnull, 'w') as null_out:
        # Save the current stdout and stderr
        stdout, stderr = sys.stdout, sys.stderr
        # Set stdout and stderr to the null device
        sys.stdout, sys.stderr = null_out, null_out
        try:
            yield
        finally:
            # Restore stdout and stderr
            sys.stdout, sys.stderr = stdout, stderr

# from kandinsky2 import get_kandinsky2
# from PIL import Image
# import numpy as np



def batch_inpaint_imgs(images, masks, prompts, pipe):
    
    with suppress_stdout_stderr():
        outputs = pipe(
            prompt=list(prompts),  # List of prompts for each image in the batch
            image=list(images),    # List of images in the batch
            mask_image=list(masks), # List of masks corresponding to each image in the batch
            num_inference_steps=50
        )
    # Extract the images from the outputs
    return outputs.images
