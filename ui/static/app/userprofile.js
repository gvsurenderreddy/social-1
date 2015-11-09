(function(){

var app = angular.module('app.userprofile', []);

app.controller('UserProfileInfoController', function($scope, $http, $location, $stateParams){
    var userID = $stateParams.user;
    $http.get('/api/user/'+userID+'/userInfo').success(function(data){
        $scope.userprofile = data;
    });
});

app.controller('AddFriendController', function($scope, $http, $location, $stateParams, $rootScope){
    var userId = $rootScope.user.id;
    var otherUserId = $stateParams.user; //bug
    $http.get('/api/user/'+otherUserId+'/userInfo').success(function(data){
        $scope.userprofile = data;
    });
    $scope.addFriend = function(){
    	$http.post('/api/user/addFriend/' + otherUserId ).success(function(data){

    	})
    }
});

})();
