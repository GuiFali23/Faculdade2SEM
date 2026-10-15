<?php
$alunos = [
    [
        "Aluno" => "Guilherme",
        "Curso"=> "ADS",
        "Nota"=> "9"
    ],
    [
        "Aluno" => "Marcelo",
        "Curso"=> "ADS",
        "Nota"=> "5"
    ],
    [
        "Aluno" => "Giovanne",
        "Curso"=> "ADS",
        "Nota"=> "10"
    ],
    [
        "Aluno" => "Gabriel",
        "Curso"=> "ADS",
        "Nota"=> "7"
    ],
    [
        "Aluno" => "Mari",
        "Curso"=> "ADS",
        "Nota"=> "6"
    ]
];
foreach ($alunos as $aluno) {
    echo "O aluno " . $aluno["Aluno"] . " Do curso: " . $aluno["Curso"] . " Tirou nota: " . $aluno["Nota"] . "<br>";
}
?> 