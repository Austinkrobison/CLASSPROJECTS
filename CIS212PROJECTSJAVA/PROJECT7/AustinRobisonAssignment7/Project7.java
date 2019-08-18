import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

public class Project7 {
	private static LinkedBlockingQueue<String> bQu = new LinkedBlockingQueue<String>(100);
	public static int maxNum = 1000;
	public static int masterCount = 0;
	public static boolean inProg = true;
	private static Object MuteX = new Object();
	
	
	static class Producer implements Runnable{

		private final String _PID;
		public int _Pprogress;
		
		public Producer(String PID){
			_PID = PID;
			_Pprogress = 0;
		}
		public void run(){
			Random tba = new Random();
			//synchronized(MuteX){
			try{
				for(int i = 0; i< Project7.maxNum; i++){
					tba.nextDouble();
					String Fadd = tba.toString();
					Project7.bQu.put(Fadd);
					if((i % 100 == 0)&& i != 0){
						System.out.println(_PID + " Produced " + (i));
					}
				}
				}catch(InterruptedException e){
					System.out.println(_PID + e);
				}
			//}
		
	}
	}
	
	static class Consumer implements Runnable{
		private final String _CID;

		public int _Cprogress;
		
		public Consumer(String CID){
			_CID = CID;
			_Cprogress = 0;
		}

		public void run(){

			//synchronized(MuteX){
				while(inProg){
					try{
					if(Project7.bQu.poll((int)(Math.random()*10), TimeUnit.MILLISECONDS) != null){
						_Cprogress++;
						masterCount++;
						if((_Cprogress)%100 == 0){
							System.out.println(_CID + " Consumed " + (_Cprogress));
						}
						
					}if(masterCount == maxNum){
						inProg= false;
					}
				}catch(Exception e){
					e.printStackTrace();
				}
				}


		//}
	}
	}
		
	public static void main(String args[]) throws InterruptedException{
			Project7.Producer producer1 = new Project7.Producer("Producer 1");
			Thread t1 = new Thread(producer1);
			
			Project7.Consumer consumer1 = new Project7.Consumer("Consumer 1");
			
			Project7.Consumer consumer2 = new Project7.Consumer("Consumer 2");

			Thread t2 = new Thread(consumer1);
			Thread t3 = new Thread(consumer2);

			t1.start();
			t2.start();
			t3.start();
					
			t1.join();
			t2.join();
			t3.join();
	
			//ExecutorService executor = Executors.newCachedThreadPool();
			//executor.execute(producer1);
			//executor.execute(consumer1);
			//executor.execute(consumer2);
			//executor.shutdown();
			
			//if(!t2.isAlive() && !t3.isAlive()){
				System.out.println("Summary: ");
				System.out.println(producer1._PID + " Produced "+ maxNum);
				System.out.println(consumer1._CID + " Consumed "+ consumer1._Cprogress);
				System.out.println(consumer2._CID + " Consumed "+ consumer2._Cprogress);
			//}	
		}
}
