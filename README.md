# ranked-choice-voting
A python script to tally ranked-choice voting on Google Forms. 

## Usage
### Creating the Form
Google Forms does not natively support ranked-choice forms. Instead, create a new form,  create a new question as a **multiple choice grid**, and select both **Require a response in each row** and **Limit to one response per column**. Under **rows**, put the ranks (e.g. *first choice, second choice, ...*) and under **columns**, put the choices. 

Under **Responses** click **View responses in sheets** and then under **File** select **save as** and choose either .csv or .tsv 

### Using the script
In a console, run the script using the **-i** flag to set the input file:

```bash
python -i google-form-responses.tsv
```

Use **>** to save the output to a file:

```bash
python -i google-form-responses.tsv > results.txt
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)