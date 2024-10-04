const delay = (time) => {
    return new Promise((resolve) => {
        const id = setTimeout(() => {
            resolve();
            clearTimeout(id);
        }, time);
    });

};

const URLs = Object.freeze({
    store: "https://www.dragoncitygame.com/",
    dailyStreak: "https://www.dragoncitygame.com/dragon-city-daily-streak",
});
const key = "finished";
const collected = "collected";
const url = "url";

(async () => {
    const storedUrl = sessionStorage.getItem(url);

    if (storedUrl === null) {
        sessionStorage.setItem(url, URLs.dailyStreak);
        window.location.href = URLs.dailyStreak;
        console.log('redirect to dailyStreak');
        return;
    } else sessionStorage.setItem(url, URLs.store);

    await delay(2_000);

    const elements = document.querySelectorAll('[data-testid="list-view-buy-button"]');

    elements?.forEach((el) => {
        if (el?.textContent?.toLowerCase().includes("claim")) {
            el?.click();
            sessionStorage.setItem(collected, "true");
        }
        else console.log(el?.textContent);
    });

    if (sessionStorage.getItem(key) === "true") {
        const url = sessionStorage.getItem(collected) === "true" ? "http://localhost:8080/collect" : "http://localhost:8080/stop";
        fetch(url);
        return;
    }

    sessionStorage.setItem(key, "true");
    window.location.href = URLs.store;
})();