angular.module('directoryApp', [])
	.controller('directoryController', function() { // dont need to pass, this refers to controller
		
		var dirList = this; // we want to namespace this to controller

		dirList.toggle = false; // hide the names first

		// adding to scope means making visible to HTML
		dirList.list = [
			{name:'scott', age : '20', img:'https://s3.amazonaws.com/uifaces/faces/twitter/zeldman/128.jpg'}, 
			{name:'ben', age : '44', img:'https://s3.amazonaws.com/uifaces/faces/twitter/zeldman/128.jpg'}, 
			{name:'ross', age : '31', img:'https://s3.amazonaws.com/uifaces/faces/twitter/zeldman/128.jpg'},
			{name: 'jesse', age: '22', img:'https://s3.amazonaws.com/uifaces/faces/twitter/zeldman/128.jpg'}
		];

		dirList.addPerson = function() {
			dirList.list.push(
				{name: dirList.name, 
				 age:  dirList.age
				});
			dirList.name = '';
			dirList.age = 0;
		};
	});