import numpy as np
from dataclasses import dataclass, field
import os
from pathlib import Path
from main import Item_Stats



def dim_val_met(cost_item, lifespan, days_held, perc_work, item_instance: Item_Stats):

    
    calc_dim_val = 0
    fis_start_early = 0
    if days_held == 365 or days_held ==  366:
        fis_start_early = 1
        bo_fis_start_early = True

    asset_cost = cost_item * perc_work
    stop_year = lifespan + 1 if fis_start_early else lifespan + 1
    for year in range(0 + fis_start_early, stop_year, 1):

        if not calc_dim_val:
            if year == 0:
                dim_val = float(asset_cost * (days_held / 365) * (2 / lifespan))
                calc_dim_val = True
                asset_cost = asset_cost - dim_val
            else:
                dim_val = float(asset_cost * (365 / 365) * (2 / lifespan))
                asset_cost = asset_cost - dim_val
                calc_dim_val = True
        
        else:
            dim_val = float(asset_cost * (365 / 365) * (2 / lifespan))
            asset_cost = asset_cost - dim_val

        if year == 0:
            print(f"Year 0, Day {days_held} deduction: ${dim_val:.2f}")
            

        else:
            print(f"Year {year} deduction: ${dim_val:.2f}")
        
        item_instance.dep_amount.append(dim_val)

        
        



if __name__ == "__main__":
    dim_val_met(1256, 10, 187, 1)