import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import java.util.Scanner;

public class MoviePubSubMain {

    private static final String url = ActiveMQConnection.DEFAULT_BROKER_URL;

    public static void main(String[] args) throws Exception{
        ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
        Scanner input = new Scanner(System.in);
        int number= input.nextInt();
        for(int i=0;i<number;i++) {
            Thread MovieConsumer = new Thread(new MovieTopicConsumer(connectionFactory));
            MovieConsumer.start();

            Thread.sleep(1000);

            Thread MovieProducer = new Thread(new MovieTopicProducer(connectionFactory));
            MovieProducer.start();

            Thread.sleep(1000);
        }
    }
}
