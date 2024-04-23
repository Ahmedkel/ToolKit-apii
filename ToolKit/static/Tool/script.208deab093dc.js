// website_tools.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('/website_tools/')
       .then(response => response.json())
       .then(data => {
         const list = document.querySelector('ul');
         data.forEach(tool => {
           const listItem = document.createElement('li');
           listItem.textContent = tool.name;
           list.appendChild(listItem);
         });
       });
   });
   