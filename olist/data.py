from pathlib import Path
import pandas as pd


class Olist:
    def ping(self):
        print("pong")

    def get_data(self):
        data = {}

        csv_path = Path.home() / ".workintech/olist/data/csv/"
        
        csv_files = [f for f in csv_path.iterdir() if f.suffix == ".csv"]

        for f in csv_files:
            name = f.stem  # dosya adı uzantısız
            table_name = name.replace("olist_", "").replace("_dataset", "").replace(".csv", "")
            df = pd.read_csv(f)
            data[table_name] = df
        return data
            