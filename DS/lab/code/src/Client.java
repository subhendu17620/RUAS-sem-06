import java.rmi.*;
import java.util.Scanner;

public class Client {
    public Client() {

        System.out.println("Starting the client");

        // trying to access the Registry server to retrieve the inteface
        try {
            msi = (InterfaceServerFunc) Naming.lookup("rmi://127.0.0.1/server_1");
        } catch (Exception e) {
            System.out.println("Client boot Failed\n" + e);
            System.out.println(
                    "Make sure that both the Registry server and the server application are running correctly");
            System.exit(0);
        }
    }

    public static void main(String[] argv) {

        Client c = new Client();
        try {

            Scanner sc = new Scanner(System.in);
            int a, b;

            System.out.print("Enter first operand : ");
            a = sc.nextInt();
            System.out.print("Enter second operand : ");
            b = sc.nextInt();

            System.out.println("Add: " + c.msi.sum(a, b));
            System.out.println("Subtract: " + c.msi.subtract(a, b));
            System.out.println("Multiply: " + c.msi.multiply(a, b));
            System.out.println("Divide: " + c.msi.divide(a, b));

            sc.close();

        } catch (Exception e) {
            System.out.println("Error occured during remote calls :" + e);
        }

    }

    private InterfaceServerFunc msi; // A interface to the remote object
}