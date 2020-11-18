import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MovieTopicConsumer implements Runnable{

    ActiveMQConnectionFactory connectionFactory = null;

    public MovieTopicConsumer(ActiveMQConnectionFactory connectionFactory) {
        this.connectionFactory = connectionFactory;
    }

    @Override
    public void run() {
        try{
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createTopic(MovieTopicProducer.MovieTopic);

            MessageConsumer consumer = session.createConsumer(destination);

            Message message = consumer.receive();

            if(message instanceof ObjectMessage){
                ObjectMessage objectMessage = (ObjectMessage)message;
                System.out.println("Received Message:\n" + ((ObjectMessage) message).getObject());
            }
            session.close();
            connection.close();


        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
