import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('captured_packets.csv')

def plot_protocol_distribution(df):
    """
    Plot the distribution of protocols in the captured packets.

    :param df: DataFrame containing the captured packets.
    """
    sns.countplot(data=df, x='Protocol')
    plt.title('Protocol Distribution')
    plt.xlabel('Protocol')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage
    plot_protocol_distribution(df)