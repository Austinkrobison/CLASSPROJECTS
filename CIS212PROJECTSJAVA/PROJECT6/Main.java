import java.util.HashSet;
import java.util.Set;
public class Main {
	public static void main(String[] a){
		OccurrenceSet<Integer> oSet = new OccurrenceSet<Integer>();
		oSet.add(1);
		oSet.add(3);
		oSet.add(5);
		oSet.add(5);
		oSet.add(3);
		oSet.add(3);
		System.out.println(oSet);
		
		OccurrenceSet<String> sSet = new OccurrenceSet<String>();
		sSet.add("wow");
		sSet.add("wow");
		sSet.add("this");
		sSet.add("is neat");
		sSet.add("is neat");
		sSet.add("is neat");

		System.out.println(sSet);


	}
}
