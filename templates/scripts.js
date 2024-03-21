const formArea = document.getElementById('inner_form');
const imgUpload = document.getElementById('img-upload');

formArea.addEventListener("dragover", function (e){
    e.preventDefault();
    imgUpload.style.transition = 'all 0.25s'
});

formArea.addEventListener("drop", function(e){
    e.preventDefault();
    imgUpload.files = e.dataTransfer.files
});

formArea.addEventListener('click', function(e){
    e.preventDefault();
    imgUpload.click();
});