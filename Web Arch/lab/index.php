

<html>
    <head>
        <meta charset="UTF-8">
        <title> Laptop_Store </title>
    </head>
    <body>
        <h1> Welcome to Online Laptop Store</h1>
        <h4> The products are listed below</h4>
        <br>
           
 <?php
        $con = mysqli_connect("localhost","root","subhendu","world");
        
        if(mysqli_connect_errno())
        {
            echo "DATABASE ERROR";
        }

        $query="";
      
        $result=mysqli_query($con, $query);

        echo"<table border =2>
        <tr>
        <th> Name</th>
        <th> CountryCode</th>
        <th> District</th>
        <th> Population</th>
        </tr>";
        if (mysqli_num_rows($result)>1)
        {
            while($row=mysqli_fetch_assoc($result))
            {
                echo'<tr>';
                echo '<td>'.$row['Name'].'</td>';
                echo '<td>'.$row['CountryCode'].'</td>';
                echo '<td>'.$row['District'].'</td>';
                echo '<td>'.$row['Population'].'</td>';
                echo'<tr>';
            }
        }?>
    </body>
</html>