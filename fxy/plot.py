import os

mode = os.environ.get('_FXY_MODE_')

try:
    import matplotlib; import matplotlib.pyplot as plt
    if mode:
        print('import matplotlib; .pyplot as plt')
except:
    pass

try:
    import seaborn; import seaborn as sns
    if mode:
        print('import seaborn; as sns')
except:
    pass
