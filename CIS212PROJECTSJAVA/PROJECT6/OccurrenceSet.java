import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

public class OccurrenceSet<T> implements Set<T> {
	HashMap<T, Integer> info = new HashMap<T, Integer>();
	
	@Override
	public boolean add(T tba){
		Integer added = info.get(tba);
		if(added == null){
			info.put(tba, 1);
		}else{
			info.put(tba, added+1);
		}
		return info.keySet().contains(tba);
	}
	
	@Override
	public boolean addAll(Collection<? extends T> group){
		Integer size1 = info.size();
		for(T index: group){
			add(index);
		}
		Integer size2 = info.size();
		if(size1 == size2){
			return false;
		}
		return true;
	}
	
	@Override
	public boolean remove(Object tbr){
		Integer toBeRemoved = info.get(tbr);
	 	if( toBeRemoved != null){
	 		info.remove(tbr);
	 	}
	 	return !(info.keySet().contains(tbr));
	}
	
	@Override
	public boolean removeAll(Collection<?> group){
		Integer size1 = info.size();
		for(Object index: group){
			info.remove(index);
		}
		Integer size2 = info.size();
		if(size1 != size2){
			return true;
		}
		return false;
	}
	
	@Override
	public boolean retainAll(Collection<?> group){
		Integer size1 = info.size();
		HashMap<T, Integer> newInfo = new HashMap<T, Integer>();
		for(Object index: group){
			if(info.keySet().contains(index)){
				newInfo.put((T) index ,	info.get(index));
			}
		}
		Integer size2 = newInfo.size();
		info = newInfo;
		if(size1 != size2){
			return true;
		}
		return false;
	}
	
	@Override 
	public boolean contains(Object find){
		return info.keySet().contains(find);
	}
	
	@Override
	public boolean containsAll(Collection<?> findGroup){
		return info.keySet().containsAll(findGroup);
	}
	
	@Override
	public int size(){
		return info.size();
	}
	
	@Override
	public void clear(){
		info.clear();
	}
	
	@Override
	public boolean isEmpty(){
		if(info.isEmpty()){
			return true;
		}
		return false;
	}
	
	@Override
	public Iterator<T> iterator(){
		Set<Map.Entry<T, Integer>> list = info.entrySet();
		ArrayList<Map.Entry<T, Integer>> nextList = new ArrayList<Map.Entry<T,Integer>>(list);
		ArrayList<T> sorted = new ArrayList<T>();
		
		Collections.sort(nextList, new Comparator<Map.Entry<T,Integer>>(){
			public int compare(Map.Entry<T, Integer> x, Map.Entry<T, Integer> y){
				return x.getValue().compareTo(y.getValue());
			}
		});
		for(Map.Entry<T, Integer> x: nextList){
			sorted.add(x.getKey());
		}
		return sorted.iterator();
	}
	
	@Override
	public String toString(){

		return info.toString();
	}
	
	@SuppressWarnings({ "unchecked", "hiding" })
	@Override
	public <T> T[] toArray(T[] arg) {
		Object[] retList = (T[]) info.keySet().toArray();
		int i = 0;
		for(Object k: info.keySet()){
			retList[i] = k;
			i++;
		}
	return (T[]) retList;
	}

	@Override
	public Object[] toArray() {
		// TODO Auto-generated method stub
		return null;
	}

}

