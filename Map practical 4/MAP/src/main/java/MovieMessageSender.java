import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;
import java.util.ArrayList;


public class MovieMessageSender {
    private static final String url = ActiveMQConnection.DEFAULT_BROKER_URL;

    private static final String MovieQueueName = "Movie_QUEUE";
    static ArrayList<Movie> MovieList;

    public static void main(String[] args) throws Exception {
        System.out.println("URL: " + url);


        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
        Connection connection = connectionFactory.createConnection();
        connection.start();


        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        Destination destination = session.createQueue(MovieQueueName);
        MovieList = new ArrayList<Movie>();


        MessageProducer producer = session.createProducer(destination);

        Movie myMovie = new Movie();
        myMovie.setId( MovieList.size()+1+"");
        myMovie.setMovieName("Second Movie");
        myMovie.setAlbumName("First Movie");
        myMovie.setArtistName("First Movie");

        MovieList.add(myMovie);

        ObjectMessage message = session.createObjectMessage(myMovie);
        producer.send(message);

        System.out.println("Message: " + message.getObject() + " sent successfully to the Queue");
        connection.close();
    }
}
