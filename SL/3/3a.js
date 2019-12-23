window.onload=()=>{
    var obj=[
        {
            "name":"KSK",
            "country":"India",
            "year":"1996",
            "title":"The Hell"
        },
        {
            "name":"Khan",
            "country":"India",
            "year":"2020",
            "title":"The Death of All"
        }, {
            "name":"Saba",
            "country":"India",
            "year":"2030",
            "title":"Fiendship"
        }, {
            "name":"Khanum",
            "country":"India",
            "year":"1998",
            "title":"The Crime"
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