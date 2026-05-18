from dataclasses import dataclass, field
import datetime
import calendar
from pathlib import Path

@dataclass
class Item_Stats:
    item_name: str
    asset_worth: float
    aff_life: int
    perc_work: float
    year_bought: int
    days_held: int
    dep_amount: list[float] = field(default_factory=list)




def main():
    from calc_logic import dim_val_met
    item_dic = {}
    data_list = []
    while True:
        
        item_name = str(input("\nEnter item name: "))
        asset_worth = float(input("\nEnter Value of item: "))
        aff_life = int(input("\nEnter the lifespan: "))
        perc_work = float(input("\nEnter (%) used for work: "))
        perc_work = perc_work / 100
        year_bought = int(input("\nYear bought: "))
        
        while True:
            days_held = int(input("\nHow many days held: "))

            if days_held > 366 and not calendar.isleap(year_bought): 
                print(f"\nWoahhhh... That's a lot of days in a year :?, Try again. P.S there are {366 if calendar.isleap(year_bought) else 365} days in {year_bought}")
                continue

            elif days_held == 366 and not calendar.isleap(year_bought):
                print(f"\n{year_bought} is not a leap year... P.S there are {366 if calendar.isleap(year_bought) else 365} days in {year_bought}")
                continue
            
            elif days_held > 366 and calendar.isleap(year_bought):
                print(f"\n{year_bought} is not a leap year... P.S there are {366 if calendar.isleap(year_bought) else 365} days in {year_bought}")
                continue
            
            else:
                break





        
        item_instance = Item_Stats(
            item_name=item_name,
            asset_worth=asset_worth,
            aff_life=aff_life,
            perc_work=perc_work,
            year_bought=year_bought,
            days_held=days_held
                                )
        dim_val_met(item_instance.asset_worth, item_instance.aff_life, item_instance.days_held, item_instance.perc_work, item_instance)

        item_dic[item_name] = item_instance
        data_list.append(item_instance)

        print(data_list[0])
        
        
        
                                
        
        


        print("\n\nCalculating asset / time...")






    



if __name__ == "__main__":
    main()



    
