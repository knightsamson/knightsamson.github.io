var textarea=document.getElementById("textarea");
function makeBig(){
    textarea.style.fontSize="24pt";
}
document.getElementsByName("fancify")[0].addEventListener("change",function(){
    textarea.style.fontWeight="bold";
    textarea.style.color="blue";
    textarea.style.textDecoration="underline"
    alert("styles added to the text area");
})
document.getElementsByName("fancify")[1].addEventListener("change",function(){
    textarea.style.fontWeight="normal";
    textarea.style.color="black";
    textarea.style.textDecoration="none"
    alert("styles removed from the text area");
})
function makeMoo(){
    textarea.style.textTransform="uppercase"
    let str=textarea.value.split(".");
    let str2=str.join("-Moo");
    textarea.value=str2;
}