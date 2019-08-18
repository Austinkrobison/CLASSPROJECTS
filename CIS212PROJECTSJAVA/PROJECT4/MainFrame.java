import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class MainFrame extends JFrame{
	private final PointTemp template;
	public MainFrame(){
		setLayout(new BorderLayout());
		template = new PointTemp();
		template.setPreferredSize(new Dimension(600,600));
		add(template, BorderLayout.CENTER);
		
		
		// COLOR BUTTONS
		JButton blackButton = new JButton("Black");
		blackButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.black();
			}
		});
		JButton greenButton = new JButton("Green");
		greenButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.green();
			}
		});
		JButton yellowButton = new JButton("Yellow");
		yellowButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.yellow();
			}
		});
		JButton greyButton = new JButton("Gray");
		greyButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.gray();
			}
		});
		// SIZE BUTTONS
		JButton fiveButton = new JButton("Size 5");
		fiveButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.five();
			}
		});
		JButton tenButton = new JButton("Size 10");
		tenButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.ten();
			}
		});
		JButton twentyButton = new JButton("Size 20");
		twentyButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.twenty();
			}
		});
		JButton clearButton = new JButton("Clear");
		clearButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent a){
				template.clear();
			}
		});
		JPanel buttonPanel = new JPanel(new GridLayout(2,4));
		buttonPanel.add(blackButton);
		buttonPanel.add(greenButton);
		buttonPanel.add(greyButton);
		buttonPanel.add(yellowButton);
		buttonPanel.add(fiveButton);
		buttonPanel.add(tenButton);
		buttonPanel.add(twentyButton);
		buttonPanel.add(clearButton);
		add(buttonPanel, BorderLayout.WEST);

	}
	
}
