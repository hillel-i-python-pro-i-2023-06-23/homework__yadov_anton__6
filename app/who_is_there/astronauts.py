import pandas as pd
from app.config import FILES_OUTPUT_DIR

def average():
    url = 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'
    csv_file_path = FILES_OUTPUT_DIR.joinpath("test.csv")
    df = pd.io.parsers.read_csv(url)
    df.to_csv(csv_file_path)
    hight = df[['Height(Inches)']].mean()
    weight = df[['Weight(Pounds)']].mean()
    print(f'Height {round(hight*2.54)[0]} kg')
    print(f'Weight {round(weight*0.453592)[0]} sm')
    df=FILES_OUTPUT_DIR.joinpath("test.csv")
    df.unlink()