from dataclasses import dataclass, field
from calc_logic import dim_val_met

@dataclass
class Item_Stats:
    item_name: str
    asset_worth: float
    aff_life: int
    perc_work: float
    year_bought: int
    days_held: int



def main():
    item_dic = {}
    while True:
        
        item_name = str(input("\nEnter item name: "))
        appendix_val = len(item_dic)
        item_dic["item_name"] = appendix_val
        asset_worth = float(input("\nEnter Value of item: "))
        aff_life = int(input("\nEnter the lifespan: "))
        perc_work = float(input("\nEnter (%) used for work: "))
        perc_work = perc_work / 100
        year_bought = int(input("\n Year bought: "))
        days_held = int(input("\n How many days held: "))


        


        print("\n\nCalculating asset / time...")






    



if __name__ == "__main__":
    main()



    
