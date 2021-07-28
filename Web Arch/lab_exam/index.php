

<html>
    <head>
        <meta charset="UTF-8">
        <title> Online Clothing Store </title>
    </head>
    <body>
        <h1> Welcome to Online Clothing Store</h1>

<br/>
        <h4> The items are listed below</h4>
           
 <?php
        // connecting to mysqli client using username and password
        $con = mysqli_connect("localhost","root","subhendu","online_clothing");
        
        // handling error for database connection
        if(mysqli_connect_errno())
        {
            echo "DATABASE ERROR";
        }

        // query to fetch items from the database whose cost is less than 879 
        $query="select * from items where cost < 879";

        // fetching the result of the query
        $result=mysqli_query($con,$query);

        // displaying the result
        echo"<table border=3>
        <tr>
        <th> ID</th>
        <th> Name</th>
        <th> Description</th>
        <th> Cost (in ₹)</th>
        </tr>";
        if (mysqli_num_rows($result)>1)
        {
            while($row=mysqli_fetch_assoc($result))
            {
                echo'<tr>';
                echo '<td>'.$row['item_id'].'</td>';
                echo '<td>'.$row['item_name'].'</td>';
                echo '<td>'.$row['description'].'</td>';
                echo '<td>'.$row['cost'].'</td>';
                echo'<tr>';
            }
        }?>
        
    </body>
</html>