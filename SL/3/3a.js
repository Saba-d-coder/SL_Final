window.onload=()=>{
    var obj=[
        {
            "name":"KSK",
            "country":"India",
            "year":"2050",
            "title":"The Hell"
        },
        {
            "name":"Violet Evergarden",
            "country":"Japan",
            "year":"2020",
            "title":"Doll"
        }, {
            "name":"Erie",
            "country":"Japan",
            "year":"2030",
            "title":"Fiendship"
        }, {
            "name":"Midoriya",
            "country":"Japan",
            "year":"2020",
            "title":"One for all"
        }

    ]

    obj.forEach(function(item,index){
        if(index<=1){
            var table=document.createElement('tr')
            
            var a=document.createElement('td')
            a.innerHTML=item.name

            var b=document.createElement('td')
            b.innerHTML=item.country

            var c=document.createElement('td')
            c.innerHTML=item.year

            var d=document.createElement('td')
            d.innerHTML=item.title

            table.appendChild(a)
            table.appendChild(b)
            table.appendChild(c)
            table.appendChild(d)

            document.getElementById("auth").appendChild(table)
        } else{
            var a=document.createElement('p')
            a.innerHTML=item.name+"</br>"+ item.country+"</br>"+item.year+"</br>"+item.title
            document.getElementById('author').appendChild(a)
        }
    })
}