import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import java.util.ArrayList;

import javax.swing.JPanel;

public class PointTemp extends JPanel{
	private ArrayList<Point> coords;
	private int p_size = 10;
	private Color p_color;
	
	public PointTemp(){
		coords = new ArrayList<Point>();
		p_color = Color.black;

		
		addMouseMotionListener(new MouseMotionAdapter(){
			public void mouseDragged(MouseEvent a){
				Color n_color = p_color;
				int s = p_size;
				coords.add(new Point(a.getX(), a.getY(), s, n_color));
				repaint();
			}
			});
		addMouseListener(new MouseAdapter(){
			public void mousePressed(MouseEvent a){
				Color n_color = p_color;
				int s = p_size;
				coords.add(new Point(a.getX(), a.getY(), s, n_color));
				repaint();
			}
			});
	}
	@Override
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		for (Point coord: coords){
			coord.draw(g);
		}
	}
	public void black(){
		p_color = Color.black;
	}
	public void gray(){
		p_color = Color.gray;
	}
	public void green(){
		p_color = Color.green;
	}
	public void yellow(){
		p_color = Color.yellow;
	}
	public void five(){
		p_size = 5;
	}
	public void ten(){
		p_size = 10;
	}
	public void twenty(){
		p_size = 20;
	}
	public void clear(){
		coords = new ArrayList<Point>();
		repaint();

			}
	}
