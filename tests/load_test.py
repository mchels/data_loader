import os
import sys
sys.path.append('..')
from sweep import Sweep

# Load 1D reference data.
path = os.path.relpath('C:/git_repos/data_loader/tests/1D_data_reference')
sweep1D = Sweep(path=path)
print(sweep1D.data['backgate'])

# Load 2D reference data.
path = os.path.relpath('C:/git_repos/data_loader/tests/2D_data_reference')
sweep2D = Sweep(path=path)
print(sweep2D.data['backgate'])
