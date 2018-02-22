var layout = {  height: 400,  width: 500,  showlegend: {"orientation": "h"} };var data = [{  values: ["23","23",],  labels: ["Bartek Górkiewicz","Someone",],  type: 'pie',  marker: {

colors: [    "#d83434","#ff9999",

]},  name: "Who texts the most",  textinfo:'none',  hole: .6,}];var data2 = [  {    x: ['00:00', '01:00', '02:00','03:00', '04:00', '05:00','06:00', '07:00', '08:00','09:00', '10:00', '11:00','12:00', '13:00', '14:00','15:00', '16:00', '17:00','18:00', '19:00', '20:00','21:00', '22:00', '23:00'],    y: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,24,0,],    type: 'bar',    marker: {     

 color: "#d83434", 

 },  }];var data3 = [  {    x: ["15 kwietnia 2017 ",],y: [46,],    type: 'bar',    marker: {      

 color: "#d83434", 

  },  }];var data4 = [  {    x: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",],    y: [0,0,0,0,0,46,0,],    type: 'bar',    marker: {    

  color: "#d83434", 

 },  }];var data5 = [  {    x: [String.fromCodePoint(0x1f648),String.fromCodePoint(0x1f60f),String.fromCodePoint(0x1f604),String.fromCodePoint(0x1f60a),String.fromCodePoint(0x1f618),String.fromCodePoint(0x1f61c),String.fromCodePoint(0x1f628),String.fromCodePoint(0x1f436),String.fromCodePoint(0x1f431),String.fromCodePoint(0x1f42d),],    y: [5,4,1,1,1,1,1,0,0,0,],    type: 'bar',    marker: {   

   color: "#d83434", 

 },  }];var data6 = [  {    x: ["nie","to","ze","tak","ale","w","no","x","sie","co",],    y: [22,12,9,9,8,8,7,7,7,6,],    type: 'bar',    marker: {    

  color: "#d83434", 

 },  }];