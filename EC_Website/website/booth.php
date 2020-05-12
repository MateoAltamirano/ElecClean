<?php
if(isset($_GET['submit']) && $_GET['idBooth'] != "") {
  $candidatosURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato";
  $mesaURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/table?pk=" . $_GET['idBooth'];

  $dataMesa = json_decode( file_get_contents($mesaURL), true );
  $dataCandidatos = json_decode( file_get_contents($candidatosURL), true );
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
        <li><a href="school.php">Colegios</a></li>
        <li>Mesa</li>
      </ul>
    </nav>
    <section>
      <form class="formulario" method="GET">
        <label for="idBooth">Código de mesa:</label><br>
        <input type="text" name="idBooth" value=""><br>
        <input type="submit" name="submit" value="Buscar">
      </form>
    </section>
    <?php
    if(isset($_GET['submit']) && $_GET['idBooth'] != "") {
      if(count($dataMesa) > 0) {
    ?>
    <section>
      <table id="tableForm">
        <thead>
          <tr>
            <th id="first">Candidato</th>
            <?php
            $mesa = "";
            foreach($dataCandidatos as $candidato)
            {
              $pk = $candidato['PK'];
              echo "<th>" . $candidato['info'] . "</th>";
              $mesa .= "<th>" . $dataMesa[0][$pk] . "</th>";
            }
            ?>
          </tr>
        </thead>
        <tbody id="tableGlobal">
          <tr>
            <th id="first">Número de votos</th>
            <?php
            echo $mesa;
            ?>
          </tr>
        </tbody>
      </table>
    </section>
    <section>
      <?php
      echo '<img src="' . $dataMesa[0]['foto-url'] . '" width="400">';
      ?>
    </section>
    <?php
      }
    }
    ?>
  </body>
</html>
