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
  An entry of a bag, which wraps one of the bag's elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CoItem  {

  private URI itemContent;


}