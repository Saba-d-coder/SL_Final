window.onload=()=>{
    cars=[
        {
            "model":"BMW",
            "name":"modelS",
            "price":65743,
            "year":2016
        },
        {
            "model": "FIAT ",
            "name": "modelX",
            "price": 83700,
            "year": 2017
        },
        {
            "model": "FORD",
            "name": "model3",
            "price": 35000,
            "year": 2019
        },
    ]

    cars.forEach(function(item,index){
        th=document.createElement('th')
        th.id=item.model
        th.innerHTML=item.model
        document.getElementById('menu').appendChild(th)

    })

    cars.forEach(function(item,index){
        s=document.getElementById(item.model)
        s.onmouseover=(function(){
            car=item
            if(item){
                document.getElementById('detail').removeAttribute('hidden')
                document.getElementById(item.model).style.backgroundColor='pink'
                document.getElementById('name').innerHTML=item.model
                document.getElementById('img').innerHTML='<img src="img/'+item.name+'.jpeg" alt="car"/>'
                document.getElementById('cost').innerHTML="$"+item.price
                document.getElementById('yr').innerHTML=item.year
    
            }
            
        })

        s.onmouseout=function(){
            car=item
            if(item){
                document.getElementById(item.model).style.backgroundColor='blueviolet'
                document.getElementById('detail').toggleAttribute('hidden')

            }
        }
    })
}