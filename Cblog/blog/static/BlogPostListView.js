const content = document.getAllElementById('content');
const posts = document.getElementById("posts");
const announcements = document.getElementById("announcements");
console.log('something');
posts.addEventListner("onClick",(e)=>{
    e.classList.remove("text-gray-800");
    e.classList.add("text-blue-800");
})

document.addEventListener("DOMContentLoaded", function () {
const tabButtons = document.querySelectorAll(".tab-button");
const tabContents = document.querySelectorAll(".tab-content");

tabButtons.forEach(button => {
    button.addEventListener("click", () => {
    const target = button.getAttribute("data-tab");

    // Reset all tabs
    tabButtons.forEach(btn => {
        btn.classList.remove("border-blue-600", "text-blue-600");
        btn.classList.add("text-gray-600", "border-transparent");
    });
    tabContents.forEach(content => content.classList.add("hidden"));

    // Activate clicked tab
    button.classList.remove("text-gray-600", "border-transparent");
    button.classList.add("border-blue-600", "text-blue-600");

    document.getElementById(target).classList.remove("hidden");
    });
});
});
