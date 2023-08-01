import os
import requests

# URLs for the datasets
URLS = {
    "season_2021.csv": "https://www.football-data.co.uk/mmz4281/2021/D1.csv",
    "season_1920.csv": "https://www.football-data.co.uk/mmz4281/1920/D1.csv",
    "season_1819.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1819_csv/data/b5d1d632500bf4f26791f91a2990ee2a/season-1819_csv.csv",
    "season_1718.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1718_csv/data/26fe5a3646f607a523e0257c7ee70cce/season-1718_csv.csv",
    "season_1617.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1617_csv/data/8f0d10c346a02caa5ae3cd70ec0c104a/season-1617_csv.csv",
    "season_1516.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1516_csv/data/e80cd71251723a74416cfe0acea8af39/season-1516_csv.csv",
    "season_1415.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1415_csv/data/4ca47cf8526001ab7a9098824c5cd88d/season-1415_csv.csv",
    "season_1314.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1314_csv/data/00c4a3143f03d9ca96ca39d85a46713a/season-1314_csv.csv",
    "season_1213.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1213_csv/data/7eca11f594896fa4e6a35bae0445788e/season-1213_csv.csv",
    "season_1112.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1112_csv/data/7057ead6c924b58952d023c3fa46fa07/season-1112_csv.csv",
    "season_1011.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-1011_csv/data/3a8a53c3c9aec630cf0f47d154360e21/season-1011_csv.csv",
    "season_0910.csv": "https://pkgstore.datahub.io/sports-data/german-bundesliga/season-0910_csv/data/85412a4130fec6b2a1b26c2ca4a94a61/season-0910_csv.csv",
    "season_0809.csv": "https://www.football-data.co.uk/mmz4281/0809/D1.csv",
    "season_0708.csv": "https://www.football-data.co.uk/mmz4281/0708/D1.csv",
    "season_0607.csv": "https://www.football-data.co.uk/mmz4281/0607/D1.csv",
    "season_0506.csv": "https://www.football-data.co.uk/mmz4281/0506/D1.csv",
    "market_cap.csv": "https://transfer.sh/wmkmtQ/market_cap.csv" # Note: This link might be temporary
}

DATA_DIR = "data"

def download_data():
    """Downloads all datasets into the data/ directory."""
    os.makedirs(DATA_DIR, exist_ok=True)
    for filename, url in URLS.items():
        save_path = os.path.join(DATA_DIR, filename)
        try:
            print(f"Downloading {filename} from {url}...")
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for bad status codes
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved to {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    download_data()
