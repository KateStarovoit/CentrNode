let get_stats = (url) => {
    let data;
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            data = JSON.parse(xhr.responseText);
        }
    }
    xhr.open("GET", url, true);
    xhr.send();

    return data;
}

let show_stats = () => {
    let url = "https://" + window.location.hostname + '/stats/';

    console.log(url);
}
