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
  An item of a list, which has a place in the list's order.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListItem extends CoItem {

  private int index;
  private ListItem nextItem;
  private ListItem previousItem;
  private List<ListItem> followedBy;
  private List<ListItem> precededBy;


}