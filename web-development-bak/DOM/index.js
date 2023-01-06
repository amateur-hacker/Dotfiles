// alert("Hello");


// Document Object Model (DOM):

// querySelector

// document.querySelector("h1").innerHTML = "Good Bye";
// document.querySelector("input").click();

// firstElementChild, lastElementChild or innerHTML
// document.firstElementChild.lastElementChild.lastElementChild.lastElementChild.innerHTML="Sachin";
-
// getElementsByTagName
// document.getElementsByTagName("li")[2].style.color="purple";
// document.getElementsByTagName("li").length;

// getElementsByClassName
// document.getElementsByClassName("btn");
// document.getElementsByClassName("btn")[0].style.color = "red";

// getElementById
// document.getElementById("title");
// document.getElementById("title").innerHTML="Good Bye";
// document.getElementById("title").style.color= "blue";


// querySelector
// document.querySelector("h1");
// document.querySelector("#title");
// document.querySelector(".btn");
// document.querySelector("li a");
// document.querySelector("li.item");
// document.querySelector("#list a");
// document.querySelector("#list .item");

// querySelectorAll
// document.querySelectorAll("#list .item");
// document.querySelectorAll("#list .item")[2].style.color = "blue";

// Quick Challenge:
// document.querySelector("#list .item a").style.color = "red";
// document.querySelector("#list a").style.color = "red";
// document.querySelector("li a").style.color = "red";

// To change first listitem bullet point color.
// document.querySelector("li").style.color = "orange";

// sytling using JavaScript:
// document.querySelector("h1").style.fontSize = "5rem";
// document.querySelector("h1").style.visibility = "hidden";

// Quick Challenge:
// document.querySelector("button").style.backgroundColor = "yellow";

// classList property:
// document.querySelector("button").classList.add("invisible");
// document.querySelector("button").classList.remove("invisible");
// document.querySelector("button").classList.toggle("invisible");

// Quick Challenge:
// document.querySelector("h1").classList.add("huge");

// difference between textContent and innerHTML:

// textContent:
// document.querySelector("h1").textContent = "Good Bye";
// document.querySelector("h1").textContent = "<em> Good Bye </em>";

// innerHTML:
// document.querySelector("h1").innerHTML = "Good Bye";
// document.querySelector("h1").innerHTML = "<em>Good Bye</em>";


// Manipulating Html element attribute:
// document.querySelector("a");
// document.querySelector("a").attributes;
// document.querySelector("a").getAttribute("href");
// document.querySelector("a").setAttribute("href", "www.bing.com");
