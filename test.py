"""
...
"""

from pythonosc import udp_client


def main() -> None:
    """
    ...
    """

    client = udp_client.SimpleUDPClient("localhost", 9000)

    while True:
        try:
            msg = input()
            client.send_message("/chatbox/input", [msg, True, False])
            print("\033[1A" + "\033[K", end="")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
