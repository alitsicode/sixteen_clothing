function like(pk) {
    var element=document.getElementById("like")
    var count=document.getElementById("count")
    $.get(`/like/${pk}`).then(Response => {
        if(Response['response'] === "liked"){
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) +1
        }else{
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) -1
        }
    })
}

// function bookmark(pk) {
//     var element=document.getElementById("bookmark")
//     var count=document.getElementById("count")
//     $.get(`/save_post/${pk}`).then(Response => {
//         if(Response['response'] === "bookmark"){
//             element.className = "fa fa-bookmark"
//             count.innerText = Number(count.innerText) +1
//         }else{
//             element.className = "fa fa-bookmark-o"
//             count.innerText = Number(count.innerText) -1
//         }
//     })
// }
