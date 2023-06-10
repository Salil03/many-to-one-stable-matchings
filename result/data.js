var nbMen = 13;
var nbWomen = 11;
var nbMatchings = 7;
var nbRotations = 6;
var downset = [
[1,0,0,0,0,0],
[1,1,0,0,0,0],
[1,1,1,0,0,0],
[1,1,1,1,0,0],
[1,1,1,1,1,0],
[1,1,1,1,0,1],
[1,1,1,1,1,1]
];
var transition = [
[0,1,2,3,4,5],
[0,0,2,3,4,5],
[0,0,1,3,4,5],
[0,0,1,2,4,5],
[0,0,1,2,3,6],
[0,0,1,2,6,3],
[0,0,1,2,5,4]
];
var prefM = [
[2,3,4,5,1,-1,-1,1,2,3,1,2,2],
[2,4,5,6,1,-1,-1,1,2,3,2,3,5],
[2,4,6,7,1,-1,-1,1,3,4,3,4,5],
[4,6,7,9,1,-1,-1,1,4,5,3,5,7],
[4,6,7,10,1,-1,-1,1,5,7,3,5,7],
[4,6,7,9,1,-1,-1,1,4,5,5,7,8],
[4,6,7,10,1,-1,-1,1,5,7,5,7,8]
];
var prefW = [
[8,8,5,8,2,2,0,5,2,7,4],
[7,7,5,7,1,2,0,5,2,6,2],
[7,6,4,4,1,2,0,3,2,5,1],
[6,5,2,2,0,2,0,2,1,4,1],
[2,3,2,1,0,2,0,2,1,4,1],
[6,5,1,2,0,2,0,2,0,4,0],
[2,3,1,1,0,2,0,2,0,4,0]
];
var stableM = [
[-1,-1,0,-1,3,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,0,1,-1,3,-1,-1,-1,-1],
[-1,-1,-1,-1,0,1,2,3,-1,-1,-1],
[-1,-1,-1,-1,-1,0,1,2,-1,3,4],
[-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,0,2,3,4,-1,-1,-1,-1,-1],
[-1,-1,-1,0,2,3,-1,4,-1,-1,-1],
[-1,0,1,2,-1,5,-1,-1,-1,-1,-1],
[-1,-1,0,1,2,3,-1,5,-1,-1,-1],
[-1,-1,0,-1,-1,1,-1,3,5,-1,-1]
];
var stableW = [
[-1,-1,4,-1,-1,-1,3,1,0,-1,-1,-1,-1],
[-1,-1,-1,4,-1,3,2,1,0,-1,-1,-1,-1],
[-1,5,3,-1,2,0,-1,-1,-1,-1,-1,-1,-1],
[-1,4,3,-1,2,-1,-1,1,0,-1,-1,-1,-1],
[3,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,3,2,-1,0,-1,-1,-1,-1,-1,-1,-1],
[5,3,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,3,2,1,0,-1,-1,-1,-1,-1],
[5,2,1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1]
];
