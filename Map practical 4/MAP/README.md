# Activemq-Project
This is a simple ActiveMQ and JMS project. Project handler used is Maven.

## Requirements
- Intellij-Idea (Java IDE)
- Java 8 or above
- ActiveMQ installed

## Installing ActiveMQ
- Download activemq from here https://activemq.apache.org/components/classic/download/
- Unzip the folder and keep in any directory you want.(Say in -> C:\Program Files\apache-activemq-5.16.0 )
- Set the PATH Environment variable till the bin directory. In above example (C:\Program Files\apache-activemq-5.16.0\bin)
- You are done with installation.

## Starting ActiveMQ web console
- Run cmd as Administrator
- Type -> avtivemq start
- Wait for some time till it completely starts
- In your browser go to http://127.0.0.1:8161/
- Now go to Admin page from the opened web page. (Username : admin, Password: admin)

## Running this project
- Complete all above installation
- Clone this repository. (git clone "https://github.com/yash311/Activemq-Project.git")
- Open Intellij-idea and open the cloned project from your PC
- Run SongPubSubMain.java
- from the activemq web console go to TOPICS and "SONG TOPIC" can be seen

