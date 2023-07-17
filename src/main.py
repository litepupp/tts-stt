"""
...
"""

import argparse

from pythonosc import udp_client


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument(
        "--port",
        type=int,
        default=5005,
        help="The port the OSC server is listening on",
    )
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    while True:
        try:
            msg = input()
            client.send_message("/filter", msg)
            print("\033[1A" + "\033[K", end="")
        except KeyboardInterrupt:
            break
