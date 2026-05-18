import numpy as np
import os
from pathlib import Path



def dim_val_met(cost_item, lifespan, days_held, perc_work):

    fis_start_late = 1
    if days_held == 365 or days_held ==  366:
        fis_start_late = 0

    asset_cost = cost_item * perc_work
    for i in range(0, lifespan + fis_start_late, 1):

        