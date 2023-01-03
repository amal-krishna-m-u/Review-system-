<?php
  include('config.php');
   session_start();
  

   if($_SERVER["REQUEST_METHOD"] == "POST")
    {
      // username and password sent from form 
      
      $myemail = mysqli_real_escape_string($conn,$_POST['email']);
      $mypassword = mysqli_real_escape_string($conn,$_POST['password']); 
      
      $sql = "SELECT * FROM User_details WHERE  email= '$myemail'";
      $result = mysqli_query($conn,$sql);
      $count = mysqli_num_rows($result);
      if($count == 1)
      {
        $row = mysqli_fetch_assoc($result);
        $upass = $row['password2'];
        

        if(md5($mypassword) == $upass) {
           $admin = $row['email'];
           $a=1;
           $un = $row['user_name'];
           $_SESSION['login_user'] = $un;
           if($admin == 'admin@gmail.com')
         { header('location:http://'.$_SERVER['HTTP_HOST'].'/Admin_dashboard/sudo.php');
            exit();
         }
           else if($a==1)
           {
            header('location:http://'.$_SERVER['HTTP_HOST'].'/Dashboard/dashboard.php');
         exit();

        }
        else
        {
          echo"wrong password";
          echo '<br> <br> <button class="button"name="prev" id="prev" onclick="window.history.back()">PREV</button>';
         exit();
        }

       }

        else
        {
       
         echo '<script type="text/JavaScript">
            if(!alert("Invalid User details")) document.location = "http://'.$_SERVER['HTTP_HOST'].'/Login_page/index.php";
            </script>';
     
         
        }
       }
             else{
   
   
            echo '<script type="text/JavaScript">
             if(!alert("Invalid User details")) document.location = "http://'.$_SERVER['HTTP_HOST'].'/Login_page/index.php";
           </script>';

           }
      } 
     else{
   
      echo '<script type="text/JavaScript">
      if(!alert("Invalid Method")) document.location = "http://'.$_SERVER['HTTP_HOST'].'/Login_page/index.php";
      </script>';
}
?>
