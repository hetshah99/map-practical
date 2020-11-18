import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;
import java.util.Random;

public class MovieTopicProducer implements Runnable{
    ActiveMQConnectionFactory connectionFactory = null;
    public static final String MovieTopic = "Movie Topic";

    public MovieTopicProducer(ActiveMQConnectionFactory connectionFactory) {
        this.connectionFactory = connectionFactory;
    }

    @Override
    public void run() {
        try{
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            Destination destination = session.createTopic(MovieTopic);

            MessageProducer producer = session.createProducer(destination);
            producer.setDeliveryMode(DeliveryMode.PERSISTENT);

            Movie myMovie = new Movie();
            myMovie.setId(new Random().nextInt(100) +"");
            myMovie.setMovieName("Second Movie");
            myMovie.setAlbumName("First Movie");
            myMovie.setArtistName("First Movie");

            ObjectMessage message = session.createObjectMessage(myMovie);

            producer.send(message);

            System.out.println("Producer has sent the message: " + myMovie);

            session.close();
            connection.close();

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
