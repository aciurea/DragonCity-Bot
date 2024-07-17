console.log('main.js loaded');

const delay = (fn, time) => {
    const id = setTimeout(() => {
        fn();
        clearTimeout(id);
    }, time);
};

const elements = document.querySelectorAll('[data-testid="list-view-buy-button"]');

elements?.forEach((el) => {
    if(!el?.textContent?.includes("€")) {
        el?.click();
    } else {
        console.log(el?.textContent);
    }
});

console.log(sessionStorage);

delay(() => {
    const key =  "dc-automation";
    if(sessionStorage.getItem(key) === "true") return;

    window.location.href = "https://www.dragoncitygame.com/";
    sessionStorage.setItem(key, "true");
}, 3000);
