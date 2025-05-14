from net_capture import capture_packets
from analyzer import analyze_packets_from_csv
from graph import plot_packet_analysis
import os
import pandas as pd

def main():
    interface = 'en0'  # Replace with your actual interface
    output_file = 'captured_packets.csv'
    duration = 10  # in seconds

    # Check if the file already exists
    if not os.path.exists(output_file):
        print("No existing capture found. Starting packet capture...")
        capture_packets(interface, output_file, duration)
    else:
        print(f"Using existing capture file: {output_file}")

    # Analyze the captured packets
    if os.path.exists(output_file):
        analysis_results = analyze_packets_from_csv(output_file)
        print(f"\nTotal packets: {analysis_results['total_packets']}")
        print("Protocol distribution:")
        for protocol, count in analysis_results['protocol_distribution'].items():
            print(f"{protocol}: {count}")

        # Load data for graphing
        df = pd.read_csv(output_file)
        plot_packet_analysis(df)
    else:
        print(f"Error: File '{output_file}' does not exist. Cannot analyze or plot.")

if __name__ == "__main__":
    main()
