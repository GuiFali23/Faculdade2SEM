<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulários com HTML e PHP</title>
    <style type="text/css">
        input {
            display: block;
            margin-bottom: 8px;
            padding: 8px 5px;
        }
    </style>
</head>

<body>
    <!-- Mothod -> get(mostra os dados na url) ou post -->
    <form action="" method="post">
        <input type="text" name="nome" placeholder="Seu nome: " required>
        <input type="email" name="email" placeholder="Seu email: ">
        <input type="number" name="idade" placeholder="Sua idade: ">
        <input type="submit" name="enviar">
    </form>
    <?php
    // No PHP  os dados enviados via post são recuperados pela var $_POST  
    if (isset($_POST['enviar'])) {
        $nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
        $idade = filter_input(INPUT_POST, 'idade', FILTER_SANITIZE_NUMBER_INT); //Posso usar o validate
        $erros = [];
         

        // print_r($_POST);


        if (strlen(trim($nome)) < 3) {
            $erros[] = "Preencha seu nome completo";
        }

        if (empty($email)){
            $erros[] = "Preencha seu email corretamente";
        }

        if ($idade < 18){
            $erros[] = "Cadastro apenas para maiores de 18 anos";
        }

        if (empty($erros) ) {
            // continuar o envio do formulario
    
            echo "<h2>Confira seus dados: </h2>";
            echo "Nome: $_POST[nome] . <br>";
            echo "E-mail: $_POST[email] . <br>";
            echo "Idade: $_POST[idade]";
        } else {
            foreach ($erros as $erro) {
                echo "$erro <br>";
            }
        }
    }

    ?>

</body>

</html>