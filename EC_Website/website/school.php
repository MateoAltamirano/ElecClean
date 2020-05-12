<?php
$candidatosAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato";
$colegioAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=colegio";
$ciudadAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=ciudad";

$dataCandidatos = json_decode( file_get_contents($candidatosAPI), true );
$dataColegios = json_decode( file_get_contents($colegioAPI), true );
$dataCiudades = json_decode( file_get_contents($ciudadAPI), true );

$ciudades = array();
for ($x = 0; $x < count($dataCiudades); $x++)
{
  $ciudades[$dataCiudades[$x]['PK']] = $dataCiudades[$x]['info'];
}
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
        <li><a href="index.php">Global</a></li>
        <li><a href="city.php">Ciudades</a></li>
        <li>Colegios</li>
        <li><a href="booth.php">Mesa</a></li>
      </ul>
    </nav>
    <table>
      <thead>
        <tr>
          <th>Colegio</th>
          <th id="first">Ciudad</th>
          <?php
          $colegios = array();
          for ($x = 0; $x < count($dataColegios); $x++)
          {
            $colegios[] = "<tr><th>" . $dataColegios[$x]['info'] . '<th id="first">' . $ciudades[$dataColegios[$x]['ciudad-ID']] . "</th>";
          }
          foreach($dataCandidatos as $candidato)
          {
            $pk = $candidato['PK'];
            echo "<th>" . $candidato['info'] . "</th>";
            for ($x = 0; $x < count($dataColegios); $x++)
            {
              $colegios[$x] .= "<th>" . $dataColegios[$x][$pk] . "</th>";
            }
          }
          ?>
        </tr>
      </thead>
      <tbody id="tableGlobal">
        <tr>
          <?php
          for ($x = 0; $x < count($dataColegios); $x++)
          {
            $colegios[$x] .= "</tr>";
            echo $colegios[$x];
          }
          ?>
      </tbody>
    </table>
  </body>
</html>
