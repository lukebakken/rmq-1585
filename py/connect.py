# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103,R0205

import logging
import pika
import pprint

logging.basicConfig(level=logging.INFO)

credentials = pika.PlainCredentials('rabbit01', 'changeme')
parameters = pika.ConnectionParameters('localhost', credentials=credentials, virtual_host='vhost_jam')
connection = pika.BlockingConnection(parameters)
print("[INFO] successfully connected!")
channel = connection.channel()
q = channel.queue_declare(queue="", exclusive=True)
print("[INFO] declared queue")
pprint.pp(q)
connection.sleep(60)
connection.close()
