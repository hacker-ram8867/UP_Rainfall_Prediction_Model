// ==========================================================
// TRUERIZE DASHBOARD
// script.js
// ==========================================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("🚀 TRUERIZE Dashboard Loaded");

    // ======================================================
    // ACTIVE SIDEBAR MENU
    // ======================================================

    const currentPage = window.location.pathname;

    const menuLinks = document.querySelectorAll(".sidebar nav a");

    menuLinks.forEach(link => {

        const href = link.getAttribute("href");

        if (href === currentPage) {

            link.classList.add("active");

        } else {

            link.classList.remove("active");

        }

    });

    // ======================================================
    // CURRENT YEAR
    // ======================================================

    const year = document.querySelector(".current-year");

    if (year) {

        year.textContent = new Date().getFullYear();

    }

    // ======================================================
    // CARD HOVER EFFECT
    // ======================================================

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-8px)";
            card.style.transition = "0.3s";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

    // ======================================================
    // PIPELINE CARD EFFECT
    // ======================================================

    const pipelines = document.querySelectorAll(".pipeline-box");

    pipelines.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.boxShadow =
                "0 15px 35px rgba(37,99,235,.30)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.boxShadow = "";

        });

    });

    // ======================================================
    // SUMMARY COUNTER ANIMATION
    // ======================================================

    function animateCounter(element) {

        const text = element.textContent;

        const target = parseInt(text);

        if (isNaN(target)) return;

        let value = 0;

        const interval = setInterval(() => {

            value++;

            element.textContent = value;

            if (value >= target) {

                element.textContent = target;

                clearInterval(interval);

            }

        }, 30);

    }

    document.querySelectorAll(".summary-card h2").forEach(counter => {

        animateCounter(counter);

    });

    // ======================================================
    // SCROLL TO TOP ON PAGE LOAD
    // ======================================================

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

    // ======================================================
    // SMOOTH SCROLL FOR INTERNAL LINKS
    // ======================================================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function(e){

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if(target){

                target.scrollIntoView({

                    behavior:"smooth"

                });

            }

        });

    });

    // ======================================================
    // FADE IN EFFECT
    // ======================================================

    const observer = new IntersectionObserver(entries=>{

        entries.forEach(entry=>{

            if(entry.isIntersecting){

                entry.target.classList.add("fade");

            }

        });

    });

    document.querySelectorAll(

        ".card,.summary-card,.pipeline-box,.step"

    ).forEach(item=>{

        observer.observe(item);

    });

});

// ==========================================================
// TRUERIZE DASHBOARD
// script.js (Part 2)
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {

    // ======================================================
    // PIPELINE SEARCH
    // ======================================================

    const pipelineSearch = document.getElementById("pipelineSearch");

    if (pipelineSearch) {

        pipelineSearch.addEventListener("keyup", function () {

            const value = this.value.toLowerCase();

            document.querySelectorAll(".pipeline-box").forEach(card => {

                const text = card.innerText.toLowerCase();

                card.style.display = text.includes(value)
                    ? "block"
                    : "none";

            });

        });

    }

    // ======================================================
    // REPORT SEARCH
    // ======================================================

    const reportSearch = document.getElementById("reportSearch");

    if (reportSearch) {

        reportSearch.addEventListener("keyup", function () {

            const value = this.value.toLowerCase();

            document.querySelectorAll(".report-item").forEach(report => {

                const text = report.innerText.toLowerCase();

                report.style.display = text.includes(value)
                    ? "flex"
                    : "none";

            });

        });

    }

    // ======================================================
    // COLLAPSIBLE CARDS
    // ======================================================

    document.querySelectorAll(".card-header").forEach(header => {

        header.style.cursor = "pointer";

        header.addEventListener("click", () => {

            const body = header.nextElementSibling;

            if (!body) return;

            if (body.style.display === "none") {

                body.style.display = "block";

                header.innerHTML = header.innerHTML.replace("▶", "▼");

            } else {

                body.style.display = "none";

                header.innerHTML = header.innerHTML.replace("▼", "▶");

            }

        });

    });

    // ======================================================
    // PIPELINE ACCORDION
    // ======================================================

    document.querySelectorAll(".step-content h3").forEach(title => {

        title.style.cursor = "pointer";

        title.addEventListener("click", () => {

            const paragraph = title.nextElementSibling;

            if (!paragraph) return;

            paragraph.style.display =
                paragraph.style.display === "none"
                    ? "block"
                    : "none";

        });

    });

    // ======================================================
    // TABLE ROW HOVER
    // ======================================================

    document.querySelectorAll("table tr").forEach(row => {

        row.addEventListener("mouseenter", () => {

            row.style.background = "#1e293b";

        });

        row.addEventListener("mouseleave", () => {

            row.style.background = "";

        });

    });

    // ======================================================
    // IMAGE PREVIEW
    // ======================================================

    document.querySelectorAll("img").forEach(img => {

        img.addEventListener("click", () => {

            window.open(img.src, "_blank");

        });

    });

    // ======================================================
    // SCROLL TO TOP BUTTON
    // ======================================================

    const topButton = document.createElement("button");

    topButton.innerHTML = "↑";

    topButton.id = "scrollTop";

    document.body.appendChild(topButton);

    Object.assign(topButton.style, {
        position: "fixed",
        bottom: "30px",
        right: "30px",
        width: "50px",
        height: "50px",
        borderRadius: "50%",
        border: "none",
        background: "#2563eb",
        color: "white",
        fontSize: "22px",
        cursor: "pointer",
        display: "none",
        zIndex: "999"
    });

    window.addEventListener("scroll", () => {

        topButton.style.display =
            window.scrollY > 300 ? "block" : "none";

    });

    topButton.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

    // ======================================================
    // LOADING SPINNER
    // ======================================================

    window.addEventListener("load", () => {

        const loader = document.querySelector(".loader");

        if (loader) {

            loader.style.display = "none";

        }

    });

    // ======================================================
    // NOTIFICATION
    // ======================================================

    function showNotification(message) {

        const note = document.createElement("div");

        note.className = "alert alert-success";

        note.innerHTML = message;

        note.style.position = "fixed";
        note.style.top = "20px";
        note.style.right = "20px";
        note.style.zIndex = "9999";

        document.body.appendChild(note);

        setTimeout(() => {

            note.remove();

        }, 3000);

    }

    // ======================================================
    // COPY REPORT PATH
    // ======================================================

    document.querySelectorAll(".copy-path").forEach(btn => {

        btn.addEventListener("click", () => {

            navigator.clipboard.writeText(

                btn.dataset.path

            );

            showNotification("✅ Report path copied.");

        });

    });

    // ======================================================
    // KEYBOARD SHORTCUTS
    // ======================================================

    document.addEventListener("keydown", e => {

        if (e.key === "Home") {

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        }

        if (e.key === "End") {

            window.scrollTo({

                top: document.body.scrollHeight,

                behavior: "smooth"

            });

        }

    });

    // ======================================================
    // CONSOLE BANNER
    // ======================================================

    console.log(`
=========================================================
                 TRUERIZE DASHBOARD
=========================================================

✓ Dashboard Ready
✓ Reports Loaded
✓ Pipeline Viewer Ready
✓ Flask Connected

Pipeline Modules
----------------
• Polars Configuration
• Great Expectations
• Cerberus Validation
• Pydantic Validation
• Data Preprocessing
• Statistics
• Drift Detection
• Model Training
• SHAP Explainability
• LIME Explainability

=========================================================
`);

});

// ==========================================================
// TRUERIZE DASHBOARD
// script.js (Part 3)
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {

    // ======================================================
    // FILTER PIPELINES BY CATEGORY
    // ======================================================

    const filterButtons = document.querySelectorAll(".filter-btn");

    filterButtons.forEach(button => {

        button.addEventListener("click", () => {

            const category = button.dataset.filter;

            document.querySelectorAll(".pipeline-box").forEach(card => {

                if (
                    category === "all" ||
                    card.dataset.category === category
                ) {

                    card.style.display = "block";

                } else {

                    card.style.display = "none";

                }

            });

        });

    });

    // ======================================================
    // REPORT COUNT
    // ======================================================

    const totalReports = document.querySelectorAll(".report-item").length;

    const reportCounter = document.getElementById("reportCounter");

    if(reportCounter){

        reportCounter.innerHTML = totalReports;

    }

    // ======================================================
    // PIPELINE COUNT
    // ======================================================

    const totalPipelines = document.querySelectorAll(".pipeline-box").length;

    const pipelineCounter = document.getElementById("pipelineCounter");

    if(pipelineCounter){

        pipelineCounter.innerHTML = totalPipelines;

    }

    // ======================================================
    // AUTO REFRESH TIMER
    // ======================================================

    let seconds = 0;

    const timer = document.getElementById("runningTime");

    setInterval(()=>{

        seconds++;

        if(timer){

            timer.innerHTML = seconds + " sec";

        }

    },1000);

    // ======================================================
    // PROGRESS BAR ANIMATION
    // ======================================================

    document.querySelectorAll(".progress-bar").forEach(bar=>{

        const value = bar.dataset.value || 100;

        let width = 0;

        const interval = setInterval(()=>{

            width++;

            bar.style.width = width + "%";

            if(width >= value){

                clearInterval(interval);

            }

        },15);

    });

    // ======================================================
    // TABLE SEARCH
    // ======================================================

    const tableSearch = document.getElementById("tableSearch");

    if(tableSearch){

        tableSearch.addEventListener("keyup",function(){

            const filter = this.value.toLowerCase();

            document.querySelectorAll("tbody tr").forEach(row=>{

                row.style.display =

                row.innerText.toLowerCase().includes(filter)

                ? ""

                : "none";

            });

        });

    }

    // ======================================================
    // REPORT DOWNLOAD BUTTON
    // ======================================================

    document.querySelectorAll(".download-report").forEach(btn=>{

        btn.addEventListener("click",()=>{

            window.open(btn.dataset.file);

        });

    });

    // ======================================================
    // TOOLTIP
    // ======================================================

    document.querySelectorAll("[data-tooltip]").forEach(item=>{

        item.addEventListener("mouseenter",()=>{

            const tip=document.createElement("div");

            tip.className="tooltip";

            tip.innerHTML=item.dataset.tooltip;

            tip.id="tooltip";

            document.body.appendChild(tip);

            const rect=item.getBoundingClientRect();

            tip.style.position="fixed";

            tip.style.left=rect.left+"px";

            tip.style.top=(rect.top-35)+"px";

        });

        item.addEventListener("mouseleave",()=>{

            const tip=document.getElementById("tooltip");

            if(tip) tip.remove();

        });

    });

    // ======================================================
    // PRINT REPORT
    // ======================================================

    const printButton=document.getElementById("printReport");

    if(printButton){

        printButton.addEventListener("click",()=>{

            window.print();

        });

    }

    // ======================================================
    // FULLSCREEN REPORT
    // ======================================================

    const fullscreen=document.getElementById("fullscreen");

    if(fullscreen){

        fullscreen.addEventListener("click",()=>{

            document.documentElement.requestFullscreen();

        });

    }

    // ======================================================
    // COLLAPSE SIDEBAR
    // ======================================================

    const collapse=document.getElementById("collapseSidebar");

    if(collapse){

        collapse.addEventListener("click",()=>{

            document.querySelector(".sidebar").classList.toggle("collapsed");

        });

    }

    // ======================================================
    // SHOW CURRENT DATE
    // ======================================================

    const date=document.getElementById("currentDate");

    if(date){

        date.innerHTML=new Date().toLocaleDateString();

    }

    // ======================================================
    // SHOW CURRENT TIME
    // ======================================================

    const time=document.getElementById("currentTime");

    if(time){

        setInterval(()=>{

            time.innerHTML=new Date().toLocaleTimeString();

        },1000);

    }

    // ======================================================
    // EXPORT TABLE TO CSV
    // ======================================================

    const exportBtn=document.getElementById("exportCSV");

    if(exportBtn){

        exportBtn.addEventListener("click",()=>{

            alert("CSV Export can be connected to Flask.");

        });

    }

    // ======================================================
    // SHOW DASHBOARD INFO
    // ======================================================

    console.table({

        Framework:"TRUERIZE",

        Backend:"Flask",

        Language:"Python",

        Reports:totalReports,

        Pipelines:totalPipelines,

        Version:"1.0"

    });

    console.log(
        "%cTRUERIZE DASHBOARD READY",
        "color:#38bdf8;font-size:18px;font-weight:bold;"
    );

});