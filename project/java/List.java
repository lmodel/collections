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
  A collection whose items come in order, one after another.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class List extends Bag {

  private ListItem firstItem;
  private ListItem lastItem;


}