import { mkdirSync, writeFileSync } from "fs";
import { pages, domain } from "./api";

pages.forEach( (page) => {
    const api = domain + page;
    mkdirSync(`./results/${page}`);
    fetch(api).then( r => r.text() ).then( (response) => {
        writeFileSync(`./results/${page}/source.html`, response);
    });
});
