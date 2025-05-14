# network-traffic-analyzer
A tool for capturing, analyzing, and visualizing network traffic using Python. 

Tech Stack: Python 3.12.3
Main Libraries used: 
- pyshark
- matplotlib
- seaborn
- pandas
- os

Main features:
1. Capture networks packets in the specified interface and save it to a csv file
2. Analyze the data captured and shows protocol distribution
3. Plot data on a graph (protocol, top IP's, packet length)

To run this on your machine locally, make sure to download the libraries using the command:
pip install pyshark pandas matplotlib seaborn
