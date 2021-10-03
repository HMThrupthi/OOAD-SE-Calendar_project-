<?php      
    include('connection.php');  
    $emailid = $_POST['email'];  
    $password = $_POST['pass'];  
      
        //to prevent from mysqli injection  
        $emailid = stripcslashes($emailid);  
        $password = stripcslashes($password);  
        $emailid = mysqli_real_escape_string($con, $emailid);  
        $password = mysqli_real_escape_string($con, $password);  
      
        $sql = "select *from login where emailid = '$emailid' and password = '$password'";  
        $result = mysqli_query($con, $sql);  
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);  
        $count = mysqli_num_rows($result);  
          
        if($count == 1){  
            echo "<h1><center> Login successful </center></h1>";  
        }  
        else{  
            echo "<h1> Login failed. Invalid username or password.</h1>";  
        }     
?>