import messaging
from threading import Thread
import time

publisherThread = Thread(
    target=messaging.run_publisher,
    args=[]
)

subscriber1Thread = Thread(
    target=messaging.run_subscriber,
    args=["Subscriber 1"]
)

subscriber2Thread = Thread(
    target=messaging.run_subscriber,
    args=["Subscriber 2"]
)

if __name__ == "__main__":
    print("Starting Publisher...")
    publisherThread.start()

    print("Starting Subscribers...")
    subscriber1Thread.start()
    subscriber2Thread.start()

    subscriber2Thread.join()
