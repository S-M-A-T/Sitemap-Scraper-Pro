<h1>Sitemap Scraper Pro</h1>

<h2>Overview</h2>
<p><strong>Sitemap Scraper Pro</strong> is a Python-based web scraping tool designed to extract data from websites through their sitemap. It fetches URLs, scrapes specific information (such as categories, titles, and contact details), and exports the results into an Excel file for easy access and further analysis. This project is useful for gathering structured data from websites that provide an accessible sitemap in XML format.</p>

<h2>Features</h2>
<ul>
    <li>Fetches URLs from a sitemap and paginated sitemap structure.</li>
    <li>Scrapes main categories, subcategories, titles, phone numbers, and country details from each URL.</li>
    <li>Supports easy export of scraped data into an Excel file (.xlsx).</li>
    <li>Gracefully handles errors such as network issues or missing elements on pages.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python 3.x</strong></li>
    <li><strong>Requests</strong>: For making HTTP requests to the sitemap and individual pages.</li>
    <li><strong>BeautifulSoup (bs4)</strong>: For parsing the HTML and XML of the webpages.</li>
    <li><strong>pandas</strong>: For data manipulation and exporting scraped data to an Excel file.</li>
</ul>

<h2>Installation</h2>
<p>To run this project locally, follow these steps:</p>

<h3>Prerequisites</h3>
<p>Ensure that Python 3.x and <code>pip</code> are installed on your machine. You also need to install the following libraries:</p>

<pre><code>pip install requests beautifulsoup4 lxml pandas</code></pre>

<h3>Clone the Repository</h3>
<ol>
    <li>Clone this repository to your local machine using the following command:</li>
</ol>
<pre><code>git clone https://github.com/S-M-A-T/Sitemap-Scraper-Pro.git</code></pre>
<ol start="2">
    <li>Navigate to the project directory:</li>
</ol>
<pre><code>cd sitemap-scraper-pro</code></pre>

<h2>Usage</h2>

<h3>Step 1: Modify the Base URL</h3>
<p>Edit the Python script and change the base URL (<code>base_url</code>) to the sitemap of the website you want to scrape. The default in the script is:</p>
<pre><code>base_url = "https://www.abc.com/sitemap.xml"</code></pre>

<h3>Step 2: Run the Script</h3>
<p>Once you've set the desired sitemap URL, you can run the script using Python:</p>
<pre><code>python scraper.py</code></pre>

<h3>Step 3: View Results</h3>
<p>After running the script, the data will be saved to an Excel file named <strong>scraped_data.xlsx</strong>. You can open this file to view the scraped information.</p>

<h3>Step 4: Check Output</h3>
<p>The script will also print the scraped data in the console. Additionally, it will show how many URLs were processed and the total number of entries scraped:</p>
<pre><code>Total data entries scraped: X
Data saved to scraped_data.xlsx</code></pre>

<h2>Customization</h2>
<p>You can easily customize the script to extract other data from the target website by modifying the <code>scrape_data()</code> function to suit your needs. Simply update the parsing logic using BeautifulSoup based on the page structure you are scraping.</p>

<h2>Error Handling</h2>
<p>The script includes error handling to manage issues such as:</p>
<ul>
    <li>Connection failures.</li>
    <li>Invalid or missing data on pages.</li>
    <li>Pages not matching the expected format.</li>
</ul>
<p>If an error occurs during scraping, it will be printed in the console and the script will continue with the next URL.</p>

<h2>Contribution</h2>
<p>Feel free to contribute to this project by forking the repository and submitting a pull request. Any improvements or additional features are welcome!</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
