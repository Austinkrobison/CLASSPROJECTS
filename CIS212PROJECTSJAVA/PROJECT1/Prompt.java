
import java.util.Scanner;

public class Prompt{
	public static void main(String[] args){
			
		boolean active = true;
		Scanner sc = new Scanner(System.in);
		int counter = 0;
			
		do
		{
			System.out.println(" Enter a positive integer (-3 to print, -2 to reset, -1 to quit)" );
			int i = sc.nextInt();
			if (i == -1){
				active = false;
				
			} else if (i == -2){
				counter = 0;
					
			} else if (i == -3){
				System.out.println("Sum: " + counter);
				
			} else if (i > 0){
				counter += i;
			}
			
		}while(active);
		sc.close();
		
	}
}

