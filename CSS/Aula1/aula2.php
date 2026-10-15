<?php

// Array simples
$lanches = array("Pastel","Pizza","Hamburguer","HotDog","Xis","Churrasquinho");


// echo $lanches[0];

echo "Hoje pela manhã comi $lanches[0], $lanches[2] e comi $lanches[5]";

echo "<hr>";
print_r($lanches);  

// Vale a partir do php 5.6

$bebidas = array("vodka","fanta uva","suco","Água","Whisky","Café");

echo "<hr>";
print_r($bebidas);
echo "<h1>$bebidas[4]</h1>";


// Array Associativo(Dicionario do PYTHON)

$aluno = [
    "nome" => "Roblox",
    "idade"=> "21",
    "curso"=> ["ADS", "Moda"]
];

print_r($aluno);

echo "<h2>$aluno[nome], está com $aluno[idade] anos. E está matriculado no curso de" . $aluno['curso'] [0] . $aluno['curso'][1] . "</h2>";

// Array Multi dimensional

$funcionarios = [
    [
        "nome"=> "Ricardo",
        "setor" => "Administrativo",
        "email"=> "ricardo@email.com"
    ],
    [
        "nome"=> "Gustavo",
        "setor" => "Financeiro",
        "email"=> "gustavo@email.com"
    ],
    [
        "nome"=> "Ana da Silva",
        "setor" => ["Marketing","T.I"],
        "email"=> "ana@email.com"
    ]
];
// echo "<pre>";
// print_r($funcinarios);
// No PHP usamos o "." para concatenar strings
echo "<p>A funcionaria " .  $funcionarios[2]['nome'] . " possui o email " . $funcionarios[2]['email'] . " e trabalha no setor de " . $funcionarios[2]['setor'][1] . " e no setor de " . $funcionarios[2]['setor'][0] . "</p>" ;
########################################################################    


// Comando de repetição (loop)

/*
    - indice = de onde começa a repetição. (ponto de partida)
    - Teste lógico - Lógica para que o comando continue repetindo
    - incremento = é o que ocorre com o indice a cada repetição.
*/
$num = "2";
for ($i = 0; $i < 10; $i += $num) {
    echo "OLA";
    echo "<p>$i</p>";
};

$bebidas = array("vodka","fanta uva","suco","Água","Minecraft");

$contar = count($bebidas);
for ($i = 0; $i < $contar; $i++){
    echo $bebidas[$i] . "<br>";
}

?>