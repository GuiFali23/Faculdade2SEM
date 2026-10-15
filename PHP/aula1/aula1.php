<?php

$aluno = "Model"; //String
$idade = 21; //INT
$altura = 1.84; //Float
$matriculado = true; //boolean

echo "Olá, $aluno Bem vindos as aulas de PHP!<br>";
echo '<h1>Olá, $aluno Bem vindos as aulas de PHP!</h1>';
//Soma
$x = "15";
$y = 5.3;

$soma = $x + $y;

echo $soma;




//Concatenação, juntar strings
$nome = "Gabriel ";
$nome .= "Model";


echo "<h2>$nome</h2>";



// Constantes

define("CURSO", "programação com PHP");

echo CURSO;
//Não permite mudar o valor
// define("CURSO", "HTML e CSS");

const TESTE = "Novo";
echo "<br>" . TESTE;
?>