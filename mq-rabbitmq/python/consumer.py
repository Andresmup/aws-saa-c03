from basicClient import BasicPikaClient

class BasicMessageReceiver(BasicPikaClient):

    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            print('No message returned')

    def close(self):
        self.channel.close()
        self.connection.close()


if __name__ == "__main__":

    # Create Basic Message Receiver which creates a connection
    # and channel for consuming messages.
    basic_message_receiver = BasicMessageReceiver(
        "b-1c0a14d3-fb9f-484c-9d3b-6aaa2effe7d1",
        "admin",
        "Password12345!",
        "us-east-1"
    )

    # Consume the message that was sent.
    basic_message_receiver.get_message("QueueV1")

    # Close connections.
    basic_message_receiver.close()