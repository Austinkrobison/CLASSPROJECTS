import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Client {
	public static void main(String[] args){
		System.out.println("client active");
		
		Socket s  = null;
		ObjectOutputStream outStream = null;
		ObjectInputStream inStream = null;
		ArrayList<Integer> outList = new ArrayList<Integer>(makeServerBoundList());
		
		try{
			InetAddress addy = InetAddress.getLocalHost();
			s = new Socket(addy, 1377);
			
			outStream = new ObjectOutputStream(s.getOutputStream());
			System.out.println("Sent: " + outList);
			outStream.writeObject(outList);
			outStream.flush();

			inStream = new ObjectInputStream(s.getInputStream());
			
			@SuppressWarnings("unchecked")
			ArrayList<Integer> tBA = (ArrayList<Integer>) inStream.readObject();

			System.out.println("Recieved: " + tBA);
			
			inStream.close();
			outStream.close();
			s.close();
		}catch(IOException | ClassNotFoundException err){
			err.printStackTrace();
		}
	}
	public static ArrayList<Integer> makeServerBoundList(){
		ArrayList<Integer> list = new ArrayList<Integer>();
		System.out.println("enter an integer or ! to quit");

		Scanner tbScanned = new Scanner(System.in);
		try{
		while(tbScanned.hasNext()){

			int num = tbScanned.nextInt();
				
			String st = tbScanned.nextLine();
				
			if(num <= 0| !st.equals('!')){
				System.out.println("please enter an integer or ! to quit");
			}if(st.equals('!')){
				 break;
			}else{
				list.add(num);	
			}
			}
		}catch(InputMismatchException err){
			tbScanned.close();
			return list;
		
		}
		tbScanned.close();
		return list;
		
	}
}