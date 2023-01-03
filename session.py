<?php
   include('config.php');
   session_start();
   
   $user_check = $_SESSION['login_user'];
   
   $ses_sql = mysqli_query($conn,"select * from User_details where user_name = '$user_check' ");
   
   $row = mysqli_fetch_array($ses_sql,MYSQLI_ASSOC);
  
    $_SESSION['login_session'] = $row['user_id'];
   
   if(!isset($_SESSION['login_user'])){
      header("location:index.php");
      die();
   }
?>
