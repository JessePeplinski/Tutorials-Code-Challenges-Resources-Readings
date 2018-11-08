angular.module('directoryApp', [])
	.controller('directoryController', function($scope) {
		$scope.list = [
			{name:'scott', age : '20'}, 
			{name:'ben', age : '44'}, 
			{name:'ross', age : '31'},
			{name: 'jesse', age: '22'}
		];

	$scope.addPerson = function() {
		$scope.list.push(
			{name: $scope.name, 
			 age:  $scope.age
			});
		$scope.name = '';
		$scope.age = 0;
		};
	});