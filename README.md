# evidencia_2

Este proyecto se encarga de visualizar un voltaje en tiempo real el cual es adequirido de la tarjeta arduino uno , su otro proposito es el de controlar dos salidas digitales las cuales se podran encender y apagar en cualquier momento que se desea.
Arduino 
Se procede abrir el archivo codigo_u2.ino el cual contiene el codigo de arduino , una vez abierto este archivo tienes que seleccionar tus salidas digitales en las lineas 11 y 12 las cuales estan pre-configuradas como 6 y 7, en la linea 15 del codigo seleccionas tu entrada analogica la cual tiene pre-configurada como a0 , una vez concluido con estos pasos se procede a conectar la tarjeta a la PC , el siguiente paso seria verificar en que puerto esta conectada la tarjeta y eso se realiza en la opcion de select bord and port,ya  que se selecciono el puerto como la tarjeta correspondiente se porcede a verificar el codigo y cargalo a la tarjeta.

Pyhton
Ahora conitnuamos con la parte de python ,  se debe de abrir el archivo requirements.txt para poder instalar las librerias necesarias para poder correr el programa en  el equipo , una vez instalado se abre el archvio codigo_2.py el cual contiene la programacion lado python.Al estar dentro del programa se tiene que configurar el puerto con el que se va a conectar por medio serial con la tarjeta y esto se realiza en la linea 11 del codigo  el cual cunta con una configuracion pre-programada con el 'COM7'.
Una vez configurado el puerto serial se porcede a seleccionar la opcion de run module y a continuacion aparecera dos cuadros los cuales contiene la grafica con el voltaje en tiempo real y el otro contiene dos botones los cuales manejan las dos salidas digitales y por medio de estos dos botones se controla el encendido y apagado de dichas salidas mostrando en estado "OFF" cuando las salidas estan apagadas y en estado "ON" cuando las salidas estan activadas.

Los nombres de los integrantes son :
Roman Ruiz Corral
Marco Polo Mancinas Valdez
Carlos Ivan Ramirez Vazquez
Christian Lopez Ramirez