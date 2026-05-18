from dataclasses import dataclass, field
from calc_logic import dim_val_met

@dataclass
class item_stats:
    asset_worth: float
    aff_life: int
    perc_work: float
    year_bought: int
    days_held: int


def main():

    while True:
        asset_worth = float(input("\nEnter Value of item: "))
        aff_life = int(input("\nEnter the lifespan: "))
        perc_work = float(input("\nEnter (%) used for work: "))
        perc_work = perc_work / 100
        year_bought = int(input("\n Year bought: "))
        days_held = int(input("\n How many days held: "))

        print("\n\nCalculating asset / time...")




    



if __name__ == "__main__":
    main()



    
