var updatecart = document.getElementsByClassName("update-cart")
for(var i=0;i<updatecart.length;i++){
    updatecart[i].addEventListener('click',function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('product',productId,'action',action)
    console.log('USER',user)
    if(user=='AnonymousUser'){
    console.log("You are not authenticated.. Login first")
    window.location.href= "/login/"
    }
    else{
        updatebasket(productId,action)
    }
    })
}

function updatebasket(productId,action){
    console.log("You are logged in... ")
    url = '/update-order/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action}),
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
    console.log('data :',data)
    location.reload()
    })
}


