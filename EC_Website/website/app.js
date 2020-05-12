var candidatosURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/list?list=candidato"
var totalURL = "https://rj1rx7fjzh.execute-api.us-east-2.amazonaws.com/prod/total"

var tableCandidatos = document.getElementById('trCandidatos')
var tableGlobal = document.getElementById('trGlobal')
var button = document.getElementById('button')
console.log(tableCandidatos)

console.log("js funcionando")

axios({
  method: 'GET',
  url: candidatosURL
}).then(candidatos => {
  axios({
    method: 'GET',
    url: totalURL
  }).then(total => {
    console.log(total);
    console.log(candidatos.data)
    candidatos.data.forEach(candidato => {
      tableCandidatos.innerHTML += `<th>${candidato.info}</th>`
      tableGlobal.innerHTML += `<th>${total.data[0][candidato.PK]}</th>`
    })
  })
})
