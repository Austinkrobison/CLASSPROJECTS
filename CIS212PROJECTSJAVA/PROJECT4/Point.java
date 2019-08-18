import java.awt.Graphics;
import java.awt.Color;
public class Point {
	
	private final int x_coord;
	private final int y_coord;
	public int point_size;
	public Color point_color;
	
	public Point(int x, int y, int size, Color color){
		x_coord = x;
		y_coord = y;
		point_size = size;
		point_color = color;
		
	}
	public int getX(){
		return x_coord;
	}
	public int getY(){
		return y_coord;
	}
	public int getSize(){
		return point_size;
	}
	public void draw(Graphics g){
		g.setColor(point_color);
		g.fillOval(x_coord, y_coord, point_size, point_size);
	}
}

