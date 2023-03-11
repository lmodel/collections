package None;

import java.util.List;
import lombok.*;



/* version: 2.0.0 */


/**
  A group of objects that can be considered as a whole.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Collection extends Thing {

  private List<Thing> element;
  private String size;

}