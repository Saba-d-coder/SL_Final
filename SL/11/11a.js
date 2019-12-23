Authors=[
    {
        "name":"KSK",
        "country":"India",
        "year":"2023",
        "title":"The Death of all"
    }, 
    {
        "name":"Tomioka Giyu",
        "country":"Japan",
        "year":"2020",
        "title":"Water Pillar"
    }, 
    {
        "name":"Shoto Todoroki",
        "country":"Japan",
        "year":"2030",
        "title":"Half-Cold,Half-Hot"
    },
    {
        "name":"Katsuki Bakugo",
        "country":"Japan",
        "year":"2021",
        "title":"Explosion"
    }
]

Authors.forEach(function(item,index){
    if(index<2){
        t=document.getElementById('table')
        t.innerHTML+='<tr><td>'+item.name+'</td><td>'+item.country+'</td><td>'+item.title+'</td><td>'+item.year+'</td></tr'
    } else{
        span=document.getElementById('details')
        p=document.createElement('p')
        p.innerHTML+='<hr><strong>Name: </strong> '+item.name+'<br><strong>Country: </strong> '+item.country+'<br><strong>Title: </strong> '+item.title+'<br><strong>Year of publicication: </strong> '+item.year
        span.append(p)
    }
})

