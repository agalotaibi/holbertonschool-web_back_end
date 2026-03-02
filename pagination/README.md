# Pagination

This project explores different techniques for paginating large datasets in Python. Pagination is a crucial concept in backend development and API design, allowing applications to send data in manageable chunks rather than overwhelming the client with a massive dataset all at once.

## Repository Details
* **GitHub repository:** `holbertonschool-web_back_end`
* **Directory:** `pagination`

## Requirements
* **Language:** Python 3.7+
* **OS:** Ubuntu 18.04 LTS (or similar Unix-like environment)
* **Dataset:** `Popular_Baby_Names.csv`
* **Style:** Code should follow `pycodestyle` (version 2.5.*)
* All files must be executable.
* All modules, classes, and functions must have appropriate documentation (docstrings).
* Type annotations are required for all functions and methods.

---

## Tasks

### 0. Simple helper function
* **File:** `0-simple_helper_function.py`
* **Description:** Write a function named `index_range` that takes two integer arguments `page` and `page_size`. The function returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed (the first page is page 1).

### 1. Simple pagination
* **File:** `1-simple_pagination.py`
* **Description:** Implement a `Server` class to paginate a database of popular baby names. Includes a `get_page` method that takes two integer arguments `page` with default value 1 and `page_size` with default value 10. It uses `index_range` to find the correct indexes and returns the appropriate slice of the dataset.

### 2. Hypermedia pagination
* **File:** `2-hypermedia_pagination.py`
* **Description:** Enhances the simple pagination by implementing a `get_hyper` method that returns a dictionary containing hypermedia metadata:
  * `page_size`: the length of the returned dataset page
  * `page`: the current page number
  * `data`: the dataset page
  * `next_page`: number of the next page, `None` if no next page
  * `prev_page`: number of the previous page, `None` if no previous page
  * `total_pages`: the total number of pages in the dataset

### 3. Deletion-resilient hypermedia pagination
* **File:** `3-hypermedia_del_pagination.py`
* **Description:** Implements a cursor-based pagination method (`get_hyper_index`) to ensure that if rows are removed from the dataset between queries, the user does not miss items when changing pages. It returns a dictionary containing:
  * `index`: the current start index of the return page
  * `next_index`: the next index to query with
  * `page_size`: the current page size
  * `data`: the actual page of the dataset
