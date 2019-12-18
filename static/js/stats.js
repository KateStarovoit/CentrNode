let get_stats = (url) => {
    console.log(url);
    let data;
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = () => {
        console.log("readyState", xhr.readyState)
        console.log("status", xhr.status)
        if (xhr.readyState === 4 ) {
            data = JSON.parse(xhr.responseText);
        }
        else {
            data  = {"hello": "hello"}
        }
    }
    xhr.open("GET", url, true);
    xhr.send();

    return data;
}

let show_stats = () => {
    let url = "https://" + window.location.hostname + '/get_stats/';
    let data = get_stats(url);
    console.log(data)
    let block;
    let finil_block_html;

    for (let d of data['stats']) {
        block = `
        <div class="row stat">
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['create_queue_duration']} 
            </div>
  
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['delete_queue_duration']}
            </div>
    
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['write_message_duration']}
            </div>
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['read_message_duration']}
            </div>
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['msg_num_in_qname']}
            </div>
            <div class="col statistic px-4 py-3 bg-dark">
            ${d['msg_num_in_anotherqname']}
            </div>
      </div>
        `
        finil_block_html += block;
    }

    let stats = document.getElementById('stats');
    stats.innerHTML = ' ';
    stats.innerHTML = finil_block_html;

    console.log(url);
}
