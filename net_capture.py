import pyshark
import csv
import time

def capture_packets(interface, output_file, duration):
    """
    Capture packets on a specified network interface and save to a CSV file.

    :param interface: Network interface to capture packets from.
    :param output_file: File to save captured packets.
    :param duration: Duration of the capture in seconds.
    """
    # Start capturing packets
    capture = pyshark.LiveCapture(interface=interface)

    print(f"Capturing packets on {interface} for {duration} seconds...")

    # Open the output CSV file and write the header
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Source IP", "Destination IP", "Protocol", "Length"])

        # Capture packets for the specified duration
        start_time = time.time() #current time
        for packet in capture.sniff_continuously():
            if time.time() - start_time >= duration:
                break

            # Extract the relevant details from each packet
            try:
                timestamp = packet.sniff_time
                source_ip = packet.ip.src 
                destination_ip = packet.ip.dst 
                protocol = packet.highest_layer
                length = packet.length

                # Write the packet details to the CSV file
                writer.writerow([timestamp, source_ip, destination_ip, protocol, length])
            except AttributeError:
                # Skip packets that don't have the expected attributes (e.g., non-IP packets)
                continue

    print(f"Capture complete. Packets saved to {output_file}.")

# Example usage
capture_packets('en0', 'captured_packets.csv', 10)
