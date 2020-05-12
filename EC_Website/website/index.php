<?php
$candidatosAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato";
$totalAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/total";

$dataCandidatos = json_decode( file_get_contents($candidatosAPI), true );
$dataTotal = json_decode( file_get_contents($totalAPI), true );
?>
<!DOCTYPE html>
<html lang="es" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ElecCLean</title>
    <link rel="stylesheet" type="text/css" href="css/master.css">
  </head>
  <body>
    <header>
      ElecCLean
    </header>
    <nav>
      <ul>
        <li>Global</li>
        <li><a href="city.php">Ciudades</a></li>
        <li><a href="school.php">Colegios</a></li>
        <li><a href="booth.php">Mesa</a></li>
      </ul>
    </nav>
    <section>
      <table>
        <thead>
          <tr>
            <th id="first">Candidato</th>
            <?php
            $total = "";
            foreach($dataCandidatos as $candidato)
            {
              $pk = $candidato['PK'];
              echo "<th>" . $candidato['info'] . "</th>";
              $total .= "<th>" . $dataTotal[0][$pk] . "</th>";
            }
            ?>
          </tr>
        </thead>
        <tbody id="tableGlobal">
          <tr>
            <th id="first">Número de votos</th>
            <?php
            echo $total;
            ?>
          </tr>
        </tbody>
      </table>
    </section>
  </body>
</html>
