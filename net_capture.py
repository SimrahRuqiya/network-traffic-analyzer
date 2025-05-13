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
    capture_packets = pyshark.LiveCapture(interface=interface)
    capture_packets.sniff(timeout=duration)
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'source', 'destination', 'protocol', 'length']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for packet in capture_packets:
            try:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(packet.sniff_time)))
                source = packet.ip.src if hasattr(packet, 'ip') else ''
                destination = packet.ip.dst if hasattr(packet, 'ip') else ''
                protocol = packet.transport_layer if hasattr(packet, 'transport_layer') else ''
                length = packet.length if hasattr(packet, 'length') else ''
                
                writer.writerow({
                    'timestamp': timestamp,
                    'source': source,
                    'destination': destination,
                    'protocol': protocol,
                    'length': length
                })
            except AttributeError as e:
                print(f"Error processing packet: {e}")
    print(f"Packet capture complete. Data saved to {output_file}")

# Example usage
capture_packets('en0', 'captured_packets.csv', 20)
