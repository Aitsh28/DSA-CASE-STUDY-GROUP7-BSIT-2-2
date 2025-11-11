<div id="top" align="center">
  <img src="/Polytechnic_University_of_the_Philippines_Quezon_City_Logo.svg.png" alt="PUP IMS Logo" width="150"/>

<div align="center">
  <h1>Academic Analytics Lite</h1>
  <p class="lead">
    A lightweight Python pipeline for processing student performance data — array-first, modular, and easy to configure.
  </p>
  <div class="badges" style="margin-top:8px" align="center">
    <img src="https://img.shields.io/badge/Python%203.8%2B-white?style=for-the-badge&logo=python" alt="Badge">
    <img src="https://img.shields.io/badge/License-Academic-white?style=for-the-badge&labelColor=blue" alt="license">
    <img src="https://img.shields.io/badge/Status%3A%20v1.0-blue?style=for-the-badge" alt="Badge">
  </div>
</div>

<p align="center">
  <a href="#overview"><strong>🟦 OVERVIEW</strong></a> &nbsp;|&nbsp;
  <a href="#key-features"><strong>🟩 KEY FEATURES</strong></a> &nbsp;|&nbsp;
  <a href="#prerequisites--setup"><strong>🟪 PREREQUISITES & SETUP</strong></a> &nbsp;|&nbsp;
  <a href="#project-structure"><strong>🟥 PROJECT STRUCTURE</strong></a> &nbsp;|&nbsp;
  <a href="#complexity--performance"><strong>🟫 COMPLEXITY & PERFORMANCE</strong></a> &nbsp;|&nbsp;
</p>

<h2 align="center" id="overview">Overview</h2>
<p align="center"> 
  This project ingests CSV data exported from an LMS, applies array-based transformations and analytics, and produces instructor-facing reports: grade distributions, per-section exports, and at-risk lists. It favors plain Python data structures (lists, dicts) and JSON configuration, with an optional NumPy-accelerated mode.
</p>

<div align="center" style="color:#1a1a1a; padding:20px; border-radius:12px; max-width:800px; margin:auto; ">
  <h2 id="key-features">Key Features</h2>
  <ul style="text-align:left; padding-left:20px; line-height:1.6;">
    <li>CSV ingestion & validation (handles missing/invalid fields)</li>
    <li>Array operations: select, project, sort, insert, delete</li>
    <li>Analytics: weighted grades, letter mapping, percentiles, outliers</li>
    <li>Export reports per-section and at-risk students as CSV</li>
    <li>Configurable via <code>config.json</code></li>
    <li>Unit tests and timing for performance checks</li>
    <li>Stretch: CLI menu and NumPy version</li>
  </ul>
</div>

<section class="card" align="center">
<h2 id="prerequisites--setup">Prerequisites & Setup</h2>
<div align="center">
  <table style="width: 600px; border-collapse: collapse; margin-top: 10px; font-size: 15px;">
    <tr>
      <td align="center" style="width: 48px;">1️⃣</td>
      <td>
        <strong>Python 3.8+</strong><br>
        Required to run all scripts.
      </td>
    </tr>
    <tr>
      <td align="center">2️⃣</td>
      <td>
        <strong>NumPy (optional)</strong><br>
        <code>pip install numpy</code> for NumPy-accelerated mode.
      </td>
    </tr>
    <tr>
      <td align="center">3️⃣</td>
      <td>
        <strong>Project ZIP file</strong><br>
        <em>DSA-CASE STUDY-GROUP7-BSIT 2-2.zip</em> — contains all source files, config, and data.
      </td>
    </tr>
    <tr>
      <td align="center">4️⃣</td>
      <td>
        <strong>Unzip & Configure</strong><br>
        Unzip the project into your workspace and edit <code>config.json</code> for weights, thresholds, and paths.
      </td>
    </tr>
  </table>
</div>
</section>

<section class="card" align="center">
<h2>Usage Instructions</h2>
<div align="center">
  <table style="width: 600px; border-collapse: collapse; margin-top: 24px; justify-content: center; font-size: 15px;">
    <tr>
      <td align="center" style="width: 48px;">1️⃣</td>
      <td>
        <strong>Run the main script</strong><br>
        <pre><code>python src/main.py</code></pre>
        Outputs include per-section CSVs and <code>at_risk.csv</code> in the <code>output/</code> folder.
      </td>
    </tr>
  </table>
</div>
</section>

<h2 align="center" id="project-structure">Project Structure</h2>

<details>
<summary>📁 pycache/ - Compiled Python bytecode files</summary>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>analyze.cpython-313.pyc</td><td>File</td><td>Compiled analyze.py</td></tr>
    <tr><td>ingest.cpython-313.pyc</td><td>File</td><td>Compiled ingest.py</td></tr>
    <tr><td>reports.cpython-313.pyc</td><td>File</td><td>Compiled reports.py</td></tr>
    <tr><td>transform.cpython-313.pyc</td><td>File</td><td>Compiled transform.py</td></tr>
  </tbody>
</table>
</details>

<details>
<summary>📁 output_reports/ - Generated CSV reports</summary>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>at_risk_students.csv</td><td>File</td><td>At-risk students report</td></tr>
    <tr><td>section_a.csv</td><td>File</td><td>Section A report</td></tr>
    <tr><td>section_b.csv</td><td>File</td><td>Section B report</td></tr>
    <tr><td>section_c.csv</td><td>File</td><td>Section C report</td></tr>
  </tbody>
</table>
</details>

<details>
<summary>📁 src/ - Core Python source files</summary>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>analyze.py</td><td>File</td><td>Handles data analysis and computations</td></tr>
    <tr><td>ingest.py</td><td>File</td><td>Reads and loads input data</td></tr>
    <tr><td>main.py</td><td>File</td><td>Main program execution</td></tr>
    <tr><td>reports.py</td><td>File</td><td>Generates reports and summaries</td></tr>
    <tr><td>transform.py</td><td>File</td><td>Processes and transforms data</td></tr>
  </tbody>
</table>
</details>

<details>
<summary>Other files ⚙️🖼️📄</summary>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>config.json</td><td>File</td><td>Configuration file (weights, thresholds, paths)</td></tr>
    <tr><td>cs-output.png</td><td>File</td><td>Output visualization</td></tr>
    <tr><td>csv.PNG</td><td>File</td><td>CSV file reference or sample screenshot</td></tr>
    <tr><td>input.csv</td><td>File</td><td>Input dataset</td></tr>
    <tr><td>Polytechnic_University_of_the_Philippines_Quezon_City.png</td><td>File</td><td>School logo</td></tr>
    <tr><td>README.md</td><td>File</td><td>Documentation file</td></tr>
  </tbody>
</table>
</details>


<section class="card">
<h3>Sample <code>config.json</code></h3>
<pre><code>
{
  "weights": {
    "quizzes": 0.2,
    "midterm": 0.3,
    "final": 0.3,
    "attendance": 0.2
  },
  "at_risk_threshold": 75
}
</code></pre>
</section>

<section class="card columns">
<div>
<h2 id="complexity--performance">Complexity & Performance</h2>
<table style="width: 600px; border-collapse: collapse; margin-top: 30px; justify-content: center;">
<thead><tr><th>Stage</th><th>Time</th><th>Space</th></tr></thead>
<tbody>
<tr><td>Ingestion</td><td>O(N)</td><td>O(N)</td></tr>
<tr><td>Sorting</td><td>O(N log N)</td><td>O(N)</td></tr>
<tr><td>Analytics</td><td>O(N)</td><td>O(N)</td></tr>
<tr><td>Outlier Detection</td><td>O(N²) worst-case</td><td>O(N)</td></tr>
</tbody>
</table>
<p class="muted">NumPy mode vectorizes many computations and yields significant speedups for large datasets.</p>
</div>
<div>

<section class="card">
<h2>Input Format</h2>
<p>CSV columns expected:</p>
<pre>student_id,last_name,first_name,section,quiz1,...,quiz5,midterm,final,attendance_percent</pre>
<p class="muted">Scores should be 0–100; missing numeric values will be treated as <code>null</code> and handled by validation logic.</p>
</section>

<section class="card">
<h2>Screenshots / Demo (placeholders)</h2>
<div class="columns">
<div class="screenshot">CLI Summary Output</div>
<img src="/cs-output.png" alt="CS-Output"/>
<div class="screenshot">Per-section CSV Preview</div>
<img src="/csv.PNG" alt="CSV Preview"/>
</div>
</section>

<div align="center">
  <h3>BSIT 2-2 S.Y. 2025-2026 Group 7</h3>
  <p>Polytechnic University of the Philippines - Quezon City</p>
  <section class="card" align="center" style="padding:1rem;">
  <p>🌟 <b>Trish Anne Adoray</b></p>
  <p>🎨 <b>Chini Drew Ante</b></p>
  <p>📊 <b>Paul John Delloro</b></p>
  <p>⚙️ <b>John Andrew General</b></p>
  <p>📝 <b>Sena Alondra Gutierrez</b></p>
  <p>🧩 <b>Jems Vin Rhestie Petallo</b></p>
</section>
  
<div align="center" style="color:#1a1a1a; padding:20px; border-radius:12px; max-width:800px; margin:auto;">
  <h2>Reflection & Learning</h2>
  <ul style="text-align:left; padding-left:20px; line-height:1.6;">
    <li><strong>Programming & Skills:</strong> Applied Python, handled modules, data ingestion, and visualization; improved problem-solving, debugging, and coding practices.</li>
    <li><strong>Teamwork & Collaboration:</strong> Learned to communicate, understand teammates’ logic, and integrate work effectively.</li>
    <li><strong>Personal Growth:</strong> Built patience, resilience, and resourcefulness; realized programming is continuous learning.</li>
    <li><strong>Practical Application:</strong> Gained knowledge applicable to real-life situations and future projects.</li>
  </ul>
</div>


<footer>
<p>Academic Analytics Lite — v1.0 &middot; Author: Data Structures and Algorithms Team (BSIT2-2 - GROUP 7)</p>
</footer>
