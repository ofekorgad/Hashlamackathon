
function sendFiles() {
    files_item = document.getElementById("file")
    console.log(files_item.files)

    fetch('https://reqbin.com/echo/post/json', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "id": 78912 })
})
}
