import java.rmi.*;
import java.rmi.server.*;

public class ServerFunc extends UnicastRemoteObject implements InterfaceServerFunc {

    public ServerFunc() throws RemoteException {
        System.out.println("New Server Initiated...");
    }

    public double sum(double a, double b) throws RemoteException {
        return a + b;
    }

    public double subtract(double a, double b) throws RemoteException {
        return a - b;
    }

    public double multiply(double a, double b) throws RemoteException {
        return a * b;
    }

    public double divide(double a, double b) throws RemoteException {
        return a / b;
    }
}
