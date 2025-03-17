## robotics-academy-challenge
Complete a lap following the line painted on the racing circuit.

### Installation

This is a breif introduction of installation, full installation refers to this [LINK](https://jderobot.github.io/RoboticsAcademy/user_guide/).


#### Step 1 - Pull images

Pull images with the following commands:

````
docker pull jderobot/robotics-database:latest
docker pull jderobot/robotics-academy:latest
````

#### Step 2 - Launch Robotics Academy Container

##### Terminal 1 - Launch Databases:

````
docker run --hostname my-postgres --name academy_db -d\
    -e POSTGRES_DB=academy_db \
    -e POSTGRES_USER=user-dev \
    -e POSTGRES_PASSWORD=robotics-academy-dev \
    -e POSTGRES_PORT=5432 \
    -d -p 5432:5432 \
    jderobot/robotics-database:latest
````

##### Terminal 2 - Launch image with Nvidia option:

````
docker run --rm -it $(nvidia-smi >/dev/null 2>&1 && echo "--gpus all" || echo "") --device /dev/dri -p 6080:6080 -p 1108:1108 -p 7163:7163 -p 7164:7164 --link academy_db jderobot/robotics-academy:latest
````

#### Step 3 - Perform the exercises

1. On the local machine navigate to 127.0.0.1:7164/ in the browser and choose the desired exercise.

2. Click on the exercise you want to work with.

3. Wait until the exercise is fully loaded. You know it is fully loaded when the Robotics Backend, World and Visualization state boxes are green.

4. This repo provide one of the solution for the [FOLLOW LINE](https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/) exercise, you can use the LOADFILE option at the top left corner to load the script in the scripts folder to check the result.

