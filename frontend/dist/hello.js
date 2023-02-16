
var dropBox = document.getElementById('dropBox');

dropBox.addEventListener('dragover', function(e) {
  e.preventDefault();
  e.stopPropagation();
  dropBox.style.border = '3px dashed #999';
});

dropBox.addEventListener('dragleave', function(e) {
  e.preventDefault();
  e.stopPropagation();
  dropBox.style.border = '3px dashed #bbb';
});

dropBox.addEventListener('drop', function(e) {
  e.preventDefault();
  e.stopPropagation();
  dropBox.style.border = '3px dashed #bbb';
  var files = e.dataTransfer.files;
  send_files(files);
});

function read_file(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = () => {
            resolve(reader.result);
        };

        reader.onerror = () => {
            reject(reader.error());
        };

        reader.readAsBinaryString(file);
    });
}

async function send_files(files) {
    console.log(files);
    
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const content = await read_file(file)

        const options = {
            method: 'POST',
            headers: new Headers({'content-type': 'application/json'}),
        };

        options.body = JSON.stringify({
                "metadata": {
                    "is_zip": true,
                    "type": 0,
                    "strict": 0,
                },
                "data": btoa(content)
            });
        
        const request = await fetch("http://127.0.0.1:5000/run", options)
        json_dict = JSON.parse(await request.text())
        let file_jsons = []
        key_name = Object.keys(json_dict);
        for (let k of key_name) {
            file_jsons.push({"name":k.substring(0,k.lastIndexOf(".")).replace("_", " "), "score":json_dict[k]});
        }
        file_jsons = file_jsons.sort((a, b) => {
            if (a["score"] > b["score"]) {return -1;}
        })
        updateTable(file_jsons);
        console.log(file_jsons);
    }
    
}

// Example data for testing
var scores = [  { name: 'Eyal', score: 80 },  { name: 'Alon', score: 90 },  { name: 'Yuval', score: 100 }];

function updateTable(data) {
  var table = document.getElementById('score-table').getElementsByTagName('tbody')[0];
  
  // Clear existing table rows
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }
  
  // Add new table rows based on data
  data.forEach(function(item) {
    var row = table.insertRow();
    var nameCell = row.insertCell();
    var scoreCell = row.insertCell();
    nameCell.innerHTML = item.name;
    scoreCell.innerHTML = (item.score).toString().slice(0,5);
  });
}

// Call the function with the example data to update the table
