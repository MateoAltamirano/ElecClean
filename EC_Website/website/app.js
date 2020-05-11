var totalAPI = "https://j4220em7i6.execute-api.us-east-2.amazonaws.com/prod/total"
var funAPI = "https://mindicador.cl/api/dolar"
//var totalAPI = "total.json"
var tableGlobal = document.getElementById('tableGlobal')
var button = document.getElementById('button')

console.log("js funcionando");

function fetchfun() {
  console.log("fetch");

  fetch(funAPI)
  .then( res => res.json() )
  .then( datos => {
    console.log(datos);
  })

}

function ajaxfun(){
  console.log("ajax")

  const api = new XMLHttpRequest();
  api.open('GET', funAPI, true);
  api.send();
  api.onreadystatechange = function() {
    if(this.status == 200 && this.readyState == 4) {
      let datos = JSON.parse(this.responseText);
      console.log(datos);
    }
  }

}

function axiosfun() {
  console.log("axios");

  axios({
    method: 'GET',
    url: funAPI
  }).then(res => {
    console.log(res.data)
  })

}

function fetchee() {
  console.log("fetch");

  fetch(totalAPI)
  .then( res => res.json() )
  .then( datos => {
    console.log(datos);
  })

}

function ajaxee(){
  console.log("ajax")

  const api = new XMLHttpRequest();
  api.open('GET', totalAPI, true);
  api.send();
  api.onreadystatechange = function() {
    if(this.status == 200 && this.readyState == 4) {
      let datos = JSON.parse(this.responseText);
      console.log(datos);
    }
  }

}

function axiosee() {
  console.log("axios");

  axios({
    method: 'GET',
    url: totalAPI
  }).then(res => {
    console.log(res.data)
  })

}
