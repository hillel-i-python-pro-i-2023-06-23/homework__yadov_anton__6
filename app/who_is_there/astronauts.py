import pandas as pd
def average():
    url = 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'
    df = pd.read_csv(url)
    height = df['Height(Inches)'].mean()
    weight = df['Weight(Pounds)'].mean()
    print(f'Mean height {height*2.54} sm')
    print(f'Mean weight {weight*0.453592} kg')
