function myFunction() {
    // body...
var date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

let currentDate = day + "-" + month + "-" + year;



	//start 
	//
	var img = document.createElement("img"); // Create the img element once

if (month == "12" || month == "01") {  // LOGO FOOTER - December or January
    img.src = "{{ url_for('static', filename='img/maxnews2.png') }}";
} else {  // For other months
    img.src = "{{ url_for('static', filename='img/maxnews.png') }}";
}

var src = document.getElementById("logo2");
src.appendChild(img);  // Append the image to the div

// end





if (month == "12" || month == "1") {
    document.getElementById("greetings").innerHTML = "Merry Christmas & Happy New Year!!! &#x1F389;";
} else if (currentDate == "09-09-2025") {
    document.getElementById("greetings").innerHTML = "Happy Birthday, Eliazer!!! &#127881;&#x1F389;";
}

}

myFunction();











function openNav() {
		// body...
		document.getElementById("mySidenav").style.width = "200px";
	}

	function closeNav() {
		// body...
		document.getElementById("mySidenav").style.width = "0";
	}

	var open = document.querySelector(".nav-menu");

	open.addEventListener("click", function() {
		// body...
		document.querySelector("body").classList.toggle("active");
	})





