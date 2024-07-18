from basicClient import BasicPikaClient

class BasicMessageSender(BasicPikaClient):

    def declare_queue(self, queue_name):
        print(f"Trying to declare queue({queue_name})...")
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body)
        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")

    def close(self):
        self.channel.close()
        self.connection.close()

if __name__ == "__main__":

    # Initialize Basic Message Sender which creates a connection
    # and channel for sending messages.
    basic_message_sender = BasicMessageSender(
        "b-1c0a14d3-fb9f-484c-9d3b-6aaa2effe7d1",
        "admin",
        "Password12345!",
        "us-east-1"
    )

    # Declare a queue
    basic_message_sender.declare_queue("QueueV1")

    # Send a message to the queue.
    basic_message_sender.send_message(exchange="", routing_key="QueueV1", body=b'Message N3')

    # Close connections.
    basic_message_sender.close()