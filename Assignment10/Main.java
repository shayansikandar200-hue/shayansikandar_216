import javax.swing.*;
import java.awt.*;
import java.io.*;

public class Main {

    // Text area where user types
    static JTextArea textArea = new JTextArea();

    // Keeps track of currently opened file
    static File currentFile = null;

    public static void main(String[] args) {

        // Create main window
        JFrame frame = new JFrame("Text Editor");
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Add text area with scroll
        frame.add(new JScrollPane(textArea));

        // Create menu bar
        JMenuBar menuBar = new JMenuBar();

        // ================= FILE MENU =================
        JMenu fileMenu = new JMenu("File");

        JMenuItem open = new JMenuItem("Open");
        JMenuItem save = new JMenuItem("Save");
        JMenuItem saveAs = new JMenuItem("Save As");

        fileMenu.add(open);
        fileMenu.add(save);
        fileMenu.add(saveAs);

        // ================= FORMAT MENU =================
        JMenu formatMenu = new JMenu("Format");
        JMenuItem color = new JMenuItem("Change Color");

        formatMenu.add(color);

        // Add menus
        menuBar.add(fileMenu);
        menuBar.add(formatMenu);
        frame.setJMenuBar(menuBar);

        // ================= OPEN =================
        open.addActionListener(e -> {
            JFileChooser chooser = new JFileChooser();
            if (chooser.showOpenDialog(frame) == JFileChooser.APPROVE_OPTION) {
                currentFile = chooser.getSelectedFile();
                try (BufferedReader reader = new BufferedReader(new FileReader(currentFile))) {
                    textArea.read(reader, null);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        });

        // ================= SAVE =================
        save.addActionListener(e -> {
            try {
                if (currentFile == null) {
                    JFileChooser chooser = new JFileChooser();
                    if (chooser.showSaveDialog(frame) == JFileChooser.APPROVE_OPTION) {
                        currentFile = chooser.getSelectedFile();
                    }
                }

                if (currentFile != null) {
                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(currentFile))) {
                        textArea.write(writer);
                    }
                }
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        });

        // ================= SAVE AS =================
        saveAs.addActionListener(e -> {
            JFileChooser chooser = new JFileChooser();
            if (chooser.showSaveDialog(frame) == JFileChooser.APPROVE_OPTION) {
                currentFile = chooser.getSelectedFile();
                try (BufferedWriter writer = new BufferedWriter(new FileWriter(currentFile))) {
                    textArea.write(writer);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        });

        // ================= CHANGE COLOR =================
        color.addActionListener(e -> {
            Color c = JColorChooser.showDialog(frame, "Choose Color", Color.BLACK);
            if (c != null) {
                textArea.setForeground(c);
            }
        });

        // Show window
        frame.setVisible(true);
    }
}