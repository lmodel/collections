package None;

import java.util.List;
import lombok.*;



/* version: 2.0.0 */


/**
  An ordered array of items, that can be present in multiple copies
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class List extends Bag {

  private List<ListItem> item;
  private ListItem lastItem;
  private ListItem firstItem;

}