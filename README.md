# Decode Oculus Packet Captures

This script is intended to decode oculus packet captures. After importing output.pcap into wireshark, you'll notice that the conversations to Facebook IPs are fragmented across multiple packets, so right click and follow the conversation to see the full message. The payload is url encoded, base64 encoded, and compressed. This script will decode it so you can see the information that Facebook sends back from your device.

The data will be returned in JSON format.

## Installing a certificate on your Oculus
From your terminal, run `adb shell am start -a android.intent.action.VIEW -d com.oculus.tv -e uri com.android.settings/.Settings$TrustedCredentialsSettingsActivity com.oculus.vrshell/.MainActivity`. Then scroll to Security -> User credentials. First, you'll have to set a screen lock pin, but then you'll be able to install your own root certificates.

## Running mitmproxy with a script
`mitmproxy -s mitmpcap.py`
