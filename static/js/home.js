function enc_hide() {
    if (document.getElementById('enc_selectchoice').options[document.getElementById('enc_selectchoice').selectedIndex].value === "enc_text") {
        document.getElementById('enc_text-field').style.display = "";
        document.getElementById('enc_text-field1').style.display = "";
        document.getElementById('enc_img-field').style.display = "none";
        document.getElementById('enc_img-field1').style.display = "none";
        document.getElementById('enc_bin-field').style.display = "none";
        document.getElementById('enc_bin-field1').style.display = "none";
        document.getElementById('enc_steg_text').setAttribute('required', '');
        document.getElementById('enc_c_img').removeAttribute('required');
        document.getElementById('enc_c_bfile').removeAttribute('required');
    } else if (document.getElementById('enc_selectchoice').options[document.getElementById('enc_selectchoice').selectedIndex].value === "enc_image") {
        document.getElementById('enc_img-field').style.display = "";
        document.getElementById('enc_img-field1').style.display = "";
        document.getElementById('enc_bin-field').style.display = "none";
        document.getElementById('enc_bin-field1').style.display = "none";
        document.getElementById('enc_text-field').style.display = "none";
        document.getElementById('enc_text-field1').style.display = "none";
        document.getElementById('enc_c_img').setAttribute('required', '');
        document.getElementById('enc_steg_text').removeAttribute('required');
        document.getElementById('enc_c_bfile').removeAttribute('required');
    } else if (document.getElementById('enc_selectchoice').options[document.getElementById('enc_selectchoice').selectedIndex].value == "enc_binary") {
        document.getElementById('enc_bin-field').style.display = "";
        document.getElementById('enc_bin-field1').style.display = "";
        document.getElementById('enc_img-field').style.display = "none";
        document.getElementById('enc_img-field1').style.display = "none";
        document.getElementById('enc_text-field').style.display = "none";
        document.getElementById('enc_text-field1').style.display = "none";
        document.getElementById('enc_c_bfile').setAttribute('required', '');
        document.getElementById('enc_steg_text').removeAttribute('required');
        document.getElementById('enc_c_img').removeAttribute('required');
    }
}

function dec_hide() {
    if (document.getElementById('dec_selectchoice').options[document.getElementById('dec_selectchoice').selectedIndex].value == "dec_text") {
        document.getElementById('dec_text-field').style.display = "";
        document.getElementById('dec_text-field1').style.display = "";
    } else {
        document.getElementById('dec_text-field').style.display = "none";
        document.getElementById('dec_text-field1').style.display = "none";
    }
}

function dec_method() {
    document.getElementById('dec_steg_text').innerHTML = '{{ dec_text }}';
}

function copy_text() {
    /* Get the text field */
    var copyText = document.getElementById("dec_steg_text");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
    if (copyText.value !== '') {
        /* Alert the copied text */
        alert("Copied the text: " + copyText.value + "\nCheck your Clipboard!");
    } else {
        alert('Textbox does not contains any values! please select file and retrieve data first!');
    }
}