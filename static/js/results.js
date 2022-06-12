const requestOptions = {
    method: 'GET',
    redirect: 'follow'
}

let ID = 0
const loadingID = startLoadingAnimation()

window.onload = function () {

    const urlParameters = new URLSearchParams(window.location.search)

    const minMag = urlParameters.get('minMag')
    const maxMag = urlParameters.get('maxMag')
    const location = urlParameters.get('location')
    const minDate = urlParameters.get('minDate')
    const maxDate = urlParameters.get('maxDate')

    let apiUrl = "http://localhost:5000/"
    if (minMag) {
        apiUrl += `significant_magnitude/${parseFloat(minMag).toFixed(1)}&${parseFloat(maxMag).toFixed(1)}`
    } else if (location) {
        apiUrl += `location/${location}`
    } else if (minDate) {
        apiUrl += `date/${date2timestamp(minDate)}&${date2timestamp(maxDate)}`
    }

    fetch(apiUrl, requestOptions)
        .then(response => response.text())
        .then(result => {

            setTimeout(endLoadingAnimation(loadingID), 1000)

            document.querySelector(".content").style.opacity = 1;

            if (JSON.parse(result).length) {
                JSON.parse(result).forEach(earthquake => {
                    addRow(++ID, earthquake.place, earthquake.mag, timestamp2date(parseInt(earthquake.date)))
                })
            } else {
                const msg = document.createElement("div")
                msg.classList.add("no-eq-msg")
                msg.innerText = "0 earthquakes found"
                document.querySelector("body").appendChild(msg)
                console.log("0 earthquakes happened")
            }

        })
        .catch(error => console.log('error', error))

}

function addRow(id, location, magnitude, date) {

    // create column elements
    const row = document.createElement("tr")
    const cID = document.createElement("td")
    const cLoc = document.createElement("td")
    const cMag = document.createElement("td")
    const cDate = document.createElement("td")

    // add classes
    cID.classList.add("id-col")
    cLoc.classList.add("loc-col")
    cMag.classList.add("mag-col")
    cDate.classList.add("date-col")

    // add earthquake's content
    cID.innerText = id
    cLoc.innerText = location
    cMag.innerText = magnitude
    cDate.innerText = date

    // insert earthquake in a row
    row.appendChild(cID)
    row.appendChild(cLoc)
    row.appendChild(cMag)
    row.appendChild(cDate)

    // show earthquake
    document.querySelector(".eq-entries").appendChild(row)
}

function timestamp2date(ts) {
    return new Date(ts).toString().slice(4, 21)
}

function date2timestamp(date) {
    return new Date(date).getTime()
}

function startLoadingAnimation() {

    const animationBox = document.createElement("div")
    animationBox.classList.add("animation-box")
    const canvas = document.createElement('canvas');
    canvas.classList.add("loading-animation-canvas")
    const context = canvas.getContext('2d');

    animationBox.appendChild(canvas)
    document.querySelector("body").appendChild(animationBox)

    canvas.width = 300;
    canvas.height = 300;

    var x = canvas.width / 2;
    var y = canvas.height / 2;
    var radius = 60;

    var startAngle = 0.02 * Math.PI;
    var endAngle = 0.4 * Math.PI;

    var counterClockwise = false;

    context.lineWidth = 8;
    context.strokeStyle = 'white';

    var red = 255;
    var blue = 0;
    var green = 0;

    var red_done = false;
    var blue_done = false;
    var green_done = false;

    return setInterval(() => {
        startAngle = startAngle + 0.02 * Math.PI;
        endAngle = endAngle + 0.02 * Math.PI;
        if ((red == 255) && (red_done == false)) {
            blue = blue + 5;
        } else if ((blue == 255) && (blue_done == false)) {
            red = red - 5;
        } else if ((blue == 255) && (red == 0) && (green_done == false)) {
            green = green + 5;
        } else if ((green == 255) && (blue > 0)) {
            blue = blue - 5;
        } else if ((green == 255) && (blue == 0) && (red < 255)) {
            red = red + 5;
        } else if (red == 255) {
            green = green - 5;
        }
        if (blue == 255) {
            red_done = true;
        }
        if ((blue == 255) && (red == 0)) {
            blue_done = true;
        }
        if ((blue == 255) && (green == 255)) {
            green_done = true;
        }
        if ((green_done == true) && (green == 0)) {
            red_done = false;
            blue_done = false;
            green_done = false;
        }
        context.strokeStyle = 'rgba(' + red + ',' + green + ',' + blue + ',1)';
        if (endAngle > (2 * Math.PI)) {
            endAngle = 0;
        }
        if (startAngle > (2 * Math.PI)) {
            startAngle = 0;
        }

        context.fillStyle = 'rgba(255,255,255,0.05)';
        context.fillRect(0, 0, 500, 300);
        context.beginPath();
        context.arc(x, y, radius, startAngle, endAngle, counterClockwise);
        context.stroke();
        context.closePath();
    }, 10);


}

function endLoadingAnimation() {
    const animationBox = document.querySelector(".animation-box")
    animationBox.parentNode.removeChild(animationBox)
}