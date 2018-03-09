import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.net.*;
import java.net.Socket;

public class forwardButtonListener implements ActionListener
{
    private carPanel a;

    public forwardButtonListener(carPanel a)
    {
        this.a=a;
    }
   
    public void actionPerformed(ActionEvent event)
    {
         
        JButton button = (JButton) event.getSource();

        
        try{
          
          DatagramSocket clientSocket = new DatagramSocket();
          InetAddress IPAddress = InetAddress.getByName("192.168.0.17");
          byte[] sendData = new byte[1024];
          byte[] receiveData = new byte[1024];
          String buff = "w";
          sendData = buff.getBytes();

          DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 31500);
          
          clientSocket.send(sendPacket);
          System.out.println("forward");
     
       }catch(Exception e){
		   System.err.println(e);
	   }
	   
    }
}
