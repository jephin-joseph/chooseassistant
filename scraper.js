const puppeteer= require('puppeteer');

async function scrapeProduct(){
    const browser = await puppeteer.launch();
    const page =await browser.newPage();
    await page.goto('https://www.amazon.in/HP-RX5500M-Graphics-Flicker-16-e0162AX/dp/B098QBT5KT/ref=sr_1_1_sspa?crid=8S55OLVJ8NZU&keywords=msi+gf65+thin&qid=1648878812&sprefix=msi+gf%2Caps%2C326&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNzY4QkdGS00xRk40JmVuY3J5cHRlZElkPUEwNDQ1NjY5VkRKSE5COEJFSUdOJmVuY3J5cHRlZEFkSWQ9QTA3NzcxMDIzMjMwODhMV1FMWkxJJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==');
    
    // const grabPara=await page.evaluate(() => {
    //     const pgTag =document.querySelector(".a-size-large.product-title-word-break p")
    //     return pgTag.innerHTML;
    // });
    const [el]=await page.$x('/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[1]/div/h1/span')
    const src=await el.getProperty('src');
    const srcText=await src.jsonValue();
    console.log({srcText});
    // await browser.close();
}
scrapeProduct()






// async function scrapProduct(url) {
    // const browser = await puppeteer.launch( );
    // const page =await browser.newPage();
    // page.goto(url);
// }

// #productTitle
// <span id="productTitle" class="a-size-large product-title-word-break">        HP Victus AMD Ryzen 5 5600H 16.1 inches FHD Gaming Laptop (8GB RAM/512GB SSD/4GB Radeon RX5500M Graphics/Flicker Free Display/Windows 10 Home/MS Office/Mica Silver/2.48 Kg), 16-e0162AX, Black       </span>