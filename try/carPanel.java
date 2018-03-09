
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.applet.Applet;

public class carPanel extends Applet
{

    private JButton forward;
    private JButton back;
    private JButton left;
    private JButton right;
    private JButton stop;

    public carPanel()
    {
       setLayout(new BorderLayout());
       
       forward = new JButton("forward"); 
       forwardButtonListener listener1 = new forwardButtonListener(this);
       forward.addActionListener(listener1);
       add(forward,BorderLayout.NORTH);
       forward.setBackground(Color.GRAY);
       
       back = new JButton("back"); 
       backButtonListener listener2 = new backButtonListener(this);
       back.addActionListener(listener2);
       add(back,BorderLayout.SOUTH);
       back.setBackground(Color.GRAY);
       
       left = new JButton("left"); 
       leftButtonListener listener3 = new leftButtonListener(this);
       left.addActionListener(listener3);
       add(left,BorderLayout.WEST);
       left.setBackground(Color.GRAY);
       
       
       right = new JButton("right"); 
       rightButtonListener listener4 = new rightButtonListener(this);
       right.addActionListener(listener4);
       add(right,BorderLayout.EAST);
       right.setBackground(Color.GRAY);

       stop = new JButton("stop"); 
       stopButtonListener listener5 = new stopButtonListener(this);
       stop.addActionListener(listener5);
       add(stop,BorderLayout.CENTER);
       stop.setBackground(Color.GRAY);
   
    }
    
 
}