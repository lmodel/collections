package example;

/* metamodel_version: 1.12.0 */
/* version: 2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A group of things that is taken as a whole.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Collection  {

  private Integer coSize;
  private List<CoElement> element;


}