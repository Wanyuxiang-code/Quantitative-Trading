'''do a mean of the high and low prices and plot it'''
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Qt4Agg')



df = pd.read_csv("C:\\Users\\wyx\\Desktop\\Codes\\Python_work\\test\\IBM.csv")
df['High'].tail().plot
plt.show()  # must be called to show plots

def test_run():
    df = pd.read_csv("C:\\Users\\wyx\\Desktop\\Codes\\Python_work\\test\\IBM.csv")
    df['Mean'] = (df['High'] + df['Low']) / 2
    df['Mean'].plot()
    plt.show()  # must be called to show plots
print(2)

if __name__ == "__main__":
    test_run()

