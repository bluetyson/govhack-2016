
var markovList = markovList  || (function (window, document, undefined) {

	var messages = [];

	function loadMessages(callback){
		// do a GET to the API and get a list of things 
		// in the meantime
		// messages = messages.concat(lelelel);
		$.ajax({
			method: "GET",
			url: "http://127.0.0.1:5000/markovstuff",
			dataType: "json",
			crossDomain: true,
			success: callback
		});
		
		// sort them
		//messages.sort(sortByOrder);
	}

	function setMessages(newMessages){
		messages = messages.concat(newMessages);
	}

	function getNextMessage(){
		//alert('Hello World');
		// GET NEXT MESSAGE TO INPUT
		// RETURN IT
		var nextMessage = messages.shift();
		while(nextMessage.content.trim().length == 0)
		{
			nextMessage = messages.shift();
		}
		return messages.shift();
	}

	function getPoliticians(){
		ids = messages.map(function(message) { return message.politician_id; });
		var uniqueNames = [];
		$.each(ids, function(i, el){
			if($.inArray(el, uniqueNames) === -1) uniqueNames.push(el);
		});
		return uniqueNames;
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
		GetPoliticians: getPoliticians,
		HasMessages: hasMessages,
		SetMessages: setMessages,
	};
	
})(this, this.document);
