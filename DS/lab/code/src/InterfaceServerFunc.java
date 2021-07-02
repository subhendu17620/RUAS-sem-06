import java.rmi.*;

public interface InterfaceServerFunc extends Remote {
    public double sum(double a, double b) throws RemoteException;

    public double subtract(double a, double b) throws RemoteException;

    public double multiply(double a, double b) throws RemoteException;

    public double divide(double a, double b) throws RemoteException;
}
