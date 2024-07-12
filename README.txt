
# Aviation Directory Scraper

This program scrapes aviation company information from the [Aviation Directory](https://aviationdirectory.biz/) and stores the data in an Excel file. The information collected includes the company name, phone number, contact person, email, and website.

## Requirements

- Python 3.x
- Selenium
- Pandas
- ChromeDriver

## Installation

1. Install Python 3.x if not already installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Install the required Python libraries using pip:
    ```bash
    pip install selenium pandas
    ```

3. Download ChromeDriver from the [official ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory of your choice. Make sure to note the path to the ChromeDriver executable.

4. Create a `settings.py` file and add the following line, replacing `path/to/chromedriver` with the actual path to your ChromeDriver:
    ```python
    CHROMEDRIVER_PATH = 'path/to/chromedriver'
    ```

## Usage

1. Place the `settings.py` file in the same directory as the Python script.

2. Run the script:
    ```bash
    python scraper.py
    ```

3. The script will navigate through the first 20 pages of the aviation directory, gather company information, and save it to `updated_aviation_directory_data.xlsx` in the current working directory.

## Script Explanation

- **Imports**: The script imports the necessary modules and the `CHROMEDRIVER_PATH` from the `settings.py` file.
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from settings import CHROMEDRIVER_PATH
    import pandas as pd
    ```

- **Driver Setup**: Initializes the Chrome WebDriver using the specified path.
    ```python
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    ```

- **DataFrame Setup**: Creates an empty DataFrame to store the collected data.
    ```python
    full_data = pd.DataFrame(columns=['Company Name', 'Phone', 'Contact Person', 'Email', 'Website'])
    rows = []
    ```

- **Scraping Loop**: Iterates through the first 20 pages of the directory, collecting links to individual company pages.
    ```python
    for i in range(1, 21):
        driver.get(f'https://aviationdirectory.biz/directory/?pp={i}')
        a_tags = driver.find_elements(By.CSS_SELECTOR, '#directory-listing-box a')
        links = [j.get_attribute('href') for j in a_tags]
        for link in links:
            driver.get(link)
            try:
                company_name = driver.find_element(By.CSS_SELECTOR, '.title').text
            except NoSuchElementException:
                company_name = ''
            try:
                phone_number = driver.find_element(By.XPATH, "//div[strong[contains(text(),'Telephone:')]]").text
            except NoSuchElementException:
                try:
                    phone_number = driver.find_element(By.XPATH, "//div[span[contains(text(),'TEL:')]]").text
                except NoSuchElementException:
                    phone_number = ''
            try:
                contact = driver.find_element(By.XPATH, "//h4[@class='left-listing-sub-title' and text()='EXECUTIVE INFO']/following-sibling::p").text
            except NoSuchElementException:
                contact = ''
            try:
                email = driver.find_element(By.XPATH, "//*[contains(text(),'Email')]/following-sibling::a").text
            except NoSuchElementException:
                email = ''
            try:
                website = driver.find_element(By.XPATH, "//*[contains(text(),'Website')]/following-sibling::a").text
            except NoSuchElementException:
                website = ''
            data = {
                'Company Name': company_name,
                'Phone': phone_number,
                'Contact Person': contact,
                'Email': email,
                'Website': website
            }
            rows.append(data)
    ```

- **DataFrame Creation and Export**: Converts the collected data to a DataFrame and saves it as an Excel file.
    ```python
    full_data = pd.DataFrame(rows)
    full_data.to_excel('updated_aviation_directory_data.xlsx', index=False)
    ```

## Notes

- Ensure that ChromeDriver is compatible with your version of Chrome.
- The script currently scrapes the first 20 pages of the directory. You can modify the range in the `for` loop to scrape more or fewer pages.
- Error handling is implemented to catch missing elements on the pages. If an element is not found, an empty string is recorded in the DataFrame.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
