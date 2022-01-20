# rpi-dht22-mqtt
This python script is measuring temperature and humidity from dht22 sensor connected to specified gpio port of 
raspberry pi and sending it to mqtt broker to specified topic.

## build docker image
```sh
docker build . -t rpi-dht22-mqtt
```

## run docker container
```sh
docker run -d \
        -e GPIO_ID="4" \
        -e BROKER_IP="192.168.1.2" \
        -e BROKER_PORT="1883" \
        -e TOPIC="Home/Livingroom/humitemp" \
        -e USER="mqtt_user" \
        -e PASSWORD="mqtt_password" \
        --device /dev/ttyAMA0:/dev/ttyAMA0 \
        --device /dev/mem:/dev/mem \
        --privileged \
        --name humidity_temp_livingroom \
        --restart always \
        rpi-dht22-mqtt
```

##Acknowledgment
Thanks to Angel Castro Martinez, (https://github.com/kronos-cm) for docker multistage 
build recommendations for python projects.