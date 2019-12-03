# Decode Oculus Packet Captures

This script is intended to decode oculus packet captures. After importing output.pcap into wireshark, you'll notice that the conversations to Facebook IPs are fragmented across multiple packets, so right click and follow the conversation to see the full message. The payload is url encoded, base64 encoded, and compressed. This script will decode it so you can see the information that Facebook sends back from your device.

The data will be returned in JSON format.
