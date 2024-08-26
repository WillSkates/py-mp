import time
import zmq


def run_publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    messageFormat = "{0} {1}"

    while True:
        # All subscribers should get this message.
        msg0 = messageFormat.format(
            "Global",
            "A message for all subscribers"
        )

        msg1 = messageFormat.format(
            "Subscriber 1",
            "A message for subscriber 1"
        )

        msg2 = messageFormat.format(
            "Subscriber 2",
            "A message for subscriber 2"
        )

        # There is no subscriber 3 so we shouldn't see these messages.
        msg3 = messageFormat.format(
            "Subscriber 3",
            "A message for subscriber 3"
        )

        socket.send(str.encode(msg0))
        socket.send(str.encode(msg1))
        socket.send(str.encode(msg2))
        socket.send(str.encode(msg3))

        time.sleep(1)
