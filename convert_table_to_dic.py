import tabula

# Read all tables from a specific page or 'all' pages
tables = tabula.read_pdf("li2025-020.pdf", pages='all')

for table in tables:
    # Loop through each row in the table
    for idx, row in table.iterrows():
        asset_name = row['ASSET']
        asset_life = row['LIFE\r(IN YEARS)']  # Note: includes the \r (carriage return)
        
        print(f"{asset_name} - {asset_life} years")