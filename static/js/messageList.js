
var markovList = markovList  || (function (window, document, undefined) {

	var messages = [];

	function loadMessages(){
		// do a GET to the API and get a list of things 
		// in the meantime
		messages = messages.concat(lelelel);
		// sort them
		messages.sort(sortByOrder);
	}

	function getNextMessage(){
		//alert('Hello World');
		// GET NEXT MESSAGE TO INPUT
		// RETURN IT
		return messages.shift();
	}

	function hasMessages(){
		return messages.length > 0;
	}

	function sortByOrder(a, b){
		var aOrder = a.order;
		var bOrder = b.order;
		return ((aOrder < bOrder) ? -1 : ((aOrder > bOrder) ? 1 : 0));
	}

	return {
		LoadMessages: loadMessages,
		GetNextMessage: getNextMessage,
		HasMessages: hasMessages
	};
	
})(this, this.document);
