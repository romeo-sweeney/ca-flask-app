function copyToClipboard(elementId) {
    var copyText = document.getElementById(elementId);
    var range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");

    var copyStatus = document.getElementById("copy-status");
    copyStatus.textContent = "Copied!";
    copyStatus.parentElement.classList.add("copied");

    setTimeout(function () {
        copyStatus.textContent = ""; // Reset the copy status after a delay
        copyStatus.parentElement.classList.remove("copied");
    }, 1500); // Adjust the delay as needed
}
