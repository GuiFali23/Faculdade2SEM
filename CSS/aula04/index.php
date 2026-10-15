<?php

// Comandos condicionais
// Switch: diversas opções de resposta

$pedido = 100;
switch ($pedido) {
    case 100:
        $resposta = "Pendente";
        break;
    case 200:
        $resposta = "Processando";
        break;
    case 300:
        $resposta = "Aprovado";
        break;
    case 400:
        $resposta = "Evniado";
        break;
    case 500:
        $resposta = "Entregue";
        break;
    case 600:
        $resposta = "Cancelado";
        break;
    default:
        $resposta = "Pedido não encontrado!";
        break;
}

echo $resposta;
echo "<hr>";

// Match: Introduzida em php 8.0, é diferente do switch que precisa que o comando break seja chamado para parar de rodar um codigo

// match (expression) {
//      => ,
//      => ,
// }

$semana = "teste";
// Normalmente se coloca dentro de uma variavel
$retorno = match ($semana) {
    "Segunda-feira" => "Início da semana.",
    "Terca-feira" => "A semana ainda está no início.",
    "Quarta-feira" => "Meio da semana.",
    "Quinta-feira" => "Quase sextando.",
    "Sexta-feira" => "Sextou.",
    "Sábado" => "Findou.",
    "Domingo" => "Quase Segunda-feira.",
    default => "valor não encontrado"
};

echo $retorno;
echo "<hr>";

// Operador Ternário
// Teste lÓGICO ? "valor se verdadeiro" : valor se falso
$notafinal= 8;
$final = $notafinal >= 7 ?"Aprovado":"Reprovado";
echo $final;
?>