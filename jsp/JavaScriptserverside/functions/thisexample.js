// const video = {
//     title:'a',
//     play()
//     {
//         console.log(this);
//     }
// };
// video.play();
// video.stop = function()
// {
//     console.log(this);
// }
// video.stop();

// function Video(title)
// {
//     this.title=title;
//     console.log(this);
// }

//onsole.log(v);

//another use case of this
const test={
    title:'a',
    tags:['a','b','c'],
    showTags()
    {
        this.tags.forEach(function(tag)
            {
console.log(this,tag);
            },this);
        
    }
};
test.showTags();