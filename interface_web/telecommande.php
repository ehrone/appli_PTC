<!DOCTYPE HTML>
    <html>
        <head>
            <title> AranaCorp </title>
            <meta http-equiv='content-type' content='text/html; charset=UTF-8'>
            <meta name='apple-mobile-web-app-capable' content='yes' />
            <meta name='apple-mobile-web-app-status-bar-style' content='black-translucent' />
            <meta http-equiv='refresh' content='10'>
            <link rel="stylesheet" href='rpi_style.css'/>
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        </head>
        
        <body bgcolor = '#70706F'> 
           <?php

           function write_command($cmd)
           {
              $file ="/var/www/html/Commandes.txt";
              $fileopen=(fopen($file,'w'));
              fwrite($fileopen,$cmd);
              fclose($fileopen);

           }
              if( isset($_POST['up']) )
              {
               
                write_command("up");
              }

              if( isset($_POST['down']) )
              {
               
                write_command("down");
              }

              if( isset($_POST['right']) )
              {
               
                write_command("right");
              }
              if( isset($_POST['left']) )
              {
               
                write_command("left");
              }
  

             ?>
            <hr/><hr>
            <h1 style='color : #3AAA35;'><center> Telecommande </center></h1>
            <hr/><hr>
            <br><br>
            <h2><center><p>Equipe D 3</p></center></h2>
            <br><br><h2> Commandes </h2>
            <div id='btnContainer'>
              <form method="post">
                  <center>
                  <input type="submit" name='up' value="up">
                  </center>
                  <center>
                    <input type="submit" name='down' value="down">
                  </center>
                  <center>
                    <input type="submit" name='left' value="left">
                  </center>
                  <center>
                    <input type="submit" name='right' value="right"> 
                   </center>
              </form>
             </div>
            
    </body>
</html>