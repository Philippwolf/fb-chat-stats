var layout = {  height: 400,  width: 500,  showlegend: {"orientation": "h"} };var data = [{  values: ["2971","2872",],  labels: ["Someone","Bartek Górkiewicz",],  type: 'pie',  marker: {

colors: [    "#d83434","#ff9999",

]},  name: "Who texts the most",  textinfo:'none',  hole: .6,}];var data2 = [  {    x: ['00:00', '01:00', '02:00','03:00', '04:00', '05:00','06:00', '07:00', '08:00','09:00', '10:00', '11:00','12:00', '13:00', '14:00','15:00', '16:00', '17:00','18:00', '19:00', '20:00','21:00', '22:00', '23:00'],    y: [550,87,82,15,32,0,1,10,70,72,76,298,136,199,207,298,275,304,689,247,305,918,448,524,],    type: 'bar',    marker: {     

 color: "#d83434", 

 },  }];var data3 = [  {    x: ["2 września 2014 ","6 września 2014 ","8 września 2014 ","9 września 2014 ","15 września 2014 ","22 września 2014 ","29 września 2014 ","30 września 2014 ","4 października 2014 ","13 października 2014 ","15 października 2014 ","16 października 2014 ","19 października 2014 ","20 października 2014 ","21 października 2014 ","22 października 2014 ","24 października 2014 ","25 października 2014 ","27 października 2014 ","29 października 2014 ","6 listopada 2014 ","7 listopada 2014 ","16 listopada 2014 ","27 listopada 2014 ","1 grudnia 2014 ","2 grudnia 2014 ","3 grudnia 2014 ","11 grudnia 2014 ","26 grudnia 2014 ","27 grudnia 2014 ","30 grudnia 2014 ","29 stycznia 2015 ","11 marca 2015 ","26 marca 2015 ","3 kwietnia 2015 ","15 kwietnia 2015 ","27 kwietnia 2015 ","28 kwietnia 2015 ","3 maja 2015 ","14 maja 2015 ","15 maja 2015 ","16 maja 2015 ","17 maja 2015 ","18 maja 2015 ","19 maja 2015 ","20 maja 2015 ","21 maja 2015 ","22 maja 2015 ","2 czerwca 2015 ","4 czerwca 2015 ","15 czerwca 2015 ","17 czerwca 2015 ","2 lipca 2015 ","8 sierpnia 2015 ","2 września 2015 ","3 września 2015 ","4 września 2015 ","6 września 2015 ","7 września 2015 ","8 września 2015 ","9 września 2015 ","12 września 2015 ","13 września 2015 ","14 września 2015 ","15 września 2015 ","21 września 2015 ","22 września 2015 ","23 września 2015 ","24 września 2015 ","30 września 2015 ","8 października 2015 ","31 października 2015 ","1 listopada 2015 ","10 listopada 2015 ","11 listopada 2015 ","12 listopada 2015 ","23 listopada 2015 ","24 listopada 2015 ","30 listopada 2015 ","9 grudnia 2015 ","11 grudnia 2015 ","19 grudnia 2015 ","22 grudnia 2015 ","8 stycznia 2016 ","10 stycznia 2016 ","16 stycznia 2016 ","18 stycznia 2016 ","23 stycznia 2016 ","25 stycznia 2016 ","31 stycznia 2016 ","10 lutego 2016 ","14 lutego 2016 ","29 lutego 2016 ","2 marca 2016 ","8 marca 2016 ","24 marca 2016 ","1 kwietnia 2016 ","7 kwietnia 2016 ","26 kwietnia 2016 ","11 maja 2016 ","22 maja 2016 ","24 maja 2016 ","13 czerwca 2016 ","14 czerwca 2016 ","15 czerwca 2016 ","16 czerwca 2016 ","17 czerwca 2016 ","20 czerwca 2016 ","1 sierpnia 2016 ","3 sierpnia 2016 ","16 sierpnia 2016 ","30 sierpnia 2016 ","1 września 2016 ","11 września 2016 ","15 września 2016 ","22 września 2016 ","4 października 2016 ","5 października 2016 ","8 października 2016 ","9 października 2016 ","12 października 2016 ","16 października 2016 ","17 października 2016 ","19 października 2016 ","20 października 2016 ","23 października 2016 ","25 października 2016 ","26 października 2016 ","3 listopada 2016 ","7 listopada 2016 ","8 listopada 2016 ","9 listopada 2016 ","14 listopada 2016 ","15 listopada 2016 ","16 listopada 2016 ","21 listopada 2016 ","23 listopada 2016 ","1 grudnia 2016 ","5 grudnia 2016 ","7 grudnia 2016 ","8 grudnia 2016 ","9 grudnia 2016 ","20 grudnia 2016 ","2 stycznia 2017 ","9 lutego 2017 ","13 lutego 2017 ","14 lutego 2017 ","20 lutego 2017 ","22 lutego 2017 ","4 marca 2017 ","7 marca 2017 ","8 marca 2017 ","13 marca 2017 ","15 marca 2017 ","16 marca 2017 ","17 marca 2017 ","5 kwietnia 2017 ","21 kwietnia 2017 ","24 kwietnia 2017 ","27 kwietnia 2017 ","28 kwietnia 2017 ","5 maja 2017 ","12 maja 2017 ","1 czerwca 2017 ","9 czerwca 2017 ","13 czerwca 2017 ","23 czerwca 2017 ","27 czerwca 2017 ","4 lipca 2017 ","5 lipca 2017 ","9 lipca 2017 ","10 lipca 2017 ","15 lipca 2017 ","25 lipca 2017 ","28 lipca 2017 ","29 lipca 2017 ","7 września 2017 ","9 września 2017 ","29 września 2017 ","30 września 2017 ","1 października 2017 ","2 października 2017 ","3 października 2017 ","6 października 2017 ","7 października 2017 ","8 października 2017 ","12 października 2017 ","15 października 2017 ","18 października 2017 ","19 października 2017 ","20 października 2017 ","21 października 2017 ","22 października 2017 ","24 października 2017 ","25 października 2017 ","1 grudnia 2017 ","3 grudnia 2017 ","4 grudnia 2017 ","5 grudnia 2017 ","20 grudnia 2017 ","4 stycznia 2018 ","5 stycznia 2018 ","7 stycznia 2018 ","9 stycznia 2018 ","10 stycznia 2018 ","31 stycznia 2018 ","4 lutego 2018 ","6 lutego 2018 ","7 lutego 2018 ","8 lutego 2018 ","9 lutego 2018 ",],y: [20,5,6,186,16,63,45,53,11,3,4,6,17,68,4,3,20,1,3,10,27,1,7,36,43,8,13,1,1,6,18,23,6,19,2,2,125,78,25,44,28,3,11,12,19,3,12,25,10,11,11,23,2,32,12,57,21,19,28,46,7,4,31,6,11,23,2,33,3,6,5,379,12,7,2,6,182,20,32,25,2,2,21,3,15,2,11,1,1,6,1,1,1,29,11,1,51,1,1,15,29,1,26,196,513,10,31,27,19,42,11,3,1,9,3,1,19,33,9,2,4,25,3,33,41,3,27,38,26,2,2,83,39,20,1,2,14,22,20,59,121,28,106,18,1,77,24,66,3,24,1,4,18,9,29,90,54,41,39,73,1,6,29,5,7,18,14,35,18,19,6,53,3,33,16,8,11,6,5,13,1,1,1,19,43,3,44,16,21,23,63,55,12,7,15,69,37,5,18,131,33,8,8,7,32,15,16,2,104,51,16,],    type: 'bar',    marker: {      

 color: "#d83434", 

  },  }];var data4 = [  {    x: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",],    y: [1094,1064,1421,749,597,607,311,],    type: 'bar',    marker: {    

  color: "#d83434", 

 },  }];var data5 = [  {    x: [String.fromCodePoint(0x1f612),String.fromCodePoint(0x1f620),String.fromCodePoint(0x1f60f),String.fromCodePoint(0x1f604),String.fromCodePoint(0x1f60e),String.fromCodePoint(0x1f611),String.fromCodePoint(0x1f62d),String.fromCodePoint(0x1f605),String.fromCodePoint(0x1f60d),String.fromCodePoint(0x1f62e),],    y: [7,5,4,3,3,3,3,2,2,2,],    type: 'bar',    marker: {   

   color: "#d83434", 

 },  }];var data6 = [  {    x: ["nie","to","i","na","sie","a","no","w","ze","xd",],    y: [649,559,402,291,270,261,260,246,236,233,],    type: 'bar',    marker: {    

  color: "#d83434", 

 },  }];