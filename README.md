# TrabajoPercepcion
El presente trabajo se realizo con motivo de proyecto final de modulo de percepcion, correspondiente al Diplomado en Robotica dictado en la Universidad Catolica Boliviana San Pablo

# Resumen
El proyecto consiste en detectar grietas presentes en las paredes mediante el uso de equalizacion de histograma adaptativo (CLAHE) y difentes fltros de paso alto. La equalizacion de histograma consiste en tratar de equilibrar los valores altos presentes en la distribucion de pixeles, en el caso se aplico este metodo ya que tenia mejor resultado mejorando el contraste y brillo, en comparacion de la equalizacion tradicional. La etapa de filtrado presenta la conjuncion de dos filtros orientados a la deteccion de bordes como son el filtro canny y el filtro laplaciano. Para la eliminacion del background presente en las imagenes se procedio a utilizar un threshold adaptativo el cual conjunciona los threshold de la media y la binarzacion inversa. La ultima etapa realizada fue la aplicacion de un algorimtmo morfologico, en este caso fue aplicado la operacion de opening el cual aplica los de erosion y dilatacion.
# Requisitos
- Ubuntu 20
- ROS Noetic
- Python 3.9
- OpenCV 4.6
- CVBridge
- USBcam
- RViz

# Procedimiento
El siguiente procedimiento debe ser realizado en terminales separadas, por lo cual se aconseja el uso de Terminator para un mejor manejo de los siguientes comandos.

1. Ejecutar el comando roscore en una terminal

{% filename %}command-line{% endfilename %}
  
    $ roscore
2. Como topicos de entrada se utlizaron ROS bags que fueron grabado con una camara USB calibrada. El ROS bag utilizado esta disponible en el siguiente [enlace](https://drive.google.com/file/d/1hWHPUwRl5bPH15qT9tBOvUa7anlseXw-/view?usp=sharing). Para ejecutarlo se debe correr el comando rosbag play en la ubicacion del archivo.

{% filename %}command-line{% endfilename %}
  
    $ rosbag play -l filename
 3.  Una vez iniciados los topicos, procedemos a correr el script en python en cual esta ubicado en el package trabajo_final en la carpeta scripts. Se recuerda que antes de ejecutarlo se debe realizar el proceso de darle permisos para que se ejecute.
 
{% filename %}command-line{% endfilename %}
  
    $ chmod +x deteccion_grietas.py
    
{% filename %}command-line{% endfilename %}
    
    $ python3 deteccion_grietas.py
 4. Para la visualizacion de los resultados del procesamiento del video se debe utilizar RViz y anadir los topicos de usb_cam y resultado. La siguiente linea de comando ejecuta RViz.

{% filename %}command-line{% endfilename %}
    
    $ rosrun rviz rviz
# Resultados  
A continuacion se presentan los resultados de las diferentes etapas de procesamiento:
- ![Implementacion raw](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/1.png)
- ![Implementacion de CLAHE](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/2.png)
- ![Filtro Canny](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/3.png)
- ![Filtro Laplaciano](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/4.png)
- ![Implementacion de un Threshold Adaptativo](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/5.png)
- ![Aplicacion del algoritmo morfologico de Opening](https://github.com/jaquiroz/TrabajoPercepcion/tree/main/src/trabajo_final/Imagenes/6.png)

# Conclusiones
- Para obtener mejores resultados es preferible tener a disposicion una cmaara con buena resolucion, para evitar el desenfoque o la inclusion de ruido.
- La iluminacion es un factor de relevancia debido a que genera una desbalance al momento de realizar el proceso de equalizacion.
- Para mejores resultados es preferible utilizar filtros nmo lineles con el tradeoff de aumentar el poder computo. 
    
  
