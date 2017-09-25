angular.module('directoryApp', ['ngAnimate', 'ui.router']) // add ng-animate
	   .config(function($stateProvider, $urlRouterProvider) {

		$urlRouterProvider.otherwise('/'); // if no other routers are picked, go to home

		$stateProvider
			.state('home', {
				url: '/', // can give a route like /home and access with localhost/#/home
				templateUrl: '/static/home.html', // Change to templateUrl to render a file
				controller: 'directoryController as dirList'
			})

			.state('about', {
				url: '/about', // localhost/#/about
				templateUrl: '/static/about.html' // template URL property, reference another template. can also just use html
			});
	})

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
	})
	
	// camelcase is important
	.directive('helloWorld', function() {
		return {
			template: 'Hello World' // output this text in the directive
		}
	});