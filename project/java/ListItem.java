package None;

import java.util.List;
import lombok.*;



/* version: 2.0.0 */


/**
  element belonging to a list
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListItem extends CoItem {

  private String index;

}