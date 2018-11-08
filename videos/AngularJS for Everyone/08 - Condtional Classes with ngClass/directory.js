angular.module('directoryApp', [])
	.controller('directoryController', function() { // dont need to pass, this refers to controller
		
		var dirList = this; // we want to namespace this to controller

		dirList.toggle = false; // hide the names first

		// adding to scope means making visible to HTML
		dirList.list = [
			{name:'scott', age : '20'}, 
			{name:'ben', age : '44'}, 
			{name:'ross', age : '31'},
			{name: 'jesse', age: '22'}
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