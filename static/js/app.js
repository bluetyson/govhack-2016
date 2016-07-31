$( document ).ready(
	runApp
)


// A SINGLE MESSAGE LOOKS LIKE THIS 
/*
{
	order,
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
	markovList.LoadMessages();

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

	var templateName = "#message-template";
	if (message.order % 2 == 1){
		templateName = "#message-alt-template";
	}

	var source   = $(templateName).html();
	var template = Handlebars.compile(source);
	var context = message
	var html    = template(context);
	var middleColumn = $('#middle-column');
	middleColumn.append(html);
	var newMessageElement = $('#message-' + message.order);
	newMessageElement.hide();
	newMessageElement.slideDown(400);
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