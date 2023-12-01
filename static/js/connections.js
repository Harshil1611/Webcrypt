function showfields() {
    const bool = document.getElementById("chkbox");
    if (bool.checked === true) {
        document.getElementById('c_name').style.display = "";
        document.getElementById('connections').style.display = "";
    } else {
        document.getElementById('connections').style.display = "none";
        document.getElementById('c_name').style.display = "none";
    }
}