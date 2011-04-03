load=function(){
    var script=document.createElement('script');
    script.setAttribute('type','text/javascript');
    script.setAttribute('src','http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js');
    if(typeof script!='undefined'){
        document.getElementsByTagName('head')[0].appendChild(script)}
    tryReady(0);
    };
tryReady=function(time_elapsed){


    if(typeof $=='undefined'){
        if(time_elapsed<=5000){
            setTimeout('tryReady('+(time_elapsed+200)+')',200);} 
        else{alert('Timed out while loading jQuery.');}
    }
    else{$(function(){
        var params='?url='+window.location;
        if($('a[rel*=license]').attr('href')){
            params+='&license='+$('a[rel*=license]').attr('href');}
        if($('title').html()){
            params+='&title='+$('title').html();}
        if($('meta[name=author]').attr('content')){
            params+='&author='+$('meta[name=author]').attr('content');}
        if($('meta[name*=publisher]').attr('content')){
            params+='&publisher='+$('meta[name*=publisher]').attr('content');}
        window.location='http://localhost:8110/bookmarks/add/'+params;
        });
        }};
load();
