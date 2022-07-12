function displayMenu() {
    var menu = document.getElementById("MyNav");
    menu.style.visibility="visible";
}

function hideMenu(){
    var close = document.getElementById("MyNav");
    close.style.visibility='hidden';
}

function whatsOn(){
    document.getElementById("annex_img").style.display='none';

    if (document.getElementById("new_div") != null){
        let ids = ['new_div','new_heading','new_text'];
        for (let i=0; i<ids.length; i++){
            document.getElementById(ids[i]).style.display = 'block';
        }
    } 

    else{
    var image = document.createElement('img');

    image.src = "/static/rocco-dipoppa-_uDj_lyPVpA-unsplash.jpg";
    image.style.position='relative';
    image.style.width='400px';
    image.style.top='-20px';

    var div = document.createElement('div');
    div.id='new_div';

    var heading = document.createElement('h2');
    heading.id = 'new_heading';

    var text = document.createElement('p');
    text.id = 'new_text';
    
    heading.textContent="WHAT'S ON ?";
    text.textContent='Want to catch our upcoming events! \n';
    text.textContent+='You can even make a reservation online \n';
    text.textContent+='just hit the link and book a seat !';

    div.style.position = 'relative';
    div.style.top = '20vh';
    div.style.left='80px';
    text.style.whiteSpace = 'pre-line';


    document.getElementById("annex").appendChild(div);
    document.getElementById("new_div").appendChild(image);
    document.getElementById("new_div").appendChild(heading);
    document.getElementById("new_div").appendChild(text);

    }
}

function hideWhatsOn(){

    let ids = ['new_div','new_heading','new_text'];
    for (let i=0; i<ids.length; i++){
        document.getElementById(ids[i]).style.display = 'none';
    }
    document.getElementById("annex_img").style.display='inline';

}

function study(){
    document.getElementById("annex_img").style.display='none';

    if (document.getElementById("study_div") != null){
        let ids = ['study_div','study_heading','study_text'];
        for (let i=0; i<ids.length; i++){
            document.getElementById(ids[i]).style.display = 'block';
        }
    } 

    else{
    var image = document.createElement('img');

    image.src = '/static/lorenzo-spoleti-MlhJNEUQpBs-unsplash.jpg';
    image.style.position='relative';
    image.style.width='400px';
    image.style.top='-20px';

    var div = document.createElement('div');
    div.id='study_div';

    var heading = document.createElement('h2');
    heading.id = 'study_heading';

    var text = document.createElement('p');
    text.id = 'study_text';
    
    heading.textContent="STUDY";
    text.textContent='See more about our study program, \n';
    text.textContent+='instruments we teach and teachers... \n';

    div.style.position = 'relative';
    div.style.top = '20vh';
    div.style.left='80px';
    text.style.whiteSpace = 'pre-line';


    document.getElementById("annex").appendChild(div);
    document.getElementById("study_div").appendChild(image);
    document.getElementById("study_div").appendChild(heading);
    document.getElementById("study_div").appendChild(text);
    }
}

function hideStudy(){
    let ids = ['study_div','study_heading','study_text'];
    for (let i=0; i<ids.length; i++){
        document.getElementById(ids[i]).style.display = 'none';
    }
    document.getElementById("annex_img").style.display='inline';

}


 


