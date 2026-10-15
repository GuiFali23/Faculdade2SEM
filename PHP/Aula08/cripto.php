<?php

echo $senha = "UmasenhaMuitodificildedesborir#senha";
echo "<hr>";
echo $cripto = base64_encode($senha);
echo base64_decode($cripto);
echo "<hr>";
echo md5($senha);
echo "<hr>";
echo password_hash($senha, PASSWORD_DEFAULT);
