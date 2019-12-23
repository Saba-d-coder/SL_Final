Patients=[
    {
        "name":"Asha",
        "AdhaarNo":123456789000,
        "lab_tests":[' Blood Test',' Vitamin Test']
    },
    {
        "name":"Jay",
        "AdhaarNo":123456789001,
        "lab_tests":[' Blood Test',' Immunity Test',' Hormone Test']
    }
]

Hospitals=[
    {
        "name":"Apollo Hospital",
        "location":"Bangalore"
    },
    {
        "name":"Fortis Hospital",
        "location":"Bangalore"
    },
    {
        "name":"Nanavati Hospital",
        "location":"Mumbai"
    }
]

Hospitals.forEach(function(item){
    document.getElementById('hsp').innerHTML+="<tr><td>"+item.name+"</td><td>"+item.location+"</td></tr>"
})


document.getElementById('patient-details').onmouseover=(function(){
    this.style.color='blue'
    span=document.getElementById('detail')
    span.removeAttribute('hidden')

    p=document.createElement('p')
    Patients.forEach(function(item,index){
        p.innerHTML+="<strong>Patient "+index+"</strong><br>Name:"+item.name+"<br>AdhaarNo:"+item.AdhaarNo+"<br>Tests:"+item.lab_tests+"<br>"
    })

    span.append(p)
})
    
    
document.getElementById('patient-details').onmouseout=(function(){
    this.style.color='chocolate'
    p.toggleAttribute('hidden')
})



