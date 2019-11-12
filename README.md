# Kafka + Python con Faust


Antes de instalar Kafka como requerimiento principal debemos tener instalado Java.


Luego de esto instalamos Kafka.
En MacOS es simple con el manejador de Paquetes 

`brew install kafka`

En linux especificamente en Ubuntu si es un poco mas complicado.

[https://linuxhint.com/install-apache-kafka-ubuntu/](https://)

Vamos a iniciar Kafka y Zookeeper

De todas maneras les dejo un post donde explican mejor la configuración previa y posterior que hay que hacer para poder correr Kafka

[https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273](https://)

Corremos Kafka y Zookeper de acuerdo a y creamos los dos topics que vamos a usar



```
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic_erp

kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic_notif
```



Y corremos cada worker de la siguiente manera
```
python worker_process.py worker -l info --web-port=6067
python worker_erp.py worker -l info --web-port=6068
python worker_notify.py worker -l info --web-port=6069
```


Vamos a simular esta arquitectura:

![](https://i.imgur.com/tyc4E6A.png)
