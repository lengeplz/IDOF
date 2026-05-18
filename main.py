from dataclasses import dataclass, field
from calc_logic import dim_val_met
from pathlib import Path

@dataclass
class Item_Stats:
    item_name: str
    asset_worth: float
    aff_life: int
    perc_work: float
    year_bought: int
    days_held: int
    ded_amount: list[float] = field(default_factory=list)




def main():
    item_dic = {}
    data_list = []
    while True:
        
        item_name = str(input("\nEnter item name: "))
        asset_worth = float(input("\nEnter Value of item: "))
        aff_life = int(input("\nEnter the lifespan: "))
        perc_work = float(input("\nEnter (%) used for work: "))
        perc_work = perc_work / 100
        year_bought = int(input("\n Year bought: "))
        days_held = int(input("\n How many days held: "))

        
        item_instance = Item_Stats(
            item_name=item_name,
            asset_worth=asset_worth,
            aff_life=aff_life,
            perc_work=perc_work,
            year_bought=year_bought,
            days_held=days_held
                                )
        
        item_dic[item_name] = item_instance
        data_list.append(item_instance)

        
        
                                
        
        


        print("\n\nCalculating asset / time...")






    



if __name__ == "__main__":
    main()



    
