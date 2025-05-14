import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the CSV file
df = pd.read_csv('captured_packets.csv')

def plot_packet_analysis(df):
    """
    Create subplots to analyze captured packet data.
    
    :param df: DataFrame containing captured packet information.
    """
    
    # Create a figure and axes (3 subplots side by side)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # --- Plot 1: Protocol distribution ---
    sns.countplot(data=df, x='Protocol', ax=axes[0], palette='viridis')
    axes[0].set_title('Protocol Distribution')
    axes[0].set_xlabel('Protocol')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    # --- Plot 2: Top 5 Source IPs ---
    top_sources = df['Source IP'].value_counts().nlargest(5)
    sns.barplot(x=top_sources.values, y=top_sources.index, ax=axes[1], palette='magma')
    axes[1].set_title('Top 5 Source IPs')
    axes[1].set_xlabel('Packet Count')
    axes[1].set_ylabel('Source IP')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_packet_analysis(df)
