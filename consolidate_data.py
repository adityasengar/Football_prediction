import pandas as pd
import os

DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "full_dataset.csv")

def consolidate_data():
    """
    Loads all season CSVs, standardizes columns, and saves them into a single file.
    """
    all_seasons_df = []
    
    # List of common columns to keep
    # Different sources have different column names, so we need to standardize
    columns_req = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']

    for filename in sorted(os.listdir(DATA_DIR)):
        if filename.startswith("season_") and filename.endswith(".csv"):
            filepath = os.path.join(DATA_DIR, filename)
            print(f"Processing {filepath}...")
            df = pd.read_csv(filepath)
            
            # The schemas are slightly different, so we select what we need
            # This is a simplified way to handle schema differences.
            # A more robust solution would map columns explicitly.
            
            # Check for required columns before proceeding
            if all(col in df.columns for col in columns_req):
                 season_df = df[columns_req]
                 all_seasons_df.append(season_df)
            else:
                print(f"  - Warning: Skipping {filename} due to missing columns.")

    if not all_seasons_df:
        print("No valid season data found. Exiting.")
        return

    # Concatenate all dataframes
    full_df = pd.concat(all_seasons_df, ignore_index=True)
    
    # Convert 'Date' to datetime and sort
    full_df['Date'] = pd.to_datetime(full_df['Date'], errors='coerce', dayfirst=True)
    full_df = full_df.dropna(subset=['Date'])
    full_df = full_df.sort_values(by="Date").reset_index(drop=True)

    # Save to a new CSV
    full_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSuccessfully consolidated {len(full_df)} matches into {OUTPUT_FILE}")

if __name__ == "__main__":
    # Note: Run download_data.py first to get the raw files.
    if not os.path.exists(DATA_DIR) or not any(f.startswith("season_") for f in os.listdir(DATA_DIR)):
         print("Data files not found. Please run 'python download_data.py' first.")
    else:
        consolidate_data()
