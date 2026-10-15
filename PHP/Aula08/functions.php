<?php

$emailAcesso = "admin@gmail.com";
$senhaAcesso = sha1("admin123");

if (isset($_POST['logar'])) {
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $usuario = filter_input(INPUT_POST, 'usuario', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $senha = sha1($_POST['senha']);
    if (!empty($senha) and !empty($email)) {
        if($emailAcesso == $email and $senhaAcesso == $senha){
            session_start();
            $_SESSION['usuario'] = $usuario;
            $_SESSION['email'] = $email;
            $_SESSION['ativa'] = true;
            //Redicionar página
            header("location:admin.php");
        }else{
        echo "E-mail ou senha inválidos";
        }
    }else{
        echo "E-mail ou senha inválidos";
    }





}






// // INCIA A SESSÃO
// session_start();
// // VARIAVEIS DE SESSÃO
// $_SESSION['Usuario'] = "Gabriel Roblox";
// $_SESSION['Email'] = "model@email.com";
// $_SESSION['ativa'] = true;

// echo "<a href = 'admin.php'>Acessar Admin</a>";
//
