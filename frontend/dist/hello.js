
async function sendFiles() {
    files_item = document.getElementById("file")
    console.log(files_item.files)

    const options = {
        method: 'POST',
        headers: new Headers({'content-type': 'application/json'}),
    };

    options.body = JSON.stringify({
            "metadata": {
                "is_zip": false,
                "type": 0,
                "strict": 0,
            },
            "data": "YmxhdA=="
        });
    
    const request = await fetch("http://127.0.0.1:5000/run", options)
    json_dict = JSON.parse(await request.text())
}
