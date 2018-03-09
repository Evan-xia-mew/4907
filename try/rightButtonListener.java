import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.net.*;


public class rightButtonListener implements ActionListener
{
    private carPanel a;

    public rightButtonListener(carPanel a)
    {
        this.a=a;
    }
   
    public void actionPerformed(ActionEvent event)
    {
         
        JButton button = (JButton) event.getSource();


        try{
          
          DatagramSocket clientSocket = new DatagramSocket();
          InetAddress IPAddress = InetAddress.getByName("192.168.0.20");
          byte[] sendData = new byte[1024];
          byte[] receiveData = new byte[1024];
          String buff = "d";
          sendData = buff.getBytes();
          
          DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 42000);
          
          clientSocket.send(sendPacket);
          System.out.println("right");
       
       }catch(Exception e){
		   System.err.println(e);
	   }
    }
}
