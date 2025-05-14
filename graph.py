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

    # Create a figure and 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()  # flatten for easier indexing

    # Plot 1: Protocol distribution
    sns.countplot(data=df, x='Protocol', hue='Protocol', ax=axes[0], palette='viridis', legend=False)
    axes[0].set_title('Protocol Distribution')
    axes[0].set_xlabel('Protocol')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    # Plot 2: Top Source IPs 
    top_sources = df['Source IP'].value_counts().nlargest(5)
    sns.barplot(x=top_sources.values, y=top_sources.index, hue=top_sources.index, ax=axes[1], palette='magma', legend=False)
    axes[1].set_title('Top Source IPs')
    axes[1].set_xlabel('Packet Count')
    axes[1].set_ylabel('Source IP')

    # Plot 3: Packet Length Distribution
    sns.histplot(df['Length'].dropna(), bins=15, ax=axes[2], kde=True, color='coral')
    axes[2].set_title('Packet Length Distribution')
    axes[2].set_xlabel('Packet Length')
    axes[2].set_ylabel('Frequency')

    # Plot 4: Top Destination IPs
    top_destinations = df['Destination IP'].value_counts().nlargest(5)
    sns.barplot(x=top_destinations.values, y=top_destinations.index, hue=top_destinations.index, ax=axes[3], palette='plasma', legend=False)
    axes[3].set_title('Top Destination IPs')
    axes[3].set_xlabel('Packet Count')
    axes[3].set_ylabel('Destination IP')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_packet_analysis(df)
