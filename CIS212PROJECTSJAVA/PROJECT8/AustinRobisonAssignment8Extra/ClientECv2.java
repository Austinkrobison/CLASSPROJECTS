import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Random;

public class ClientECv2 {
	static BufferedReader tbRead = new BufferedReader(new InputStreamReader(System.in));
	static boolean active = false; 
	private static int activeCount = 0;


	public static void main(String[] args){
		System.out.println("client active");
		System.out.println("enter ! to start or stop, # to quit");

		//String input = tbScanned.nextLine();
		Socket s  = null;
		ObjectOutputStream outStream = null;
		ObjectInputStream inStream = null;


		
		
		try{
			InetAddress addy = InetAddress.getLocalHost();
			s = new Socket(addy, 1377);
			outStream = new ObjectOutputStream(s.getOutputStream());
			inStream = new ObjectInputStream(s.getInputStream());
			String inputP = tbRead.readLine();

			while(true){

				if(inputP.equals("!")){
					activeCount++;
					inputP = "ERROR";
				}
				if(inputP.equals("#")){
					inStream.close();
					outStream.close();
					s.close();
					break;
				}
				if(activeCount % 2 == 0){
					inputP = tbRead.readLine();
				}
				
				ArrayList<Integer> outList = new ArrayList<Integer>(assembleList());
				if(!inputP.equals("#")){
					System.out.println("Sent: " + outList);
					outStream.writeObject(outList);
					outStream.flush();

			
					@SuppressWarnings("unchecked")
					ArrayList<Integer> tBA = (ArrayList<Integer>) inStream.readObject();

					System.out.println("Recieved: " + tBA);	
				}
				Thread.sleep(1000);



				long startTime = System.currentTimeMillis();
				
				while((System.currentTimeMillis()- startTime < 1000) && tbRead.ready()){
				}if(tbRead.ready()){
					inputP = tbRead.readLine();
					if(inputP.equals("#")){
						System.out.println("Client exiting...");
						inStream.close();
						outStream.close();
						s.close();
						break;
					}
				}else{
				}

				
			}
				inStream.close();
				outStream.close();
				s.close();
		
		
		}catch(IOException | ClassNotFoundException | InterruptedException err){
			err.printStackTrace();
		}
	}
	

	public static ArrayList<Integer> assembleList(){
		ArrayList<Integer> lInstance = new ArrayList<Integer>(); 

		for(int i =0; i<5; i++){
			Random random = new Random();
			int instanceVal = (random.nextInt(97) +2);
			//System.out.println(instanceVal);
			lInstance.add(i, instanceVal);
		}
		return lInstance;
	}

}

