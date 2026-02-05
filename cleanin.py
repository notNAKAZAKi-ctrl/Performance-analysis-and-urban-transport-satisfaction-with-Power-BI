import pandas as pd
import xml.etree.ElementTree as ET
import glob
import os

# --- CONFIGURATION ---
# We define these at the top so they are easy to change later.
START_YEAR = 2019
END_YEAR = 2025
OUTPUT_FILE = "Unified_Ridership_2019_2025.csv"

def parse_chicago_data():
    """
    Reads all Chicago RDF files, extracts data, and cleans XML tags.
    Returns: A Pandas DataFrame.
    """
    print(f"--- 1. Processing Chicago Data ({START_YEAR}-{END_YEAR}) ---")
    
    # 'glob' finds every file ending in .rdf in the current folder
    rdf_files = glob.glob("Data/rdf_CTA__Ridership__Daily_by_Route_routes_2001_2025/*.rdf")
    print(f"   Found {len(rdf_files)} raw files.")
    
    cleaned_rows = []
    
    for file_path in rdf_files:
        try:
            # Parse the XML tree structure
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            for row in root:
                record = {}
                for field in row:
                    # XML tags often come with annoying URLs like {http://...}route
                    # This line splits the tag and keeps only the clean name at the end
                    tag_name = field.tag.split('}')[-1] if '}' in field.tag else field.tag
                    record[tag_name] = field.text
                
                # --- FILTERING LOGIC ---
                # We check the date immediately to save memory.
                # Format is usually '2023-09-11T00:00:00'
                if 'date' in record and record['date']:
                    year = int(record['date'][:4]) # Grab the first 4 digits
                    if START_YEAR <= year <= END_YEAR:
                        cleaned_rows.append(record)
                        
        except Exception as e:
            print(f"   Warning: Could not read {file_path}. Reason: {e}")
            
    # Convert list of dictionaries to a Table
    df = pd.DataFrame(cleaned_rows)
    
    if not df.empty:
        # Standardize columns to match our final schema
        df = df.rename(columns={'rides': 'ridership_count', 'daytype': 'day_type'})
        df['city'] = 'Chicago'
        df['date'] = pd.to_datetime(df['date']).dt.date
        print(f"   -> Successfully extracted {len(df)} rows for Chicago.")
        return df
    else:
        print("   -> Warning: No matching data found for Chicago.")
        return pd.DataFrame()

def parse_philly_data():
    """
    Reads Philadelphia CSV, fixes dates, and standardizes columns.
    Returns: A Pandas DataFrame.
    """
    print(f"\n--- 2. Processing Philadelphia Data ({START_YEAR}-{END_YEAR}) ---")
    
    # Find any CSV that looks like the Philly route file
    philly_files = glob.glob("Data/*By_Route*.csv")
    
    if not philly_files:
        print("   -> Error: Philadelphia CSV file not found.")
        return pd.DataFrame()
    
    # Load the file
    df = pd.read_csv(philly_files[0])
    
    # 1. Filter by Year
    df = df[(df['Calendar_Year'] >= START_YEAR) & (df['Calendar_Year'] <= END_YEAR)]
    
    # 2. Create a proper Date column (The CSV has separate Year/Month columns)
    # We create a string like "2023-9-1" and convert it to a real date
    df['date'] = pd.to_datetime(
        df['Calendar_Year'].astype(str) + '-' + 
        df['Calendar_Month'].astype(str) + '-01'
    ).dt.date
    
    # 3. Rename columns to match Chicago's structure
    df = df.rename(columns={
        'Route': 'route', 
        'Average_Daily_Ridership': 'ridership_count'
    })
    df['city'] = 'Philadelphia'
    
    # 4. Select only the columns we need
    final_columns = ['date', 'city', 'route', 'ridership_count']
    df_clean = df[final_columns]
    
    print(f"   -> Successfully extracted {len(df_clean)} rows for Philadelphia.")
    return df_clean

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Step 1: Get the data
    chicago_df = parse_chicago_data()
    philly_df = parse_philly_data()
    
    # Step 2: Combine them
    if not chicago_df.empty and not philly_df.empty:
        print("\n--- 3. Merging Datasets ---")
        # Stack them on top of each other
        unified_df = pd.concat([chicago_df, philly_df], ignore_index=True)
        
        # Step 3: Save the result
        unified_df.to_csv(OUTPUT_FILE, index=False)
        print(f"SUCCESS! Final dataset saved as: {OUTPUT_FILE}")
        print(f"Total Rows: {len(unified_df)}")
    else:
        print("\nCRITICAL ERROR: One or both datasets failed to load.")