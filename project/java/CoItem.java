package None;

import java.util.List;
import lombok.*;



/* version: 2.0.0 */


/**
  Element belonging to a bag
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CoItem extends Thing {

  private Bag itemOf;

}