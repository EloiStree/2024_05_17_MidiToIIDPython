# Source: https://chatgpt.com/share/67694673-eb75-4ec6-bc2a-19f9ed737c40

import mido

iid_offset=2147483647
iid_offset=1300000000

# Function to list available MIDI input ports
def list_midi_ports():
    print("Available MIDI input ports:")
    for port in mido.get_input_names():
        print(port)

# Define the port name for the Arduino Leonardo MIDI output
# Replace 'Arduino Leonardo' with the actual port name
port_name = 'Arduino Leonardo 0'

# Function to handle MIDI messages
def handle_message(message):
    print("Received MIDI message:", message)
    value = iid_offset
    value+=message.channel*1000000
    value+=message.note*1000
    value+=message.velocity
    print("Sending value:", value)

# Main function to listen for MIDI messages
def listen_midi(port_name):
    # Try to open the MIDI port
    try:
        port = mido.open_input(port_name)
        print(f"Listening to MIDI messages from {port_name}. Press Ctrl+C to exit.")

        # Keep listening for MIDI messages
        for message in port:
            handle_message(message)

    # Handle port not found or other errors
    except OSError:
        print(f"Error: MIDI port '{port_name}' not found.")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        if port:
            port.close()

# Run the main function
if __name__ == "__main__":
    list_midi_ports()
    listen_midi(port_name)
