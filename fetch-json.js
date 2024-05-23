import { writeFileSync, readFileSync } from "fs";
import { pages } from "./api.js";
import { JSDOM } from "jsdom";

const root_domain = `https://tm.ncl.edu.tw`;

pages.forEach( (page) => {
    const source = readFileSync(`./results/${page}/source.html`, "utf-8");
    const dom = new JSDOM(source);
    const book = [
        ...dom.window.document.querySelectorAll(".div-for-book")
    ].map( its => `${root_domain}${its.textContent}` );
    writeFileSync(`./results/${page}/book.json`, JSON.stringify(book));
});
