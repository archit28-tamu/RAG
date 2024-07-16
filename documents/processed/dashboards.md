 


# Dashboard

## What is a Dashboard

Dashboards feature in RDA Fabric platform provides analytics and reporting using which different UI views can be created for different user personas such as executives, IT admins and operators etc. Dashboards are composable and customizable to fit specific user needs within the IT operations landscape.  

Below are some of the available different data types in RDA Fabric platform using which Dashboards can be created, but not limited to.

*   **Metrics**
*   **Alerts / Events**
*   **Logs**
*   **Traces**
*   **Asset Inventory**
*   **Tickets**
*   **Other IT operations & service management data**

## Creating a Dashboard

Follow the below steps to access the **Dashboard** feature in RDA Fabric platform

### ****2.1 Dashboard Configuration****

**Step-1:** Login into RDA Fabric platform as a **MSP Admin** user.

**Step-2:** Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Dashboards**

**Step-3:** Click on **Add** button to create a new Dashboard.

Dashboard configuration need to be provided in **JSON / YAML** format. Below is a sample configuration to create a new Dashboard.
```
 { 
     "name": "rdaf-platform-log-analytics-2", 
     "label": "RDAF Platform Logs2", 
     "description": "RDAF Platform service's log analysis dashboard", 
     "version": "22.9.22.2", 
     "enabled": true, 
     "dashboard_style": "tabbed", 
     "status_poller": {}, 
     "dashboard_filters": { 
         "time_filter": true, 
         "columns_filter": [], 
         "group_filters": [] 
     }, 
     "dashboard_sections": [], 
     "dashboard_type": "app", 
     "dashboard_pages": [] 
 }

```

Please refer the below table for details about **Dashboard's configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `name` | yes | Unique name or ID for the Dashboard. May contain letters, digits and hyphen only. |
| `label` | yes | Label for the dashboard. This is visible to users of the dashboard |
| `description` | yes | Description for the dashboard. This is also visible to the users |
| `version` | no  | Dashboard version to track the changes for better management of it's configuration. Ex: YYYY.MM.DD.NUMBER `2022.12.01.01` or any alphanumerical value which uniquely distinguishes between each version. |
| `enabled` | yes | Specifies if the dashboard to be enabled / disabled. If not enabled, Dashboard would not be visible to users. Valid values are `true` or `false`. Default is `false` |
| `dashboard_style` | no  | Dashboards can be `tabbed` or `sectioned`. If set to `auto`, tabs will be shown only if more than one section is specified under `dashboard_sections`. Default is `auto` |
| `dashboard_folder` | no  | Specify the folder name under which the dashboard to be created. When it is not specified, it is placed under `Default` folder. |
| `status_poller` | no  | It is a smart dashboard UI **refresh** feature. When used, it will refresh the Dashboard with new data within the user defined polling frequency automatically. It will refresh the Dashboard UI **only** if there is **new data** since last poll. |
| `dashboard_filters` | yes | This object defines if and how filtering should be enabled for dashboard. |
| `dashboard_sections` | yes | This is list of objects which specify list of sections, and widgets in each section. How to add the widgets to the Dashboard Section Refer Widgets Type |
| `dashboard_type` | no  | Specify the Dashboard type. Supported values are `app`. |
| `dashboard_pages` | no  | Specify the sub Dashboard configuration parameters. This parameter is needed when `dashboard_type` is set to `app` |

### ****2.2 Status Poller****

It is a smart dashboard UI **refresh** feature. When used, it will refresh the Dashboard with new data within the user defined polling frequency automatically. It will refresh the Dashboard UI only if there is **new data** since last poll.

Please refer the below sample configuration settings to enable **Status Poller** feature within the Dashboard configuration.
```
     "status_poller": { 
         "stream": "rdaf_pstream_name", 
         "frequency": 30, 
         "columns": [ 
             "timestamp" 
         ], 
         "sorting": [ 
             { 
                 "timestamp": "desc" 
             } 
         ], 
         "query": "timestamp is after '${timestamp}'", 
         "defaults": { 
             "timestamp": "$UTCNOW" 
         }, 
         "action": "refresh" 
     }
 ```

Please refer the below table for details about **Status poller's configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `stream` | yes | Persistent stream name from which the data to be polled to refresh the data within the Dashboard. |
| `frequency` | yes | Specify the polling frequency in Seconds. Ex: `15` or `30` or `60` etc. |
| `columns` | no  | Specify the timestamp column within the persistent stream name. It is an array field and supports multiple values. Default value is `timestamp` |
| `sorting` | no  | Specifies the sorting to be applied on the queried data. Default setting is `desc`. Supported values as `desc` and `asc` |
| `query` | yes | Specify the query in CFXQL format to query the data during the refresh poll. |
| `defaults` | yes | Specify the timestamp format of the RDA Fabric system, UTC vs Local time. Syntax is `{ "timestamp": "$UTCNOW" }`. **timestamp** is timestamp column within the specified pstream name. Supported values are `$NOW` and `$UTCNOW` |
| `action` | yes | Supported value is `refresh` |

### ****2.3 Dashboard Filters****

Dashboard filters is a feature within each Dashboard which allows the user to expose selective columns from supported datasources such as persistent stream or a dataset as **Filters**.

*   **Time Filters**
*   **Column Filters**
*   **Group Filters**

![Dashboard_Filter_Bar](https://bot-docs.cloudfabrix.io/images/widgets/dashboard_filter_bar.png) ![Dashboard_Group_Filter_Bar](https://bot-docs.cloudfabrix.io/images/widgets/dashboard_group_filters.png)

**Time Filters**: When the time filter is set to true, it allows for the adjustment or re-arrangement of intervals for a timestamp column. This feature enables users to manipulate and organize the time intervals displayed or analyzed within the dashboard. By setting the time filter to true, users gain the capability to modify how the timestamps are grouped, displayed, or analyzed based on their preferences or requirements.

**Default Time Filter Labels**: The `default_time_filter_labels` feature establishes a preset interval as the default selection for the dashboard when using time filters. This means that when a user accesses the dashboard or interface, it will automatically display or use the specified time interval as the default option for filtering or organizing the time-based data without requiring the user to manually select it each time.

Below is the sample configuration to specify Default Time Filter Labels
```
 "dashboard_filters": { 
   "time_filter": true, 
   "default_time_filter_labels": [ 
     "Last 1 month" 
   ] 
 }

```

Note

Make sure the `time_filter` is enabled and set to `true`

**Custom Time Filters**: When custom time filters are enabled along with the time filter, users can define precise intervals for their timestamp data. This functionality permits users to customize intervals, like minutes (m), hours (h), days (d), weeks (w), months (M), and years (y). However, it's important to note that, users must input a number followed by the interval type letter. Just providing the 'm' designation won't display any results; users need to adhere to the format of providing a numerical value followed by the interval type letter to ensure accurate interval definitions.

Below is the sample configuration to specify Custom Time Filter
```
 "dashboard_filters": { 
 "time_filter": true, 
 "custom_time_filters": [ 
     "15m", 
     "32m", 
     "72m", 
     "1h", 
     "4h", 
     "36h", 
     "1d", 
     "3d", 
     "1w", 
     "2w", 
     "1M", 
     "3M", 
     "1y", 
     "10y" 
   ] 
 }

```

![Custom Time Filters](https://bot-docs.cloudfabrix.io/images/dashboards/custom_time_filters.png)

Note

Make sure the `time_filter` is enabled and set to `true`

**Column Filters**: option allows the user to query and filter the data on one or more selected column(s) using the dashboard's **filter bar** on demand.
```
     "dashboard_filters": { 
         "time_filter": true, 
         "columns_filter": [ 
             { 
                 "id": "timestamp", 
                 "label": "Timestamp", 
                 "type": "DATETIME" 
             }, 
             ... 
             ... 
             { 
                 "id": "host", 
                 "label": "IP Address", 
                 "type": "TEXT" 
             } 
         ] 
     }
 ```

Please refer the below table for details about **Dashboard filter's configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `time_filter` | no  | This parameter is to enable time filter or not for the dashboard. Supported values are `true` or `false`. |
| `columns_filter` | no  | Configure the parameters and specify the columns which need to be exposed as filterable columns. |
| `group_filters` | no  | Configure the parameters and specify the columns which need to be exposed as group or quick (drop down) filters. |

Please refer the below table for details about **Column filter's configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `id` | yes | Column name from the persistent stream or dataset. |
| `label` | yes | Specify the label for the selected column under `id` parameter. |
| `type` | yes | Specify the selected column's data type. Supported values are `TEXT`, `DATETIME` |

**Group Filters**: option acts as a quick filter, when defined, it provides a simple drop down with unique filtered values from the selected column and allows the user to select one or more values to filter the data quickly.

Tip

Both **Column Filters** and **Group Filters** are optional within the Dashboard configuration.
```
     "group_filters": [ 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "Log Severity", 
                 "group_by": [ 
                     "log_severity" 
                 ], 
                 "ts_column": "@timestamp", 
                 "agg": "value_count", 
                 "column": "_id", 
                 "type": "int", 
                 "show_counts": true, 
             }, 
             ... 
             ... 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "RDA Host IPAddress", 
                 "group_by": [ 
                     "service_host" 
                 ], 
                 "ts_column": "@timestamp", 
                 "agg": "value_count", 
                 "column": "_id", 
                 "type": "int" 
             } 
         ]
 ```

Please refer the below table for details about **Group filter's configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `stream` | yes | Specify the persistent stream. |
| `title` | yes | Specify the label for group filter |
| `group_by` | yes | Specify one or more columns to apply the `group_by`. This parameter supports multiple column values. Ex: `"group_by": [ "column_01", "column_02", "column_n"]` |
| `column` | yes | Specify the column name that is to uniquely identify the selected `group_by` column values within each record of persistent stream or dataset. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | no  | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation operations and these are not applicable for group filters. |
| `show_counts` | no  | This Parameter is used to show or hide counts in group filters. supported values are `true` or `false` |

### ****2.4 Dashboard Pages****

Dashboards can be grouped and used as sub dashboards within another main dashboard and they are configured as **Dashboard Pages**.

Below is the configuration format for Dashboard Pages.
```
     "dashboard_pages": [ 
         { 
             "name": "CFX Incidents - Dashboard", 
             "label": "Incidents", 
             "icon": "incident.svg", 
             "group": "group1" 
         }, 
         ... 
         ... 
         { 
             "name": "Operational Metric - Dashboard", 
             "label": "Metric Analysis", 
             "icon": "metrics.svg", 
             "group":"group2" 
         } 
     ]
 ```

Please refer the below table for details about **Dashboard page(s) configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `name` | yes | Specify name of the Dashboard which need to be added as a page. |
| `label` | yes | Specify the label for Dashboard page. |
| `icon` | no  | Specify an icon image file name which can be used for the Dashboard page. Some of the provided icons within the system are, `incident.svg`, `metrics.svg`, `alert.svg`, `contract.svg`, `customer.svg`, `asset.svg`, `detail.svg`, `hands.svg`, `hardware.svg`, `overall.svg`, `room.svg`, `software.svg`, `activities.svg`, `alertGroups.svg`, `Analytics.svg`, `attachments.svg`, `bots.svg`, `changes.svg`, `cluster.svg`, `collaboration.svg`, `datasource.svg`, `diagnostic.svg`, `enrichment.svg`, `eye.svg`, `file.svg`, `gateway.svg`, `insights.svg`, `ipTelephony.svg`, `jobs.svg`, `metrics.svg`, `ml.svg`, `outcome.svg`, `pipeline.svg`, `rca.svg`, `rda.svg`, `remedial.svg`, `schedule.svg`, `security.svg`, `stack.svg`, `status.svg`, `suppression.svg`, `team.svg`, `topology.svg`, `version.svg` |
| `group` | no  | Specify multiple pages under single group |

Below is the sample screenshot of **Dashboard Pages**

![Dashboard_Pages](https://bot-docs.cloudfabrix.io/images/dashboards/dashboard_pages.png)

### ****2.5 Dashboard Groups****

Dashboards can be used to group multiple pages in a single group and used as sub dashboards within another main dashboard and they are configured as Dashboard Groups. Once we specify the groups, later we can arrange which page can be used in which group.

Below is the configuration format for Dashboard Groups.
```
 "dashboard_groups": { 
 "group1": { 
 "icon": "overall.svg", 
 "label": "Network" 
 }, 
 ... 
 ... 
 "group2": { 
 "icon": "jobs.svg", 
 "label": "vCenter" 
 } 
 }, 
 "dashboard_pages": [ 
 { 
 "name": "aia-network-overall", 
 "label": "Network", 
 "icon": "hardware.svg", 
 "group": "group1" 
 } 
 ]

```

Please refer the below table for details about **Dashboard group(s) configuration parameters**.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `icon` | no  | Specify an icon image file name which can be used for the Dashboard group |
| `label` | yes | Specify the label for Dashboard group |

Below is the sample screenshot of **Dashboard Groups**

![Dashboard_Group](https://bot-docs.cloudfabrix.io/images/dashboards/dashboard_groups.png)

### ****2.6 Dashboard Grid Layout****

![Dashboard_Grid_layout](https://bot-docs.cloudfabrix.io/images/dashboards/Grid%20Layout.png)

RDA Dashboards use a grid to display specified widgets. Grid width is always **12**. column parameter of the layout can be between **0** (left most()) to **11** (right most). Grid Height is indefinite. row parameter of layout can start 0 for first row at these top.

RDA Dashboard uses an automated algorithm to layout the specified widgets in a dashboard.

Each widget's size and dimensions within a Dashboard is configured using the below parameters.

*   **min\_width**
*   **height**
*   **max\_width**

Please refer the below configuration example and highlighted parameters
```
 { 
   "name": "my-dashboard", 
   "label": "My Dashboard", 
   "description": "Example dashboard", 
   "enabled": true, 
   "dashboard_style": "tabbed", 
   "dashboard_filters": { 
     "time_filter": true, 
     "columns_filter": [ 
       { 
         "id": "sys_created_on", 
         "label": "Created On", 
         "type": "DATETIME" 
       }, 
       { 
         "id": "assigned_to", 
         "label": "Assigned To", 
         "type": "TEXT" 
       } 
     ] 
   }, 
   "dashboard_sections": [ 
     { 
       "title": "Service Now", 
       "show_filter": true, 
       "widgets": [ 
         { 
           "title": "Sample Data", 
           "widget_type": "tabular", 
           "min_width": 8, 
           "height": 8, 
           "max_width": 12, 
           "timestamp": "sys_created_on", 
           "columns": { 
             "assigned_to": "Assigned To", 
             "sys_created_on": "Created On", 
             "severity": "Severity" 
           }, 
           "dataset": "servicenow_data" 
         } 
       ] 
     } 
   ] 
 }

```

## Dashboard Charts / Widgets

Dashboards support many different types of charts / widgets using which data can be presented and visualized as per the targeted user persona requirements.

Below are the supported widget types & features.

1.  **Pie Chart**
2.  **Tabular Report**
3.  **Counter Chart**
4.  **Bar Chart**
5.  **Multi Bar Chart**
6.  **Line Graph/Timeseries Chart**
7.  **Data Flow Chart**
8.  **Image Chart**
9.  **3-Column Navigator**
10.  **Shaded Chart**
11.  **Label Chart**
12.  **Features**

Please refer the below **widget parameter** table which has the associated type value for each of the above widgets / charts.

| Widget / Chart Parameter Name | Description |
| --- | --- |
| `pie_chart` | A pie chart is a circle / a donut that is divided into areas, or slices. Each area / slice represents the count or percentage of the observations of a level for the variable. |
| `tabular` | Tabular report is used to visualize the data in tabular format using one or more selected fields. |
| `custom_counter` | Custom counter chart is used to show the total count of the selected field's value. |
| `expressions_counter` | Expression counter chart can be used to show the derived computed values using one more fields value. |
| `bar_chart` | Bar chart can be used to display the selected fields values as individual bars (horizontal / vertical) whose height is determined by the value. |
| `topology` | Topology chart is used to visualize the relationship between different nodes or components which exchanges the data between them. |
| `timeseries` | Timeseries is a line graph chart to visualize any timeseries metric data |
| `timeseries_multisource` | Timeseries multisource is another type of line graph chart to visualize any timeseries metric data from more than one datasource |
| `dataflow` | Dataflow chart is used to visualize the dataflow between different end points within the RDA Fabric platform. |
| `image` | Image chart is used to add and visualize any URL based image within a Dashboard. |
| `shaded` | Shaded chart is used to display the Train and Predict Data |
| `label` | Label Chart is used as a Label inside the Dashboard Section |
| `3-column navigator` | A `3-column navigator` is a type of website or application layout where the screen is divided into three vertical sections or columns |

### ****3.1 Pie Chart****

Please refer the below **configuration parameter** table which are used to configure a pie chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the pie chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `pie_chart` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `extra_filter` | no  | Use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `column` | yes | Specify the column name that is to uniquely identify the selected `group_by` column values within each record of persistent stream or dataset. |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `group_by` | yes | Specify one or more columns to apply the group\_by. This parameter supports multiple column values. Ex: "group\_by": \[ "column\_01", "column\_02", "column\_n"\] |
| `type` | no  | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `style` | no  | Using this parameter, each grouped value can be visualized using a specific color using `color-map` parameter as shown in the one of the below examples. |
| `min_width` | no  | Specify the chart / widget's minimum width size, range is `0` to `12`. |
| `height` | no  | Specify the chart / widget's height, range is `0` to `n`. |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is `0` to `12`. |
| `formatting` | no  | To format number with localized units, Use the `style` & `unit` option |
| `notation` | no  | We can specify as `standard`, `compact`, `scientific` and `engineering` **Standard Notation**: is the implied default, **Compact Notation**: uses locale-specific symbols to represent large numbers. It is a more human-friendly alternative to scientific notation, **Scientific Notation**: will only have one significant digit, **Engineering Notation**: will have three significant digits **Note**: By default, **Compact Notation** rounds to the nearest integer, but always keeps 2 significant digits. You can set any of `minimum, maximum`FractionDigits or `minimum, maximum` SignificantDigits to override that behavior |
| `style` | no  | The possible values for style are `currency` & `unit` |
| `unit` | no  | The unit can have following values **angle**: `degree`, **area**: `acre` , `hectare` **concentration**: `percent` **digital**: `bit`, `byte`, `kilobit`, `kilobyte`, `megabit`, `megabyte`, `gigabit`, `gigabyte`, `terabit`, `terabyte`, `petabyte` **duration**: `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `year` **length**: `millimeter`, `centimeter`, `meter`, `kilometer`, `inch`, `foot`, `yard`, `mile`, `mile-scandinavian` **mass**: `gram`, `kilogram`, `ounce`, `pound`, `stone` **temperature**: `celsius`, `fahrenheit` **volume**: `liter`, `milliliter`, `gallon`, `fluid-ounce` **speed**: `meter-per-second` |
| `currency` | no  | The Possible value for currency is `USD` |
| `SignDisplay` | no  | It helps to explicitly display the sign, even when the number is positive. The possible values are `always` To prevent showing the sign when the value is 0, use signDisplay: `exceptZero` |
| `currencySign` | no  | when the `currencySign` is set to `accounting` it enables a locale-specific format for negative currency amounts. example, wrapping the amount in parentheses |
| `top_n` | no  | Filters `top x` values to show ex. When `top_n`:2 then the top 2 values are shown in the chart |
| `bottom_n` | no  | Filters `bottom x` values to show ex. When `bottom_n`:2 then the bottom 2 values are shown in the chart |
| `others_spec` | no  | This Parameter will help in sorting, limiting & labeling the others column |
| `name_based_limit` | no  | This Parameter is used to sort the report by name in ascending order |
| `limit` | no  | This Parameter is used to limit the visible reports |
| `label` | no  | This Parameter is used to rename the others column. By default we have `others` |
| `segment_filter` | no  | When we set this filter as false we don't have the ability to filter when we click on the segment **Note**: By default its TRUE |

Below is the sample configuration of Pie Chart / Widget.
```
  { 
   "widget_type": "pie_chart", 
   "title": "Logs by RDA Host", 
   "stream": "rdaf_services_logs", 
   "ts_column": "timestamp", 
   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", 
   "column": "_id", 
   "agg": "value_count", 
   "group_by": [ 
     "service_host" 
   ], 
   "type": "str", 
   "min_width": 4, 
   "height": 2, 
   "max_width": 4 
 }
 ```

#### ****3.1.1 Sample Pie Chart****

| ****Pie Chart Using Group By Example:**** | ****Pie Chart Using Group By Example Percentage:**** |
| --- | --- |
| ![PieChart_Group_By_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_GroupBy_Example.png) | ![PieChart_Group_By_Example_Percentage](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_GroupBy_Perc_Example.png) |

#### ****3.1.2 Pie Chart using extra\_filter****
```
 { 
   "widget_type": "pie_chart", 
   "title": "Pie Chart Using Extra Filter Example", 
   "stream": "rdaf_services_logs", 
   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", 
   "ts_column": "timestamp", 
   "column": "_id", 
   "agg": "value_count", 
   "group_by": [ 
     "log_severity" 
   ], 
   "type": "str" 
 }

```

![PieChart_Extra_Filter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_Extra_Filter_Example.png)

#### ****3.1.3 Pie Chart with color-mapping****
```
 { 
   "widget_type": "pie_chart", 
   "title": "Pie Chart with Color Map Example", 
   "stream": "rdaf_services_logs", 
   "ts_column": "timestamp", 
   "column": "_id", 
   "agg": "value_count", 
   "group_by": [ 
     "log_severity" 
   ], 
   "type": "str", 
   "style": { 
     "color-map": { 
       "ERROR": [ 
         "#ef5350", 
         "#ffffff" 
       ], 
       "WARNING": [ 
         "#FFA726", 
         "#ffffff" 
       ], 
       "INFO": [ 
         "#388e3c", 
         "#ffffff" 
       ], 
       "DEBUG": [ 
         "#000000", 
         "#ffffff" 
       ], 
       "UNKNOWN": [ 
         "#bcaaa4", 
         "#ffffff" 
       ] 
     } 
   } 
 }

```

![Dashboard_Pie_Chart_with_Color_Map_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_ColorMap_Example.png)

#### ****3.1.4 Pie Chart Showing Bottom N Values****

Below is the sample configuration of Pie Chart Showing Bottom N Values
```
 { 
   "widget_type": "pie_chart", 
   "title": "City", 
   "duration_hours": 1080, 
   "stream": "people_custom_timestamp", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "bottom_n": 3, 
   "type": "int", 
   "min_width": 3, 
   "height": 3, 
   "max_width": 6 
 }

```

![Piechart_BottomExample](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_bottom.png)

#### ****3.1.5 Pie Chart Using Formatting Options****

Below is the sample configuration of Pie Chart Using Formatting Options
```
 { 
   "widget_type": "pie_chart", 
   "title": "Pie Chart", 
   "duration_hours": 1080, 
   "stream": "main", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "formatting": { 
     "style": "unit", 
     "unit": "percent", 
     "signDisplay": "always" 
   }, 
   "type": "int", 
   "min_width": 3, 
   "height": 3, 
   "max_width": 6 
 }

```

![Piechart_Formatting Example](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_formatting.png)

#### ****3.1.6 Pie Chart Using Others Spec****

Below is the sample configuration of Pie Chart Using Others Spec
```
 { 
   "widget_type": "pie_chart", 
   "title": "Name- Pie chart", 
   "duration_hours": 10800, 
   "stream": "main", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "others_spec": { 
   "city": { 
   "name_based_limit": true 
     } 
   }, 
   "type": "int", 
   "min_width": 6, 
   "height": 6, 
   "max_width": 6 
 }

```

![Piechart_Others_Spec_Pie](https://bot-docs.cloudfabrix.io/images/dashboards/others_spec_pie.png)

#### ****3.1.7 Pie Chart Using Sorting Type****

Please refer the below **configuration parameter** table which are additionally used to configure a Pie Chart Using Sorting Type within the dashboard.

Note

**semantic sort**: is used to sort data by month, weekday, date, severity, priority

**ordinal sort**: is used for custom ordering that is specified by an ordered set in widget definition

**lexical sort**: is used to have control over case sensitivity in standard sort

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `groups_meta` | yes | This Parameter is used for sorting groups in reports. Possible values are `type`,`ignore_case`,`order`,`format` |
| `type` | yes | This Parameter is used to specify the sorting type, Expected Parameters are `month`, `weekday` , `date` , `severity` , `priority`, `custom` |
| `order` | no  | is to specify a custom ordered set when the type is custom, Expected Order to Pass `<str1>, <str2>, <str3>….<strn>` |
| `format` | no  | This Parameter is to specify the date format using the python date format rules, Expected format `%d %b %Y`,`%d-%b-%Y` |
| `ignore_case` | no  | This Parameter specifies if the data values must be a case sensitive match to the Ordinal values, Expected Parameters are |

Below is the sample configuration of Pie Chart Using Sorting Type / Widget.
```
 { 
   "widget_type": "pie_chart", 
   "title": "Date based Pie_chart", 
   "duration_hours": 10800, 
   "stream": "trail", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "value_count", 
   "group_by": [ 
     "date" 
   ], 
   "groups_meta": { 
     "type": "date", 
     "format": "%d-%b-%y" 
   }, 
   "type": "int", 
   "limit": 15, 
   "min_width": 6, 
   "height": 5, 
   "max_width": 6 
 }

```

![Piechart_Piechart_Sorting_Type](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_sorting_type.png)

#### ****3.1.8 Pie Chart with No Filter Option****

Below is the sample configuration of Pie Chart Using Sorting Type / Widget.
```
 { 
   "widget_type": "pie_chart", 
   "title": "Pie Chart ", 
   "stream": "main", 
   "ts_column": "timestamp", 
   "description": "Pie Charts", 
   "segment_filter": false, 
   "column": "donation", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "min_width": 3, 
   "max_width": 4, 
   "type": "str" 
 }

```

![Piechart_ Segment](https://bot-docs.cloudfabrix.io/images/dashboards/segment.png)

Note

When user clicks on the segment and when the `segment_filter` is set to `false` user would not have the ability to filter

### ****3.2 Tabular Report****

Please refer the below **configuration parameter** table which are used to configure a Tabular report within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Tabular report. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `tabular` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed. |
| `query` | no  | Specify CFXQL based query to filter the data. `*` gets all of the data from the selected persistent stream or dataset. |
| `truncateColumns` | no  | Specify the array of fields / columns (comma separated) which need to be truncated if the length of the value is very long. It shows the full value on mouse hover. |
| `resizableColumns` | no  | Specify `true` or `false` to enable or disable to enable the flexibility of adjusting each column's width |
| `paginated` | no  | Specify `true` or `false` to enable or disable paginated data for tabular report. |
| `virtual_scrolling` | no  | Specify `true` or `false` to enable or disable this parameter. It allows to scroll through the paginated data instead of manually going through one page at a time. |
| `showRowSummary` | no  | Specify `true` or `false` to enable or disable this parameter. It provides a clickable UI option for each row to view it's summary that includes all of the columns and their values in a vertical form. |
| `max_rows` | no  | Specify the maximum number of rows to be shown within a page. |
| `sorting` | no  | Specify the column / field names on which the sorting to enabled. Supported values for sorting is `desc` or `asc`. The default value is `desc` |
| `columns` | yes | Specify one or more columns / fields to be shown in the tabular report. Syntax is as shown above. `columns: { "column_a_name": "column a label", "column_b_name": "column b label", ...}` |
| `min_width` | no  | Specify the chart / widget's minimum width size, range is `0` to `12`. |
| `height` | no  | Specify the chart / widget's height, range is `0` to `n`. |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is `0` to `12`. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `remote_searchable` | no  | is set to true by default. If users want local search, they can set it to false. |
| `remote_searchable_cols` | no  | is set, we will honor the fields in here for remote search. If it is not set, we will use up-to 10 TEXT visible columns defined in the table. |
| `remote_search_columns_count` | no  | is set, to specify how many columns to pick for remote search. |
| `custom_columns` | no  | Allows user to add the expression to the columns. |
| `columnGroupLabel` | no  | Allows user to add Header to multiple columns. |
| `Pivot` | no  | Pivot table is used to arrange, group and summarize for an easy analysis of large sets of data in a tabular form.Supported values are pivot\_type, agg,group\_by, columns, series. |
| `pivot_type` | no  | Supported pivot types are standard, extended and advanced. By default its standard |
| `group_by` | yes | Specify column to apply |
| `agg` | yes | Specify the aggregation function. Supported values are value\_count (shows total count), min, max & cardinality (shows unique count) |
| `column` | yes | Name of the column in the data to perform aggregations |
| `series` | no  | if pivot\_type is extended or advanced, this is mandatory |
| `label` | yes | if new column is created, then this will let user to add the label to that column |

#### ****3.2.1 Sample Tabular Report****

Below is the sample configuration of Tabular Report / Widget.
```
 { 
   "title": "Tabular with Pstream Query Example", 
   "widget_type": "tabular", 
   "stream": "dli-synthetic-logs-raw", 
   "query": "*", 
   "min_width": 6, 
   "height": 8, 
   "max_width": 6, 
   "paginated": true, 
   "remote_searchable": true, 
   "remote_searchable_cols": [ 
        "device", 
        "message" 
   ], 
   "max_rows": 50, 
   "sorting": [ 
     { 
       "timestamp": "desc" 
     } 
   ], 
   "columns": { 
     "timestamp": "Timestamp", 
     "device": "Device", 
     "count_": "Count", 
     "message": "Message" 
   }, 
   "widget_id": "94a3fc11" 
 }

```

![Time_Series_Stream_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tablular_Query.png)

#### ****3.2.2 Tabular Report with truncateColumns****

Below is the sample configuration of Tabular Report / Widget with `truncateColumns` parameter.
```
 { 
   "title": "Tabular chart with truncate columns", 
   "widget_type": "tabular", 
   "stream": "main", 
   "columns": { 
     "name": { 
       "title": "Name", 
       "formatter": "truncate" 
     }, 
     "city": { 
       "title": "City" 
     } 
   } 
 }

``` 

![tabular report truncate Columns](https://bot-docs.cloudfabrix.io/images/dashboards/tabular_report_truncate_Columns.png)

#### ****3.2.3 Tabular Report with resizableColumns****

Below is the sample configuration of Tabular Report / Widget with `resizableColumns` parameter.
```
 { 
   "title": "Tabular with Pstream Query resizableColumns Example", 
   "widget_type": "tabular", 
   "stream": "dli-synthetic-logs-raw", 
   "query": "*", 
   "min_width": 6, 
   "height": 8, 
   "max_width": 6, 
   "resizableColumns": true, 
   "paginated": true, 
   "max_rows": 50, 
   "sorting": [ 
     { 
       "timestamp": "desc" 
     } 
   ], 
   "columns": { 
     "timestamp": "Timestamp", 
     "device": "Device", 
     "count_": "Count", 
     "message": "Message" 
   }, 
   "widget_id": "94a3fc11" 
 }

```

![Tabular_resizableColumns_before_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tabular_resizableColumns_before.png)

![Tabular_resizableColumns_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tabular_ResizableColumn.png)

#### ****3.2.4 Tabular Report with virtual\_scrolling & showRowSummary****

Below is the sample configuration of Tabular Report / Widget with `Virtual_scrolling & showRowSummary` parameter.
```
 { 
   "title": "virtual_scrolling and showRowSummary", 
   "widget_type": "tabular", 
   "stream": "rda_synthetic_metrics", 
   "ts_column": "timestamp", 
   "query": "*", 
   "min_width": 6, 
   "height": 8, 
   "max_width": 6, 
   "paginated": true, 
   "virtual_scrolling": true, 
   "showRowSummary": true, 
   "max_rows": 50, 
   "sorting": [ 
     { 
       "timestamp": "desc" 
     } 
   ], 
   "columns": { 
     "timestamp": "Timestamp", 
     "metric_name": "metric_name", 
     "count_": "Count", 
     "source_tool": "source_tool", 
     "stack_name": "stack_name" 
   }, 
   "widget_id": "94a3fc11" 
 }

```

![Tabular_Virtual_scrolling_showsummary_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Virtual_scrolling_showsummary.png)

#### ****3.2.5 Tabular Report with Column Specific Hyperlink****

Below is the sample configuration of Tabular Report / Widget with `Column specific Hyperlink`.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `appName` | yes | Specify the appName. Supported values are `user-dashboard` |
| `permission` | yes | Specify the permission in order to enable Hyperlink. Supported values are `aia:page:view`, `oia:page:view` |
| `drillDownContext` | yes | Context column-id that needs to be passed to the landing dashboard |
| `drillDownLinkField` | yes | Column-id that needs to be enabled with hyperlink |
| `identifier` | yes | Column-id that needs to be enabled with hyperlink |
| `selectionType` | yes | Specify the selectionType. Supported values are `SINGLE` |
| `stateName` | yes | Specify the stateName. Supported values are `app.featureapp` |
| `title` | yes | Specify the label for the action |
| `actionCondition` | no  | Enables hyperlink when it satisfies action conditions |
| `actionControl` | no  | Specify the actionControl. Supported values are `SHOW_IF` |
| `conditionType` | no  | Specify the conditionType. Supported values are `EQUAL` |
| `conditionValue` | no  | Matches according to the value present in stream data |
| `fieldId` | no  | Need to pass column-id that has condition value specified |
| `type` | yes | Specify the app type. Supported values are `GO_TO_APP_STATE`. |
```
 "actions": [ 
   { 
     "appName": "user-dashboard", 
     "permission": "aia:page:view", 
     "drillDownContext": "id", 
     "drillDownLinkField": "dns_name", 
     "identifier": "dns_name", 
     "selectionType": "SINGLE", 
     "stateName": "app.featureapp", 
     "title": "View Details", 
     "actionCondition": { 
       "actionControl": "SHOW_IF", 
       "conditionalField": [ 
         { 
           "conditionType": "EQUAL", 
           "conditionValue": "CHASSIS", 
           "fieldId": "equipment_type" 
         } 
       ] 
     }, 
     "type": "GO_TO_APP_STATE" 
   } 
 ]

```

Note

Mentioned below needs to be part of the columns list and the value needs to be replaced with the template/dashboard/app name

Ex: user-dashboard-`<template/dashboard/app name>`
```
 "id": { 
        "title": "ID", 
        "value": "user-dashboard-aia-network-drilldown-app", 
        "key": true, 
        "type": "FIXED_VALUE", 
        "hidden": true, 
        "visible": false 
       }

```

Note

All the report definitions that are part of the above `template/dashboard/app` needs to be added with mentioned below parameters
```
 "include_context_in_query": true 
 "include_context_keys" : ["column1","column2","column3"]

```

Note

In order to pass column(s) as a context to `template/dashboard/app`, make sure the list of `include_context_keys` mentioned above are the key column(s)

[Example](#__tabbed_1_1)
```
 "dns_name": { 
               "title": "DNS Name", 
               "type": "TEXT", 
               "key": true 
             }

```

#### ****3.2.6 Tabular Report with External URL Hyperlink****

Below is the sample configuration of Tabular Report / Widget with `External URL Hyperlink`.

Note

Make sure the URL values are present as one of the column value in Pstream/Dataset as shown in Below Example

Below is how the column needs to be added in order to enable External URL on Specific column
```
 "<column-id>": { 
         "title": "<label>", 
         "htmlTemplateForRow": "<a href=\"{{row.<column-id>}}\" target='_blank'>{{row.<column-id>}}</a>" 
        }

```

[Example](#__tabbed_2_1)
```
 "drilldown_url": { 
         "title": "Drilldown_URL", 
         "htmlTemplateForRow": "<a href=\"{{row.drilldown_url}}\" target='_blank'>{{row.controller_name}}</a>" 
        }

```

Note

Same URL link can be launched by enabling hyperlink on different column, Below is the syntax for `column Definition`
```
 "drilldown_url": { 
         "title": "Controller", 
         "htmlTemplateForRow": "<a href=\"{{row.drilldown_url}}\" target='_blank'>{{row.controller_name}}</a>" 
        }

```

#### ****3.2.7 Tabular Report with Custom Columns****

Please refer the below **configuration parameter** table which are additionally used to configure a Tabular Report Using Custom Columns within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `id` | yes | It will be the column\_id for the custom column, If you want to use that column any where else you can refer with that column id |
| `expr` | yes | The expression on any arithmetic operations on given columns will support the following syntax for example: `expr`: "((input-output)/input) \* 100" |
| `label` | yes | This will specify the label for obtained column |

Below is the sample configuration of Tabular Report / Widget with `custom_columns`.
```
 { 
   "widget_type": "tabular", 
   "title": "Summary Report", 
   "stream": "network-devices-inventory", 
   "ts_column": "collection_timestamp", 
   "sorting": [], 
   "extra_filter": "up_eth_ports is not None", 
   "columns": { 
     "up_eth_ports": "UP ETH PORTS", 
     "total_eth_ports": "TOTAL ETH PORTS" 
   }, 
   "custom_columns": [ 
     { 
       "id": "avg_up_ports", 
       "label": "Avg UP Ports(%)", 
       "expr": "((up_eth_ports / total_eth_ports) * 100) " 
     } 
   ] 
 }

```

![Custom_Clolumns_Example](https://bot-docs.cloudfabrix.io/images/dashboards/custom_columns.png)

#### ****3.2.8 Tabular Report with Remote Search & Local Search****

Below is the sample configuration of Tabular Report / Widget with `remote search & local search`.

[Remote Search](#__tabbed_3_1)
```
 { 
   "title": "Tabular report with Remote Search enabled on first column only", 
   "widget_type": "tabular", 
   "duration_hours": 10000, 
   "stream": "people_1k", 
   "min_width": 8, 
   "height": 5, 
   "paginated": true, 
   "max_rows": 50, 
   "defaultColumnWidth": 100, 
   "remote_search_columns_count": 1, 
   "remote_searchable_cols": [ 
     "city" 
   ], 
   "columns": { 
     "name": "Name", 
     "city": "City", 
     "age": "Age", 
     "timestamp": "Timestamp" 
   } 
 }

```

![Remote Search_Example](https://bot-docs.cloudfabrix.io/images/dashboards/remote_search.png)

[Local Search](#__tabbed_4_1)
```
 { 
   "title": "Tabular report with Local Search", 
   "widget_type": "tabular", 
   "stream": "main", 
   "min_width": 8, 
   "height": 5, 
   "paginated": true, 
   "max_rows": 50, 
   "defaultColumnWidth": 100, 
   "remote_searchable": false, 
   "columns": { 
     "name": "Name", 
     "city": { 
       "title": "City" 
     }, 
     "timestamp": { 
       "title": "Timestamp" 
     } 
   } 
 }

```

![Remote Search_Example](https://bot-docs.cloudfabrix.io/images/dashboards/local_search.png)

#### ****3.2.9 Tabular Report with Grouped Columns****

Below is the sample configuration of Tabular Report / Widget with `Grouped Columns`.
```
 { 
   "title": "Grouping in Tabular", 
   "widget_type": "tabular", 
   "stream": "main", 
   "columns": { 
     "name": { 
       "title": "Name", 
       "columnGroupLabel": "Group 1", 
       "defaultColumnWidth": 60, 
       "visible": true 
     }, 
     "city": { 
       "title": "City", 
       "columnGroupLabel": "Details 1", 
       "defaultColumnWidth": 60, 
       "visible": true 
     }, 
     "age": { 
       "title": "Age", 
       "columnGroupLabel": "Group 1", 
       "defaultColumnWidth": 20, 
       "visible": true 
     }, 
     "timestamp": { 
       "title": "Timestamp", 
       "type": "DATETIME", 
       "columnGroupLabel": "Details 2", 
       "defaultColumnWidth": 300 
     } 
   } 
 }

```

[![Grouped Columns](https://bot-docs.cloudfabrix.io/images/dashboards/grouped_columns.png)](/images/dashboards/grouped_columns.png)

#### ****3.2.10 Pivot Tabular Report****

Below is the sample configuration of Pivot Tabular Report.
```
 { 
   "title": "Mock Data Standard", 
   "widget_type": "tabular", 
   "stream": "mock_data", 
   "min_width": 12, 
   "height": 6, 
   "max_width": 12, 
   "columns": { 
     "A": "A", 
     "B": "B" 
   }, 
   "pivot": { 
     "pivot_type": "standard", 
     "group_by": [ 
       "A", 
       "B" 
     ], 
     "column": "count_", 
     "agg": "value_count" 
   }   
 }

```

[![Standard Pivot](https://bot-docs.cloudfabrix.io/images/dashboards/standard_pivot.png)](/images/dashboards/standard_pivot.png)

#### ****3.2.11 Extended Pivot Tabular Report****

Below is the sample configuration of Extended Pivot Tabular Report.
```
 { 
   "title": "Mock Data Extended", 
   "widget_type": "tabular", 
   "stream": "mock_data", 
   "min_width": 12, 
   "height": 6, 
   "max_width": 12, 
   "columns": { 
     "A": "A", 
     "B": "B" 
   }, 
   "pivot": { 
     "pivot_type": "extended", 
     "group_by": [ 
       "A", 
       "B" 
     ], 
     "series": [ 
       { 
         "column": "count_", 
         "agg": "value_count", 
         "type": "int", 
         "label": "Count" 
       } 
     ] 
   } 
 }

```

[![Extended Pivot](https://bot-docs.cloudfabrix.io/images/dashboards/extended_pivot.png)](/images/dashboards/extended_pivot.png)

#### ****3.2.12 Advanced Pivot Tabular Report****

Below is the sample configuration of Advanced Pivot Tabular Report.
```
 { 
   "title": "Mock Data Advanced", 
   "widget_type": "tabular", 
   "stream": "mock_data", 
   "min_width": 12, 
   "height": 6, 
   "max_width": 12, 
   "columns": { 
     "A": "A", 
     "B": "B" 
   }, 
   "pivot": { 
     "pivot_type": "advanced", 
     "group_by": [ 
       "A", 
       "B" 
     ], 
     "series": [ 
       { 
         "column": "count_", 
         "agg": "value_count", 
         "type": "int", 
         "label": "Count" 
       } 
     ] 
   } 
 }

```

[![Advanced Pivot](https://bot-docs.cloudfabrix.io/images/dashboards/advanced_pivot.png)](/images/dashboards/advanced_pivot.png)

### ****3.3 Counter Chart****

Please refer the below **configuration parameter** table which are used to configure a simple Counter chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Group Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `counter`,`custom_counter`,`expression_counter` |
| `formatter` | no  | Formats integer values as K for thousands, M for Millions. If the input value is already a counted as thousands, optional value multiplier can be specified. |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `duration_hours` | no  | this parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` or `float` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `expression` | yes | the expression on any arithmetic operations on given columns will support Example syntax: "expression": "((input-output)/input) \* 100" needed only for expression\_counter not needed for other counter types |
| `unit` | yes | Units to be displayed next to the value |
| `segments` | yes | Segments is a list of objects. Each segment defines a variable to be computed. needed only for expression\_counter |
| `extra_filter` | no  | Use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `min_Width` | no  | Specify the timestamp column name within the selected persistent stream or dataset. |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is 0 to 12. |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` or `float` option is valid only for `min`, `max`, `sum`, `mean` |
| `variable` | no  | Name of the variable to be computed. **Note** This variable name may be used in expression. |
| `duration_hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group_by` | yes | Specify one or more columns to apply the group\_by. This parameter supports multiple column values. Ex: "group\_by": \[ "column\_01", "column\_02", "column\_n"\] |
| `formatter` | yes | Formats integer values as K for thousands, M for Millions. If the input value is already a counted as thousands, optional value multiplier can be specified. |
| `style` | no  | Using this parameter, each grouped value can be visualized using a specific color using `color-map` parameter as shown in the above example. **Note** not needed in custom\_counter and expression\_counter |
| `limit` | no  | Limiting of groups/segments |
| `sparkline` | no  | Optional visualization configuration for the grouped counts with default interval as 1D, fill as True and smooth also as True |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, it is autogenerated if not provided |
| `total_counter` | no  | When widget\_type is set to counter this parameter enables showing an additional counter chart that sums up the values of counter charts and shows the total. |

#### ****3.3.1 Simple Counter Chart Example****

Below is a sample configuration of Counter Chart / Widget.
```
 { 
   "title": "Simple Counter Example", 
   "widget_type": "custom_counter", 
   "formatter": "DescriptiveCountFormatter", 
   "stream": "rda_system_worker_trace_summary", 
   "ts_column": "timestamp", 
   "duration_hours": 96, 
   "column": "num_bot_executions", 
   "agg": "sum", 
   "type": "int", 
   "widget_id": "02be1e20" 
 }

```

![Dashboard_Simple_Counter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Simple_Counter.png)

#### ****3.3.2 Expression Counter Example****

Below is a sample configuration of Counter Chart / Widget with `expression_counter` and `expression`.
```
 { 
   "title": "Expression Counter Example", 
   "widget_type": "expression_counter", 
   "expression": "((input-output)/input) * 100", 
   "unit": "%", 
   "segments": [ 
     { 
       "variable": "output", 
       "stream": "dli-log-stats", 
       "extra_filter": "mode is 'processed'", 
       "ts_column": "timestamp", 
       "duration_hours": 720, 
       "group_by": [ 
         "mode" 
       ], 
       "column": "count", 
       "agg": "sum", 
       "type": "int" 
     }, 
     { 
       "variable": "input", 
       "stream": "dli-log-stats", 
       "extra_filter": "mode is 'ingested'", 
       "ts_column": "timestamp", 
       "duration_hours": 720, 
       "group_by": [ 
         "mode" 
       ], 
       "column": "count", 
       "agg": "sum", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Expression_Counter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Expression_Counter.png)

#### ****3.3.3 Group Counter Chart Example****

Note

To show up the **Total Counter**, Use the following parameters:

`show` - Set it to true for total counter chart to show up.

`label` - Optional. Default: “Total”.

`location` - Where to show the total counter. Optional. Default: “left”.

`color` - Hex Color Code

Below is a sample configuration of Counter Chart / Widget grouping multiples of them.
```
 { 
   "title": "Group Counter Chart Example", 
   "widget_type": "counter", 
   "min_width": 12, 
   "max_width": 12, 
   "stream": "main", 
   "ts_column": "timestamp", 
   "style": { 
     "color-map": { 
       "Chennai": "#388e3c", 
       "Delhi": "#8e24aa", 
       "Mumbai": "#d32f2f" 
     } 
   }, 
   "sparkline": { 
     "interval": "1d" 
   }, 
   "group_by": [ 
     "city" 
   ], 
   "total_counter": { 
     "show": true, 
     "label": "Total Count", 
     "location": "right", 
     "color": "#0096FF" 
   }, 
   "column": "count_", 
   "agg": "sum", 
   "type": "int" 
 }

```

[![](https://bot-docs.cloudfabrix.io/images/dashboards/Group_Counter_Chart.png)](/images/dashboards/Group_Counter_Chart.png)

### ****3.4 Bar Chart****

Please refer the below **configuration parameter** table which are used to configure a Bar chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Bar Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `bar_chart` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `chartProperties` |     | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `duration hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group by` | yes | Specify one or more columns to apply `group_by`. This parameter supports multiple column values. Ex: `"group_by": [ "column_01", "column_02", "column_n"]` |
| `extra_filter` | no  | use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | no  | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `formatting` | no  | To format number with localized units, Use the `style` & `unit` option |
| `notation` | no  | We can specify as `standard`, `compact`, `scientific` and `engineering` **Standard Notation**: is the implied default, **Compact Notation**: uses locale-specific symbols to represent large numbers. It is a more human-friendly alternative to scientific notation, **Scientific Notation**: will only have one significant digit, **Engineering Notation**: will have three significant digits **Note**: By default, **Compact Notation** rounds to the nearest integer, but always keeps 2 significant digits. You can set any of `minimum, maximum`FractionDigits or `minimum, maximum` SignificantDigits to override that behavior |
| `style` | no  | The possible values for style are `currency` & `unit` |
| `unit` | no  | The unit can have following values **angle**: `degree`, **area**: `acre` , `hectare` **concentration**: `percent` **digital**: `bit`, `byte`, `kilobit`, `kilobyte`, `megabit`, `megabyte`, `gigabit`, `gigabyte`, `terabit`, `terabyte`, `petabyte` **duration**: `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `year` **length**: `millimeter`, `centimeter`, `meter`, `kilometer`, `inch`, `foot`, `yard`, `mile`, `mile-scandinavian` **mass**: `gram`, `kilogram`, `ounce`, `pound`, `stone` **temperature**: `celsius`, `fahrenheit` **volume**: `liter`, `milliliter`, `gallon`, `fluid-ounce` **speed**: `meter-per-second` |
| `currency` | no  | The Possible value for currency is `USD` |
| `SignDisplay` | no  | It helps to explicitly display the sign, even when the number is positive. The possible values are `always` To prevent showing the sign when the value is 0, use signDisplay: `exceptZero` |
| `currencySign` | no  | when the `currencySign` is set to `accounting` it enables a locale-specific format for negative currency amounts. example, wrapping the amount in parentheses |
| `top_n` | no  | Filters `top x` values to show ex. When `top_n`:2 then the top 2 values are shown in the chart |
| `bottom_n` | no  | Filters `bottom x` values to show ex. When `bottom_n`:2 then the bottom 2 values are shown in the chart |
| `others_spec` | no  | This Parameter will help in sorting, limiting & labeling the others column |
| `name_based_limit` | no  | This Parameter is used to sort the report by name in ascending order |
| `limit` | no  | This Parameter is used to limit the visible reports |
| `label` | no  | This Parameter is used to rename the others column. By default we have `others` |

#### ****3.4.1 Bar Chart Example****

Below is a sample of Bar Chart / Widget configuration.
```
 { 
   "title": "Bar Chart Example", 
   "widget_type": "bar_chart", 
   "stream": "rda_microservice_traces", 
   "ts_column": "timestamp", 
   "chartProperties": { 
     "yAxisLabel": null, 
     "xAxisLabel": "Count", 
     "stacked": true, 
     "legendLocation": "none", 
     "orientation": "vertical" 
   }, 
   "duration_hours": 24, 
   "group_by": [ 
     "request_type" 
   ], 
   "column": "duration", 
   "agg": "value_count", 
   "type": "int", 
   "widget_id": "f4786acb" 
 }

```

![Dashboard_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Bar_Chart.png)

#### ****3.4.2 Bar Chart with extra filter****

Below is a sample of Bar Chart / Widget configuration with `extra_filter`
```
 { 
   "title": "Bar Chart Example", 
   "widget_type": "bar_chart", 
   "stream": "rda_microservice_traces", 
   "extra_filter": "request_type != 'are-you-there'", 
   "ts_column": "timestamp", 
   "chartProperties": { 
     "yAxisLabel": null, 
     "xAxisLabel": "Count", 
     "stacked": true, 
     "legendLocation": "none", 
     "orientation": "vertical" 
   }, 
   "duration_hours": 24, 
   "group_by": [ 
     "request_type" 
   ], 
   "column": "duration", 
   "agg": "value_count", 
   "type": "int", 
   "widget_id": "f4786acb" 
 }

```

![Dashboard_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Barchart_with_filter.png)

#### ****3.4.3 Bar Chart with Formatting Option****

Below is a sample configurations of Bar Chart with Formatting Options / Widget.

[Formatting Style Unit](#__tabbed_5_1)
```
 { 
   "widget_type": "bar_chart", 
   "title": "BAR CHART with formatting option", 
   "stream": "main", 
   "chartProperties": { 
     "orientation": "vertical" 
   }, 
   "formatting": { 
     "style": "unit", 
     "unit": "percent", 
     "signDisplay": "exceptZero" 
   }, 
   "ts_column": "timestamp", 
   "column": "count_", 
   "agg": "value_count", 
   "group_by": [ 
     "name" 
   ], 
   "type": "str" 
 }

```

![Dashboard_Formating_Percent](https://bot-docs.cloudfabrix.io/images/dashboards/formating_percent.png)

[Formatting Style Currency](#__tabbed_6_1)
```
 { 
   "widget_type": "bar_chart", 
   "title": "City asset value", 
   "stream": "people_custom_timestamp", 
   "chartProperties": { 
     "barThickness": 10, 
     "orientation": "vertical" 
   }, 
   "formatting": { 
     "style": "currency", 
     "currency": "USD" 
   }, 
   "ts_column": "timestamp", 
   "column": "count_", 
   "agg": "value_count", 
   "group_by": [ 
     "city" 
   ], 
   "type": "str" 
 }

```

![Dashboard_Formatting_Currency](https://bot-docs.cloudfabrix.io/images/dashboards/formatting_currency.png)

[Formatting with Standard Notation](#__tabbed_7_1)
```
 { 
   "widget_type": "bar_chart", 
   "title": "City Donation Value", 
   "stream": "donationn", 
   "chartProperties": { 
     "orientation": "vertical" 
   }, 
   "formatting": { 
     "notation": "standard" 
   }, 
   "ts_column": "timestamp", 
   "column": "donation", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "type": "int" 
 }

```

![Dashboard_standard_notation](https://bot-docs.cloudfabrix.io/images/dashboards/standard_notation.png)

[Formatting with Compact Notation](#__tabbed_8_1)
```
 { 
   "widget_type": "bar_chart", 
   "title": "City Donation Value", 
   "stream": "donationn", 
   "chartProperties": { 
     "orientation": "vertical" 
   }, 
   "formatting": { 
     "notation": "compact" 
   }, 
   "ts_column": "timestamp", 
   "column": "donation", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "type": "int" 
 }

```

![Dashboard_Compact_notation](https://bot-docs.cloudfabrix.io/images/dashboards/compact_notation.png)

#### ****3.4.4 Bar Chart Showing Top N Values****

Below is a sample configuration of Bar Chart Showing Top N Values / Widget.
```
 { 
   "widget_type": "bar_chart", 
   "title": "City Donation Value", 
   "stream": "donationn", 
   "chartProperties": { 
     "orientation": "vertical" 
   }, 
   "formatting": { 
     "notation": "compact" 
   }, 
   "ts_column": "timestamp", 
   "top_n": 3, 
   "column": "donation", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
   "type": "str" 
 }

```

![Dashboard_Barchart_Topn](https://bot-docs.cloudfabrix.io/images/dashboards/barchart_topn.png)

#### ****3.4.5 Bar Chart With Others Spec****

Below is a sample configuration of Bar Chart With Others Spec / Widget.
```
 { 
   "widget_type": "bar_chart", 
   "title": "Name based sort in Bar", 
   "duration_hours": 1080, 
   "stream": "main", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "sum", 
   "group_by": [ 
     "city" 
   ], 
     "others_spec": { 
     "label": "other state", 
     "Country": { 
     "name_based_limit": true 
     } 
   }, 
   "type": "int", 
   "min_width": 6, 
   "height": 6, 
   "max_width": 6 
 }

```

![Dashboard_Others_spec](https://bot-docs.cloudfabrix.io/images/dashboards/others_spec.png)

#### ****3.4.6 Bar Chart Using Sorting Type****

Please refer the below **configuration parameter** table which are additionally used to configure a Bar Chart Using Sorting Type within the dashboard.

Note

**semantic sort**: is used to sort data by month, weekday, date, severity, priority

**ordinal sort**: is used for custom ordering that is specified by an ordered set in widget definition

**lexical sort**: is used to have control over case sensitivity in standard sort

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `groups_meta` | yes | This Parameter is used for sorting groups in reports. Possible values are `type`,`ignore_case`,`order`,`format` |
| `type` | yes | This Parameter is used to specify the sorting type, Expected Parameters are `month`, `weekday` , `date` , `severity` , `priority`, `custom` |
| `order` | no  | This Parameter is to specify a custom ordered set when the type is custom, Expected Order to Pass `<str1>, <str2>, <str3>….<strn>` |
| `format` | no  | This Parameter is to specify the date format using the python date format rules, Expected format `%d %b %Y`,`%d-%b-%Y` |
| `ignore_case` | no  | This Parameter specifies if the data values must be a case sensitive match to the Ordinal values, Expected Parameters are |

Below is the sample configuration of Bar Chart Using Sorting Type / Widget.
```
 { 
   "widget_type": "bar_chart", 
   "title": "Month based Bar", 
   "duration_hours": 10800, 
   "stream": "trail", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "value_count", 
   "group_by": [ 
     "Months" 
   ], 
   "groups_meta": { 
     "type": "month" 
   }, 
   "type": "int", 
   "limit": 15, 
   "min_width": 6, 
   "height": 5, 
   "max_width": 6 
 }

```

![Dashboard_Barchart_Sorting_Type](https://bot-docs.cloudfabrix.io/images/dashboards/barchart_sorting_type.png)

#### ****3.4.7 Fixed Bar Width Chart****

Please refer the below **configuration parameter** table which are used to configure a Fixed Bar Width Chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the FIXED\_BAR\_WIDTH\_CHART. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `fixed_bar_width_chart` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `chartProperties` | yes | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like barThickness, zooming, color etc... |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `duration hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group by` | yes | Specify one or more columns to apply `group_by`. This parameter supports multiple column values. Ex: `"group_by": [ "column_01", "column_02", "column_n"]` |
| `extra_filter` | no  | use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | no  | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |

Below is a sample configuration of Fixed Bar Width Chart / Widget.
```
 { 
   "title": "FIXED_BAR_WIDTH_CHART", 
   "widget_type": "fixed_bar_width_chart", 
   "stream": "people_custom_timestamp", 
   "chartProperties": { 
     "barThickness": 100 
   }, 
   "ts_column": "timestamp", 
   "column": "age", 
   "agg": "value_count", 
   "group_by": [ 
     "city" 
   ] 
 }

```

![Dashboard_Width_chart](https://bot-docs.cloudfabrix.io/images/dashboards/width_chart.png)

### ****3.5 Multi Bar Chart****

Please refer the below **configuration parameter** table which are used to configure a Multi Bar chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Multi Bar Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `multi_bar_chart` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `extra_filter` | no  | use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `chartProperties` |     | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `duration hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group_by` | yes | Specify one or more columns to apply the `group_by`. This parameter supports multiple column values. Ex: `"group_by": [ "column_01", "column_02", "column_n"]` |
| `Column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `limit` | no  | Limiting of groups/segments |
| `formatting` | no  | To format number with localized units, Use the `style` & `unit` option |
| `notation` | no  | We can specify as `standard`, `compact`, `scientific` and `engineering` **Standard Notation**: is the implied default, **Compact Notation**: uses locale-specific symbols to represent large numbers. It is a more human-friendly alternative to scientific notation, **Scientific Notation**: will only have one significant digit, **Engineering Notation**: will have three significant digits **Note**: By default, **Compact Notation** rounds to the nearest integer, but always keeps 2 significant digits. You can set any of `minimum, maximum`FractionDigits or `minimum, maximum` SignificantDigits to override that behavior |
| `style` | no  | The possible values for style are `currency` & `unit` |
| `unit` | no  | The unit can have following values **angle**: `degree`, **area**: `acre` , `hectare` **concentration**: `percent` **digital**: `bit`, `byte`, `kilobit`, `kilobyte`, `megabit`, `megabyte`, `gigabit`, `gigabyte`, `terabit`, `terabyte`, `petabyte` **duration**: `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `year` **length**: `millimeter`, `centimeter`, `meter`, `kilometer`, `inch`, `foot`, `yard`, `mile`, `mile-scandinavian` **mass**: `gram`, `kilogram`, `ounce`, `pound`, `stone` **temperature**: `celsius`, `fahrenheit` **volume**: `liter`, `milliliter`, `gallon`, `fluid-ounce` **speed**: `meter-per-second` |
| `currency` | no  | The Possible value for currency is `USD` |
| `SignDisplay` | no  | It helps to explicitly display the sign, even when the number is positive. The possible values are `always` To prevent showing the sign when the value is 0, use signDisplay: `exceptZero` |
| `currencySign` | no  | when the `currencySign` is set to `accounting` it enables a locale-specific format for negative currency amounts. example, wrapping the amount in parentheses |
| `others_spec` | no  | This Parameter will help in sorting, limiting & labeling the others column |
| `largest` | no  | This Parameter is used to sort the report by largest value in asc order |
| `descending_order` | no  | This Parameter is used to sort the report by largest value in descending order |
| `name_based_limit` | no  | This Parameter is used to sort the report by name in ascending order |
| `limit` | no  | This Parameter is used to limit the visible reports |
| `label` | no  | This Parameter is used to rename the others column. By default we have `others` |

#### ****3.5.1 Multi Bar Chart Example****

Below is a sample configuration of Multi Bar Chart / Widget .
```
 { 
   "title": "Multi Bar Chart Example", 
   "widget_type": "multi_bar_chart", 
   "stream": "rda_microservice_traces", 
   "extra_filter": "request_type != 'are-you-there'", 
   "ts_column": "timestamp", 
   "chartProperties": { 
     "yAxisLabel": "Duration", 
     "xAxisLabel": "Services", 
     "stacked": true, 
     "legendLocation": "right", 
     "orientation": "vertical" 
   }, 
   "duration_hours": 24, 
   "group_by": [ 
     "request_type", 
     "destination" 
   ], 
   "column": "duration", 
   "agg": "value_count", 
   "type": "int", 
   "widget_id": "172919af" 
 }

```

![Dashboard_Multi_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Multi_Bar_Chart.png)

#### ****3.5.2 Multi Bar Chart with extra filter****

Below is a sample configuration of Multi Bar Chart / Widget with `extra_filter`
```
 { 
   "title": "Multi Bar Chart Example", 
   "widget_type": "multi_bar_chart", 
   "stream": "rda_microservice_traces", 
   "extra_filter": "source in ['scheduler', 'alert-ingester']", 
   "ts_column": "timestamp", 
   "chartProperties": { 
     "yAxisLabel": "Duration", 
     "xAxisLabel": "Services", 
     "stacked": true, 
     "legendLocation": "right", 
     "orientation": "vertical" 
   }, 
   "duration_hours": 24, 
   "group_by": [ 
     "request_type", 
     "destination" 
   ], 
   "column": "duration", 
   "agg": "value_count", 
   "type": "int", 
   "widget_id": "172919af" 
 }

```

![Dashboard_Multi_Bar_Chart_scheduler_alert-ingester](https://bot-docs.cloudfabrix.io/images/dashboards/scheduler_alert-ingester.png)

#### ****3.5.3 Multi Bar Chart Without Filters****
```
 { 
   "title": "Multi Bar Chart Example", 
   "widget_type": "multi_bar_chart", 
   "stream": "rda_microservice_traces", 
   "ts_column": "timestamp", 
   "chartProperties": { 
     "yAxisLabel": "Duration", 
     "xAxisLabel": "Services", 
     "stacked": true, 
     "legendLocation": "right", 
     "orientation": "vertical" 
   }, 
   "duration_hours": 24, 
   "group_by": [ 
     "request_type", 
     "destination" 
   ], 
   "column": "duration", 
   "agg": "value_count", 
   "type": "int", 
   "widget_id": "172919af" 
 }

```

![Dashboard_Multi_Bar_Chart_Without_Filters](https://bot-docs.cloudfabrix.io/images/dashboards/Multi_Bar_Chart_Without_Filters.png)

#### ****3.5.4 Multi Bar Chart With Formatting Options****

Below is a sample configuration of Multi Bar Chart With Formatting Options.
```
 { 
   "title": "Multi Bar Chart Format", 
   "widget_type": "multi_bar_chart", 
   "stream": "main", 
   "ts_column": "timestamp", 
   "group_by": [ 
     "city", 
     "name" 
   ], 
   "formatting": { 
     "notation": "compact", 
     "style": "unit", 
     "unit": "percent", 
     "signDisplay": "always" 
   }, 
   "chartProperties": { 
     "yAxisLabel": null, 
     "xAxisLabel": "name", 
     "stacked": false, 
     "legendLocation": "right", 
     "orientation": "vertical", 
     "barThickness": 100 
   }, 
   "column": "donation", 
   "agg": "sum", 
   "type": "str" 
 }

```

![Dashboard_Multi_Bar_Formatting](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_formatting.png)

#### ****3.5.5 Multi Bar Chart Showing Top N Values****

Below is a sample configuration of Bar Chart Showing Top N Values.
```
 { 
   "title": "Multi Bar Chart", 
   "widget_type": "multi_bar_chart", 
   "stream": "donationn", 
   "ts_column": "timestamp", 
   "group_by": [ 
     "city", 
     "name" 
   ], 
   "chartProperties": { 
     "yAxisLabel": null, 
     "xAxisLabel": "name", 
     "stacked": false, 
     "legendLocation": "right", 
     "orientation": "vertical" 
   }, 
   "others_spec": { 
   "limit": 2, 
   "show_others": false 
   }, 
   "column": "donation", 
   "agg": "sum", 
   "type": "str" 
 }

```

![Dashboard_Multibar_Limit](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_limit.png)

#### ****3.5.6 Multi Bar Chart Using Others Spec****

Below is a sample configuration of Multi Bar Chart Using Others Spec
```
 { 
   "title": "Multi Bar Chart Format desc Based", 
   "widget_type": "multi_bar_chart", 
   "stream": "main", 
   "ts_column": "timestamp", 
   "group_by": [ 
     "city", 
     "name" 
   ], 
   "formatting": { 
     "notation": "compact", 
     "style": "unit", 
     "unit": "percent" 
   }, 
   "chartProperties": { 
     "yAxisLabel": null, 
     "xAxisLabel": "name", 
     "stacked": false, 
     "legendLocation": "right", 
     "orientation": "vertical" 
   }, 
   "descending_order": true, 
   "others_spec": { 
     "limit": 3, 
     "label": "Other Names", 
     "show_others": true, 
     "city": { 
       "largest": false, 
       "name_based_limit": false 
     }, 
     "name": { 
       "largest": false, 
       "name_based_limit": false 
     } 
   }, 
   "column": "donation", 
   "agg": "sum", 
   "type": "str" 
 }

```

![Dashboard_Multibar_Others_Spec](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_others_spec.png)

#### ****3.5.7 Multi Bar Chart Using Sorting Type****

Please refer the below **configuration parameter** table which are additionally used to configure a Multi Bar Chart Using Sorting Type within the dashboard.

Note

**semantic sort**: is used to sort data by month, weekday, date, severity, priority

**ordinal sort**: is used for custom ordering that is specified by an ordered set in widget definition

**lexical sort**: is used to have control over case sensitivity in standard sort

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `groups_meta` | yes | This parameter is used for sorting groups in reports. Possible values are `type`,`ignore_case`,`order`,`format` |
| `series_meta` | yes | This parameter is used for For sorting the series (segments of each bar) in Multi Bar chart, Possible values are `type`, `ignore_case`,`order`,`format` |
| `type` | yes | This parameter is used to specify the sorting type, Expected Parameters are `month`, `weekday` , `date` , `severity` , `priority`, `custom` |
| `order` | no  | is to specify a custom ordered set when the type is custom, Expected Order to Pass `<str1>, <str2>, <str3>….<strn>` |
| `format` | no  | This parameter is to specify the date format using the python date format rules, Expected format `%d %b %Y`,`%d-%b-%Y` |
| `ignore_case` | no  | This Parameter specifies if the data values must be a case sensitive match to the Ordinal values, Expected Parameters are |

Below is the sample configuration of Multi Bar Chart Using Sorting Type / Widget.
```
 { 
   "widget_type": "multi_bar_chart", 
   "title": "Week based Multibar", 
   "duration_hours": 10800, 
   "stream": "mw1", 
   "ts_column": "timestamp", 
   "extra_filter": null, 
   "column": "count_", 
   "agg": "value_count", 
   "group_by": [ 
     "Week", 
     "date" 
   ], 
   "groups_meta": { 
     "type": "date" 
   }, 
   "series_meta": { 
     "type": "weekday" 
   }, 
   "type": "int", 
   "min_width": 6, 
   "height": 5, 
   "max_width": 6 
 }

```

![Dashboard_Multibar_Sorting_Type](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_sorting_type.png)

### ****3.6 Mixed Chart Bucket****

Please refer the below **configuration parameter** table which are used to configure a Mixed Chart Bucket within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Mixed Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `mixed_chart_buckets` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `extra_filter` | no  | use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `chartProperties` | no  | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `duration hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group_by` | yes | Specify one or more columns to apply the `group_by`. This parameter supports multiple column values. Ex: `"group_by": [ "column_01", "column_02", "column_n"]` |
| `Column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `axis` | no  | To provide another y-axis support we will add the new definition here **Note**: Cannot have more than 2 axis entries in the array. |
| `graph_type` | no  | It expects two parameters `bar` & `line`, **Note:** Default is `bar` |
| `group_label` | no  | This Parameter if specified avoids multiple names, when same group\_by is passed in different axis we can assign a name for group\_label |
| `formatting` | no  | To format number with localized units, Use the `style` & `unit` option |
| `notation` | no  | We can specify as `standard`, `compact`, `scientific` and `engineering` **Standard Notation**: is the implied default, **Compact Notation**: uses locale-specific symbols to represent large numbers. It is a more human-friendly alternative to scientific notation, **Scientific Notation**: will only have one significant digit, **Engineering Notation**: will have three significant digits **Note**: By default, **Compact Notation** rounds to the nearest integer, but always keeps 2 significant digits. You can set any of `minimum, maximum`FractionDigits or `minimum, maximum` SignificantDigits to override that behavior |
| `style` | no  | The possible values for style are `currency` & `unit` |
| `unit` | no  | The unit can have following values **angle**: `degree`, **area**: `acre` , `hectare` **concentration**: `percent` **digital**: `bit`, `byte`, `kilobit`, `kilobyte`, `megabit`, `megabyte`, `gigabit`, `gigabyte`, `terabit`, `terabyte`, `petabyte` **duration**: `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `year` **length**: `millimeter`, `centimeter`, `meter`, `kilometer`, `inch`, `foot`, `yard`, `mile`, `mile-scandinavian` **mass**: `gram`, `kilogram`, `ounce`, `pound`, `stone` **temperature**: `celsius`, `fahrenheit` **volume**: `liter`, `milliliter`, `gallon`, `fluid-ounce` **speed**: `meter-per-second` |
| `currency` | no  | The Possible value for currency is `USD` |
| `SignDisplay` | no  | It helps to explicitly display the sign, even when the number is positive. The possible values are `always` To prevent showing the sign when the value is 0, use signDisplay: `exceptZero` |
| `currencySign` | no  | when the `currencySign` is set to `accounting` it enables a locale-specific format for negative currency amounts. example, wrapping the amount in parentheses |

Note

The formatting provided in one axis will be used for both.

Below is a sample configuration of Mixed Chart Bucket / Widget.
```
 { 
   "title": "Mixed Chart", 
   "widget_type": "mixed_chart_buckets", 
   "axis": [ 
     { 
       "stream": "people_custom_timestamp", 
       "ts_column": "timestamp", 
       "chartProperties": { 
         "yAxisLabel": "Same name people in City", 
         "xAxisLabel": "Name", 
         "stacked": false, 
         "legendLocation": "right", 
         "orientation": "vertical" 
       }, 
       "group_by": [ 
         "city", 
         "name" 
       ], 
       "column": "_RDA_Id", 
       "agg": "value_count", 
       "type": "int" 
     }, 
     { 
       "stream": "people_custom_timestamp", 
       "ts_column": "timestamp", 
       "chartProperties": { 
         "yAxisLabel": "Number of people in Age group", 
         "xAxisLabel": "Name" 
       }, 
       "group_by": [ 
         "count_", 
         "name" 
       ], 
       "group_label": "People in Age group", 
       "column": "_RDA_Id", 
       "agg": "value_count", 
       "type": "int", 
       "graph_type": "line" 
     } 
   ] 
 }

```

![Dashboard_Mixed_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/mixed_chart.png)

### ****3.7 Line Graph / Timeseries Chart****

Please refer the below **configuration parameter** table which are used to configure a Line Graph/Timeseries Chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Line Graph chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `timeseries` |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is 0 to 12. |
| `min_Width` | no  | Specify the timestamp column name within the selected persistent stream or dataset. |
| `height` | no  | Specify the chart / widget's height, range is `0` to `n`. |
| `chartProperties` | no  | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `interval` | yes | Displays the report according to the prescribed time frame, Supported units are auto, milliseconds (ms), seconds (s), minutes (m), hours (h), days (d). example: '5m' means 5 minutes |
| `interval_type` | no  | When the interval\_type is set to calender. **Note:** the possible values for interval are `minute`,`hour`,`day`,`week`,`month`,`quarter`,`year` |
| `gap_interval` | no  | This expects `join`, `keep`, `skip` ex. **keep** - Drops the value to 0 for missing intervals, **join** - Draws the lines for missing intervals, **skip** - Shows gaps. **Note**: Default is `keep` |
| `group_by` | yes | Splitting and defining reports which are identical and showing them categorically |
| `series_spec` | yes | Its more about how many series to show and which data points to show |
| `column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count), `cardinality` (shows unique count), min, max and avg |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `fixTimeWindow` | no  | By specifying `fixTimeWindow` as true X-axis time window will show user selected duration even if the data is only for subset of the time |
| `customIntervalMap` | no  | which can contain `from` and `to` range expressed in hours, and interval for that time range. If this map is not specified, backend defaults to a built in range. |
| `style` | no  | Using this parameter, each grouped value can be visualized using a specific color using `color-map` parameter as shown in the one of the below examples. |
| `alert_markers` | no  | This parameter helps us to add markers in Time Series Graph. |

Below is a sample configuration of Line Graph/Timeseries Chart / Widget.
```
 { 
   "title": "Time Series using Stream Example", 
   "widget_type": "timeseries", 
   "stream": "rdaf_services_logs", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 3, 
   "min_width": 12, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": null, 
     "legendLocation": "bottom" 
   }, 
   "interval": "15Min", 
   "group_by": [ 
     "log_severity" 
   ], 
   "series_spec": [ 
     { 
       "column": "log_severity", 
       "agg": "value_count", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/Line_Graphchart.png)

#### ****3.7.1 Line Graph / Timeseries Chart With Fix Time Window****

Below is a sample configuration of Line Graph/Timeseries Chart With Fix Time Window / Widget.
```
 { 
   "title": "Time Series using Stream Example", 
   "widget_type": "timeseries", 
   "stream": "rda_microservice_traces", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 3, 
   "min_width": 12, 
   "fixTimeWindow": true, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": null, 
     "legendLocation": "bottom" 
   }, 
   "interval": "auto", 
   "group_by": [ 
     "request_type" 
   ], 
   "series_spec": [ 
     { 
       "column": "request_type", 
       "agg": "value_count", 
       "type": "int" 
     } 
   ], 
   "widget_id": "121762cf" 
 }

```

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/fixtime_window.png)

**User Selected Duration**

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/fixtime_userdesired.png)

#### ****3.7.2 Line Graph / Timeseries Chart with Interval and Interval Type****

Below is a sample configuration of Line Graph/Timeseries Chart with Interval and Interval Type
```
 { 
   "title": "Time Series (Calendar Interval month)", 
   "widget_type": "timeseries", 
   "stream": "covid19", 
   "ts_column": "timestamp", 
   "width": 12, 
   "height": 6, 
   "chartProperties": { 
     "yAxisLabel": "Confirmed Count", 
     "xAxisLabel": "months", 
     "legendLocation": "bottom" 
   }, 
   "interval": "month", 
   "interval_type": "calendar", 
   "series_spec": [ 
     { 
       "column": "Confirmed", 
       "agg": "value_count", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Interval_Type](https://bot-docs.cloudfabrix.io/images/dashboards/interval_type.png)

#### ****3.7.3 Line Graph / Timeseries Chart with Gap Interval****

[Gap Interval - Keep](#__tabbed_9_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Keep / Widget configuration
```
 { 
   "title": "Time Series (Gap Interval Keep)", 
   "widget_type": "timeseries", 
   "gap_interval": "keep", 
   "stream": "covi19", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 3, 
   "min_width": 12, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": "Timestamp", 
     "legendLocation": "bottom" 
   }, 
   "interval": "5m", 
   "series_spec": [ 
     { 
       "column": "Confirmed", 
       "agg": "sum", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Keep_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/keep_chart.png)

[Gap Interval - Join](#__tabbed_10_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Join / Widget configuration
```
 { 
   "title": "Time Series (Gap Interval Join)", 
   "widget_type": "timeseries", 
   "gap_interval": "join", 
   "stream": "covi19", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 3, 
   "min_width": 12, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": "Timestamp", 
     "legendLocation": "bottom" 
   }, 
   "interval": "5m", 
   "series_spec": [ 
     { 
       "column": "Confirmed", 
       "agg": "sum", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Join_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/join_chart.png)

[Gap Interval - Skip](#__tabbed_11_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Skip / Widget configuration
```
 { 
   "title": "Time Series (Gap Interval Skip)", 
   "widget_type": "timeseries", 
   "gap_interval": "skip", 
   "stream": "covi19", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 3, 
   "min_width": 12, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": "Timestamp", 
     "legendLocation": "bottom" 
   }, 
   "interval": "5m", 
   "series_spec": [ 
     { 
       "column": "Confirmed", 
       "agg": "sum", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Skip_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/skip_chart.png)

#### ****3.7.4 Line Graph / Timeseries Chart with Color Map****

Below is a sample configuration of Line Graph/Timeseries Chart with Color Map / Widget configuration

[Example One](#__tabbed_12_1)
```
 { 
   "title": "Time Series", 
   "widget_type": "timeseries", 
   "gap_interval": "keep", 
   "stream": "people_custom_timestamp", 
   "ts_column": "timestamp", 
   "width": 4, 
   "height": 4, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": null, 
     "legendLocation": "bottom" 
   }, 
   "interval": "24h", 
   "series_spec": [ 
     { 
       "column": "name", 
       "agg": "value_count", 
       "type": "int" 
     } 
   ], 
   "group_by": "city", 
   "style": { 
     "color-map": { 
       "Austin": [ 
         "#E91E63", 
         "#ffffff" 
       ], 
       "Portland": [ 
         "#FF5722", 
         "#ffffff" 
       ], 
       "San Francisco": [ 
         "#FFC107", 
         "#ffffff" 
       ], 
       "Hyderabad": [ 
         "#3F51B5", 
         "#ffffff" 
       ] 
     } 
   } 
 }

```

![Dashboard_Color_Map](https://bot-docs.cloudfabrix.io/images/dashboards/color_map.png)

[Example Two](#__tabbed_13_1)

**Color Map with Label**

Below is a sample configuration of Line Graph Chart with Color Map with Label / Widget configuration
```
 { 
   "title": "Time Series (Color-map with label)", 
   "widget_type": "timeseries", 
   "gap_interval": "keep", 
   "stream": "people_custom_timestamp", 
   "ts_column": "timestamp", 
   "width": 4, 
   "height": 4, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": null, 
     "legendLocation": "bottom" 
   }, 
   "interval": "24h", 
   "series_spec": [ 
     { 
       "column": "name", 
       "agg": "value_count", 
       "type": "int", 
       "label": "City" 
     } 
   ], 
   "group_by": "city", 
   "style": { 
     "color-map": { 
       "City (Portland)": [ 
         "#E91E63", 
         "#ffffff" 
       ], 
       "City (San Francisco)": [ 
         "#FF5722", 
         "#ffffff" 
       ], 
       "City (Hyderabad)": [ 
         "#FFC107", 
         "#ffffff" 
       ], 
       "City (Austin)": [ 
         "#3F51B5", 
         "#ffffff" 
       ] 
     } 
   } 
 }

```

![Dashboard_Color_Label](https://bot-docs.cloudfabrix.io/images/dashboards/color_label.png)

#### ****3.7.5 Line Graph / Timeseries Chart with Alert Markers****

Please refer the below **configuration parameter** table which are additionally used to configure a Line Graph/Timeseries Chart with Alert Markers within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `alert_markers` | yes | This parameter helps us to add markers in Time Series Graph |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `stream` | yes | Specify the persistent stream |
| `message_column` | yes | This parameter will display a message when hovered on the graph, This parameter expects the `message column` to be displayed |
| `extra_filter` | no  | This parameter is used to filter the data from from one or more selected field(s). It supports CFXQL query format |
| `severity_column` | yes | This parameter is used to specify the severity column for alert marker |

Below is a sample configuration of Line Graph / Timeseries Chart with Alert Markers / Widget configuration
```
 { 
   "widget_type": "timeseries", 
   "title": "Alert Trend", 
   "stream": "oia-alerts-stream", 
   "min_width": 9, 
   "height": 3, 
   "max_width": 9, 
   "interval": "auto", 
   "ts_column": "a_created_ts", 
   "fixTimeWindow": true, 
   "group_by": [ 
     "a_severity" 
   ], 
   "alert_markers": [{ 
     "stream": "oia-alerts-stream", 
     "ts_column": "a_created_ts", 
     "message_column": "a_message", 
     "extra_filter": "a_severity is 'CRITICAL'", 
     "severity_column": "a_severity" 
   }], 
   "series_spec": [ 
     { 
       "agg": "sum", 
       "column": "count_", 
       "type": "int", 
       "label": "Alert Count" 
     } 
   ], 
   "chartProperties": { 
     "yAxisLabel": "Alert Count", 
     "xAxisLabel": null, 
     "legendLocation": "right" 
   } 
 }

```

![Dashboard_Alert_Markers](https://bot-docs.cloudfabrix.io/images/dashboards/alert_markers.png)

#### ****3.7.6 Line Graph / Timeseries Chart with Auto Intervals****

Note

This widget computes aggregation based on Time Range selected (Not based on Data Availability)

Below is a sample configuration of Line Graph / Timeseries Chart with Auto Intervals / Widget configuration
```
 { 
   "title": "Time Series using Stream Example", 
   "widget_type": "timeseries", 
   "stream": "company_alerts", 
   "ts_column": "timestamp", 
   "max_width": 12, 
   "height": 7, 
   "min_width": 12, 
   "chartProperties": { 
     "yAxisLabel": "Count", 
     "xAxisLabel": null, 
     "legendLocation": "bottom" 
   }, 
   "fixTimeWindow": true, 
   "interval": "auto", 
   "series_spec": [ 
     { 
       "column": "count_", 
       "agg": "sum", 
       "type": "int" 
     } 
   ] 
 }

```

![Dashboard_Auto_Interval](https://bot-docs.cloudfabrix.io/images/dashboards/auto_interval.png)

### ****3.8 Data Flow Chart****

Please refer the below **configuration parameter** table which are used to configure a Data flow chart within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Data Flow chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `dataflow`,`eventflow` |
| `chart properties` | yes | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `dataset` | no  | Specify the dataset name. **Note:** Either of persistent stream or dataset parameter is needed |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is 0 to 12. |
| `min_Width` | no  | Specify the timestamp column name within the selected persistent stream or dataset. |
| `height` | no  | Specify the chart / widget's height, range is `0` to `n`. |
| `formatter` | no  | Formats integer values as K for thousands, M for Millions. If the input value is already a counted as thousands, optional value multiplier can be specified. |
| `extra_filter` | no  | se this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |
| `duration_hours` | no  | This parameter specifies how many hours in the past should the data be fetched. If time\_filter is set to true, time filter will override this value. |
| `group_by` | yes | Splitting and defining reports which are identical and showing them categorically |
| `column` | yes | Name of the column in the data that contains numerical data to perform aggregations |
| `agg` | yes | Specify the aggregation function. Supported values are `value_count` (shows total count) and `cardinality` (shows unique count) |
| `type` | yes | Specify the data type while performing aggregation function. Supported values are `int` and `str`. `int` option is valid only for `min`, `max`, `sum`, `mean` aggregation functions. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |

Below is the sample of Data Flow Chart / Widget configuration.
```
 { 
   "title": "Event Flow Graph", 
   "widget_type": "dataflow", 
   "chartProperties": { 
     "layoutDirection": "tb", 
     "userZoomingEnabled": false, 
     "hasToolbar": false 
   }, 
   "output": { 
     "formatter": "DescriptiveCountFormatter", 
     "stream": "dli-log-stats", 
     "extra_filter": "mode is 'processed' and device not in ['ERROR','INFO','WARNING']", 
     "ts_column": "timestamp", 
     "duration_hours": 720, 
     "group_by": [ 
       "device" 
     ], 
     "column": "count", 
     "agg": "sum", 
     "type": "int" 
   }, 
   "input": { 
     "formatter": "DescriptiveCountFormatter", 
     "stream": "dli-log-stats", 
     "extra_filter": "mode is 'ingested' and device not in ['ERROR','INFO','WARNING']", 
     "ts_column": "timestamp", 
     "duration_hours": 720, 
     "group_by": [ 
       "device" 
     ], 
     "column": "count", 
     "agg": "sum", 
     "type": "int", 
     "widget_id": "da16c98b" 
   }, 
   "widget_id": "66b927bc" 
 }

```

![Dashboard_Event_Flow_chart](https://bot-docs.cloudfabrix.io/images/dashboards/Event_Flow_Graph.png)

### ****3.9 Image Chart****

Image widget can show any image that is accessible through a URL.

Please refer the below **configuration parameter** table which are used to configure an Image chart / widget within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Image chart |
| `widget_type` | yes | Specify the chart / widget type. i.e. `image` |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is 0 to 12. |
| `min_width` | no  | Specify the timestamp column name within the selected persistent stream or dataset. |
| `imageUrl` | yes | Specify the url of the image thats needs to be represented in the chart |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |

Below is a sample configuration of Image Chart / Widget.
```
 { 
   "title": "Ocean", 
   "widget_type": "image", 
   "max_width": 6, 
   "min_width": 4, 
   "height": 6, 
   "imageUrl": "https://images.unsplash.com/photo-1657883509333-0b1d2ee75853?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=704&q=80", 
   "widget_id": "6e8df419" 
 }

```

![Dashboard_Image_chart](https://bot-docs.cloudfabrix.io/images/dashboards/image_chart.png)

### ****3.10 3-Column Navigator****

A 3 column navigator is a type of website or application layout where the screen is divided into three vertical sections or columns.

Please refer the below **configuration parameter** table which are used to configure **3-Column Navigator** within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `tree_data` | yes | It is the first visible column among 3-column navigator. Mandatory parameters are `column_name` & `pstream_name` |
| `tree_details` | yes | It is the second visible column among the 3-column navigator. Mandatory parameters are `display_column`& `pstream_name` |
| `showNodeIcon` | no  | It is used to pass the icons beside tree data |
| `showSearchBox` | no  | It is used to pass the search within tree details |

Note

Any widget part of dashboard section will be visible as third column in the 3-column navigator.

Below is the sample configuration of **3-Column Navigator**.
```
 { 
   "name": "navigator", 
   "label": "Navigator", 
   "description": "Navigator", 
   "enabled": true, 
   "dashboard_style": "auto", 
   "dashboard_type": "template", 
   "short_label": "Stack", 
   "context_label_id": "stack_name", 
   "dashboard_folder": "Default", 
   "version": "23.10.02.1", 
   "dashboard_filters": { 
     "time_filter": true, 
     "default_time_filter_labels": [ 
       "Last 1 month" 
     ] 
   }, 
   "template_variables": { 
     "CITY": { 
       "contextId": [ 
         "navigatorSelectionContexts", 
         "secondaryListSelection", 
         "city" 
       ] 
     }, 
     "NAME": { 
       "contextId": [ 
         "navigatorSelectionContexts", 
         "secondaryListSelection", 
         "name" 
       ] 
     } 
   }, 
   "navigation_dashboards": { 
     "tree_data": { 
       "column_name": "city", 
       "pstream_name": "main", 
       "cfxql_query": "timestamp is after -720d " 
     }, 
     "tree_detail": { 
       "display_column": "name", 
       "pstream_name": "main", 
       "cfxql_query": "timestamp is after -720d " 
     }, 
     "showNodeIcon": false, 
     "showSearchBox": true 
   }, 
   "dashboard_sections": [ 
     { 
       "title": "Node Details", 
       "widgets": [ 
         { 
           "title": "Details", 
           "widget_type": "tabular", 
           "extra_filter": "(name is '{{NAME}}') and (city is '{{CITY}}')", 
           "stream": "main", 
           "max_width": 12, 
           "height": 8, 
           "min_width": 12, 
           "widget_id": "cc9a9626" 
         } 
       ] 
     } 
   ], 
   "saved_time": "2023-11-02T08:25:25.205071" 
 }

```

![Dashboard_3column_navigator](https://bot-docs.cloudfabrix.io/images/dashboards/3column_navigator.png)

### ****3.11 Shaded Chart****

Please refer the below **configuration parameter** table which are used to configure Shaded Chart / widget within the dashboard.

Note

**This chart/widget is only specific to Machine Learning Data & not for Generic Use**

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Shaded Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `shaded_chart_multisource` |
| `stream` | yes | Specify the persistent stream |
| `chart properties` | yes | chartProperties defines the representation of data using Yaxis, Xaxis & Various other Combinations like zooming,color etc... |
| `downsample` | no  | if set to true chart will `downsample` the number of datapoints maintaining overall pattern of data else plot entire data |
| `baseline_column` | yes | column name representing actual data |
| `anomalies_column` | yes | column name representing anomaly values |
| `predicted_column` | yes | column name representing predicted values by the model |
| `predicted_anomalies` | yes | column name representing predicted anomaly values by the model |
| `upperBound_column` | yes | column name representing upper bound values |
| `lowerBound_column` | yes | column name representing lower bound values |
| `show-markers` | no  | if set to true charts will show an yellow vertical line which denotes Prediction start time |
| `type` | yes | This attribute accepts two types of data `train`&`predict` **train:** refers to historical trained data source & **predict:** refers to live data source that contains live data and live anomalies |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. It is optional when dataset is used. |

Below is a sample configuration of Shaded Chart / Widget.
```
 { 
   "widget_type": "shaded_chart_multisource", 
   "title": "Forecasting and Anomaly Detection", 
   "show-markers": true, 
   "max_width": 12, 
   "min_width": 12, 
   "height": 8, 
   "chartProperties": { 
     "yAxisLabel": "Value", 
     "xAxisLabel": "Time" 
   }, 
   "sources": [ 
     { 
       "type": "train", 
       "downsample": false, 
       "stream": "regression-train-output", 
       "ts_column": "timestamp", 
       "baseline_column": "baseline", 
       "anomalies_column": "anomalies", 
       "predicted_column": "predicted", 
       "predicted_anomalies": "predicted_anomalies", 
       "upperBound_column": "upperBound", 
       "lowerBound_column": "lowerBound", 
       "duration_hours": 1000000, 
       "synchronized-group": 0 
     }, 
     { 
       "type": "predict", 
       "downsample": false, 
       "stream": "regression-live-output", 
       "ts_column": "live_timestamp", 
       "baseline_column": "baseline", 
       "anomalies_column": "anomaly", 
       "predicted_column": "predicted", 
       "predicted_anomalies": "predicted_anomalies", 
       "upperBound_column": "upperBound", 
       "lowerBound_column": "lowerBound", 
       "duration_hours": 1000000, 
       "synchronized-group": 0 
     } 
   ], 
   "widget_id": "7a134625" 
 }

```

![Dashboard_Shaded_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/shaded_chart.png)

[Example Two](#__tabbed_14_1)
```
 { 
   "widget_type": "shaded_chart_multisource", 
   "title": "Forecasting and Anomaly Detection (Memory Usage - 10.95.125.90)", 
   "show-markers": true, 
   "max_width": 12, 
   "min_width": 12, 
   "height": 8, 
   "chartProperties": { 
     "yAxisLabel": "Memory Usage (bytes)", 
     "xAxisLabel": "Time" 
   }, 
   "sources": [ 
     { 
       "type": "train", 
       "downsample": false, 
       "stream": "regression-train-output", 
       "extra_filter": "status is 'Success'", 
       "ts_column": "timestamp", 
       "baseline_column": "baseline", 
       "anomalies_column": "anomalies", 
       "predicted_column": "predicted", 
       "predicted_anomalies": "predicted_anomalies", 
       "upperBound_column": "upperBound", 
       "lowerBound_column": "lowerBound", 
       "duration_hours": 1000000, 
       "synchronized-group": 0 
     }, 
     { 
       "type": "predict", 
       "downsample": false, 
       "stream": "regression-live-output", 
       "extra_filter": "status is 'Success'", 
       "ts_column": "live_timestamp", 
       "baseline_column": "baseline", 
       "anomalies_column": "anomaly", 
       "predicted_column": "predicted", 
       "predicted_anomalies": "predicted_anomalies", 
       "upperBound_column": "upperBound", 
       "lowerBound_column": "lowerBound", 
       "duration_hours": 1000000, 
       "synchronized-group": 0 
     } 
   ], 
   "widget_id": "7a134625" 
 }

```

![Dashboard_Shaded_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/shaded_chart1.png)

### ****3.12 Label Chart****

This widget can be used as a label Chart inside the dashboard section.

Please refer the below **configuration parameter** table which are used to configure Label Chart widget within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `label` | yes | Specify the content in the html format ex.heading in `<h1> to <h6>` |
| `widget_type` | yes | Specify the widget\_type as label |

[Example One](#__tabbed_15_1)
```
 { 
   "widget_type": "label", 
   "label": "<div style='text-align:center;width:100%;'><h1><a style='text-decoration:none;color:#0066ff;' target='_blank'> Welcome to RDAF Community </a></h1></div>" 
 }

```

![Label_Widget](https://bot-docs.cloudfabrix.io/images/dashboards/label_widget.png)

[Example Two](#__tabbed_16_1)
```
 { 
   "widget_type": "label", 
   "min_width": 4, 
   "height": 3, 
   "max_width": 4, 
   "sorting": [ 
     { 
       "endTime": "desc" 
     } 
   ], 
   "label": "{% set all_latest_data = {} %}\r\n{% for latest in latest_end_time %}\r\n    {% set last_updated_time = latest.get(\"label\") %}\r\n    {% set _ = all_latest_data.update({ \"latest\": last_updated_time }) or \"\" %}\r\n{% endfor %}\r\n\r\n<br><br> <center><h4> Last Collected at </h4></center><br><center><h3>{{all_latest_data.get(\"latest\")}}</h3></center>", 
   "segments": [ 
     { 
       "stream": "main", 
       "variable": "latest_end_time", 
       "ts_column": "timestamp", 
       "agg": "value_count", 
       "group_by": "endTime", 
       "column": "city" 
     } 
   ] 
 }

```

![Dashboard_Labels2](https://bot-docs.cloudfabrix.io/images/dashboards/labels2.png)

### ****3.13 Connectivity Chart****

The objective is to create a connected graph illustrating the interrelationships among various columns. Upon mouseover, additional details should be displayed. Clicking or hovering should highlight both incoming and outgoing links. In the case of numerous columns, a horizontal scroll bar should be available for navigation.

Note

This is not network connectivity or topology.

Please refer the below **configuration parameter** table which are used to configure Connectivity Chart

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `title` | yes | Specify the label for the Connectivity Chart. |
| `widget_type` | yes | Specify the chart / widget type. i.e. `connectivity_chart` |
| `stream` | no  | Specify the persistent stream. |
| `columns` | yes | Specify one or more columns / fields to be shown in the Connectivity Chart. This parameter expects `group_by`,`limit`(default is 10),`label`& `color-map`. Here `limit`,`color-map` is optional |
| `agg` | yes | Specify the aggregation function. Supported values are `sum`, `min` and `max` |
| `agg_column` | yes | Specify the column name that has the values to apply aggregate function on. |
| `min_width` | no  | Specify the chart / widget's minimum width size, range is `0` to `12`. |
| `height` | no  | Specify the chart / widget's height, range is `0` to `n`. |
| `max_width` | no  | Specify the chart / widget's maximum width size, range is `0` to `12`. |
| `ts_column` | yes | Specify the timestamp column name within the selected persistent stream. |
| `widget_id` | no  | Every widget will be represented with Unique id at the end, Its Autogenerated if not provided |
| `extra_filter` | no  | Use this parameter to filter the data from from one or more selected field(s). It supports CFXQL query format. |
```
 { 
   "widget_type": "connectivity_chart", 
   "title": "People", 
   "stream": "main", 
   "ts_column": "timestamp", 
   "min_width": 12, 
   "max_width": 12, 
   "height": 8, 
   "agg": "sum", 
   "agg_column": "count_", 
   "columns": [ 
     { 
       "group_by": "city", 
       "label": "For City", 
       "color-map": { 
         "Portland": [ 
           "#ef5350", 
           "#ffffff" 
         ], 
         "San Francisco": [ 
           "#FF9800", 
           "#ffffff" 
         ], 
         "Austin": [ 
           "#8BC34A", 
           "#ffffff" 
         ], 
         "Hyderabad": [ 
           "#1E88E5", 
           "#ffffff" 
         ] 
       } 
     }, 
     { 
       "group_by": "name", 
       "label": "For Name", 
       "color-map": { 
         "James": [ 
           "#ef5350", 
           "#ffffff" 
         ] 
       } 
     }, 
     { 
       "group_by": "age", 
       "label": "For Age" 
     }, 
     { 
       "group_by": "donation", 
       "label": "For Donation" 
     } 
   ] 
 }

```

[![](https://bot-docs.cloudfabrix.io/images/dashboards/connectivity_chart.png)](/images/dashboards/connectivity_chart.png)

### ****3.14 Markdown****

This Widget will parse Markdown text and display it as an HTML-like view. This functionality is intended to facilitate the presentation of documentation . The widget should specifically support Markdown content sourced from rda\_object(Object Store from artifacts) for integration within the dashboard. This feature will enhance the user experience by providing neatly formatted documentation within the Dashboard interface.

**Prerequisites**

**Step-1:** Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Object Store**

[![](https://bot-docs.cloudfabrix.io/images/dashboards/object_store.png)](/images/dashboards/object_store.png)

**Step-2:** Click on **Upload** to update rda object.

[![](https://bot-docs.cloudfabrix.io/images/dashboards/upload.png)](/images/dashboards/upload.png)

Please refer the below configuration parameter table which are used to configure Markdown Widget

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| widget\_type | yes | `markdown` |
| folder | yes | Folder name defined in `rda_object`(Object Store from artifacts) |
| objectName | yes | Object name defined in `rda_object`(Object Store from artifacts) |

Below is a sample configuration of Markdown / Widget.
```
 { 
 "widget_type": "markdown", 
 "folder": "markdown_syntax", 
 "objectName": "markdown" 
 }

```

[![](https://bot-docs.cloudfabrix.io/images/dashboards/markdown.png)](/images/dashboards/markdown.png)

### ****3.15 Features****

#### ****3.15.1 Library****

By using a library, Once a widget is specified it can be called any number of times. Any dashboard can be a widget library and can import widgets from any library. This approach helps users to reduce the time spent creating the same widget multiple times in various dashboards.

Please refer the below **configuration parameter** table which are used to configure Library within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `name` | yes | Specify name of the Dashboard which need to be added as a page. |
| `label` | yes | Specify the label for Dashboard page. |
| `title` | yes | Specify the title |
| `stream` | no  | Specify the persistent stream. **Note:** Either of persistent stream or dataset parameter is needed. |
| `library` | yes | Any Dashboard can be a widget library. **Note:** Any other dashboard can import any widget from any library |
| `import` | no  | `from` (the library dashboard name) and `as` (rename that dashboard temporary as) ex.`from`: "covi-library-1", `as`: "lib1" |
| `extends` | yes | will get the name of library within the definition or from other dashboard ex. "extends": "self:covi\_count" / "extends": "lib1:covi\_counter" **Note:** self is used when we call the library within the definition & name of the library if its imported |

**Library Defined**

Below is a sample configuration of Library / Widget.
```
 { 
   "name": "covi-library-1", 
   "label": "Test Library for Sample Widgets", 
   "enabled": "false", 
   "description": "Sample library", 
   "library": { 
     "widgets": { 
       "covi_counter": { 
         "title": "Deaths", 
         "min_width": 6, 
         "height": 4, 
         "max_width": 6, 
         "widget_type": "custom_counter", 
         "formatter": "DescriptiveCountFormatter", 
         "stream": "covid19", 
         "ts_column": "timestamp", 
         "duration_hours": 9600, 
         "sparkline": { 
           "interval": "360h" 
         }, 
         "style": { 
           "color-list": [ 
             "#8e24aa" 
           ] 
         }, 
         "column": "Deaths", 
         "agg": "sum" 
       } 
     } 
   } 
 
 }

```

**Library Being Called from the above Definition**

Below is a sample configuration of Library Being Called from the above Definition / Widget.
```
 { 
   "name": "covi-library-2", 
   "label": "Library Widget Covid", 
   "description": "Covid data", 
   "enabled": "false", 
   "dashboard_type": "dashboard", 
   "dashboard_folder": "Default", 
   "import": [ 
     { 
       "from": "covi-library-1", 
       "as": "lib1" 
     } 
   ], 
   "dashboard_sections": [ 
     { 
       "title": "SECTION 1", 
       "show_filter": true, 
       "widgets": [ 
         { 
           "extends": "self:covi_count", 
           "widget_id": "e1201b84" 
         }, 
         { 
           "extends": "lib1:covi_counter", 
           "widget_id": "c3ac1d59" 
         } 
       ] 
     } 
   ], 
   "library": { 
     "widgets": { 
       "covi_count": { 
         "title": "Confirmed", 
         "min_width": 6, 
         "height": 4, 
         "max_width": 6, 
         "widget_type": "custom_counter", 
         "formatter": "DescriptiveCountFormatter", 
         "stream": "covid19", 
         "ts_column": "timestamp", 
         "duration_hours": 8990, 
         "sparkline": { 
           "interval": "360h" 
         }, 
         "style": { 
           "color-list": [ 
             "#008000" 
           ] 
         }, 
         "column": "Confirmed", 
         "agg": "sum" 
       } 
     } 
   }  
 }

```

![Dashboard_Library_Report](https://bot-docs.cloudfabrix.io/images/dashboards/library_report.png)

#### ****3.15.2 Stream Query Mapping****

This feature enables to mix and match data from different PStreams into a single Dashboard.

Even though you can already do that today, when filters are applied, usually it breaks several widgets to avoid it we have introduced the new feature which helps break free connectivity within the dashboard

Please refer the below **configuration parameter** table which are used to configure Stream Query Mapping

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `stream` | yes | Name of the stream which needs to be passed |

Note

When specifying a replacement column, both columns must be of same type

Below is a sample configuration of Stream Query Mapping / Widget
```
 "stream_query_mapping": { 
         "oia-incidents-stream": { 
             "timestamp": "i_created_ts", 
             "a_severity": null 
         }, 
         "oia-alerts-stream": { 
             "timestamp": "a_created_ts", 
             "i_priority_label": null 
         } 
     }

```

Info

By adding above section to any dashboard, it will alter queries sent to OpenSearch based which stream it is querying. If filter contains column "timestamp", replace it with i\_created\_ts If the filter contains a\_severity column skip that specific filter in the query (rest of the conditions will still apply)

[Example Definition](#__tabbed_17_1)
```
 { 
   "name": "oia-trends----rv", 
   "label": "Trends", 
   "description": "Trends", 
   "version": "23.8.9", 
   "enabled": true, 
   "debug": true, 
   "dashboard_style": "auto", 
   "dashboard_type": "template", 
   "stream_query_mapping": { 
     "oia-incidents-stream": { 
       "timestamp": "i_created_ts", 
       "a_severity": null 
     }, 
     "oia-alerts-stream": { 
       "timestamp": "a_created_ts", 
       "i_priority_label": null 
     } 
   }, 
   "dashboard_filters": { 
     "time_filter": true, 
     "default_time_filter_non_removable": true, 
     "show_default_time_filter": true, 
     "additional_datetime_column_filters": [ 
       { 
         "id": "timestamp", 
         "label": "Timestamp" 
       } 
     ], 
     "default_time_filter_labels": [ 
       "Last 24 hours" 
     ], 
     "group_filters": [ 
       { 
         "stream": "oia-alerts-stream", 
         "title": "Source", 
         "group_by": [ 
           "a_source_systemname" 
         ], 
         "ts_column": "a_updated_ts", 
         "agg": "value_count", 
         "column": "a_id", 
         "type": "str" 
       } 
     ] 
   }, 
   "dashboard_sections": [ 
     { 
       "title": "Trends", 
       "show_filter": true, 
       "widgets": [ 
         { 
           "widget_type": "timeseries", 
           "title": "Alert Trend", 
           "stream": "oia-alerts-stream", 
           "min_width": 9, 
           "height": 3, 
           "max_width": 9, 
           "interval": "auto", 
           "ts_column": "a_created_ts", 
           "fixTimeWindow": true, 
           "group_by": [ 
             "a_severity" 
           ], 
           "alert_markers": [{ 
             "stream": "oia-incidents-stream", 
             "ts_column": "i_created_ts", 
             "message_column": "i_summary", 
             "extra_filter": "i_priority_label is 'Critical'", 
             "severity_column": "i_priority_label" 
           } 
           ], 
           "series_spec": [ 
             { 
               "agg": "sum", 
               "column": "count_", 
               "type": "int", 
               "label": "Alert Count" 
             } 
           ], 
           "chartProperties": { 
             "yAxisLabel": "Alert Count", 
             "xAxisLabel": null, 
             "legendLocation": "right", 
             "options": { 
               "elements": { 
                 "line": { 
                   "borderWidth": 1 
                 }, 
                 "point": { 
                   "radius": 0, 
                   "hitRadius": 3, 
                   "hoverRadius": 2 
                 } 
               } 
             } 
           }, 
           "widget_id": "e146eb95" 
         }, 
         { 
           "widget_type": "timeseries multi markers", 
           "title": "Incident Trend", 
           "stream": "oia-incidents-stream", 
           "min_width": 9, 
           "height": 3, 
           "max_width": 9, 
           "interval": "auto", 
           "ts_column": "timestamp", 
           "fixTimeWindow": true, 
           "group_by": [ 
             "i_priority_label" 
           ], 
           "alert_markers": [ 
             { 
               "stream": "oia-alerts-stream", 
               "ts_column": "timestamp", 
               "message_column": "a_message", 
               "extra_filter": "a_severity is 'CRITICAL'", 
               "severity_column": "a_severity" 
             } 
           ], 
           "series_spec": [ 
             { 
               "agg": "sum", 
               "column": "count_", 
               "type": "int", 
               "label": "Incident Count" 
             } 
           ], 
           "chartProperties": { 
             "yAxisLabel": "Incident Count", 
             "xAxisLabel": null, 
             "legendLocation": "right", 
             "options": { 
               "elements": { 
                 "line": { 
                   "borderWidth": 1 
                 }, 
                 "point": { 
                   "radius": 0, 
                   "hitRadius": 3, 
                   "hoverRadius": 2 
                 } 
               } 
             } 
           }, 
           "widget_id": "17004a8e" 
         } 
       ] 
     } 
   ], 
   "saved_time": "2023-12-13T04:47:16.762883" 
 }

```

#### ****3.15.3 Generating Dashboard using Pstream****

This feature enables the user to take data and load a dashboard from the stream specified in less time.

**Using RDA Portal**

**Step-1**: Login into **RDA Fabric platform** as a MSP Admin user.

**Step-2**: Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Stream**

**Step-3**: Click on Menu button from the stream name and click Generate Dashboard.

![Dashboard_Pstream_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/pstream_chart.png)

**Step-4**: Fill the Dashboard label and Dashboard folder, change the dashboard name if required.

**Step-5**: Need to select **Publish Dashboard** option to publish the generated dashboard. If the dashboard with name already exists you can select **Overwrite Existing Dashboard** option to overwrite existing dashboard

![Dashboard_Covi19_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/covi19_chart.png)

**Using Command**

Login to ssh session, run the below command
```
 rdac dashboard generate --stream STREAM –name NAME –publish

```

[Example Output](#__tabbed_18_1)
```
 rdac dashboard generate --stream covi19 --name dya_covi --publish

```

The above mentioned command gives the following output

![Dashboard_Dya_Covi](https://bot-docs.cloudfabrix.io/images/dashboards/dya_covi.png)

#### ****3.15.4 UI Menus****

**UI Menus**

UI Menu -> Add Menu Folder

After Clicking on Add **Folder** option from “Top Level” we will get a floating tab to add the label of parent folder, Add the name of the folder and icon name as desired and click on **Add**

[![](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu1.png)](/images/dashboards/ui_menu1.png)

Once we add them click on **save**

![Dashboard_ui_menu2](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu2.png)

****Create a child folder****

Click on the **Menu Folder** -> add **Child Folder** -> click on **Add**

[![](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu3.png)](/images/dashboards/ui_menu3.png)

![Dashboard_ui_menu4](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu4.png)

Note

Once Menu is saved successfully. **Refresh** browser to reflect changes.

Now Assign a dashboard to the saved UI menus

****Assigning a dashboard****

![Dashboard_ui_menu5](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu5.png)

Select Menu Where Dashboard will show up

[![](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu6.png)](/images/dashboards/ui_menu6.png)

Note

Once we Click on **Save**, Dashboard association to menu will be saved successfully. Now **refresh** browser to reflect changes.

![Dashboard_ui_menu7](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu7.png)

****Re-ordering by Weight****

To re-arrange the folder level by ordering the menu order (Set bigger number to position lower)

![Dashboard_ui_menu8](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu8.png)

Menu order is set to `1` for **Open Search Based OIA Alerts**

![Dashboard_ui_menu9](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu9.png)

Menu order is set to `5` for **OIA Alert Group View details**

![Dashboard_ui_menu10](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu10.png)

****Unassign Dashboard from Menu****

To Remove the UI menu associated with a particular dashboard, we can unassign them by following the below methods

[![](https://bot-docs.cloudfabrix.io/images/dashboards/ui_menu11.png)](/images/dashboards/ui_menu11.png)

#### ****3.15.5 Template Variable****

A template variable is a placeholder for a value that will be filled in at runtime. It is often used in report definition, where it allows functions and classes to operate with generic types. This allows a function or class to be written once and then be used with various data types without being rewritten for each one. The template variable is specified in the function or class definition and then the actual data type is provided when the function or class is used.

Below is the sample configuration of Template Variable.
```
 "template_variables": { 
   "CITY": { 
     "contextId": [ 
       "navigatorSelectionContexts", 
       "secondaryListSelection", 
       "city" 
     ] 
   }, 
   "NAME": { 
     "contextId": [ 
       "navigatorSelectionContexts", 
       "secondaryListSelection", 
       "name" 
     ] 
   } 
 }

```

Important

Template Variable should be passed only when dashboard type is set to Template

[Calling Template Variable](#__tabbed_19_1)
```
 { 
   "title": "Details", 
   "widget_type": "tabular", 
   "extra_filter": "(name is '{{NAME}}') and (city is '{{CITY}}')", 
   "stream": "main", 
   "max_width": 12, 
   "height": 8, 
   "min_width": 12, 
   "widget_id": "cc9a9626" 
 }

```

#### ****3.15.6 Dynamic Forms****

With this feature, we can make forms and actions right within the dashboard. An example usage of this is to provide **Add**, **Edit**, **Delete** operations on a tabular view. When user uses the form, it updates the stream or runs a pipeline, or both. We can line up actions when the form is submitted, and they happen one after the other.

Please refer the below **configuration parameter** table which are used to configure Dynamic Forms within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `type` | yes | Supported values are **UPDATE\_PSTREAM** & **RUN\_PIPELINE** |
| `pstreamName` | yes | This will update the Pstream directly |
| `operation` | yes | By default Value is **ADD** Other supported values are **UPDATE** & **DELETE** |
| `cfxql_query` | no  | Need to specify when operation is **UPDATE** & **DELETE** |
| `pipelineName` | yes | This will trigger the specified pipeline |
| `isSync` | no  | Runs pipeline in the background if `isSync` is **False**. Otherwise, it waits for the pipeline to be completed before going to the next action |

Note

cfxql\_query, operation and pstreamName are applicable only if type is **UPDATE\_PSTREAM** and isSync and pipelineName are applicable only if type is **RUN\_PIPELINE**

[Example for Pstream Update](#__tabbed_20_1)
```
 { 
 "type": "UPDATE_PSTREAM", 
 "pstreamName": "main", 
 "operation": "UPDATE", 
 "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" 
 }

```

[Example for Pipeline Run](#__tabbed_21_1)
```
 { 
 "type": "RUN_PIPELINE", 
 "pipelineName": "simple_pipeline", 
 "isSync": true 
 }

```

The pipeline used in the below example is simple\_pipeline, It will get the input from the dashboard to the temp-dataset

The content of the pipeline is as below.
```
 @dm:empty      
 → @exec:get-input 
 → @dm:save name=”temp-dataset”

```

Below is a sample configuration which performs actions using Dynamic Forms.
```
 { 
   "name": "Dynamic forms", 
   "label": "Dynamic forms", 
   "is_template": false, 
   "description": "Dynamic forms", 
   "version": "24.01.03.1", 
   "enabled": true, 
   "dashboard_type": "dashboard", 
   "dashboard_folder": "Default", 
   "dashboard_style": "auto", 
   "stream": "main", 
   "dashboard_sections": [ 
     { 
       "title": "Student App", 
       "widgets": [ 
         { 
           "title": "Registration Details", 
           "widget_type": "tabular", 
           "stream": "main", 
           "timebased": false, 
           "remote_searchable": true, 
           "ts_column": "timestamp", 
           "paginated": true, 
           "height": 10, 
           "min_wdith": 12, 
           "columns": { 
             "name": { 
               "title": "Name", 
               "key": true 
             }, 
             "city": { 
               "title": "City", 
               "key": true 
             }, 
             "age": { 
               "title": "Age", 
               "key": true 
             }, 
             "Month": { 
               "title": "Month", 
               "key": true 
             }, 
             "donations": { 
               "title": "Donations", 
               "key": true 
             }, 
             "_RDA_Id": { 
               "title": "RDA ID", 
               "key": true, 
               "visible": false 
             } 
           }, 
           "actions": [ 
             { 
               "permission": "rda:github:view", 
               "title": "Onboard Details", 
               "type": "POPUP_FORM", 
               "selectionType": "NONE", 
               "identifier": "saas-service-action:userdashboard-add-yaml", 
               "api-endpoint": { 
                 "service-name": "saas-reports", 
                 "methodName": "getForm", 
                 "stringified-params": true, 
                 "parse-output": false, 
                 "params": [ 
                   { 
                     "formId": "rda.saas.dynamic.form", 
                     "formDefinition": { 
                       "id": "rda.saas.dynamic.form", 
                       "refreshRequired": true, 
                       "formFieldList": [ 
                         { 
                           "help": "User Name", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "required": true, 
                           "editable": true, 
                           "label": "User Name", 
                           "hidden": false, 
                           "fieldId": "name" 
                         }, 
                         { 
                           "help": "City Name", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "required": true, 
                           "editable": true, 
                           "label": "City Name", 
                           "hidden": false, 
                           "fieldId": "city" 
                         }, 
                         { 
                           "help": "Age", 
                           "required": false, 
                           "editable": true, 
                           "label": "Age", 
                           "hidden": false, 
                           "fieldId": "age", 
                           "dataType": "INT", 
                           "controlType": "INT", 
                           "defaultValue": false 
                         }, 
                         { 
                           "help": "Month", 
                           "required": false, 
                           "editable": true, 
                           "label": "Month", 
                           "hidden": false, 
                           "fieldId": "Month", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "defaultValue": false 
                         }, 
                         { 
                           "help": "Donations", 
                           "required": false, 
                           "editable": true, 
                           "label": "Donations", 
                           "hidden": false, 
                           "fieldId": "donations", 
                           "dataType": "INT", 
                           "controlType": "INT", 
                           "defaultValue": false 
                         } 
                       ] 
                     }, 
                     "actions": [ 
                       { 
                         "type": "UPDATE_PSTREAM", 
                         "pstreamName": "main" 
                       }, 
                       { 
                         "type": "RUN_PIPELINE", 
                         "pipelineName": "simple_pipeline", 
                         "isSync": true 
                       } 
                     ] 
                   } 
                 ] 
               } 
             }, 
             { 
               "permission": "rda:github:view", 
               "title": "Edit User", 
               "type": "POPUP_FORM", 
               "selectionType": "SINGLE", 
               "identifier": "saas-service-action:userdashboard-add-yaml", 
               "api-endpoint": { 
                 "service-name": "saas-reports", 
                 "methodName": "getForm", 
                 "stringified-params": true, 
                 "parse-output": false, 
                 "params": [ 
                   { 
                     "formId": "rda.saas.dynamic.form", 
                     "formDefinition": { 
                       "id": "rda.saas.dynamic.form", 
                       "refreshRequired": true, 
                       "formFieldList": [ 
                         { 
                           "help": "User Name", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "required": true, 
                           "editable": true, 
                           "label": "User Name", 
                           "hidden": false, 
                           "fieldId": "name" 
                         }, 
                         { 
                           "help": "City Name", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "required": true, 
                           "editable": true, 
                           "label": "City Name", 
                           "hidden": false, 
                           "fieldId": "city" 
                         }, 
                         { 
                           "help": "Age", 
                           "required": false, 
                           "editable": true, 
                           "label": "Age", 
                           "hidden": false, 
                           "fieldId": "age", 
                           "dataType": "INT", 
                           "controlType": "INT", 
                           "defaultValue": false 
                         }, 
                         { 
                           "help": "Month", 
                           "required": false, 
                           "editable": true, 
                           "label": "Month", 
                           "hidden": false, 
                           "fieldId": "Month", 
                           "dataType": "string", 
                           "controlType": "TEXT_FIELD", 
                           "defaultValue": false 
                         }, 
                         { 
                           "help": "Donations", 
                           "required": false, 
                           "editable": true, 
                           "label": "Donations", 
                           "hidden": false, 
                           "fieldId": "donations", 
                           "dataType": "INT", 
                           "controlType": "INT", 
                           "defaultValue": false 
                         } 
                       ] 
                     }, 
                     "actions": [ 
                       { 
                         "type": "UPDATE_PSTREAM", 
                         "pstreamName": "main", 
                         "operation": "UPDATE", 
                         "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" 
                       }, 
                       { 
                         "type": "RUN_PIPELINE", 
                         "pipelineName": "simple_pipeline", 
                         "isSync": true 
                       } 
                     ] 
                   } 
                 ] 
               } 
             }, 
             { 
               "permission": "rda:github:view", 
               "title": "Delete User", 
               "type": "POPUP_FORM", 
               "selectionType": "SINGLE", 
               "identifier": "saas-service-action:userdashboard-add-yaml", 
               "api-endpoint": { 
                 "service-name": "saas-reports", 
                 "methodName": "getForm", 
                 "stringified-params": true, 
                 "parse-output": false, 
                 "params": [ 
                   { 
                     "formId": "rda.saas.dynamic.form", 
                     "formActionList": { 
                       "formActions": [ 
                         { 
                           "identifier": "Submit", 
                           "actionLabel": "Delete" 
                         } 
                       ] 
                     }, 
                     "formDefinition": { 
                       "id": "rda.saas.dynamic.form", 
                       "refreshRequired": true, 
                       "formFieldList": [ 
                         { 
                           "help": "Do you want to delete the onboarded User?", 
                           "dataType": "string", 
                           "controlType": "LABEL", 
                           "required": false, 
                           "editable": false, 
                           "label": "Do you want to delete the onboarded User?", 
                           "hidden": false, 
                           "fieldId": "name" 
                         } 
                       ] 
                     }, 
                     "actions": [ 
                       { 
                         "type": "UPDATE_PSTREAM", 
                         "pstreamName": "main", 
                         "operation": "DELETE", 
                         "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" 
                       }, 
                       { 
                         "type": "RUN_PIPELINE", 
                         "pipelineName": "simple_pipeline", 
                         "isSync": true 
                       } 
                     ] 
                   } 
                 ] 
               } 
             } 
           ] 
         } 
       ] 
     } 
   ] 
 }

```

Note

As shown in the screenshot below, we've used operations like 'ADD' for 'Onboard Details', 'UPDATE' for 'Edit User', and 'DELETE' for 'Delete User' which are highlighted in the above Configuration.

[![Onboarding](https://bot-docs.cloudfabrix.io/images/dashboards/onboarding.png)](/images/dashboards/onboarding.png)

#### ****3.15.7 Multi Widget Support****

This feature empowers users to organize multiple widgets within a dashboard layout by specifying their grouping or location. For example, assigning the widget\_group as "group1" consolidates all widgets into one layout, while setting it as "group2" accomplishes the same for another distinct set of widgets, continuing similarly for additional groups as needed.

Please refer the below **configuration parameter** table which are used to configure **Multi Widget Support** within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `widget_group` | No  | Name of the group were it belongs |

Below is a sample configuration for Multi Widget Support.
```
 { 
   "widget_group": "group", 
   "min_width": 6, 
   "height": 8, 
   "max_width": 12, 
   "widget_type": "pie_chart", 
   "title": "Widget 1", 
   "stream": "rdaf_services_logs", 
   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", 
   "ts_column": "timestamp", 
   "column": "_id", 
   "agg": "value_count", 
   "group_by": [ 
     "log_severity" 
   ], 
   "type": "str" 
 }

```

[Example](#__tabbed_22_1)
```
 { 
   "name": "Multi_support", 
   "label": "Multi Support Widget", 
   "description": "GH_2745", 
   "version": "24.01.03.1", 
   "enabled": true, 
   "dashboard_type": "dashboard", 
   "dashboard_filters": { 
     "time_filter": true 
   }, 
   "dashboard_folder": "Default", 
   "dashboard_sections": [ 
     { 
       "title": "Student App", 
       "show_filter": true, 
       "widgets": [ 
         { 
           "widget_group": "group2", 
           "title": "Student city", 
           "widget_type": "pie_chart", 
           "stream": "main", 
           "column": "count_", 
           "min_width": 6, 
           "group_by": [ 
             "city" 
           ], 
           "type": "int", 
           "agg": "value_count", 
           "ts_column": "timestamp" 
         }, 
         { 
           "widget_group": "group2", 
           "title": "Student name", 
           "widget_type": "counter", 
           "stream": "main", 
           "column": "count_", 
           "min_width": 6, 
           "group_by": [ 
             "name" 
           ], 
           "type": "int", 
           "agg": "value_count", 
           "ts_column": "timestamp" 
         }, 
         { 
           "title": "Student donation", 
           "label": "Donation", 
           "widget_group": "group1", 
           "widget_type": "bar_chart", 
           "min_width": 6, 
           "stream": "main", 
           "column": "count_", 
           "group_by": [ 
             "donation" 
           ], 
           "type": "int", 
           "agg": "value_count", 
           "ts_column": "timestamp" 
         } 
       ] 
     } 
   ] 
 }

```

[![Multiwidget](https://bot-docs.cloudfabrix.io/images/dashboards/multiwidget.png)](/images/dashboards/multiwidget.png)

[![Multiwidget Student Name](https://bot-docs.cloudfabrix.io/images/dashboards/multiwidget1.png)](/images/dashboards/multiwidget1.png)

\`\`\`

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!