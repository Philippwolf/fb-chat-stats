function Drop() {
	this.img = document.createElement("img");
	this.img.src = "img/bg.png"
	this.img.className = "heart"
	this.img.style.right = Math.floor((Math.random() * window.innerWidth)) + "px";
	this.top = Math.floor((Math.random() * -1500) - 50)
	this.img.style.top = this.top + "px";
	this.img.style.width = Math.floor((Math.random() * 40) + 10) + "px";
	this.speed = Math.floor((Math.random() * 2) + 1);
	this.maxHeight = getDocHeight();

	document.getElementById("mainDiv").appendChild(this.img);

	this.start = function() {
		setInterval(this.fall.bind(this) , 10)
	}

	this.fall = function() {
	    this.top = this.top + this.speed;
	    this.img.style.top = this.top + "px";
	    
	    if (this.top >= this.maxHeight) {
	      this.top = Math.floor((Math.random() * -500) + 100);
	      this.img.style.top = this.top + "px";
	      this.speed = Math.floor((Math.random() * 4) + 1);
	    }	    
	  }

	

}

var drops = [];

function setup() {
  for (var i = 0; i < 35; i++) {
    drops[i] = new Drop();
  }
}

function start() {
	for (var i = 0; i < drops.length; i++) {
	    drops[i].start();
	}
}

function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    );
}

