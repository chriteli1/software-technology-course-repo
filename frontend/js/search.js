const table = document.querySelector("table")
let ID = 1

window.onload = function () {

  const urlParameters = new URLSearchParams(window.location.search)

  const magMin = parseFloat(urlParameters.get('minMag'))
  const magMax = parseFloat(urlParameters.get('maxMag'))
  const loc = urlParameters.get('loc')
  const date = urlParameters.get('date')

  // go to API and get JSON to show
  const earthquakes = []

  // addRow(ID++, "1 km SW Xanthi, Greece", 7.5, date, "red")
  earthquakes.forEach(earthquake => {

    addRow(ID++,
      earthquake.properties.place,
      earthquake.properties.mag,
      timestamp2date(earthquake.properties.time),
      earthquake.properties.alert
    )

  })

}

/* FUNCTIONS */

function addRow(id, location, magnitude, date, alert) {

  const row = document.createElement("tr")
  const cID = document.createElement("td")
  const cLoc = document.createElement("td")
  const cMag = document.createElement("td")
  const cDate = document.createElement("td")
  const cAlert = document.createElement("td")

  cID.innerText = id
  cLoc.innerText = location
  cMag.innerText = magnitude
  cDate.innerText = date
  cAlert.innerText = alert

  row.appendChild(cID)
  row.appendChild(cLoc)
  row.appendChild(cMag)
  row.appendChild(cDate)
  row.appendChild(cAlert)
  table.appendChild(row)

}

function timestamp2date(d) {
  const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

  let date = new Date(d)

  return `${date.getDate()} ${MONTHS[date.getMonth()]} ${date.getFullYear()}`
}

function date2timestamp(date) {
  // date = YYYY-MM-DD
  return new Date(date).getTime()
}