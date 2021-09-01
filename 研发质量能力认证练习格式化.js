const fs = require('fs')
const fileName = '【通用】研发质量能力认证练习20210823';
const data = require(`./${fileName}.json`);

const option = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
let resultList = [];
for (let i = 0,len = data.length; i < len; i++) {
  let arr = [];
  for (let j = 0, leng = data[i].length; j < leng; j++) {
    let obj = {};
    obj.topicContent = data[i][j].topicContent;
    let answerStr = '';
    let answerContent = '';
    let list = data[i][j].topicOptionVos.map((item, index)=> {
      if (item.optionValue === 1) {
        answerStr += option[index];
        answerContent+= option[index] + ':' + item.optionContent + '-----------------'
      }
    })
    obj.answer = answerStr;
    obj.answerContent = answerContent;
    arr.push(obj)
  }
  resultList.push(arr)
}
fs.writeFile('./'+fileName+'ok.js', JSON.stringify(resultList), function(err, data) {
  console.log('fs.writeFile err', err)
  console.log('fs.writeFile data', data)
})