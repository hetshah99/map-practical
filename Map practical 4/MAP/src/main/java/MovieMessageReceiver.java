import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MovieMessageReceiver {

    private static final String url = ActiveMQConnection.DEFAULT_BROKER_URL;
    private static final String songQueueName = "Movie_QUEUE";

    public static void main(String[] args) throws Exception {
        System.out.println("URL: "+ url);

        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
        Connection connection = connectionFactory.createConnection();
        connection.start();

        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        Destination destination = session.createQueue(songQueueName);

        MessageConsumer consumer = session.createConsumer(destination);
        Message message = consumer.receive();

        if(message instanceof ObjectMessage){
            ObjectMessage textMessage = (ObjectMessage)message;
            System.out.println("Received Message" + textMessage.getObject());
        }

        connection.close();

    }
}
