# https://chatgpt.com/share/5cfe84dc-78f1-470a-8d4a-7d236bc39d7b
import mido
import threading


iid_offset=2147483647
iid_offset=1300000000

def list_midi_ports():
    print("Available MIDI input ports:")
    for port in mido.get_input_names():
        print(port)

def print_midi_input(port):
    with mido.open_input(port) as port:
        print(f"Listening to MIDI input from {port.name}")
        for message in port:
            print(message)
            value = iid_offset
            value+=message.channel*1000000
            value+=message.note*1000
            value+=message.velocity
            print("Sending value:", value)

if __name__ == "__main__":
    list_midi_ports()
    # Replace the port names with the actual names of your MIDI devices
    ports = ["Arduino Leonardo 0", "MPK mini play 2"]
    
    # Create and start a thread for each MIDI port
    threads = []
    for port_name in ports:
        thread = threading.Thread(target=print_midi_input, args=(port_name,))
        thread.start()
        threads.append(thread)

    try:
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        # If KeyboardInterrupt is raised, stop all threads
        for thread in threads:
            thread.join()
        print("Stopped listening to MIDI inputs")
