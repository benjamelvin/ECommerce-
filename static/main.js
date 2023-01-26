
function get_icon(){
  
    

    iconName = document.getElementById('my_input').value
   console.log(iconName)
    
    axios.get(`search/${iconName}`).then( (response) => {
        console.log(response)
        image_url= response.data.icon.preview_url
        div = document.createElement('div')
        div.setAttribute('id', 'my-id')
        div.innerHTML = `<span>Sorry we don't carry ${iconName}'s</span>`
        img = document.createElement('img')
        
     
     img['src'] = `${image_url}`
     div.appendChild(img);
     
     document.getElementById('noun').appendChild(div)

    }
    )
}


