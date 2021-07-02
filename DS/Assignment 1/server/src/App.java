
import java.io.*;
import java.net.*;

class Operation implements Serializable {

    String operator;
    int operand1;
    int operand2;

    // Constructor
    public Operation() {
    }
}

public class App implements java.io.Serializable {

    // Static ServerSocket variable
    private static ServerSocket server;
    // Socket server port on which it will listen
    private static int port = 5555;

    public static void main(String args[]) throws IOException, ClassNotFoundException {
        // Creating the socket server object
        server = new ServerSocket(port);
        System.out.println("listening on port " + port);

        // Creating socket and waiting for client connection
        Socket socket = server.accept();
        // Read from socket to ObjectInputStream object
        ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
        // Create ObjectOutputStream object
        ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
        String operator;
        int a, b, c = 0;
        // Server keeps listening indefinitely until it receives 'exit'
        while (true) {
            // Create new Operation object to receive operands and operator from client
            Operation opr = new Operation();
            // Read new values from client side
            opr = (Operation) ois.readObject();
            a = opr.operand1;
            b = opr.operand2;
            operator = opr.operator;
            if (operator.equals("exit"))
                break;
            // Carry out calculation
            switch (operator) {
                case "add":
                    c = a + b;
                    break;
                case "subtract":
                    c = a - b;
                    break;
                case "multiply":
                    c = a * b;
                    break;
                case "divide":
                    c = a / b;
                    break;
            }
            // Send back result after calculating
            oos.writeObject("Answer is : " + c);
        }
        // Closing resources
        server.close();
        ois.close();
        oos.close();
    }
}