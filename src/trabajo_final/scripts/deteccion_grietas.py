#! /usr/bin/python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np


def main():
    rospy.init_node('image_sub')
    pub_sub = PubSub()
    pub_sub.start()
    rospy.spin()


class PubSub(object):

    def __init__(self):
        self.image = None
        self.bridge = CvBridge()
        self.loop_rate = rospy.Rate(1)
        self.pub = rospy.Publisher('/resultado', Image, queue_size=3)

        rospy.Subscriber("/usb_cam/image_raw/", Image, self.callback)

    def callback(self, msg):
        try:
            cv2_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            rospy.sleep(1)
        except e:
            print(e)
        else:
            

            #Convertimos la imagen de entrada en escalad de grises
            
            img_gris = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
            
            #Realizamos una equalizacion de histograma 
            clahe = cv2.createCLAHE(clipLimit= 3)
            image_clahe = clahe.apply(img_gris)+30


            edges = cv2.Canny(image_clahe,120,200)

 
            #Aplicamos un filtro laplaciano para detectectar los bordes en la imagen 
            kernel_laplaciano = np.array([[0,1,0],
                                            [1,-4,1],
                                            [0,1,0]])
            filtro_laplaciano = cv2.filter2D(edges,-1,kernel_laplaciano)

            #Aplicamos la funcion de threlhold adaptativo para reducir el ruido
            thresh2 = cv2.adaptiveThreshold(filtro_laplaciano, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 3)

            # Aplicamos un algoritmo morfologico
            kernel_opening = np.ones((7,7),np.uint8)
            opening = cv2.morphologyEx(filtro_laplaciano,cv2.MORPH_CLOSE, kernel_opening)

            self.image = opening
 

    def start(self):
        while not rospy.is_shutdown():
            if self.image is not None:
                rospy.loginfo('Publicando Imagen')
                self.pub.publish(self.bridge.cv2_to_imgmsg(self.image))
            self.loop_rate.sleep()


if __name__ == '__main__':
    main()