
var data = [{
  values: [36337, 31032],
  labels: ['Bartek', 'Zuzia'],
  type: 'pie',
  marker: {colors: [
    "#d83434",
    "#ff9999"
  ]},
  name: "Kto więcej pisze",
  textinfo:'none',
  hole: .6,
}];

var layout = {
  height: 400,
  width: 500,
  showlegend: {"orientation": "h"}
};

var data2 = [
  {
    x: ['00:00', '01:00', '02:00','03:00', '04:00', '05:00','06:00', '07:00', '08:00','09:00', '10:00', '11:00','12:00', '13:00', '14:00','15:00', '16:00', '17:00','18:00', '19:00', '20:00','21:00', '22:00', '23:00'],
    y: [8495, 3147, 1477, 459, 78, 3, 71, 323,360,742,1560,2072,3221,4248,4484,3293,2099,2347,2408,3479,4107,5662,5935,7299],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

var data3 = [
  {
    x: ["8 grudnia 2016 ","9 grudnia 2016 ","17 grudnia 2016 ","18 grudnia 2016 ","24 grudnia 2016 ","31 grudnia 2016 ","1 stycznia 2017 ","2 stycznia 2017 ","23 lutego 2017 ","7 kwietnia 2017 ","8 kwietnia 2017 ","9 kwietnia 2017 ","11 kwietnia 2017 ","12 kwietnia 2017 ","13 kwietnia 2017 ","14 kwietnia 2017 ","15 kwietnia 2017 ","16 kwietnia 2017 ","17 kwietnia 2017 ","18 kwietnia 2017 ","19 kwietnia 2017 ","25 kwietnia 2017 ","26 kwietnia 2017 ","27 kwietnia 2017 ","29 kwietnia 2017 ","30 kwietnia 2017 ","5 maja 2017 ","6 maja 2017 ","7 maja 2017 ","8 maja 2017 ","10 maja 2017 ","11 maja 2017 ","12 maja 2017 ","13 maja 2017 ","14 maja 2017 ","15 maja 2017 ","16 maja 2017 ","17 maja 2017 ","18 maja 2017 ","19 maja 2017 ","20 maja 2017 ","21 maja 2017 ","22 maja 2017 ","23 maja 2017 ","24 maja 2017 ","25 maja 2017 ","26 maja 2017 ","27 maja 2017 ","28 maja 2017 ","29 maja 2017 ","30 maja 2017 ","31 maja 2017 ","1 czerwca 2017 ","2 czerwca 2017 ","3 czerwca 2017 ","4 czerwca 2017 ","5 czerwca 2017 ","6 czerwca 2017 ","7 czerwca 2017 ","8 czerwca 2017 ","9 czerwca 2017 ","10 czerwca 2017 ","11 czerwca 2017 ","12 czerwca 2017 ","13 czerwca 2017 ","14 czerwca 2017 ","15 czerwca 2017 ","16 czerwca 2017 ","17 czerwca 2017 ","18 czerwca 2017 ","19 czerwca 2017 ","20 czerwca 2017 ","21 czerwca 2017 ","22 czerwca 2017 ","23 czerwca 2017 ","24 czerwca 2017 ","25 czerwca 2017 ","26 czerwca 2017 ","27 czerwca 2017 ","29 czerwca 2017 ","30 czerwca 2017 ","1 lipca 2017 ","2 lipca 2017 ","3 lipca 2017 ","4 lipca 2017 ","5 lipca 2017 ","6 lipca 2017 ","7 lipca 2017 ","8 lipca 2017 ","9 lipca 2017 ","10 lipca 2017 ","11 lipca 2017 ","12 lipca 2017 ","13 lipca 2017 ","14 lipca 2017 ","16 lipca 2017 ","17 lipca 2017 ","18 lipca 2017 ","19 lipca 2017 ","20 lipca 2017 ","21 lipca 2017 ","22 lipca 2017 ","23 lipca 2017 ","24 lipca 2017 ","25 lipca 2017 ","26 lipca 2017 ","27 lipca 2017 ","29 lipca 2017 ","30 lipca 2017 ","31 lipca 2017 ","1 sierpnia 2017 ","2 sierpnia 2017 ","3 sierpnia 2017 ","4 sierpnia 2017 ","5 sierpnia 2017 ","6 sierpnia 2017 ","7 sierpnia 2017 ","8 sierpnia 2017 ","9 sierpnia 2017 ","10 sierpnia 2017 ","11 sierpnia 2017 ","12 sierpnia 2017 ","13 sierpnia 2017 ","14 sierpnia 2017 ","15 sierpnia 2017 ","16 sierpnia 2017 ","17 sierpnia 2017 ","18 sierpnia 2017 ","19 sierpnia 2017 ","20 sierpnia 2017 ","21 sierpnia 2017 ","22 sierpnia 2017 ","23 sierpnia 2017 ","24 sierpnia 2017 ","25 sierpnia 2017 ","26 sierpnia 2017 ","27 sierpnia 2017 ","28 sierpnia 2017 ","29 sierpnia 2017 ","30 sierpnia 2017 ","31 sierpnia 2017 ","1 września 2017 ","2 września 2017 ","3 września 2017 ","4 września 2017 ","5 września 2017 ","6 września 2017 ","7 września 2017 ","8 września 2017 ","9 września 2017 ","10 września 2017 ","11 września 2017 ","12 września 2017 ","13 września 2017 ","14 września 2017 ","15 września 2017 ","16 września 2017 ","17 września 2017 ","18 września 2017 ","19 września 2017 ","20 września 2017 ","21 września 2017 ","22 września 2017 ","23 września 2017 ","24 września 2017 ","25 września 2017 ","26 września 2017 ","27 września 2017 ","28 września 2017 ","29 września 2017 ","30 września 2017 ","1 października 2017 ","2 października 2017 ","5 października 2017 ","6 października 2017 ","7 października 2017 ","8 października 2017 ","9 października 2017 ","10 października 2017 ","11 października 2017 ","12 października 2017 ","13 października 2017 ","14 października 2017 ","15 października 2017 ","16 października 2017 ","17 października 2017 ","18 października 2017 ","19 października 2017 ","20 października 2017 ","21 października 2017 ","22 października 2017 ","23 października 2017 ","24 października 2017 ","25 października 2017 ","26 października 2017 ","27 października 2017 ","28 października 2017 ","29 października 2017 ","30 października 2017 ","31 października 2017 ","1 listopada 2017 ","2 listopada 2017 ","3 listopada 2017 ","4 listopada 2017 ","5 listopada 2017 ","6 listopada 2017 ","7 listopada 2017 ","8 listopada 2017 ","9 listopada 2017 ","11 listopada 2017 ","12 listopada 2017 ","13 listopada 2017 ","14 listopada 2017 ","15 listopada 2017 ","16 listopada 2017 ","17 listopada 2017 ","18 listopada 2017 ","19 listopada 2017 ","20 listopada 2017 ","21 listopada 2017 ","22 listopada 2017 ","23 listopada 2017 ","24 listopada 2017 ","25 listopada 2017 ","26 listopada 2017 ","27 listopada 2017 ","28 listopada 2017 ","29 listopada 2017 ","30 listopada 2017 ","1 grudnia 2017 ","2 grudnia 2017 ","3 grudnia 2017 ","4 grudnia 2017 ","5 grudnia 2017 ","6 grudnia 2017 ","7 grudnia 2017 ","8 grudnia 2017 ","10 grudnia 2017 ","11 grudnia 2017 ","12 grudnia 2017 ","13 grudnia 2017 ","14 grudnia 2017 ","15 grudnia 2017 ","16 grudnia 2017 ","17 grudnia 2017 ","18 grudnia 2017 ","21 grudnia 2017 ","22 grudnia 2017 ","24 grudnia 2017 ","25 grudnia 2017 ","27 grudnia 2017 ","28 grudnia 2017 ","29 grudnia 2017 ","30 grudnia 2017 ","1 stycznia 2018 ","2 stycznia 2018 ","4 stycznia 2018 ","5 stycznia 2018 ","6 stycznia 2018 ","7 stycznia 2018 ","8 stycznia 2018 ","9 stycznia 2018 ","10 stycznia 2018 ","11 stycznia 2018 ","12 stycznia 2018 ","13 stycznia 2018 ","14 stycznia 2018 ","15 stycznia 2018 ","16 stycznia 2018 ","17 stycznia 2018 ","18 stycznia 2018 ","19 stycznia 2018 ","20 stycznia 2018 ","21 stycznia 2018 ","22 stycznia 2018 ","23 stycznia 2018 ","25 stycznia 2018 ","26 stycznia 2018 ","27 stycznia 2018 ","28 stycznia 2018 ","29 stycznia 2018 ","30 stycznia 2018 ","31 stycznia 2018 ","1 lutego 2018 ","2 lutego 2018 ","3 lutego 2018 ","4 lutego 2018 ","5 lutego 2018 ","7 lutego 2018 ","8 lutego 2018 ","9 lutego 2018 ","10 lutego 2018 ","11 lutego 2018 ","12 lutego 2018 ","13 lutego 2018 ","14 lutego 2018 "
],
    y: [2,20,70,2,2,15,95,125,4,4,5,3,407,4,121,76,188,67,70,5,201,298,270,149,65,314,72,125,132,111,10,59,126,14,320,62,397,189,177,18,68,295,113,166,215,232,223,55,857,259,210,425,446,399,620,489,649,234,269,721,176,231,633,359,78,462,297,51,378,678,115,212,113,110,577,654,463,425,337,206,375,188,13,233,152,55,147,287,30,147,244,645,292,369,244,285,430,306,102,691,109,87,8,111,43,35,39,30,38,497,111,9,6,63,116,31,314,155,93,23,318,96,482,295,539,254,304,395,1363,1200,1045,224,69,331,336,9,31,373,720,689,192,179,138,139,49,334,286,380,12,63,149,373,221,172,106,84,39,21,65,172,170,15,13,135,181,112,425,420,260,216,33,309,69,183,100,81,395,1032,414,714,278,7,11,681,519,223,710,861,33,80,292,570,910,214,401,22,137,95,705,152,268,619,2,39,158,372,143,102,280,8,2,152,522,645,277,89,20,157,312,385,59,62,62,56,15,281,232,237,529,134,67,13,226,577,126,273,200,56,214,3,2,28,4,341,77,32,236,245,214,127,78,283,13,1,79,244,88,88,105,66,184,597,182,251,163,40,22,25,62,321,341,140,37,576,30,32,132,54,10,270,150,85,151,310,182,28,31,2,285,699,666,397,266,263,322,265
],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

var data4 = [
  {
    x: ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'],
    y: [11773,11294,9164,11518,6577,6275,10768],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

var data5 = [
  {
    x: [String.fromCodePoint(0x1F612), String.fromCodePoint(0x1F60F), String.fromCodePoint(0x1F618), String.fromCodePoint(0x1F60A), String.fromCodePoint(0x1F602), String.fromCodePoint(0x1F620), String.fromCodePoint(0x1F61A)],
    y: [584,388,274,235,183,182,162],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

var data6 = [
  {
    x: ['nie', 'to', 'no', 'i', 'xd', 'w', 'jak', 'a', 'ale', 'sie'],
    y: [12341,8242,5134,4620,3650,3269,3063,2988,2935,2820],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

var data7 = [{
  values: [12341, 2635],
  labels: ['Nie - 12341', 'Tak - 2635'],
  type: 'pie',
  marker: {colors: [
    "#d83434",
    "#ff9999"
  ]},
  name: "Tak vs Nie",
  textinfo:'none',
  hole: .6,
}];

var data8 = [{
  values: [13, 5],
  labels: ['Kocham - 13', 'Nienawidze - 5'],
  type: 'pie',
  marker: {colors: [
    "#d83434",
    "#ff9999"
  ]},
  name: "Kocham vs nienawidze",
  textinfo:'none',
  hole: .6,
}];



