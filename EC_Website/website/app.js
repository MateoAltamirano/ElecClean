var candidatosURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato";
var totalURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/total";
var ciudadURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=ciudad";
var colegioURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=colegio";
var mesaURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/table?pk=";

var tableCandidatos = document.getElementById('trCandidatos');
var tableGlobal = document.getElementById('trGlobal');
var tableCity = document.getElementById('trCity');
var tableSchool = document.getElementById('trSchool');
var tableBooth = document.getElementById('tableBooth');
var image = document.getElementById('img');
var form = document.getElementById('formulario');
var pError = document.getElementById('pError');

if(tableCandidatos && tableGlobal) {
  axios({
    method: 'GET',
    url: candidatosURL
  }).then(candidatos => {
    axios({
      method: 'GET',
      url: totalURL
    }).then(total => {
      candidatos.data.forEach(candidato => {
        tableCandidatos.innerHTML += `<th>${candidato.info}</th>`;
        tableGlobal.innerHTML += `<th>${total.data[0][candidato.PK]}</th>`;
      })
    })
  })
} else if (tableCandidatos && tableCity) {
  axios({
    method: 'GET',
    url: candidatosURL
  }).then(candidatos => {
    axios({
      method: 'GET',
      url: ciudadURL
    }).then(ciudad => {
      var ciudades = [];
      for (i = 0; i < ciudad.data.length; i++) {
        ciudades[i] = `<tr><th id="first">${ciudad.data[i].info}</th>`;
      }
      candidatos.data.forEach(candidato => {
        tableCandidatos.innerHTML += `<th>${candidato.info}</th>`;
        for (i = 0; i < ciudad.data.length; i++) {
          ciudades[i] += `<th>${ciudad.data[i][candidato.PK]}</th>`;
        }
      })
      for (i = 0; i < ciudad.data.length; i++) {
        ciudades[i] += `</tr>`;
        tableCity.innerHTML += ciudades[i];
      }
    })
  })
} else if (tableCandidatos && tableSchool) {
  axios({
    method: 'GET',
    url: candidatosURL
  }).then(candidatos => {
    axios({
      method: 'GET',
      url: colegioURL
    }).then(colegio => {
      axios({
        method: 'GET',
        url: ciudadURL
      }).then(ciudad => {
        var ciudades = new Map();
        for (i = 0; i < ciudad.data.length; i++) {
          ciudades.set(ciudad.data[i].PK, ciudad.data[i].info);
        }
        var colegios = [];
        for (i = 0; i < colegio.data.length; i++) {
          colegios[i] = `<tr><th>${colegio.data[i].info}</th><th id="first">${ciudades.get(colegio.data[i]['ciudad-ID'])}</th>`;
        }
        candidatos.data.forEach(candidato => {
          tableCandidatos.innerHTML += `<th>${candidato.info}</th>`;
          for (i = 0; i < colegio.data.length; i++) {
            colegios[i] += `<th>${colegio.data[i][candidato.PK]}</th>`;
          }
        })
        for (i = 0; i < colegio.data.length; i++) {
          colegios[i] += `</tr>`;
          tableSchool.innerHTML += colegios[i];
        }
      })
    })
  })
} else if (tableBooth && tableCandidatos && pError && image) {
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var data = new FormData(form);
    if(data.get('pk') != '') {
      axios({
        method: 'GET',
        url: mesaURL + data.get('pk')
      }).then(mesa => {
        if (mesa.data.length > 0) {
          axios({
            method: 'GET',
            url: candidatosURL
          }).then(candidatos => {
            pError.innerHTML = '';
            tableCandidatos.innerHTML = '<th id="first">Candidato</th>';
            tableBooth.innerHTML = '<th id="first">Número de votos</th>';
            candidatos.data.forEach(candidato => {
              tableCandidatos.innerHTML += `<th>${candidato.info}</th>`;
              tableBooth.innerHTML += `<th>${mesa.data[0][candidato.PK]}</th>`;
            })
            image.innerHTML = `<img src="${mesa.data[0]['foto-url']}">`;
          })
        } else {
          tableCandidatos.innerHTML = ''
          tableBooth.innerHTML = '';
          image.innerHTML = '';
          pError.innerHTML = 'Datos Erroneos';
        }
      })
    } else {
      tableCandidatos.innerHTML = '';
      tableBooth.innerHTML = '';
      image.innerHTML = '';
      pError.innerHTML = 'Datos Erroneos';
    }
  })
}
