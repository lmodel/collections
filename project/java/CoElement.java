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
  A thing that a collection holds, named by its IRI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CoElement  {

  private URI iri;


}