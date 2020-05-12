var candidatosURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato"
var totalURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/total"
var ciudadURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=ciudad"

var tableCandidatos = document.getElementById('trCandidatos')
var tableGlobal = document.getElementById('trGlobal')
var tableCity = document.getElementById('trCity')

console.log("js funcionando")

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
        tableCandidatos.innerHTML += `<th>${candidato.info}</th>`
        tableGlobal.innerHTML += `<th>${total.data[0][candidato.PK]}</th>`
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
      var ciudades = []
      for (i = 0; i < ciudad.data.length; i++) {
        ciudades[i] = `<tr><th id="first">${ciudad.data[i].info}</th>`
      }
      candidatos.data.forEach(candidato => {
        tableCandidatos.innerHTML += `<th>${candidato.info}</th>`
        for (i = 0; i < ciudad.data.length; i++) {
          ciudades[i] += `<th>${ciudad.data[i][candidato.PK]}</th>`
        }
      })
      for (i = 0; i < ciudad.data.length; i++) {
        ciudades[i] += `</tr>`
        tableCity.innerHTML += ciudades[i]
      }
    })
  })
}
