document.addEventListener("DOMContentLoaded", function(){

	const csrftoken = Cookies.get('csrftoken'); //get csrf_token

	var mymap = L.map('mapid').setView([51.505, -0.09], 13); //create map

	//customize map settings
	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);
	
	var popup = L.popup();

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(mymap);

		sendData(e.latlng)
	}

	function sendData(coord){
	

		const request = new Request(
			"log",
			{
				headers: {'X-CSRFToken': csrftoken},
			}
		);
		
		fetch(request, {
			method: 'POST',
			mode: 'same-origin',
			body: JSON.stringify(coord)
		})
	}	

	mymap.on('click', onMapClick);

});