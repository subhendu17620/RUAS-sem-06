import java.rmi.*;

public class Server {
    public static void main(String argv[]) {
        try {
            System.out.println("Starting Server");

            Naming.rebind("server_1", new ServerFunc());

        } catch (Exception e) {
            System.out.println("Problem occured while starting the server\n" + e.toString());
        }
    }
}
