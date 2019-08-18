import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class Server {
	public static void main(String[] args){
		System.out.println("...\nserver initialized");
		
		ServerSocket sSock = null;
		Socket s = null;
		ObjectOutputStream oStream = null;
		ObjectInputStream iStream = null;
		
		try{
			sSock = new ServerSocket(1377);
			System.out.println("server socket created");
			
			s = sSock.accept();
			
			oStream = new ObjectOutputStream(s.getOutputStream());
			oStream.flush();
			iStream = new ObjectInputStream(s.getInputStream());
			
			
			@SuppressWarnings("unchecked")
			ArrayList<Integer> inc = (ArrayList<Integer>) iStream.readObject();
			
			ArrayList<Integer> retList = new ArrayList<Integer>(makeList(inc));
			
			oStream.writeObject(retList);
			oStream.flush();
			
			iStream.close();
			oStream.close();
			sSock.close();
			
		}catch(IOException | ClassNotFoundException err){
			err.printStackTrace();
			
		}finally{
			try{
				if(sSock != null){
					sSock.close();
					
				}if(s != null){
					s.close();
					
				}if(iStream != null){
					iStream.close();
					
				}if(oStream != null){
					oStream.close();
				}
				
			}catch(IOException err){
				err.printStackTrace();
			}
		}
		System.out.println("server done");
	}
	
	public static boolean isPrime(int n){
		if(n == 2){
			return true;
		}
		if(n%2 == 0| n == 1){
			return false;
		}
		for(int i=3; i*i<=n; i+= 2){
			if(n%i == 0){
				return false;
			}
		}
		return true;
	}
	public static ArrayList<Integer> makeList(ArrayList<Integer> list){
		ArrayList<Integer> rList = new ArrayList<Integer>(1);
		for(int i: list){
			if(isPrime(i)){
				rList.add(i);
			}
		}
	
	return rList;
	}
}
