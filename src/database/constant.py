'''
This module provides the constants to the modules for generating database. The constants
are documented in section nine of SRS:
https://github.com/CynthiaLiu0805/BridgeCorrosion/blob/main/docs/SRS/SRS.pdf
Some names might differ because some notation could not by typed as code.'''

import pandas as pd

from pathlib import Path
# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
WEB_PUBLIC_DIR = PROJECT_ROOT / 'src' / 'web' / 'public'

class Constant:

    salt_application_rate_high = 0.07  # V_salt_h
    salt_application_rate_low = 0.05   # V_salt_l

    W_lane = 3.75                # W_lane
    V_speed = 100                # V_speed
    b = 0.56                     # b
    K = 0.75                     # K
    h_film = 0.0001              # h_film
    water_density = 997          # \rho_{water}
    V = 62.1371                  # V
    chloride_ratio = 0.61        # \theta_{chloride}
    d = 3.5                      # d
    ldv_ratio = 6                # \Theta

    df = pd.read_excel(DATA_DIR / "data.xlsx", sheet_name="t1")
    
    # Columns except the first one ('Year')
    columns = df.columns[1:]
    years = [int(y) for y in columns]
    
    # Start/end year and number of years
    START_YEAR = min(years)
    END_YEAR = max(years)
    NUM_YEARS = END_YEAR - START_YEAR + 1

    # Number of rows excluding the header
    NUM_ROWS = len(df)

