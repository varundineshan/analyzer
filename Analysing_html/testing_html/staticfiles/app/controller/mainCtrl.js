"use strict";
var app = angular.module('myhomemainCtrl',[])

app.controller("mainCtrl",function($scope,apiFactory){

	$scope.textdata = {};
	$scope.names = ["Emil", "Tobias", "Linus"];

	$scope.accepttext = function(isValid){
		
		if(isValid){
			var calledapt = apiFactory.countword($scope.textdata.selectedname)
			calledapt.then(function(responded){
					$scope.responded = responded.data;
			},function(reason) {
 				 $scope.responded = [{"tag":"data1","value":reason},{"tag":"data2","value":reason}];
 				})
		}
	};
	
})