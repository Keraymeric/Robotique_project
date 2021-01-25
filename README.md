# Groupe 8 
# Amaury de Scorraille
# Aymeric Kerserho
# Protocole

# INSTALLATION DE NOTRE REPO

Construire un ROSJECT Kinetic sans template
Ouvrir le Webshell #1 et copier :

``
rm -fr catkin_ws
git clone https://github.com/Keraymeric/Project catkin_ws
rm -fr simulation_ws
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
``
Ouvrir le Webshell #2 et copier:
``
cd catkin_ws
catkin_make
source devel/setup.bash
cd ..
cd simulation_ws
catkin_make
source devel/setup.bash
cd ..
``
# CHALLENGE 1:

1- Dans le Webshell #1, lancer la configuration de la simulation: roslaunch larm challenge-1.launch

2- Dans le Webshell #2, lancer l'architecture de contrôle: roslaunch student_package navigation.launch

3- Dans le Webshell #3, lancer la localisation globale: roslaunch student_package amcl.launch

4- Dans le Webshell #4, lancer rviz pour visualiser: rosrun rviz rviz

Ouvrir ensuite une simulation Gazebo ainsi que l'outil graphique.

Configuration RVIZ: Ajouter: RobotModel Map --> move_base/global_costmap/costmap LaserScan --> topic: /scan PoseArray --> topic: /particlecloud TF

En comparant avec Gazebo, estimer la position du robot à l'aide de 2D Pose Estimate (les données du laser et de la carte doivent se superposer)

Enfin, avec 2D nav goal faite déplacer le robot afin d'observer son comportement.

# CHALLENGE 2:
1- Dans le Webshell #1, lancer la configuration de la simulation: roslaunch larm challenge-2.launch

2- Dans le Webshell #2, lancer l'architecture de contrôle: roslaunch student_package mapping.launch

3- Dans le Webshell #3, lancer l'architecture de contrôle: roslaunch student_package navigation.launch

4- Dans le Webshell #5, lancer rviz pour visualiser: rosrun rviz rviz

Ouvrir ensuite une simulation Gazebo ainsi que l'outil graphique.

Avec 2D Nav Goal déplacer le robot, vous pouvez suivre la détection des canettes sur la caméra du robot sur Rviz. Plusieurs écrans sont disponible pour vous aidez à comprendre
le traitement de l'image de la caméra.

# CHALLENGE 3:
1- Dans le Webshell #1, lancer la configuration de la simulation: roslaunch larm challenge-3.launch

2- Dans le Webshell #2, lancer l'architecture de contrôle: roslaunch student_package mapping.launch

3- Dans le Webshell #3, lancer l'architecture de contrôle: roslaunch student_package navigation.launch

4- Dans le Webshell #3, lancer l'architecture de contrôle: roslaunch student_package exploration.launch

5- Dans le Webshell #5, lancer rviz pour visualiser: rosrun rviz rviz

Ouvrir ensuite une simulation Gazebo ainsi que l'outil graphique.

Utiliser publish point dans rviz pour poser les sommets du polygone délimitant la zone à explorer.
Pour fermer le polygone, placer le dernier point sur la position du premier: le polygone deviendra alors rouge, ce qui signifie que la zone est sélectionnnée.
Pour lancer l'exploration, placer encore un point n'importe où à l'intérieur du polygone... Le robot devrait alors s'y déplacer et commencer le balayage...

# Configuration du RVIZ:
Le fichier se situant dans le dossier rviz vous donne la configuration pour les 3 challenges
