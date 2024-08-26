import zmq


def run_subscriber(topic):
    print("Client is connecting to server")

    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5556")

    socket.setsockopt(zmq.SUBSCRIBE, str.encode(topic))
    socket.setsockopt(zmq.SUBSCRIBE, b"Global")

    while True:
        message = socket.recv()
        print("{0}: \"{1}\".".format(topic, message))
