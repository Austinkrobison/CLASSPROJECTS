import java.util.LinkedList;
import java.util.Random;



public class LLPC  {

	private static LinkedList<String> LL = new LinkedList<String>();
	public static int maxNum = 1000;
	public static int masterCountC;
	public static int masterCountP;

	public static Object MuteX = new Object();
	public static Object MuteY = new Object();

	
	private static Random tba = new Random();

	
	static class Producer implements Runnable{

		private final String _PID;
		private int _Pprogress;
		private static boolean inProgP = true;

		
		public Producer(String PID){
			_PID = PID;
		}
		public void run(){
			while(inProgP){
				synchronized(MuteX){

			
			try{
				for(int i = 0; i < LLPC.maxNum; i++){
					
					LLPC.tba.nextDouble();
					String Fadd = LLPC.tba.toString();
					LLPC.LL.add(Fadd);
					
					_Pprogress++;
					masterCountP++;

					if((_Pprogress % 100 == 0)){
						System.out.println(_PID + " Produced " + _Pprogress);
					}
					try{
						notifyAll();
						wait();
					}catch(InterruptedException e){
					
					}
				}
			}catch(Exception E){
			}
			}if(masterCountP == maxNum-1){
				inProgP = false;
			}	
	
	}
	}
	}
	
	
	static class Consumer implements Runnable{
		private final String _CID;
		private int _Cprogress;
		private static boolean inProgC = true;

		public Consumer(String CID){
			_CID = CID;
		}

		public void run(){
		
				while(inProgC){
					synchronized(MuteX){
					try{
			
						if(LLPC.LL.peekFirst() != null){
							LL.removeFirst();
							_Cprogress++;
							masterCountC++;
							if((_Cprogress)%100 == 0){
								System.out.println(_CID + " Consumed " + (_Cprogress));
							}
						}else{

							}
						if(masterCountC == maxNum-1){
						inProgC = false;
						}
						
					}finally{
						
					}
			}
		}
	}
	}
		
	public static void main(String args[]) throws InterruptedException{
			LLPC.Producer producer1 = new LLPC.Producer("Producer 1");
			Thread t1 = new Thread(producer1);
			
			LLPC.Producer producer2 = new LLPC.Producer("Producer 2");

			
			LLPC.Consumer consumer1 = new LLPC.Consumer("Consumer 1");
			
			LLPC.Consumer consumer2 = new LLPC.Consumer("Consumer 2");

			Thread t2 = new Thread(consumer1);
			Thread t3 = new Thread(consumer2);

			Thread t4 = new Thread(producer2);
			
			t1.start();
			t2.start();
			t3.start();
			t4.start();
			
			t1.join();
			t4.join();
			t2.join();
			t3.join();

			System.out.println("Summary: ");
			System.out.println(producer1._PID + " Produced "+ (producer1._Pprogress));
			System.out.println(producer2._PID + " Produced "+ producer2._Pprogress);

			System.out.println(consumer1._CID + " Consumed "+ (consumer1._Cprogress));
			System.out.println(consumer2._CID + " Consumed "+ consumer2._Cprogress);
		}
}

