var totalAPI = "https://xul88ylpzf.execute-api.us-east-2.amazonaws.com/prod/total"
//var tableGlobal = document.getElementById('#tableGlobal')

/* fetch(totalAPI, {mode: 'no-cors'})
  .then( res => res.ok ? Promise.resolve(res) : Promise.reject(res) )

  .then( res => res.text() )
  .then( json => {
    console.log(json);
    //tabla(json)
  })*/

//function tabla(json) {
//}

axios({
  method: 'GET',
  url: totalAPI
}).then(res => {
  console.log(res)
}).catch(e => {
  console.log(e);
})
