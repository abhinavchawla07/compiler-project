import java.util.*;
class Movie extends Video {
	String Movie_Name;
	rating Rating;
	Movie(double Play_Duration, Date Release_Date,String name,rating Rating) {
		super(Play_Duration, Release_Date);
		this.Movie_Name = name;
		this.Rating = Rating;
	}
}
