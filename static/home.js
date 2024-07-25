loader_container = document.getElementByClass("loader");
result_container = document.getElementByClass("result-message");

predict_button = document.getElementByClass("btn");

function hideLoader() {
    loader_container.classList.add("hide")
    result_container.classList.remove("hide")
}

predict_button.addEventListner("click", hideLoader);


// Add loader in result message div in home.html file if needed ->
// <div class="loader">
//     <img src="static/loading_animation.gif" alt="">
// </div>