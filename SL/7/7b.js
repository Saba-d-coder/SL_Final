window.onload=()=>{
    cars=[
        {
            "model":"Lamborghini Aventador",
            "name":"Lamborghini",
            "price":"789,809",
            "year":2016
        },
        {
            "model": "Tesla Model X ",
            "name": "Tesla",
            "price": "104,990",
            "year": 2017
        },
        {
            "model": "Porche 918 Spyder",
            "name": "Porche",
            "price": "845,000",
            "year": 2017
        },
    ]

    cars.forEach(function(item,index){
        th=document.createElement('th')
        th.id=item.name
        th.innerHTML=item.name
        document.getElementById('menu').appendChild(th)

    })

    cars.forEach(function(item,index){
        s=document.getElementById(item.name)
        s.onmouseover=(function(){
                document.getElementById('detail').removeAttribute('hidden')
                document.getElementById(item.name).style.backgroundColor='pink'
                document.getElementById('name').innerHTML=item.model
                document.getElementById('img').innerHTML='<img src="img/'+item.name+'.jpeg" alt="car"/>'
                document.getElementById('cost').innerHTML="$"+item.price
                document.getElementById('yr').innerHTML=item.year           
        })

        s.onmouseout=function(){
            car=item
            if(item){
                document.getElementById(item.name).style.backgroundColor='blueviolet'
                document.getElementById('detail').toggleAttribute('hidden')

            }
        }
    })
}