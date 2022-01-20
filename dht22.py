import subprocess
import time
import click
import board
import adafruit_dht
import json


@click.command()
@click.option('--gpio', required=True, help='RaspberryPi GPIO number', type=int)
@click.option('--broker_ip', required=True, help='MQTT broker ip', type=str)
@click.option('--broker_port', required=True, default="1883", help='MQTT broker port', type=str)
@click.option('--topic', required=True, help='MQTT topic', type=str)
@click.option('--interval', required=True, default=60, help='Interval of measurements in seconds', type=int)
@click.option('--user', required=True, help='MQTT user name', type=str)
@click.option('--password', required=True, help='MQTT password', type=str)
def humi_temp(gpio, broker_ip, broker_port, topic, interval, user, password):

    # configure variables
    gpio_id = gpio
    broker_ip = broker_ip
    broker_port = broker_port
    mqtt_topic = topic
    measurement_interval = interval
    mqtt_user = user
    mqtt_password = password

    pin = getattr(board, f"D{int(gpio_id)}")
    dht_device = adafruit_dht.DHT22(pin)

    while True:
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        d = {"temperature": temperature, "humidity": humidity}
        msg = json.dumps(d)

        subprocess.call(["mosquitto_pub",
                         "-h", broker_ip,
                         "-p", broker_port,
                         "-t", mqtt_topic,
                         "-m", msg,
                         "-u", mqtt_user,
                         "-P", mqtt_password])
        time.sleep(measurement_interval)


if __name__ == '__main__':
    humi_temp()