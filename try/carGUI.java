
import javax.swing.JFrame;

public class carGUI
{
   /**
    * Creates and displays the main program frame.
    */
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("car");
      carPanel panel = new carPanel();
      
      frame.getContentPane().add(panel);      
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.pack();
      frame.setVisible(true);
   }
}
