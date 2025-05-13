import csv
from collections import Counter

def analyze_packets_from_csv(file_path):
    """
    Analyze captured packets from a CSV file and return a summary of the analysis.

    :param file_path: Path to the CSV file containing captured packets.
    :return: Dictionary containing the analysis results.
    """

    # counter for the number of packets and the protocol distribution
    total_packets = 0
    protocol_counter = Counter()

    # Read the CSV file and analyze packets
    with open(file_path, mode='r') as file: 
        reader = csv.DictReader(file) # read the csv file as a dictionary
        for row in reader:
            total_packets += 1 
            protocol = row['Protocol'] # get the protocol from the row
            protocol_counter[protocol] += 1

    # saves it in this format 
    analysis_results = {
        'total_packets': total_packets,
        'protocol_distribution': dict(protocol_counter)
    }

    return analysis_results

# just for testing rn
if __name__ == "__main__":
    file_path = 'captured_packets.csv'
    analysis = analyze_packets_from_csv(file_path)
    print(f"Total packets: {analysis['total_packets']}")
    print("Protocol distribution:")
    for protocol, count in analysis['protocol_distribution'].items():
        print(f"{protocol}: {count}")