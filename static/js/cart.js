var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('Product:', productId, 'Action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('user is not authenticated!')
        }
        else{
            console.log('user is authenticated, sending data...')
        }
    })
}