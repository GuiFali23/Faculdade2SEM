<?php

// ==========================================
// O QUE O STROTIME FAZ SOZINHO (SEM A FUNÇÃO DATE)
// ==========================================
$timestampPuro = strtotime("now");

echo "=== O QUE O STROTIME() FAZ SOZINHO ===<br>";
echo "Se você der um echo direto no strtotime(\"now\"), ele mostra isto: <strong>" . $timestampPuro . "</strong><br>";
echo "<i>Isso é o 'Timestamp Unix' (o total de segundos que se passaram desde 01/01/1970).</i><br>";
echo "--------------------------------------------------<br><br>";


// ==========================================
// CÓDIGO COMPLETO INTEGRADO
// ==========================================

// 1. Criando objetos de data e usando strtotime()
$timestampExpiracao = strtotime("+7 days", $timestampPuro); 

// Criando objetos DateTime a partir dos timestamps para podermos usar o date_format
$objetoDataSorteio = date_create("@" . $timestampPuro);
$objetoDataLimite  = date_create("@" . $timestampExpiracao);

// Ajustando o fuso horário (pois o caractere '@' define o fuso para UTC)
date_timezone_set($objetoDataSorteio, timezone_open('America/Sao_Paulo'));
date_timezone_set($objetoDataLimite, timezone_open('America/Sao_Paulo'));


// 2. Formatando com a função date_format()
// Sintaxe: date_format($objeto, "formato")
$dataSorteioFormatada = date_format($objetoDataSorteio, "d/m/Y H:i:s");
$dataLimiteFormatada  = date_format($objetoDataLimite, "d/m/Y H:i:s");


// 3. Pegando a hora com a função tradicional date() antiga para manter no exemplo
$horaAtual = date("H", $timestampPuro);


echo "=== SISTEMA DE SORTEIO REGISTRADO ===<br><br>";
echo "Data do sorteio (usando date_format): $dataSorteioFormatada <br>";
echo "Data limite para resgate (usando date_format): $dataLimiteFormatada <br>";
echo "Hora do sorteio (usando date): $horaAtual h <br>";
echo "--------------------------------------------------<br>";

// Validação usando a hora extraída
if ($horaAtual >= 8 && $horaAtual <= 18) {
    echo "Status do Sistema: Sorteio realizado em horário comercial. <br>";
} else {
    echo "Status do Sistema: Sorteio realizado em horário plantão/noturno. <br>";
}
echo "--------------------------------------------------<br><br>";

// 4. Gerando números aleatórios com rand()
$numerosSorteados = [rand(1, 100), rand(1, 100), rand(1, 100), rand(1, 100)];
echo "Números sorteados: " . implode(", ", $numerosSorteados) . "<br><br>";


// 5. Encontrando o maior valor com max()
$maiorValor = max($numerosSorteados);
echo "O maior número sorteado foi: <strong>" . $maiorValor . "</strong><br>";


// 6. Encontrando o menor valor com min()
$menorValor = min($numerosSorteados);
echo "O menor número sorteado foi: <strong>" . $menorValor . "</strong><br><br>";


// 7. Calculando a média e arredondando com round()
$mediaExata = array_sum($numerosSorteados) / count($numerosSorteados);
$mediaArredondada = round($mediaExata, 2); 

echo "A média exata dos números é: " . $mediaExata . "<br>";
echo "A média arredondada (2 casas) é: <strong>" . $mediaArredondada . "</strong><br>";
?>