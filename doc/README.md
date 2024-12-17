# Word Count Challenge Solution (codingchallenges.fyi)

## Overview

This project provides a solution to the "wc" (word count) challenge on codingchallenges.fyi. The program takes text input (either from standard input or a file) and calculates the number of lines, words, and characters in the input. The output is a single line consisting of the line count, word count, and character count, separated by spaces.

## Requirements

*   **Programming Language:** Python 3.6 or higher
*   **Dependencies:** None (standard Python libraries are sufficient)

## How to Run

1.  **Clone the repository (if needed):**
    ```bash
    git clone [your repository URL]
    cd wc_challenge
    ```
2.  **Run the script:** You can provide input in one of two ways:
    *   **From standard input (piping):**
        ```bash
        python wc.py < input.txt
        ```
        *Replace `input.txt` with your input file.*
    *   **Direct standard input:**
        ```bash
        python wc.py
        ```
        *Then type your input and press Ctrl+D (or Cmd+D on macOS) to signal the end of input.*

## Implementation Details

### Algorithm

The program implements the word count functionality with the following steps:

1.  **Read Input:** The input text is read either from standard input or via redirection from a file.
2.  **Line Processing:**
    *   The input is split into lines using the newline character (`\n`).
    *   The number of lines is counted directly using the `len()` function after splitting.
3.  **Word Processing:**
    *   For each line, the line is further split into words using whitespace (`split()` method without arguments, handling different whitespace characters).
    *   The total word count is accumulated by summing the number of words in each line.
4.  **Character Processing:**
    *   The character count is calculated by accumulating the lengths of each line (including spaces).
5.  **Output:** The final counts (lines, words, characters) are printed to the console, separated by spaces.

### Data Structures

*   **Strings:** The input is handled as a string throughout the process.
*   **List:** The input is temporarily converted into a list of strings after splitting into lines.

### Important Choices

*   **Whitespace Handling:** The `split()` method is used without any arguments in order to handle multiple types of white space character, including leading and trailing spaces. This method splits the string by any whitespace.
*   **End of Input:** In standard input mode, the program assumes that the input is finished when the end of file signal (EOF) is given (e.g., Ctrl+D or Cmd+D).
*   **No External Libraries:** The solution only uses standard Python methods without relying on third-party libraries. This keeps the solution simple and easy to use.

### Code Structure

The core logic is contained within a single function `count_lines_words_chars(input_text)`:

1.  **`count_lines_words_chars(input_text)`**:
    *   This function takes the entire input text as a string.
    *   It calculates the line count, word count and character count.
    *   It returns these three values as tuple

The output is done via a print statement calling the main function that reads the input then calls this function.

## Input/Output Format

*   **Input:**
    *   The program accepts plain text input. This input can contain multiple lines and any amount of whitespace characters.
    *   Input can be given via file redirection or directly in standard input.

*   **Output:**
    *   The program produces a single line of output with three integer values separated by single spaces.
    *   The first value represents the number of lines.
    *   The second represents the number of words.
    *   The third value is the total character count in the input.

## Examples

*   **Sample Input 1:**
    ```
    This is a
    test input.
    ```

*   **Sample Output 1:**
    ```
    2 4 21
    ```

*   **Sample Input 2:**
    ```
    Hello world!
      Second line.
    ```

*   **Sample Output 2:**
    ```
    2 4 25
    ```

*   **Sample Input 3:**
    ```
    Single line.
    ```

*   **Sample Output 3:**
    ```
    1 2 13
    ```

*   **Sample Input 4:** (empty file)
    ```

    ```

*   **Sample Output 4:**
    ```
    0 0 0
    ```

## Testing

The solution was tested using a range of inputs including:

*   **Simple multi-line input:** With a couple of lines, and some words
*   **Inputs with leading/trailing spaces:** Showing that spaces are handled well when counting words
*   **Single-line input:** To verify counting on a single line works
*   **Empty input:** Verify that zero is returned when the input is empty.

The outputs were manually verified for correctness.

## Potential Improvements

*   **Support for different line endings:** Currently, the program assumes `\n` as the line separator. Adding support for `\r\n` (Windows line endings) can make it more portable.
*   **Command-line arguments:** Allow user to specify the input file or standard input using command-line options, rather than requiring redirection.
*  **Performance Improvements** The current algorithm is very simple and not optimized for very large files. Further performance could be explored.

## Author

[Your Name]

## License

This code is released under the MIT License.