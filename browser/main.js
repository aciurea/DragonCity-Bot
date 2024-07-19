const delay = (time) => {
    return new Promise((resolve) => {
        const id = setTimeout(() => {
            resolve();
            clearTimeout(id);
        }, time);
    });
    
};

(async () => {
    let times = 7;

    while (times > 0) {
        times--;
        const elements = document.querySelectorAll('[data-testid="list-view-buy-button"]');

        if(!elements?.length) {
            await delay(1000);
            continue;
        }

        elements?.forEach((el) => {
            if(!el?.textContent?.includes("€")) {
                console.log('clicking on element');
                el?.click();
            } else {
                console.log(el?.textContent);
            }
        });

        times = 0;
    }

    await delay(1000)
    const key = "dc-automation";
    if(sessionStorage.getItem(key) === "true") return;

    window.location.href = "https://www.dragoncitygame.com/";
    sessionStorage.setItem(key, "true");
})();