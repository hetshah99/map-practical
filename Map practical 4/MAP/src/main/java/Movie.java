import java.io.Serializable;
import java.util.Objects;

public class Movie implements Serializable {
    String id;
    String songName;
    String artistName;
    String albumName;

    public Movie() {
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getMovieName() {
        return songName;
    }

    public void setMovieName(String songName) {
        this.songName = songName;
    }

    public String getArtistName() {
        return artistName;
    }

    public void setArtistName(String artistName) {
        this.artistName = artistName;
    }

    public String getAlbumName() {
        return albumName;
    }

    public void setAlbumName(String albumName) {
        this.albumName = albumName;
    }


    @Override
    public int hashCode() {
        return Objects.hash(getId(), getMovieName(), getArtistName(), getAlbumName());
    }

    @Override
    public String toString() {
        return "Movie{" +
                "id='" + id + '\'' +
                ", MovieName='" + songName + '\'' +
                ", artistName='" + artistName + '\'' +
                ", albumName='" + albumName + '\'' +
                '}';
    }
}
