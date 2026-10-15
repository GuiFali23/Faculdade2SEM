<?php

$btus = null;
$area = null;
$erro = null;

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $largura = floatval($_POST["largura"]);
    $comprimento = floatval($_POST["comprimento"]);
    $ambiente = $_POST["ambiente"];

    $area = $largura * $comprimento;

    $tabela = [
        9 => [
            "residencial" => 7000,
            "comercial" => 7000
        ],
        12 => [
            "residencial" => 7000,
            "comercial" => 9000
        ],
        15 => [
            "residencial" => 9000,
            "comercial" => 12000
        ],
        20 => [
            "residencial" => 12000,
            "comercial" => 16000
        ],
        25 => [
            "residencial" => 15000,
            "comercial" => 20000
        ],
        30 => [
            "residencial" => 18000,
            "comercial" => 24000
        ],
        35 => [
            "residencial" => 21000,
            "comercial" => 28000
        ],
        40 => [
            "residencial" => 24000,
            "comercial" => 32000
        ],
        45 => [
            "residencial" => 27000,
            "comercial" => 36000
        ],
        50 => [
            "residencial" => 30000,
            "comercial" => 40000
        ],
        60 => [
            "residencial" => 36000,
            "comercial" => 48000
        ],
        70 => [
            "residencial" => 42000,
            "comercial" => 56000
        ]
    ];

    foreach ($tabela as $metros => $valores) {

        if ($area <= $metros) {
            $btus = $valores[$ambiente];
            break;
        }
    }

    if ($btus === null) {
        $erro = "Área superior a 70 m².";
    }
}

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>

    <meta charset="UTF-8">
    <title>Calculadora de BTUs</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }

        h1 {
            color: #333;
        }

        form {
            width: 300px;
        }

        label {
            display: block;
            margin-top: 15px;
        }

        input,
        select,
        button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }

        button {
            margin-top: 20px;
            cursor: pointer;
        }

        .resultado {
            margin-top: 20px;
            padding: 15px;
            background-color: #e8f5e9;
            border: 1px solid #4caf50;
        }

        .erro {
            margin-top: 20px;
            color: red;
        }

    </style>

</head>

<body>

    <h1>Calculadora de BTUs</h1>

    <form method="POST">

        <label for="largura">Largura (m):</label>

        <input
            type="number"
            name="largura"
            id="largura"
            step="0.01"
            required
        >

        <label for="comprimento">Comprimento (m):</label>

        <input
            type="number"
            name="comprimento"
            id="comprimento"
            step="0.01"
            required
        >

        <label for="ambiente">Ambiente:</label>

        <select name="ambiente" id="ambiente" required>

            <option value="">Selecione</option>

            <option value="residencial">
                Residencial
            </option>

            <option value="comercial">
                Comercial
            </option>

        </select>

        <button type="submit">
            Calcular
        </button>

    </form>

    <?php if ($btus !== null): ?>

        <div class="resultado">

            Para seu ambiente de
            <strong><?= number_format($area, 2, ',', '.') ?>m²</strong>
            é necessário um ar condicionado de
            <strong><?= number_format($btus, 0, ',', '.') ?> BTUs</strong>.

        </div>

    <?php endif; ?>

    <?php if ($erro !== null): ?>

        <div class="erro">
            <?= $erro ?>
        </div>

    <?php endif; ?>

</body>

</html>