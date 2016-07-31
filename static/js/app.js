$( document ).ready(
	runApp
)

var count = 0;
var politicians = {};

// A SINGLE MESSAGE LOOKS LIKE THIS 
/*
{
	politicianId,
	type,
	content
}
*/

var lelelel = 
[	
	{
		order: 0,
		politicianId: 'EZ5',
		name: 'ToneDawgz',
		type: 'talk',
		content: 'I am the best person ever lol, i stopped the botes.'
	},	
	{
		order: 2,
		politicianId: 'EZ5',
		name: 'ToneDawgz',
		type: 'talk',
		content: 'lmao get fucked mal, I\'ve given you the answer u deserve lmfao - will take over soon xx'
	},	
	{
		order: 1,
		politicianId: '885',
		name: 'Malcolm',
		type: 'talk',
		content: 'No you are not! You couldn\'t even stay in power. You were a gross misuse of tax-payer money. We need to focus on jobs and growth, not coal and boats!'
	}
]




function runApp(){
/*	var source   = $("#entry-template").html();
	var template = Handlebars.compile(source);
	var context = {politicianId: "21341", content: "This is my first post!"};
	var html    = template(context);
	var middleColumn = $('#middle-column');
	middleColumn.append(html);
*/
	markovList.LoadMessages(messagesLoaded);
}

function messagesLoaded(data)
{
	markovList.SetMessages(data);
	ids = markovList.GetPoliticians();
	for(i = 0; i < ids.length; i++)
	{
		scrapeName(ids[i]);
	}
	
	// get politicians
	if (markovList.HasMessages())
	{
		setInterval(addNewMessage, 3000);
	}
}	

function addNewMessage()
{
	if(!markovList.HasMessages())
	{
		//markovList.LoadMessages();
		return;
	}

	var message = markovList.GetNextMessage();	
	console.log(message.content);
	console.log(message.content);

	var templateName = "#message-template";
	if (count % 2 == 1){
		templateName = "#message-alt-template";
	}	

	if (message.politician_id == 10000)
	{
		return;
	}

	if (message.content.trim().length == 0)
	{
		return;
	}


	var pname = politicians[message.politician_id];
	if (pname.indexOf("500") != -1)
	{
		pname = "Politician " + message.politician_id;
	}



	var source   = $(templateName).html();
	var template = Handlebars.compile(source);
	var context = {politician_id : message.politician_id, content : message.content, name : pname, type : message.type };
	var html    = template(context);
	var middleColumn = $('#middle-column');
	middleColumn.append(html);
	var newMessageElement = $('#message-' + count);
	newMessageElement.hide();
	newMessageElement.slideDown(400);
	count++;
}

function appendMessageDiv(message)
{
	var message = markovList.GetNextMessage();	
	var source   = $("#entry-template").html();
	var template = Handlebars.compile(source);
	var context = message
	var html    = template(context);
	var middleColumn = $('#middle-column');
}

function scrapeName(id)
{
	$.ajax({
		method: "GET",
		url: "http://www.aph.gov.au/Senators_and_Members/Parliamentarian?MPID="+id,
		dataType: "text",
		crossDomain: true,
		success: function(data) { 
			var namergx = /<h1>([^\<]*)<\/h1>/;
			var bodyHtml = data;//"<h1><a href=fffff></a></h1><h1>Hon Malcolm Turnbull</h1>";
			var match = namergx.exec(bodyHtml); 
			politicians[id] = match[1].replace("Hon ", "").replace(" MP","");
		}
	});
}