# notebook-watchdog
Utility to track which notebook cells were executed successfully and which not.

*Important Note*: the utility current assumes that the cells are independent of each other. 

### Usage

- Enable extension using `%reload_ext nb_watchdog`
- Watch a cell by adding the magic command `%%watch` at the first line of the cell.
- Unwatch using `%watch`
- Remove extension using `%unload_ext nb_watchdog`


### Example

![image](https://user-images.githubusercontent.com/43947333/159772980-459109dc-4cc7-4d9a-9f3a-d33e27a80eaf.png)
