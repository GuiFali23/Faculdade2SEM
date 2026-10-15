<?php
session_start();

// Limpar os caches da session
session_unset();

//Encerrar a session
session_destroy();

echo "Sessão encerrada com sucesso";

// header("location: index.php")
header("Refresh: 3; url=index.php");
?>