# DMD---PSI

The code is built on python=3.8.x on Windows 10. 

## How to run
The code is based on two primary components:
- DMD_driver.py which provides DMD_driver class. This is used to control the DMD,
and is based on the ajiledriver
- adc_driver.py which provides adc_driver class. This is used to control an appropriately
coded RaspberryPi.

For example:

```python
import numpy as np
from DMD_driver import DMD_driver
import time

# Connect to the DMD
dmd = DMD_driver()
# Create a default project
dmd.create_project(project_name='test_project')
# Add an image as a subsequence
dmd.add_sequence_item(image=np.ones((1080, 1920)), 
                      seq_id=1, frame_time=1000)
# Add a sequence
dmd.create_main_sequence(seq_rep_count = 1)
# Start the sequence
dmd.start_projecting()
# Wait for 5 seconds
time.sleep(5)
# Stop the sequence
dmd.stop_projecting()
```
## Higher level image handling

We also have data structure to handle the data transfer between the computer and the DMD.
This is provided in the DMD_structures.py file:

```python
from DMD_driver import DMD_driver
from DMD_structures import dmd_image

# Connect to the driver
dmd = DMD_driver()
# Create an image (can be a named pattern, numpy array, or none)
image_to_project = dmd_image(dmd_driver=dmd, image='random_50_50')
# We can directly project this
image_to_project.project()
```
