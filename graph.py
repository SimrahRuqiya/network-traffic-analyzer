# graph.py
import csv
import matplotlib.pyplot as plt
from collections import Counter

def plot_protocol_distribution(csv_file):
    protocols = []

    # Read the CSV file and extract protocols
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            protocol = row.get("Protocol")
            if protocol:
                protocols.append(protocol)

    # Count protocols
    counts = Counter(protocols)

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# For testing directly
if __name__ == "__main__":
    plot_protocol_distribution("captured_packets.csv")
