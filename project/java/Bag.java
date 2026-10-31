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
  A collection that may hold one element more than once, in no order.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bag extends Collection {

  private List<CoItem> item;


}