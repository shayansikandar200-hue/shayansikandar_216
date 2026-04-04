// Assignment 9 - Text Editor Application
// Developed using Java Swing
// No external resources used other than course material
import javax.swing.*;
import java.awt.event.*;

public class TextEditor {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Text Editor");
        JTextArea textArea = new JTextArea();

        // ===== MENU BAR =====
        JMenuBar menuBar = new JMenuBar();

        // ===== FILE MENU =====
        JMenu fileMenu = new JMenu("File");
        JMenuItem newItem = new JMenuItem("New");
        JMenuItem exitItem = new JMenuItem("Exit");

        newItem.addActionListener(e -> textArea.setText(""));
        exitItem.addActionListener(e -> System.exit(0));

        fileMenu.add(newItem);
        fileMenu.add(exitItem);

        // ===== EDIT MENU =====
        JMenu editMenu = new JMenu("Edit");
        JMenuItem cutItem = new JMenuItem("Cut");
        JMenuItem copyItem = new JMenuItem("Copy");
        JMenuItem pasteItem = new JMenuItem("Paste");

        cutItem.addActionListener(e -> textArea.cut());
        copyItem.addActionListener(e -> textArea.copy());
        pasteItem.addActionListener(e -> textArea.paste());

        editMenu.add(cutItem);
        editMenu.add(copyItem);
        editMenu.add(pasteItem);

        // Add menus to bar
        menuBar.add(fileMenu);
        menuBar.add(editMenu);
        frame.setJMenuBar(menuBar);

        // ===== RIGHT-CLICK CONTEXT MENU =====
        JPopupMenu popupMenu = new JPopupMenu();

        JMenuItem cutPopup = new JMenuItem("Cut");
        JMenuItem copyPopup = new JMenuItem("Copy");
        JMenuItem pastePopup = new JMenuItem("Paste");

        cutPopup.addActionListener(e -> textArea.cut());
        copyPopup.addActionListener(e -> textArea.copy());
        pastePopup.addActionListener(e -> textArea.paste());

        popupMenu.add(cutPopup);
        popupMenu.add(copyPopup);
        popupMenu.add(pastePopup);

        textArea.setComponentPopupMenu(popupMenu);

        // ===== FRAME SETTINGS =====
        frame.add(new JScrollPane(textArea));
        frame.setSize(500, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}