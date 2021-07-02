import java.io.*;
import java.net.*;
import java.util.Scanner;

class Operation implements Serializable {

    String operator;
    int operand1;
    int operand2;

    public Operation() {
    }

}

public class App implements Serializable {

    public static void main(String[] args)
            throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException {

        // Open the socket connection
        Socket socket = new Socket("localhost", 5555);
        // Create ObjectOutputStream object
        ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
        // Read from socket to ObjectInputStream object
        ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
        // Creating scanner object to read values from terminal
        Scanner sc = new Scanner(System.in);
        int a, b;
        String c;
        // Keep running until 'exit' call from user
        while (true) {
            // Declare new Operation object to send operands and operator to server
            Operation opr = new Operation();
            System.out.println("==================");

            System.out.print("Enter first operand : ");
            a = sc.nextInt();
            System.out.print("Enter second operand : ");
            b = sc.nextInt();
            sc.nextLine();
            System.out.print("Enter operation (add,subtract,multiply,divide,exit) : ");
            c = sc.nextLine();
            if (c.equals("exit"))
                break;
            opr.operand1 = a;
            opr.operand2 = b;
            opr.operator = c;
            // Send Operation object to server side for calculation
            oos.writeObject(opr);
            // Receive response back from server after calculation
            System.out.println("\nServer response :\n" + ois.readObject());
        }
        // Closing resources
        sc.close();
        socket.close();
        ois.close();
        oos.close();
    }
}