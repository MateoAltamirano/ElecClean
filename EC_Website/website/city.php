<?php
$candidatosAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato";
$ciudadAPI = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=ciudad";

$dataCandidatos = json_decode( file_get_contents($candidatosAPI), true );
$dataCiudades = json_decode( file_get_contents($ciudadAPI), true );
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
        <li>Ciudades</li>
        <li><a href="school.php">Colegios</a></li>
        <li><a href="booth.php">Mesa</a></li>
      </ul>
    </nav>
    <section>
      <table>
        <thead>
          <tr>
            <th id="first">Ciudad\Candidato</th>
            <?php
            $ciudades = array();
            for ($x = 0; $x < count($dataCiudades); $x++)
            {
              $ciudades[] = '<tr><th id="first">' . $dataCiudades[$x]['info'] . "</th>";
            }
            foreach($dataCandidatos as $candidato)
            {
              $pk = $candidato['PK'];
              echo "<th>" . $candidato['info'] . "</th>";
              for ($x = 0; $x < count($dataCiudades); $x++)
              {
                $ciudades[$x] .= "<th>" . $dataCiudades[$x][$pk] . "</th>";
              }
            }
            ?>
          </tr>
        </thead>
        <tbody id="tableGlobal">
          <tr>
            <?php
            for ($x = 0; $x < count($dataCiudades); $x++)
            {
              $ciudades[$x] .= "</tr>";
              echo $ciudades[$x];
            }
            ?>
        </tbody>
      </table>
    </section>
  </body>
</html>
