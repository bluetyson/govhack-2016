$( document ).ready(
	//runApp
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
		politicianId: 'R36',
		type: 'talk',
		content: 'I am the best person ever'
	},	
	{
		order: 2,
		politicianId: 'R36',
		type: 'talk',
		content: 'I totally am! o:'
	},	
	{
		order: 1,
		politicianId: '885',
		type: 'talk',
		content: 'No you are not!'
	}
]




function runApp(){
	var source   = $("#entry-template").html();
	var template = Handlebars.compile(source);
	var context = {politicianId: "21341", content: "This is my first post!"};
	var html    = template(context);
	var middleColumn = $('#middle-column');
	middleColumn.append(html);
	markovList.LoadMessages();

	if (markovList.HasMessages())
	{
		setInterval(addNewMessage,500);
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
	var source   = $("#entry-template").html();
	var template = Handlebars.compile(source);
	var context = message
	var html    = template(context);
	var middleColumn = $('#middle-column');
	middleColumn.append(html);
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