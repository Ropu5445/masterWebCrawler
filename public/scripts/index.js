const table = document.getElementById("data-table")
const urlPattern = /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
var jsonData

async function fetchData(file) {
    try {
        const response = await fetch("../data/" + file);
        jsonData = await response.json();
        await handleData(file)
    } catch(error) {
        //pass
    }
}

function handleData() {
    removeAllChildNodes(table)
    
    let cols = Object.keys(jsonData[0]);
    let thead = document.createElement("thead");
    let tr = document.createElement("tr");
    let tbody = document.createElement("tbody");
    
    cols.forEach((item) => {
        let th = document.createElement("th");
        let modItem = item[0].toUpperCase() + item.slice(1)
        th.innerText = modItem; // Set the column name as the text of the header cell
        tr.appendChild(th); // Append the header cell to the header row
    });
    
    thead.appendChild(tr); // Append the header row to the header
    table.appendChild(thead) // Append the header to the table
    table.appendChild(tbody)
    
    jsonData.forEach((item) => {
        let tr = document.createElement("tr");
        
        // Get the values of the current object in the JSON data
        let vals = Object.values(item);
        
        // Loop through the values and create table cells
        vals.forEach((elem) => {
            let td = document.createElement("td");
            if (isValidUrl(elem)) {
                let a = document.createElement("a")
                a.href = elem
                a.innerText = "Mene sivulle"
                td.appendChild(a)
            }
            else {
                td.innerText = elem; // Set the value as the text of the table cell
            }
            tr.appendChild(td); // Append the table cell to the table row
        });
        tbody.appendChild(tr); // Append the table row to the table
    });
}

function removeAllChildNodes(parent) {
    if (parent) {
        while (parent.firstChild) {
            parent.removeChild(parent.firstChild);
        }
    }
}

function addActiveOnClick(elem) {
    var a = document.getElementsByTagName('a');
    for (i = 0; i < a.length; i++) {
        a[i].parentNode.classList.remove('is-active')
    }
    // add 'active' classs to the element that was clicked
    elem.parentNode.classList.add('is-active');
}

fetchData("test.json")

const isValidUrl = urlString=> {
    var urlPattern = new RegExp('^(https?:\\/\\/)?'+ // validate protocol
  '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // validate domain name
  '((\\d{1,3}\\.){3}\\d{1,3}))'+ // validate OR ip (v4) address
  '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // validate port and path
  '(\\?[;&a-z\\d%_.~+=-]*)?'+ // validate query string
  '(\\#[-a-z\\d_]*)?$','i'); // validate fragment locator
return !!urlPattern.test(urlString);
}