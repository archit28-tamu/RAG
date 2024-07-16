 



Dashboard
=========

****1\. What is a Dashboard****
-------------------------------

Dashboards feature in RDA Fabric platform provides analytics and reporting using which different UI views can be created for different user personas such as executives, IT admins and operators etc. Dashboards are composable and customizable to fit specific user needs within the IT operations landscape.  

Below are some of the available different data types in RDA Fabric platform using which Dashboards can be created, but not limited to.

*   **Metrics**
*   **Alerts / Events**
*   **Logs**
*   **Traces**
*   **Asset Inventory**
*   **Tickets**
*   **Other IT operations & service management data**

****2\. Creating a Dashboard****
--------------------------------

Follow the below steps to access the **Dashboard** feature in RDA Fabric platform

### ****2.1 Dashboard Configuration****

**Step-1:** Login into RDA Fabric platform as a **MSP Admin** user.

**Step-2:** Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Dashboards**

**Step-3:** Click on **Add** button to create a new Dashboard.

Dashboard configuration need to be provided in **JSON / YAML** format. Below is a sample configuration to create a new Dashboard.

`[](#__codelineno-0-1) { [](#__codelineno-0-2)     "name": "rdaf-platform-log-analytics-2", [](#__codelineno-0-3)     "label": "RDAF Platform Logs2", [](#__codelineno-0-4)     "description": "RDAF Platform service's log analysis dashboard", [](#__codelineno-0-5)     "version": "22.9.22.2", [](#__codelineno-0-6)     "enabled": true, [](#__codelineno-0-7)     "dashboard_style": "tabbed", [](#__codelineno-0-8)     "status_poller": {}, [](#__codelineno-0-9)     "dashboard_filters": { [](#__codelineno-0-10)         "time_filter": true, [](#__codelineno-0-11)         "columns_filter": [], [](#__codelineno-0-12)         "group_filters": [] [](#__codelineno-0-13)     }, [](#__codelineno-0-14)     "dashboard_sections": [], [](#__codelineno-0-15)     "dashboard_type": "app", [](#__codelineno-0-16)     "dashboard_pages": [] [](#__codelineno-0-17) }`

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

    `[](#__codelineno-1-1)     "status_poller": { [](#__codelineno-1-2)         "stream": "rdaf_pstream_name", [](#__codelineno-1-3)         "frequency": 30, [](#__codelineno-1-4)         "columns": [ [](#__codelineno-1-5)             "timestamp" [](#__codelineno-1-6)         ], [](#__codelineno-1-7)         "sorting": [ [](#__codelineno-1-8)             { [](#__codelineno-1-9)                 "timestamp": "desc" [](#__codelineno-1-10)             } [](#__codelineno-1-11)         ], [](#__codelineno-1-12)         "query": "timestamp is after '${timestamp}'", [](#__codelineno-1-13)         "defaults": { [](#__codelineno-1-14)             "timestamp": "$UTCNOW" [](#__codelineno-1-15)         }, [](#__codelineno-1-16)         "action": "refresh" [](#__codelineno-1-17)     }`

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

`[](#__codelineno-2-1) "dashboard_filters": { [](#__codelineno-2-2)   "time_filter": true, [](#__codelineno-2-3)   "default_time_filter_labels": [ [](#__codelineno-2-4)     "Last 1 month" [](#__codelineno-2-5)   ] [](#__codelineno-2-6) }`

Note

Make sure the `time_filter` is enabled and set to `true`

**Custom Time Filters**: When custom time filters are enabled along with the time filter, users can define precise intervals for their timestamp data. This functionality permits users to customize intervals, like minutes (m), hours (h), days (d), weeks (w), months (M), and years (y). However, it's important to note that, users must input a number followed by the interval type letter. Just providing the 'm' designation won't display any results; users need to adhere to the format of providing a numerical value followed by the interval type letter to ensure accurate interval definitions.

Below is the sample configuration to specify Custom Time Filter

`[](#__codelineno-3-1) "dashboard_filters": { [](#__codelineno-3-2) "time_filter": true, [](#__codelineno-3-3) "custom_time_filters": [ [](#__codelineno-3-4)     "15m", [](#__codelineno-3-5)     "32m", [](#__codelineno-3-6)     "72m", [](#__codelineno-3-7)     "1h", [](#__codelineno-3-8)     "4h", [](#__codelineno-3-9)     "36h", [](#__codelineno-3-10)     "1d", [](#__codelineno-3-11)     "3d", [](#__codelineno-3-12)     "1w", [](#__codelineno-3-13)     "2w", [](#__codelineno-3-14)     "1M", [](#__codelineno-3-15)     "3M", [](#__codelineno-3-16)     "1y", [](#__codelineno-3-17)     "10y" [](#__codelineno-3-18)   ] [](#__codelineno-3-19) }`

![Custom Time Filters](https://bot-docs.cloudfabrix.io/images/dashboards/custom_time_filters.png)

Note

Make sure the `time_filter` is enabled and set to `true`

**Column Filters**: option allows the user to query and filter the data on one or more selected column(s) using the dashboard's **filter bar** on demand.

    `[](#__codelineno-4-1)     "dashboard_filters": { [](#__codelineno-4-2)         "time_filter": true, [](#__codelineno-4-3)         "columns_filter": [ [](#__codelineno-4-4)             { [](#__codelineno-4-5)                 "id": "timestamp", [](#__codelineno-4-6)                 "label": "Timestamp", [](#__codelineno-4-7)                 "type": "DATETIME" [](#__codelineno-4-8)             }, [](#__codelineno-4-9)             ... [](#__codelineno-4-10)             ... [](#__codelineno-4-11)             { [](#__codelineno-4-12)                 "id": "host", [](#__codelineno-4-13)                 "label": "IP Address", [](#__codelineno-4-14)                 "type": "TEXT" [](#__codelineno-4-15)             } [](#__codelineno-4-16)         ] [](#__codelineno-4-17)     }`

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

    `[](#__codelineno-5-1)     "group_filters": [ [](#__codelineno-5-2)             { [](#__codelineno-5-3)                 "stream": "rdaf_services_logs", [](#__codelineno-5-4)                 "title": "Log Severity", [](#__codelineno-5-5)                 "group_by": [ [](#__codelineno-5-6)                     "log_severity" [](#__codelineno-5-7)                 ], [](#__codelineno-5-8)                 "ts_column": "@timestamp", [](#__codelineno-5-9)                 "agg": "value_count", [](#__codelineno-5-10)                 "column": "_id", [](#__codelineno-5-11)                 "type": "int", [](#__codelineno-5-12)                 "show_counts": true, [](#__codelineno-5-13)             }, [](#__codelineno-5-14)             ... [](#__codelineno-5-15)             ... [](#__codelineno-5-16)             { [](#__codelineno-5-17)                 "stream": "rdaf_services_logs", [](#__codelineno-5-18)                 "title": "RDA Host IPAddress", [](#__codelineno-5-19)                 "group_by": [ [](#__codelineno-5-20)                     "service_host" [](#__codelineno-5-21)                 ], [](#__codelineno-5-22)                 "ts_column": "@timestamp", [](#__codelineno-5-23)                 "agg": "value_count", [](#__codelineno-5-24)                 "column": "_id", [](#__codelineno-5-25)                 "type": "int" [](#__codelineno-5-26)             } [](#__codelineno-5-27)         ]`

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

    `[](#__codelineno-6-1)     "dashboard_pages": [ [](#__codelineno-6-2)         { [](#__codelineno-6-3)             "name": "CFX Incidents - Dashboard", [](#__codelineno-6-4)             "label": "Incidents", [](#__codelineno-6-5)             "icon": "incident.svg", [](#__codelineno-6-6)             "group": "group1" [](#__codelineno-6-7)         }, [](#__codelineno-6-8)         ... [](#__codelineno-6-9)         ... [](#__codelineno-6-10)         { [](#__codelineno-6-11)             "name": "Operational Metric - Dashboard", [](#__codelineno-6-12)             "label": "Metric Analysis", [](#__codelineno-6-13)             "icon": "metrics.svg", [](#__codelineno-6-14)             "group":"group2" [](#__codelineno-6-15)         } [](#__codelineno-6-16)     ]`

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

`[](#__codelineno-7-1) "dashboard_groups": { [](#__codelineno-7-2) "group1": { [](#__codelineno-7-3) "icon": "overall.svg", [](#__codelineno-7-4) "label": "Network" [](#__codelineno-7-5) }, [](#__codelineno-7-6) ... [](#__codelineno-7-7) ... [](#__codelineno-7-8) "group2": { [](#__codelineno-7-9) "icon": "jobs.svg", [](#__codelineno-7-10) "label": "vCenter" [](#__codelineno-7-11) } [](#__codelineno-7-12) }, [](#__codelineno-7-13) "dashboard_pages": [ [](#__codelineno-7-14) { [](#__codelineno-7-15) "name": "aia-network-overall", [](#__codelineno-7-16) "label": "Network", [](#__codelineno-7-17) "icon": "hardware.svg", [](#__codelineno-7-18) "group": "group1" [](#__codelineno-7-19) } [](#__codelineno-7-20) ]`

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

`[](#__codelineno-8-1) { [](#__codelineno-8-2)   "name": "my-dashboard", [](#__codelineno-8-3)   "label": "My Dashboard", [](#__codelineno-8-4)   "description": "Example dashboard", [](#__codelineno-8-5)   "enabled": true, [](#__codelineno-8-6)   "dashboard_style": "tabbed", [](#__codelineno-8-7)   "dashboard_filters": { [](#__codelineno-8-8)     "time_filter": true, [](#__codelineno-8-9)     "columns_filter": [ [](#__codelineno-8-10)       { [](#__codelineno-8-11)         "id": "sys_created_on", [](#__codelineno-8-12)         "label": "Created On", [](#__codelineno-8-13)         "type": "DATETIME" [](#__codelineno-8-14)       }, [](#__codelineno-8-15)       { [](#__codelineno-8-16)         "id": "assigned_to", [](#__codelineno-8-17)         "label": "Assigned To", [](#__codelineno-8-18)         "type": "TEXT" [](#__codelineno-8-19)       } [](#__codelineno-8-20)     ] [](#__codelineno-8-21)   }, [](#__codelineno-8-22)   "dashboard_sections": [ [](#__codelineno-8-23)     { [](#__codelineno-8-24)       "title": "Service Now", [](#__codelineno-8-25)       "show_filter": true, [](#__codelineno-8-26)       "widgets": [ [](#__codelineno-8-27)         { [](#__codelineno-8-28)           "title": "Sample Data", [](#__codelineno-8-29)           "widget_type": "tabular", [](#__codelineno-8-30)           "min_width": 8, [](#__codelineno-8-31)           "height": 8, [](#__codelineno-8-32)           "max_width": 12, [](#__codelineno-8-33)           "timestamp": "sys_created_on", [](#__codelineno-8-34)           "columns": { [](#__codelineno-8-35)             "assigned_to": "Assigned To", [](#__codelineno-8-36)             "sys_created_on": "Created On", [](#__codelineno-8-37)             "severity": "Severity" [](#__codelineno-8-38)           }, [](#__codelineno-8-39)           "dataset": "servicenow_data" [](#__codelineno-8-40)         } [](#__codelineno-8-41)       ] [](#__codelineno-8-42)     } [](#__codelineno-8-43)   ] [](#__codelineno-8-44) }`

****3\. Dashboard Charts / Widgets****
--------------------------------------

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

 `[](#__codelineno-9-1)  { [](#__codelineno-9-2)   "widget_type": "pie_chart", [](#__codelineno-9-3)   "title": "Logs by RDA Host", [](#__codelineno-9-4)   "stream": "rdaf_services_logs", [](#__codelineno-9-5)   "ts_column": "timestamp", [](#__codelineno-9-6)   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", [](#__codelineno-9-7)   "column": "_id", [](#__codelineno-9-8)   "agg": "value_count", [](#__codelineno-9-9)   "group_by": [ [](#__codelineno-9-10)     "service_host" [](#__codelineno-9-11)   ], [](#__codelineno-9-12)   "type": "str", [](#__codelineno-9-13)   "min_width": 4, [](#__codelineno-9-14)   "height": 2, [](#__codelineno-9-15)   "max_width": 4 [](#__codelineno-9-16) }`

#### ****3.1.1 Sample Pie Chart****

| ****Pie Chart Using Group By Example:**** | ****Pie Chart Using Group By Example Percentage:**** |
| --- | --- |
| ![PieChart_Group_By_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_GroupBy_Example.png) | ![PieChart_Group_By_Example_Percentage](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_GroupBy_Perc_Example.png) |

#### ****3.1.2 Pie Chart using extra\_filter****

`[](#__codelineno-10-1) { [](#__codelineno-10-2)   "widget_type": "pie_chart", [](#__codelineno-10-3)   "title": "Pie Chart Using Extra Filter Example", [](#__codelineno-10-4)   "stream": "rdaf_services_logs", [](#__codelineno-10-5)   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", [](#__codelineno-10-6)   "ts_column": "timestamp", [](#__codelineno-10-7)   "column": "_id", [](#__codelineno-10-8)   "agg": "value_count", [](#__codelineno-10-9)   "group_by": [ [](#__codelineno-10-10)     "log_severity" [](#__codelineno-10-11)   ], [](#__codelineno-10-12)   "type": "str" [](#__codelineno-10-13) }`

![PieChart_Extra_Filter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_Extra_Filter_Example.png)

#### ****3.1.3 Pie Chart with color-mapping****

`[](#__codelineno-11-1) { [](#__codelineno-11-2)   "widget_type": "pie_chart", [](#__codelineno-11-3)   "title": "Pie Chart with Color Map Example", [](#__codelineno-11-4)   "stream": "rdaf_services_logs", [](#__codelineno-11-5)   "ts_column": "timestamp", [](#__codelineno-11-6)   "column": "_id", [](#__codelineno-11-7)   "agg": "value_count", [](#__codelineno-11-8)   "group_by": [ [](#__codelineno-11-9)     "log_severity" [](#__codelineno-11-10)   ], [](#__codelineno-11-11)   "type": "str", [](#__codelineno-11-12)   "style": { [](#__codelineno-11-13)     "color-map": { [](#__codelineno-11-14)       "ERROR": [ [](#__codelineno-11-15)         "#ef5350", [](#__codelineno-11-16)         "#ffffff" [](#__codelineno-11-17)       ], [](#__codelineno-11-18)       "WARNING": [ [](#__codelineno-11-19)         "#FFA726", [](#__codelineno-11-20)         "#ffffff" [](#__codelineno-11-21)       ], [](#__codelineno-11-22)       "INFO": [ [](#__codelineno-11-23)         "#388e3c", [](#__codelineno-11-24)         "#ffffff" [](#__codelineno-11-25)       ], [](#__codelineno-11-26)       "DEBUG": [ [](#__codelineno-11-27)         "#000000", [](#__codelineno-11-28)         "#ffffff" [](#__codelineno-11-29)       ], [](#__codelineno-11-30)       "UNKNOWN": [ [](#__codelineno-11-31)         "#bcaaa4", [](#__codelineno-11-32)         "#ffffff" [](#__codelineno-11-33)       ] [](#__codelineno-11-34)     } [](#__codelineno-11-35)   } [](#__codelineno-11-36) }`

![Dashboard_Pie_Chart_with_Color_Map_Example](https://bot-docs.cloudfabrix.io/images/dashboards/PieChart_ColorMap_Example.png)

#### ****3.1.4 Pie Chart Showing Bottom N Values****

Below is the sample configuration of Pie Chart Showing Bottom N Values

`[](#__codelineno-12-1) { [](#__codelineno-12-2)   "widget_type": "pie_chart", [](#__codelineno-12-3)   "title": "City", [](#__codelineno-12-4)   "duration_hours": 1080, [](#__codelineno-12-5)   "stream": "people_custom_timestamp", [](#__codelineno-12-6)   "ts_column": "timestamp", [](#__codelineno-12-7)   "extra_filter": null, [](#__codelineno-12-8)   "column": "count_", [](#__codelineno-12-9)   "agg": "sum", [](#__codelineno-12-10)   "group_by": [ [](#__codelineno-12-11)     "city" [](#__codelineno-12-12)   ], [](#__codelineno-12-13)   "bottom_n": 3, [](#__codelineno-12-14)   "type": "int", [](#__codelineno-12-15)   "min_width": 3, [](#__codelineno-12-16)   "height": 3, [](#__codelineno-12-17)   "max_width": 6 [](#__codelineno-12-18) }`

![Piechart_BottomExample](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_bottom.png)

#### ****3.1.5 Pie Chart Using Formatting Options****

Below is the sample configuration of Pie Chart Using Formatting Options

`[](#__codelineno-13-1) { [](#__codelineno-13-2)   "widget_type": "pie_chart", [](#__codelineno-13-3)   "title": "Pie Chart", [](#__codelineno-13-4)   "duration_hours": 1080, [](#__codelineno-13-5)   "stream": "main", [](#__codelineno-13-6)   "ts_column": "timestamp", [](#__codelineno-13-7)   "extra_filter": null, [](#__codelineno-13-8)   "column": "count_", [](#__codelineno-13-9)   "agg": "sum", [](#__codelineno-13-10)   "group_by": [ [](#__codelineno-13-11)     "city" [](#__codelineno-13-12)   ], [](#__codelineno-13-13)   "formatting": { [](#__codelineno-13-14)     "style": "unit", [](#__codelineno-13-15)     "unit": "percent", [](#__codelineno-13-16)     "signDisplay": "always" [](#__codelineno-13-17)   }, [](#__codelineno-13-18)   "type": "int", [](#__codelineno-13-19)   "min_width": 3, [](#__codelineno-13-20)   "height": 3, [](#__codelineno-13-21)   "max_width": 6 [](#__codelineno-13-22) }`

![Piechart_Formatting Example](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_formatting.png)

#### ****3.1.6 Pie Chart Using Others Spec****

Below is the sample configuration of Pie Chart Using Others Spec

`[](#__codelineno-14-1) { [](#__codelineno-14-2)   "widget_type": "pie_chart", [](#__codelineno-14-3)   "title": "Name- Pie chart", [](#__codelineno-14-4)   "duration_hours": 10800, [](#__codelineno-14-5)   "stream": "main", [](#__codelineno-14-6)   "ts_column": "timestamp", [](#__codelineno-14-7)   "extra_filter": null, [](#__codelineno-14-8)   "column": "count_", [](#__codelineno-14-9)   "agg": "sum", [](#__codelineno-14-10)   "group_by": [ [](#__codelineno-14-11)     "city" [](#__codelineno-14-12)   ], [](#__codelineno-14-13)   "others_spec": { [](#__codelineno-14-14)   "city": { [](#__codelineno-14-15)   "name_based_limit": true [](#__codelineno-14-16)     } [](#__codelineno-14-17)   }, [](#__codelineno-14-18)   "type": "int", [](#__codelineno-14-19)   "min_width": 6, [](#__codelineno-14-20)   "height": 6, [](#__codelineno-14-21)   "max_width": 6 [](#__codelineno-14-22) }`

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

`[](#__codelineno-15-1) { [](#__codelineno-15-2)   "widget_type": "pie_chart", [](#__codelineno-15-3)   "title": "Date based Pie_chart", [](#__codelineno-15-4)   "duration_hours": 10800, [](#__codelineno-15-5)   "stream": "trail", [](#__codelineno-15-6)   "ts_column": "timestamp", [](#__codelineno-15-7)   "extra_filter": null, [](#__codelineno-15-8)   "column": "count_", [](#__codelineno-15-9)   "agg": "value_count", [](#__codelineno-15-10)   "group_by": [ [](#__codelineno-15-11)     "date" [](#__codelineno-15-12)   ], [](#__codelineno-15-13)   "groups_meta": { [](#__codelineno-15-14)     "type": "date", [](#__codelineno-15-15)     "format": "%d-%b-%y" [](#__codelineno-15-16)   }, [](#__codelineno-15-17)   "type": "int", [](#__codelineno-15-18)   "limit": 15, [](#__codelineno-15-19)   "min_width": 6, [](#__codelineno-15-20)   "height": 5, [](#__codelineno-15-21)   "max_width": 6 [](#__codelineno-15-22) }`

![Piechart_Piechart_Sorting_Type](https://bot-docs.cloudfabrix.io/images/dashboards/piechart_sorting_type.png)

#### ****3.1.8 Pie Chart with No Filter Option****

Below is the sample configuration of Pie Chart Using Sorting Type / Widget.

`[](#__codelineno-16-1) { [](#__codelineno-16-2)   "widget_type": "pie_chart", [](#__codelineno-16-3)   "title": "Pie Chart ", [](#__codelineno-16-4)   "stream": "main", [](#__codelineno-16-5)   "ts_column": "timestamp", [](#__codelineno-16-6)   "description": "Pie Charts", [](#__codelineno-16-7)   "segment_filter": false, [](#__codelineno-16-8)   "column": "donation", [](#__codelineno-16-9)   "agg": "sum", [](#__codelineno-16-10)   "group_by": [ [](#__codelineno-16-11)     "city" [](#__codelineno-16-12)   ], [](#__codelineno-16-13)   "min_width": 3, [](#__codelineno-16-14)   "max_width": 4, [](#__codelineno-16-15)   "type": "str" [](#__codelineno-16-16) }`

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

`[](#__codelineno-17-1) { [](#__codelineno-17-2)   "title": "Tabular with Pstream Query Example", [](#__codelineno-17-3)   "widget_type": "tabular", [](#__codelineno-17-4)   "stream": "dli-synthetic-logs-raw", [](#__codelineno-17-5)   "query": "*", [](#__codelineno-17-6)   "min_width": 6, [](#__codelineno-17-7)   "height": 8, [](#__codelineno-17-8)   "max_width": 6, [](#__codelineno-17-9)   "paginated": true, [](#__codelineno-17-10)   "remote_searchable": true, [](#__codelineno-17-11)   "remote_searchable_cols": [ [](#__codelineno-17-12)        "device", [](#__codelineno-17-13)        "message" [](#__codelineno-17-14)   ], [](#__codelineno-17-15)   "max_rows": 50, [](#__codelineno-17-16)   "sorting": [ [](#__codelineno-17-17)     { [](#__codelineno-17-18)       "timestamp": "desc" [](#__codelineno-17-19)     } [](#__codelineno-17-20)   ], [](#__codelineno-17-21)   "columns": { [](#__codelineno-17-22)     "timestamp": "Timestamp", [](#__codelineno-17-23)     "device": "Device", [](#__codelineno-17-24)     "count_": "Count", [](#__codelineno-17-25)     "message": "Message" [](#__codelineno-17-26)   }, [](#__codelineno-17-27)   "widget_id": "94a3fc11" [](#__codelineno-17-28) }`

![Time_Series_Stream_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tablular_Query.png)

#### ****3.2.2 Tabular Report with truncateColumns****

Below is the sample configuration of Tabular Report / Widget with `truncateColumns` parameter.

`[](#__codelineno-18-1) { [](#__codelineno-18-2)   "title": "Tabular chart with truncate columns", [](#__codelineno-18-3)   "widget_type": "tabular", [](#__codelineno-18-4)   "stream": "main", [](#__codelineno-18-5)   "columns": { [](#__codelineno-18-6)     "name": { [](#__codelineno-18-7)       "title": "Name", [](#__codelineno-18-8)       "formatter": "truncate" [](#__codelineno-18-9)     }, [](#__codelineno-18-10)     "city": { [](#__codelineno-18-11)       "title": "City" [](#__codelineno-18-12)     } [](#__codelineno-18-13)   } [](#__codelineno-18-14) }` 

![tabular report truncate Columns](https://bot-docs.cloudfabrix.io/images/dashboards/tabular_report_truncate_Columns.png)

#### ****3.2.3 Tabular Report with resizableColumns****

Below is the sample configuration of Tabular Report / Widget with `resizableColumns` parameter.

`[](#__codelineno-19-1) { [](#__codelineno-19-2)   "title": "Tabular with Pstream Query resizableColumns Example", [](#__codelineno-19-3)   "widget_type": "tabular", [](#__codelineno-19-4)   "stream": "dli-synthetic-logs-raw", [](#__codelineno-19-5)   "query": "*", [](#__codelineno-19-6)   "min_width": 6, [](#__codelineno-19-7)   "height": 8, [](#__codelineno-19-8)   "max_width": 6, [](#__codelineno-19-9)   "resizableColumns": true, [](#__codelineno-19-10)   "paginated": true, [](#__codelineno-19-11)   "max_rows": 50, [](#__codelineno-19-12)   "sorting": [ [](#__codelineno-19-13)     { [](#__codelineno-19-14)       "timestamp": "desc" [](#__codelineno-19-15)     } [](#__codelineno-19-16)   ], [](#__codelineno-19-17)   "columns": { [](#__codelineno-19-18)     "timestamp": "Timestamp", [](#__codelineno-19-19)     "device": "Device", [](#__codelineno-19-20)     "count_": "Count", [](#__codelineno-19-21)     "message": "Message" [](#__codelineno-19-22)   }, [](#__codelineno-19-23)   "widget_id": "94a3fc11" [](#__codelineno-19-24) }`

![Tabular_resizableColumns_before_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tabular_resizableColumns_before.png)

![Tabular_resizableColumns_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Tabular_ResizableColumn.png)

#### ****3.2.4 Tabular Report with virtual\_scrolling & showRowSummary****

Below is the sample configuration of Tabular Report / Widget with `Virtual_scrolling & showRowSummary` parameter.

`[](#__codelineno-20-1) { [](#__codelineno-20-2)   "title": "virtual_scrolling and showRowSummary", [](#__codelineno-20-3)   "widget_type": "tabular", [](#__codelineno-20-4)   "stream": "rda_synthetic_metrics", [](#__codelineno-20-5)   "ts_column": "timestamp", [](#__codelineno-20-6)   "query": "*", [](#__codelineno-20-7)   "min_width": 6, [](#__codelineno-20-8)   "height": 8, [](#__codelineno-20-9)   "max_width": 6, [](#__codelineno-20-10)   "paginated": true, [](#__codelineno-20-11)   "virtual_scrolling": true, [](#__codelineno-20-12)   "showRowSummary": true, [](#__codelineno-20-13)   "max_rows": 50, [](#__codelineno-20-14)   "sorting": [ [](#__codelineno-20-15)     { [](#__codelineno-20-16)       "timestamp": "desc" [](#__codelineno-20-17)     } [](#__codelineno-20-18)   ], [](#__codelineno-20-19)   "columns": { [](#__codelineno-20-20)     "timestamp": "Timestamp", [](#__codelineno-20-21)     "metric_name": "metric_name", [](#__codelineno-20-22)     "count_": "Count", [](#__codelineno-20-23)     "source_tool": "source_tool", [](#__codelineno-20-24)     "stack_name": "stack_name" [](#__codelineno-20-25)   }, [](#__codelineno-20-26)   "widget_id": "94a3fc11" [](#__codelineno-20-27) }`

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

`[](#__codelineno-21-1) "actions": [ [](#__codelineno-21-2)   { [](#__codelineno-21-3)     "appName": "user-dashboard", [](#__codelineno-21-4)     "permission": "aia:page:view", [](#__codelineno-21-5)     "drillDownContext": "id", [](#__codelineno-21-6)     "drillDownLinkField": "dns_name", [](#__codelineno-21-7)     "identifier": "dns_name", [](#__codelineno-21-8)     "selectionType": "SINGLE", [](#__codelineno-21-9)     "stateName": "app.featureapp", [](#__codelineno-21-10)     "title": "View Details", [](#__codelineno-21-11)     "actionCondition": { [](#__codelineno-21-12)       "actionControl": "SHOW_IF", [](#__codelineno-21-13)       "conditionalField": [ [](#__codelineno-21-14)         { [](#__codelineno-21-15)           "conditionType": "EQUAL", [](#__codelineno-21-16)           "conditionValue": "CHASSIS", [](#__codelineno-21-17)           "fieldId": "equipment_type" [](#__codelineno-21-18)         } [](#__codelineno-21-19)       ] [](#__codelineno-21-20)     }, [](#__codelineno-21-21)     "type": "GO_TO_APP_STATE" [](#__codelineno-21-22)   } [](#__codelineno-21-23) ]`

Note

Mentioned below needs to be part of the columns list and the value needs to be replaced with the template/dashboard/app name

Ex: user-dashboard-`<template/dashboard/app name>`

`[](#__codelineno-22-1) "id": { [](#__codelineno-22-2)        "title": "ID", [](#__codelineno-22-3)        "value": "user-dashboard-aia-network-drilldown-app", [](#__codelineno-22-4)        "key": true, [](#__codelineno-22-5)        "type": "FIXED_VALUE", [](#__codelineno-22-6)        "hidden": true, [](#__codelineno-22-7)        "visible": false [](#__codelineno-22-8)       }`

Note

All the report definitions that are part of the above `template/dashboard/app` needs to be added with mentioned below parameters

`[](#__codelineno-23-1) "include_context_in_query": true [](#__codelineno-23-2) "include_context_keys" : ["column1","column2","column3"]`

Note

In order to pass column(s) as a context to `template/dashboard/app`, make sure the list of `include_context_keys` mentioned above are the key column(s)

[Example](#__tabbed_1_1)

`[](#__codelineno-24-1) "dns_name": { [](#__codelineno-24-2)               "title": "DNS Name", [](#__codelineno-24-3)               "type": "TEXT", [](#__codelineno-24-4)               "key": true [](#__codelineno-24-5)             }`

#### ****3.2.6 Tabular Report with External URL Hyperlink****

Below is the sample configuration of Tabular Report / Widget with `External URL Hyperlink`.

Note

Make sure the URL values are present as one of the column value in Pstream/Dataset as shown in Below Example

Below is how the column needs to be added in order to enable External URL on Specific column

`[](#__codelineno-25-1) "<column-id>": { [](#__codelineno-25-2)         "title": "<label>", [](#__codelineno-25-3)         "htmlTemplateForRow": "<a href=\"{{row.<column-id>}}\" target='_blank'>{{row.<column-id>}}</a>" [](#__codelineno-25-4)        }`

[Example](#__tabbed_2_1)

`[](#__codelineno-26-1) "drilldown_url": { [](#__codelineno-26-2)         "title": "Drilldown_URL", [](#__codelineno-26-3)         "htmlTemplateForRow": "<a href=\"{{row.drilldown_url}}\" target='_blank'>{{row.controller_name}}</a>" [](#__codelineno-26-4)        }`

Note

Same URL link can be launched by enabling hyperlink on different column, Below is the syntax for `column Definition`

`[](#__codelineno-27-1) "drilldown_url": { [](#__codelineno-27-2)         "title": "Controller", [](#__codelineno-27-3)         "htmlTemplateForRow": "<a href=\"{{row.drilldown_url}}\" target='_blank'>{{row.controller_name}}</a>" [](#__codelineno-27-4)        }`

#### ****3.2.7 Tabular Report with Custom Columns****

Please refer the below **configuration parameter** table which are additionally used to configure a Tabular Report Using Custom Columns within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `id` | yes | It will be the column\_id for the custom column, If you want to use that column any where else you can refer with that column id |
| `expr` | yes | The expression on any arithmetic operations on given columns will support the following syntax for example: `expr`: "((input-output)/input) \* 100" |
| `label` | yes | This will specify the label for obtained column |

Below is the sample configuration of Tabular Report / Widget with `custom_columns`.

`[](#__codelineno-28-1) { [](#__codelineno-28-2)   "widget_type": "tabular", [](#__codelineno-28-3)   "title": "Summary Report", [](#__codelineno-28-4)   "stream": "network-devices-inventory", [](#__codelineno-28-5)   "ts_column": "collection_timestamp", [](#__codelineno-28-6)   "sorting": [], [](#__codelineno-28-7)   "extra_filter": "up_eth_ports is not None", [](#__codelineno-28-8)   "columns": { [](#__codelineno-28-9)     "up_eth_ports": "UP ETH PORTS", [](#__codelineno-28-10)     "total_eth_ports": "TOTAL ETH PORTS" [](#__codelineno-28-11)   }, [](#__codelineno-28-12)   "custom_columns": [ [](#__codelineno-28-13)     { [](#__codelineno-28-14)       "id": "avg_up_ports", [](#__codelineno-28-15)       "label": "Avg UP Ports(%)", [](#__codelineno-28-16)       "expr": "((up_eth_ports / total_eth_ports) * 100) " [](#__codelineno-28-17)     } [](#__codelineno-28-18)   ] [](#__codelineno-28-19) }`

![Custom_Clolumns_Example](https://bot-docs.cloudfabrix.io/images/dashboards/custom_columns.png)

#### ****3.2.8 Tabular Report with Remote Search & Local Search****

Below is the sample configuration of Tabular Report / Widget with `remote search & local search`.

[Remote Search](#__tabbed_3_1)

`[](#__codelineno-29-1) { [](#__codelineno-29-2)   "title": "Tabular report with Remote Search enabled on first column only", [](#__codelineno-29-3)   "widget_type": "tabular", [](#__codelineno-29-4)   "duration_hours": 10000, [](#__codelineno-29-5)   "stream": "people_1k", [](#__codelineno-29-6)   "min_width": 8, [](#__codelineno-29-7)   "height": 5, [](#__codelineno-29-8)   "paginated": true, [](#__codelineno-29-9)   "max_rows": 50, [](#__codelineno-29-10)   "defaultColumnWidth": 100, [](#__codelineno-29-11)   "remote_search_columns_count": 1, [](#__codelineno-29-12)   "remote_searchable_cols": [ [](#__codelineno-29-13)     "city" [](#__codelineno-29-14)   ], [](#__codelineno-29-15)   "columns": { [](#__codelineno-29-16)     "name": "Name", [](#__codelineno-29-17)     "city": "City", [](#__codelineno-29-18)     "age": "Age", [](#__codelineno-29-19)     "timestamp": "Timestamp" [](#__codelineno-29-20)   } [](#__codelineno-29-21) }`

![Remote Search_Example](https://bot-docs.cloudfabrix.io/images/dashboards/remote_search.png)

[Local Search](#__tabbed_4_1)

`[](#__codelineno-30-1) { [](#__codelineno-30-2)   "title": "Tabular report with Local Search", [](#__codelineno-30-3)   "widget_type": "tabular", [](#__codelineno-30-4)   "stream": "main", [](#__codelineno-30-5)   "min_width": 8, [](#__codelineno-30-6)   "height": 5, [](#__codelineno-30-7)   "paginated": true, [](#__codelineno-30-8)   "max_rows": 50, [](#__codelineno-30-9)   "defaultColumnWidth": 100, [](#__codelineno-30-10)   "remote_searchable": false, [](#__codelineno-30-11)   "columns": { [](#__codelineno-30-12)     "name": "Name", [](#__codelineno-30-13)     "city": { [](#__codelineno-30-14)       "title": "City" [](#__codelineno-30-15)     }, [](#__codelineno-30-16)     "timestamp": { [](#__codelineno-30-17)       "title": "Timestamp" [](#__codelineno-30-18)     } [](#__codelineno-30-19)   } [](#__codelineno-30-20) }`

![Remote Search_Example](https://bot-docs.cloudfabrix.io/images/dashboards/local_search.png)

#### ****3.2.9 Tabular Report with Grouped Columns****

Below is the sample configuration of Tabular Report / Widget with `Grouped Columns`.

`[](#__codelineno-31-1) { [](#__codelineno-31-2)   "title": "Grouping in Tabular", [](#__codelineno-31-3)   "widget_type": "tabular", [](#__codelineno-31-4)   "stream": "main", [](#__codelineno-31-5)   "columns": { [](#__codelineno-31-6)     "name": { [](#__codelineno-31-7)       "title": "Name", [](#__codelineno-31-8)       "columnGroupLabel": "Group 1", [](#__codelineno-31-9)       "defaultColumnWidth": 60, [](#__codelineno-31-10)       "visible": true [](#__codelineno-31-11)     }, [](#__codelineno-31-12)     "city": { [](#__codelineno-31-13)       "title": "City", [](#__codelineno-31-14)       "columnGroupLabel": "Details 1", [](#__codelineno-31-15)       "defaultColumnWidth": 60, [](#__codelineno-31-16)       "visible": true [](#__codelineno-31-17)     }, [](#__codelineno-31-18)     "age": { [](#__codelineno-31-19)       "title": "Age", [](#__codelineno-31-20)       "columnGroupLabel": "Group 1", [](#__codelineno-31-21)       "defaultColumnWidth": 20, [](#__codelineno-31-22)       "visible": true [](#__codelineno-31-23)     }, [](#__codelineno-31-24)     "timestamp": { [](#__codelineno-31-25)       "title": "Timestamp", [](#__codelineno-31-26)       "type": "DATETIME", [](#__codelineno-31-27)       "columnGroupLabel": "Details 2", [](#__codelineno-31-28)       "defaultColumnWidth": 300 [](#__codelineno-31-29)     } [](#__codelineno-31-30)   } [](#__codelineno-31-31) }`

[![Grouped Columns](https://bot-docs.cloudfabrix.io/images/dashboards/grouped_columns.png)](/images/dashboards/grouped_columns.png)

#### ****3.2.10 Pivot Tabular Report****

Below is the sample configuration of Pivot Tabular Report.

`[](#__codelineno-32-1) { [](#__codelineno-32-2)   "title": "Mock Data Standard", [](#__codelineno-32-3)   "widget_type": "tabular", [](#__codelineno-32-4)   "stream": "mock_data", [](#__codelineno-32-5)   "min_width": 12, [](#__codelineno-32-6)   "height": 6, [](#__codelineno-32-7)   "max_width": 12, [](#__codelineno-32-8)   "columns": { [](#__codelineno-32-9)     "A": "A", [](#__codelineno-32-10)     "B": "B" [](#__codelineno-32-11)   }, [](#__codelineno-32-12)   "pivot": { [](#__codelineno-32-13)     "pivot_type": "standard", [](#__codelineno-32-14)     "group_by": [ [](#__codelineno-32-15)       "A", [](#__codelineno-32-16)       "B" [](#__codelineno-32-17)     ], [](#__codelineno-32-18)     "column": "count_", [](#__codelineno-32-19)     "agg": "value_count" [](#__codelineno-32-20)   }   [](#__codelineno-32-21) }`

[![Standard Pivot](https://bot-docs.cloudfabrix.io/images/dashboards/standard_pivot.png)](/images/dashboards/standard_pivot.png)

#### ****3.2.11 Extended Pivot Tabular Report****

Below is the sample configuration of Extended Pivot Tabular Report.

`[](#__codelineno-33-1) { [](#__codelineno-33-2)   "title": "Mock Data Extended", [](#__codelineno-33-3)   "widget_type": "tabular", [](#__codelineno-33-4)   "stream": "mock_data", [](#__codelineno-33-5)   "min_width": 12, [](#__codelineno-33-6)   "height": 6, [](#__codelineno-33-7)   "max_width": 12, [](#__codelineno-33-8)   "columns": { [](#__codelineno-33-9)     "A": "A", [](#__codelineno-33-10)     "B": "B" [](#__codelineno-33-11)   }, [](#__codelineno-33-12)   "pivot": { [](#__codelineno-33-13)     "pivot_type": "extended", [](#__codelineno-33-14)     "group_by": [ [](#__codelineno-33-15)       "A", [](#__codelineno-33-16)       "B" [](#__codelineno-33-17)     ], [](#__codelineno-33-18)     "series": [ [](#__codelineno-33-19)       { [](#__codelineno-33-20)         "column": "count_", [](#__codelineno-33-21)         "agg": "value_count", [](#__codelineno-33-22)         "type": "int", [](#__codelineno-33-23)         "label": "Count" [](#__codelineno-33-24)       } [](#__codelineno-33-25)     ] [](#__codelineno-33-26)   } [](#__codelineno-33-27) }`

[![Extended Pivot](https://bot-docs.cloudfabrix.io/images/dashboards/extended_pivot.png)](/images/dashboards/extended_pivot.png)

#### ****3.2.12 Advanced Pivot Tabular Report****

Below is the sample configuration of Advanced Pivot Tabular Report.

`[](#__codelineno-34-1) { [](#__codelineno-34-2)   "title": "Mock Data Advanced", [](#__codelineno-34-3)   "widget_type": "tabular", [](#__codelineno-34-4)   "stream": "mock_data", [](#__codelineno-34-5)   "min_width": 12, [](#__codelineno-34-6)   "height": 6, [](#__codelineno-34-7)   "max_width": 12, [](#__codelineno-34-8)   "columns": { [](#__codelineno-34-9)     "A": "A", [](#__codelineno-34-10)     "B": "B" [](#__codelineno-34-11)   }, [](#__codelineno-34-12)   "pivot": { [](#__codelineno-34-13)     "pivot_type": "advanced", [](#__codelineno-34-14)     "group_by": [ [](#__codelineno-34-15)       "A", [](#__codelineno-34-16)       "B" [](#__codelineno-34-17)     ], [](#__codelineno-34-18)     "series": [ [](#__codelineno-34-19)       { [](#__codelineno-34-20)         "column": "count_", [](#__codelineno-34-21)         "agg": "value_count", [](#__codelineno-34-22)         "type": "int", [](#__codelineno-34-23)         "label": "Count" [](#__codelineno-34-24)       } [](#__codelineno-34-25)     ] [](#__codelineno-34-26)   } [](#__codelineno-34-27) }`

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

`[](#__codelineno-35-1) { [](#__codelineno-35-2)   "title": "Simple Counter Example", [](#__codelineno-35-3)   "widget_type": "custom_counter", [](#__codelineno-35-4)   "formatter": "DescriptiveCountFormatter", [](#__codelineno-35-5)   "stream": "rda_system_worker_trace_summary", [](#__codelineno-35-6)   "ts_column": "timestamp", [](#__codelineno-35-7)   "duration_hours": 96, [](#__codelineno-35-8)   "column": "num_bot_executions", [](#__codelineno-35-9)   "agg": "sum", [](#__codelineno-35-10)   "type": "int", [](#__codelineno-35-11)   "widget_id": "02be1e20" [](#__codelineno-35-12) }`

![Dashboard_Simple_Counter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Simple_Counter.png)

#### ****3.3.2 Expression Counter Example****

Below is a sample configuration of Counter Chart / Widget with `expression_counter` and `expression`.

`[](#__codelineno-36-1) { [](#__codelineno-36-2)   "title": "Expression Counter Example", [](#__codelineno-36-3)   "widget_type": "expression_counter", [](#__codelineno-36-4)   "expression": "((input-output)/input) * 100", [](#__codelineno-36-5)   "unit": "%", [](#__codelineno-36-6)   "segments": [ [](#__codelineno-36-7)     { [](#__codelineno-36-8)       "variable": "output", [](#__codelineno-36-9)       "stream": "dli-log-stats", [](#__codelineno-36-10)       "extra_filter": "mode is 'processed'", [](#__codelineno-36-11)       "ts_column": "timestamp", [](#__codelineno-36-12)       "duration_hours": 720, [](#__codelineno-36-13)       "group_by": [ [](#__codelineno-36-14)         "mode" [](#__codelineno-36-15)       ], [](#__codelineno-36-16)       "column": "count", [](#__codelineno-36-17)       "agg": "sum", [](#__codelineno-36-18)       "type": "int" [](#__codelineno-36-19)     }, [](#__codelineno-36-20)     { [](#__codelineno-36-21)       "variable": "input", [](#__codelineno-36-22)       "stream": "dli-log-stats", [](#__codelineno-36-23)       "extra_filter": "mode is 'ingested'", [](#__codelineno-36-24)       "ts_column": "timestamp", [](#__codelineno-36-25)       "duration_hours": 720, [](#__codelineno-36-26)       "group_by": [ [](#__codelineno-36-27)         "mode" [](#__codelineno-36-28)       ], [](#__codelineno-36-29)       "column": "count", [](#__codelineno-36-30)       "agg": "sum", [](#__codelineno-36-31)       "type": "int" [](#__codelineno-36-32)     } [](#__codelineno-36-33)   ] [](#__codelineno-36-34) }`

![Dashboard_Expression_Counter_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Expression_Counter.png)

#### ****3.3.3 Group Counter Chart Example****

Note

To show up the **Total Counter**, Use the following parameters:

`show` - Set it to true for total counter chart to show up.

`label` - Optional. Default: “Total”.

`location` - Where to show the total counter. Optional. Default: “left”.

`color` - Hex Color Code

Below is a sample configuration of Counter Chart / Widget grouping multiples of them.

`[](#__codelineno-37-1) { [](#__codelineno-37-2)   "title": "Group Counter Chart Example", [](#__codelineno-37-3)   "widget_type": "counter", [](#__codelineno-37-4)   "min_width": 12, [](#__codelineno-37-5)   "max_width": 12, [](#__codelineno-37-6)   "stream": "main", [](#__codelineno-37-7)   "ts_column": "timestamp", [](#__codelineno-37-8)   "style": { [](#__codelineno-37-9)     "color-map": { [](#__codelineno-37-10)       "Chennai": "#388e3c", [](#__codelineno-37-11)       "Delhi": "#8e24aa", [](#__codelineno-37-12)       "Mumbai": "#d32f2f" [](#__codelineno-37-13)     } [](#__codelineno-37-14)   }, [](#__codelineno-37-15)   "sparkline": { [](#__codelineno-37-16)     "interval": "1d" [](#__codelineno-37-17)   }, [](#__codelineno-37-18)   "group_by": [ [](#__codelineno-37-19)     "city" [](#__codelineno-37-20)   ], [](#__codelineno-37-21)   "total_counter": { [](#__codelineno-37-22)     "show": true, [](#__codelineno-37-23)     "label": "Total Count", [](#__codelineno-37-24)     "location": "right", [](#__codelineno-37-25)     "color": "#0096FF" [](#__codelineno-37-26)   }, [](#__codelineno-37-27)   "column": "count_", [](#__codelineno-37-28)   "agg": "sum", [](#__codelineno-37-29)   "type": "int" [](#__codelineno-37-30) }`

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

`[](#__codelineno-38-1) { [](#__codelineno-38-2)   "title": "Bar Chart Example", [](#__codelineno-38-3)   "widget_type": "bar_chart", [](#__codelineno-38-4)   "stream": "rda_microservice_traces", [](#__codelineno-38-5)   "ts_column": "timestamp", [](#__codelineno-38-6)   "chartProperties": { [](#__codelineno-38-7)     "yAxisLabel": null, [](#__codelineno-38-8)     "xAxisLabel": "Count", [](#__codelineno-38-9)     "stacked": true, [](#__codelineno-38-10)     "legendLocation": "none", [](#__codelineno-38-11)     "orientation": "vertical" [](#__codelineno-38-12)   }, [](#__codelineno-38-13)   "duration_hours": 24, [](#__codelineno-38-14)   "group_by": [ [](#__codelineno-38-15)     "request_type" [](#__codelineno-38-16)   ], [](#__codelineno-38-17)   "column": "duration", [](#__codelineno-38-18)   "agg": "value_count", [](#__codelineno-38-19)   "type": "int", [](#__codelineno-38-20)   "widget_id": "f4786acb" [](#__codelineno-38-21) }`

![Dashboard_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Bar_Chart.png)

#### ****3.4.2 Bar Chart with extra filter****

Below is a sample of Bar Chart / Widget configuration with `extra_filter`

`[](#__codelineno-39-1) { [](#__codelineno-39-2)   "title": "Bar Chart Example", [](#__codelineno-39-3)   "widget_type": "bar_chart", [](#__codelineno-39-4)   "stream": "rda_microservice_traces", [](#__codelineno-39-5)   "extra_filter": "request_type != 'are-you-there'", [](#__codelineno-39-6)   "ts_column": "timestamp", [](#__codelineno-39-7)   "chartProperties": { [](#__codelineno-39-8)     "yAxisLabel": null, [](#__codelineno-39-9)     "xAxisLabel": "Count", [](#__codelineno-39-10)     "stacked": true, [](#__codelineno-39-11)     "legendLocation": "none", [](#__codelineno-39-12)     "orientation": "vertical" [](#__codelineno-39-13)   }, [](#__codelineno-39-14)   "duration_hours": 24, [](#__codelineno-39-15)   "group_by": [ [](#__codelineno-39-16)     "request_type" [](#__codelineno-39-17)   ], [](#__codelineno-39-18)   "column": "duration", [](#__codelineno-39-19)   "agg": "value_count", [](#__codelineno-39-20)   "type": "int", [](#__codelineno-39-21)   "widget_id": "f4786acb" [](#__codelineno-39-22) }`

![Dashboard_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Barchart_with_filter.png)

#### ****3.4.3 Bar Chart with Formatting Option****

Below is a sample configurations of Bar Chart with Formatting Options / Widget.

[Formatting Style Unit](#__tabbed_5_1)

`[](#__codelineno-40-1) { [](#__codelineno-40-2)   "widget_type": "bar_chart", [](#__codelineno-40-3)   "title": "BAR CHART with formatting option", [](#__codelineno-40-4)   "stream": "main", [](#__codelineno-40-5)   "chartProperties": { [](#__codelineno-40-6)     "orientation": "vertical" [](#__codelineno-40-7)   }, [](#__codelineno-40-8)   "formatting": { [](#__codelineno-40-9)     "style": "unit", [](#__codelineno-40-10)     "unit": "percent", [](#__codelineno-40-11)     "signDisplay": "exceptZero" [](#__codelineno-40-12)   }, [](#__codelineno-40-13)   "ts_column": "timestamp", [](#__codelineno-40-14)   "column": "count_", [](#__codelineno-40-15)   "agg": "value_count", [](#__codelineno-40-16)   "group_by": [ [](#__codelineno-40-17)     "name" [](#__codelineno-40-18)   ], [](#__codelineno-40-19)   "type": "str" [](#__codelineno-40-20) }`

![Dashboard_Formating_Percent](https://bot-docs.cloudfabrix.io/images/dashboards/formating_percent.png)

[Formatting Style Currency](#__tabbed_6_1)

`[](#__codelineno-41-1) { [](#__codelineno-41-2)   "widget_type": "bar_chart", [](#__codelineno-41-3)   "title": "City asset value", [](#__codelineno-41-4)   "stream": "people_custom_timestamp", [](#__codelineno-41-5)   "chartProperties": { [](#__codelineno-41-6)     "barThickness": 10, [](#__codelineno-41-7)     "orientation": "vertical" [](#__codelineno-41-8)   }, [](#__codelineno-41-9)   "formatting": { [](#__codelineno-41-10)     "style": "currency", [](#__codelineno-41-11)     "currency": "USD" [](#__codelineno-41-12)   }, [](#__codelineno-41-13)   "ts_column": "timestamp", [](#__codelineno-41-14)   "column": "count_", [](#__codelineno-41-15)   "agg": "value_count", [](#__codelineno-41-16)   "group_by": [ [](#__codelineno-41-17)     "city" [](#__codelineno-41-18)   ], [](#__codelineno-41-19)   "type": "str" [](#__codelineno-41-20) }`

![Dashboard_Formatting_Currency](https://bot-docs.cloudfabrix.io/images/dashboards/formatting_currency.png)

[Formatting with Standard Notation](#__tabbed_7_1)

`[](#__codelineno-42-1) { [](#__codelineno-42-2)   "widget_type": "bar_chart", [](#__codelineno-42-3)   "title": "City Donation Value", [](#__codelineno-42-4)   "stream": "donationn", [](#__codelineno-42-5)   "chartProperties": { [](#__codelineno-42-6)     "orientation": "vertical" [](#__codelineno-42-7)   }, [](#__codelineno-42-8)   "formatting": { [](#__codelineno-42-9)     "notation": "standard" [](#__codelineno-42-10)   }, [](#__codelineno-42-11)   "ts_column": "timestamp", [](#__codelineno-42-12)   "column": "donation", [](#__codelineno-42-13)   "agg": "sum", [](#__codelineno-42-14)   "group_by": [ [](#__codelineno-42-15)     "city" [](#__codelineno-42-16)   ], [](#__codelineno-42-17)   "type": "int" [](#__codelineno-42-18) }`

![Dashboard_standard_notation](https://bot-docs.cloudfabrix.io/images/dashboards/standard_notation.png)

[Formatting with Compact Notation](#__tabbed_8_1)

`[](#__codelineno-43-1) { [](#__codelineno-43-2)   "widget_type": "bar_chart", [](#__codelineno-43-3)   "title": "City Donation Value", [](#__codelineno-43-4)   "stream": "donationn", [](#__codelineno-43-5)   "chartProperties": { [](#__codelineno-43-6)     "orientation": "vertical" [](#__codelineno-43-7)   }, [](#__codelineno-43-8)   "formatting": { [](#__codelineno-43-9)     "notation": "compact" [](#__codelineno-43-10)   }, [](#__codelineno-43-11)   "ts_column": "timestamp", [](#__codelineno-43-12)   "column": "donation", [](#__codelineno-43-13)   "agg": "sum", [](#__codelineno-43-14)   "group_by": [ [](#__codelineno-43-15)     "city" [](#__codelineno-43-16)   ], [](#__codelineno-43-17)   "type": "int" [](#__codelineno-43-18) }`

![Dashboard_Compact_notation](https://bot-docs.cloudfabrix.io/images/dashboards/compact_notation.png)

#### ****3.4.4 Bar Chart Showing Top N Values****

Below is a sample configuration of Bar Chart Showing Top N Values / Widget.

`[](#__codelineno-44-1) { [](#__codelineno-44-2)   "widget_type": "bar_chart", [](#__codelineno-44-3)   "title": "City Donation Value", [](#__codelineno-44-4)   "stream": "donationn", [](#__codelineno-44-5)   "chartProperties": { [](#__codelineno-44-6)     "orientation": "vertical" [](#__codelineno-44-7)   }, [](#__codelineno-44-8)   "formatting": { [](#__codelineno-44-9)     "notation": "compact" [](#__codelineno-44-10)   }, [](#__codelineno-44-11)   "ts_column": "timestamp", [](#__codelineno-44-12)   "top_n": 3, [](#__codelineno-44-13)   "column": "donation", [](#__codelineno-44-14)   "agg": "sum", [](#__codelineno-44-15)   "group_by": [ [](#__codelineno-44-16)     "city" [](#__codelineno-44-17)   ], [](#__codelineno-44-18)   "type": "str" [](#__codelineno-44-19) }`

![Dashboard_Barchart_Topn](https://bot-docs.cloudfabrix.io/images/dashboards/barchart_topn.png)

#### ****3.4.5 Bar Chart With Others Spec****

Below is a sample configuration of Bar Chart With Others Spec / Widget.

`[](#__codelineno-45-1) { [](#__codelineno-45-2)   "widget_type": "bar_chart", [](#__codelineno-45-3)   "title": "Name based sort in Bar", [](#__codelineno-45-4)   "duration_hours": 1080, [](#__codelineno-45-5)   "stream": "main", [](#__codelineno-45-6)   "ts_column": "timestamp", [](#__codelineno-45-7)   "extra_filter": null, [](#__codelineno-45-8)   "column": "count_", [](#__codelineno-45-9)   "agg": "sum", [](#__codelineno-45-10)   "group_by": [ [](#__codelineno-45-11)     "city" [](#__codelineno-45-12)   ], [](#__codelineno-45-13)     "others_spec": { [](#__codelineno-45-14)     "label": "other state", [](#__codelineno-45-15)     "Country": { [](#__codelineno-45-16)     "name_based_limit": true [](#__codelineno-45-17)     } [](#__codelineno-45-18)   }, [](#__codelineno-45-19)   "type": "int", [](#__codelineno-45-20)   "min_width": 6, [](#__codelineno-45-21)   "height": 6, [](#__codelineno-45-22)   "max_width": 6 [](#__codelineno-45-23) }`

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

`[](#__codelineno-46-1) { [](#__codelineno-46-2)   "widget_type": "bar_chart", [](#__codelineno-46-3)   "title": "Month based Bar", [](#__codelineno-46-4)   "duration_hours": 10800, [](#__codelineno-46-5)   "stream": "trail", [](#__codelineno-46-6)   "ts_column": "timestamp", [](#__codelineno-46-7)   "extra_filter": null, [](#__codelineno-46-8)   "column": "count_", [](#__codelineno-46-9)   "agg": "value_count", [](#__codelineno-46-10)   "group_by": [ [](#__codelineno-46-11)     "Months" [](#__codelineno-46-12)   ], [](#__codelineno-46-13)   "groups_meta": { [](#__codelineno-46-14)     "type": "month" [](#__codelineno-46-15)   }, [](#__codelineno-46-16)   "type": "int", [](#__codelineno-46-17)   "limit": 15, [](#__codelineno-46-18)   "min_width": 6, [](#__codelineno-46-19)   "height": 5, [](#__codelineno-46-20)   "max_width": 6 [](#__codelineno-46-21) }`

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

`[](#__codelineno-47-1) { [](#__codelineno-47-2)   "title": "FIXED_BAR_WIDTH_CHART", [](#__codelineno-47-3)   "widget_type": "fixed_bar_width_chart", [](#__codelineno-47-4)   "stream": "people_custom_timestamp", [](#__codelineno-47-5)   "chartProperties": { [](#__codelineno-47-6)     "barThickness": 100 [](#__codelineno-47-7)   }, [](#__codelineno-47-8)   "ts_column": "timestamp", [](#__codelineno-47-9)   "column": "age", [](#__codelineno-47-10)   "agg": "value_count", [](#__codelineno-47-11)   "group_by": [ [](#__codelineno-47-12)     "city" [](#__codelineno-47-13)   ] [](#__codelineno-47-14) }`

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

`[](#__codelineno-48-1) { [](#__codelineno-48-2)   "title": "Multi Bar Chart Example", [](#__codelineno-48-3)   "widget_type": "multi_bar_chart", [](#__codelineno-48-4)   "stream": "rda_microservice_traces", [](#__codelineno-48-5)   "extra_filter": "request_type != 'are-you-there'", [](#__codelineno-48-6)   "ts_column": "timestamp", [](#__codelineno-48-7)   "chartProperties": { [](#__codelineno-48-8)     "yAxisLabel": "Duration", [](#__codelineno-48-9)     "xAxisLabel": "Services", [](#__codelineno-48-10)     "stacked": true, [](#__codelineno-48-11)     "legendLocation": "right", [](#__codelineno-48-12)     "orientation": "vertical" [](#__codelineno-48-13)   }, [](#__codelineno-48-14)   "duration_hours": 24, [](#__codelineno-48-15)   "group_by": [ [](#__codelineno-48-16)     "request_type", [](#__codelineno-48-17)     "destination" [](#__codelineno-48-18)   ], [](#__codelineno-48-19)   "column": "duration", [](#__codelineno-48-20)   "agg": "value_count", [](#__codelineno-48-21)   "type": "int", [](#__codelineno-48-22)   "widget_id": "172919af" [](#__codelineno-48-23) }`

![Dashboard_Multi_Bar_Chart_Example](https://bot-docs.cloudfabrix.io/images/dashboards/Multi_Bar_Chart.png)

#### ****3.5.2 Multi Bar Chart with extra filter****

Below is a sample configuration of Multi Bar Chart / Widget with `extra_filter`

`[](#__codelineno-49-1) { [](#__codelineno-49-2)   "title": "Multi Bar Chart Example", [](#__codelineno-49-3)   "widget_type": "multi_bar_chart", [](#__codelineno-49-4)   "stream": "rda_microservice_traces", [](#__codelineno-49-5)   "extra_filter": "source in ['scheduler', 'alert-ingester']", [](#__codelineno-49-6)   "ts_column": "timestamp", [](#__codelineno-49-7)   "chartProperties": { [](#__codelineno-49-8)     "yAxisLabel": "Duration", [](#__codelineno-49-9)     "xAxisLabel": "Services", [](#__codelineno-49-10)     "stacked": true, [](#__codelineno-49-11)     "legendLocation": "right", [](#__codelineno-49-12)     "orientation": "vertical" [](#__codelineno-49-13)   }, [](#__codelineno-49-14)   "duration_hours": 24, [](#__codelineno-49-15)   "group_by": [ [](#__codelineno-49-16)     "request_type", [](#__codelineno-49-17)     "destination" [](#__codelineno-49-18)   ], [](#__codelineno-49-19)   "column": "duration", [](#__codelineno-49-20)   "agg": "value_count", [](#__codelineno-49-21)   "type": "int", [](#__codelineno-49-22)   "widget_id": "172919af" [](#__codelineno-49-23) }`

![Dashboard_Multi_Bar_Chart_scheduler_alert-ingester](https://bot-docs.cloudfabrix.io/images/dashboards/scheduler_alert-ingester.png)

#### ****3.5.3 Multi Bar Chart Without Filters****

`[](#__codelineno-50-1) { [](#__codelineno-50-2)   "title": "Multi Bar Chart Example", [](#__codelineno-50-3)   "widget_type": "multi_bar_chart", [](#__codelineno-50-4)   "stream": "rda_microservice_traces", [](#__codelineno-50-5)   "ts_column": "timestamp", [](#__codelineno-50-6)   "chartProperties": { [](#__codelineno-50-7)     "yAxisLabel": "Duration", [](#__codelineno-50-8)     "xAxisLabel": "Services", [](#__codelineno-50-9)     "stacked": true, [](#__codelineno-50-10)     "legendLocation": "right", [](#__codelineno-50-11)     "orientation": "vertical" [](#__codelineno-50-12)   }, [](#__codelineno-50-13)   "duration_hours": 24, [](#__codelineno-50-14)   "group_by": [ [](#__codelineno-50-15)     "request_type", [](#__codelineno-50-16)     "destination" [](#__codelineno-50-17)   ], [](#__codelineno-50-18)   "column": "duration", [](#__codelineno-50-19)   "agg": "value_count", [](#__codelineno-50-20)   "type": "int", [](#__codelineno-50-21)   "widget_id": "172919af" [](#__codelineno-50-22) }`

![Dashboard_Multi_Bar_Chart_Without_Filters](https://bot-docs.cloudfabrix.io/images/dashboards/Multi_Bar_Chart_Without_Filters.png)

#### ****3.5.4 Multi Bar Chart With Formatting Options****

Below is a sample configuration of Multi Bar Chart With Formatting Options.

`[](#__codelineno-51-1) { [](#__codelineno-51-2)   "title": "Multi Bar Chart Format", [](#__codelineno-51-3)   "widget_type": "multi_bar_chart", [](#__codelineno-51-4)   "stream": "main", [](#__codelineno-51-5)   "ts_column": "timestamp", [](#__codelineno-51-6)   "group_by": [ [](#__codelineno-51-7)     "city", [](#__codelineno-51-8)     "name" [](#__codelineno-51-9)   ], [](#__codelineno-51-10)   "formatting": { [](#__codelineno-51-11)     "notation": "compact", [](#__codelineno-51-12)     "style": "unit", [](#__codelineno-51-13)     "unit": "percent", [](#__codelineno-51-14)     "signDisplay": "always" [](#__codelineno-51-15)   }, [](#__codelineno-51-16)   "chartProperties": { [](#__codelineno-51-17)     "yAxisLabel": null, [](#__codelineno-51-18)     "xAxisLabel": "name", [](#__codelineno-51-19)     "stacked": false, [](#__codelineno-51-20)     "legendLocation": "right", [](#__codelineno-51-21)     "orientation": "vertical", [](#__codelineno-51-22)     "barThickness": 100 [](#__codelineno-51-23)   }, [](#__codelineno-51-24)   "column": "donation", [](#__codelineno-51-25)   "agg": "sum", [](#__codelineno-51-26)   "type": "str" [](#__codelineno-51-27) }`

![Dashboard_Multi_Bar_Formatting](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_formatting.png)

#### ****3.5.5 Multi Bar Chart Showing Top N Values****

Below is a sample configuration of Bar Chart Showing Top N Values.

`[](#__codelineno-52-1) { [](#__codelineno-52-2)   "title": "Multi Bar Chart", [](#__codelineno-52-3)   "widget_type": "multi_bar_chart", [](#__codelineno-52-4)   "stream": "donationn", [](#__codelineno-52-5)   "ts_column": "timestamp", [](#__codelineno-52-6)   "group_by": [ [](#__codelineno-52-7)     "city", [](#__codelineno-52-8)     "name" [](#__codelineno-52-9)   ], [](#__codelineno-52-10)   "chartProperties": { [](#__codelineno-52-11)     "yAxisLabel": null, [](#__codelineno-52-12)     "xAxisLabel": "name", [](#__codelineno-52-13)     "stacked": false, [](#__codelineno-52-14)     "legendLocation": "right", [](#__codelineno-52-15)     "orientation": "vertical" [](#__codelineno-52-16)   }, [](#__codelineno-52-17)   "others_spec": { [](#__codelineno-52-18)   "limit": 2, [](#__codelineno-52-19)   "show_others": false [](#__codelineno-52-20)   }, [](#__codelineno-52-21)   "column": "donation", [](#__codelineno-52-22)   "agg": "sum", [](#__codelineno-52-23)   "type": "str" [](#__codelineno-52-24) }`

![Dashboard_Multibar_Limit](https://bot-docs.cloudfabrix.io/images/dashboards/multibar_limit.png)

#### ****3.5.6 Multi Bar Chart Using Others Spec****

Below is a sample configuration of Multi Bar Chart Using Others Spec

`[](#__codelineno-53-1) { [](#__codelineno-53-2)   "title": "Multi Bar Chart Format desc Based", [](#__codelineno-53-3)   "widget_type": "multi_bar_chart", [](#__codelineno-53-4)   "stream": "main", [](#__codelineno-53-5)   "ts_column": "timestamp", [](#__codelineno-53-6)   "group_by": [ [](#__codelineno-53-7)     "city", [](#__codelineno-53-8)     "name" [](#__codelineno-53-9)   ], [](#__codelineno-53-10)   "formatting": { [](#__codelineno-53-11)     "notation": "compact", [](#__codelineno-53-12)     "style": "unit", [](#__codelineno-53-13)     "unit": "percent" [](#__codelineno-53-14)   }, [](#__codelineno-53-15)   "chartProperties": { [](#__codelineno-53-16)     "yAxisLabel": null, [](#__codelineno-53-17)     "xAxisLabel": "name", [](#__codelineno-53-18)     "stacked": false, [](#__codelineno-53-19)     "legendLocation": "right", [](#__codelineno-53-20)     "orientation": "vertical" [](#__codelineno-53-21)   }, [](#__codelineno-53-22)   "descending_order": true, [](#__codelineno-53-23)   "others_spec": { [](#__codelineno-53-24)     "limit": 3, [](#__codelineno-53-25)     "label": "Other Names", [](#__codelineno-53-26)     "show_others": true, [](#__codelineno-53-27)     "city": { [](#__codelineno-53-28)       "largest": false, [](#__codelineno-53-29)       "name_based_limit": false [](#__codelineno-53-30)     }, [](#__codelineno-53-31)     "name": { [](#__codelineno-53-32)       "largest": false, [](#__codelineno-53-33)       "name_based_limit": false [](#__codelineno-53-34)     } [](#__codelineno-53-35)   }, [](#__codelineno-53-36)   "column": "donation", [](#__codelineno-53-37)   "agg": "sum", [](#__codelineno-53-38)   "type": "str" [](#__codelineno-53-39) }`

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

`[](#__codelineno-54-1) { [](#__codelineno-54-2)   "widget_type": "multi_bar_chart", [](#__codelineno-54-3)   "title": "Week based Multibar", [](#__codelineno-54-4)   "duration_hours": 10800, [](#__codelineno-54-5)   "stream": "mw1", [](#__codelineno-54-6)   "ts_column": "timestamp", [](#__codelineno-54-7)   "extra_filter": null, [](#__codelineno-54-8)   "column": "count_", [](#__codelineno-54-9)   "agg": "value_count", [](#__codelineno-54-10)   "group_by": [ [](#__codelineno-54-11)     "Week", [](#__codelineno-54-12)     "date" [](#__codelineno-54-13)   ], [](#__codelineno-54-14)   "groups_meta": { [](#__codelineno-54-15)     "type": "date" [](#__codelineno-54-16)   }, [](#__codelineno-54-17)   "series_meta": { [](#__codelineno-54-18)     "type": "weekday" [](#__codelineno-54-19)   }, [](#__codelineno-54-20)   "type": "int", [](#__codelineno-54-21)   "min_width": 6, [](#__codelineno-54-22)   "height": 5, [](#__codelineno-54-23)   "max_width": 6 [](#__codelineno-54-24) }`

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

`[](#__codelineno-55-1) { [](#__codelineno-55-2)   "title": "Mixed Chart", [](#__codelineno-55-3)   "widget_type": "mixed_chart_buckets", [](#__codelineno-55-4)   "axis": [ [](#__codelineno-55-5)     { [](#__codelineno-55-6)       "stream": "people_custom_timestamp", [](#__codelineno-55-7)       "ts_column": "timestamp", [](#__codelineno-55-8)       "chartProperties": { [](#__codelineno-55-9)         "yAxisLabel": "Same name people in City", [](#__codelineno-55-10)         "xAxisLabel": "Name", [](#__codelineno-55-11)         "stacked": false, [](#__codelineno-55-12)         "legendLocation": "right", [](#__codelineno-55-13)         "orientation": "vertical" [](#__codelineno-55-14)       }, [](#__codelineno-55-15)       "group_by": [ [](#__codelineno-55-16)         "city", [](#__codelineno-55-17)         "name" [](#__codelineno-55-18)       ], [](#__codelineno-55-19)       "column": "_RDA_Id", [](#__codelineno-55-20)       "agg": "value_count", [](#__codelineno-55-21)       "type": "int" [](#__codelineno-55-22)     }, [](#__codelineno-55-23)     { [](#__codelineno-55-24)       "stream": "people_custom_timestamp", [](#__codelineno-55-25)       "ts_column": "timestamp", [](#__codelineno-55-26)       "chartProperties": { [](#__codelineno-55-27)         "yAxisLabel": "Number of people in Age group", [](#__codelineno-55-28)         "xAxisLabel": "Name" [](#__codelineno-55-29)       }, [](#__codelineno-55-30)       "group_by": [ [](#__codelineno-55-31)         "count_", [](#__codelineno-55-32)         "name" [](#__codelineno-55-33)       ], [](#__codelineno-55-34)       "group_label": "People in Age group", [](#__codelineno-55-35)       "column": "_RDA_Id", [](#__codelineno-55-36)       "agg": "value_count", [](#__codelineno-55-37)       "type": "int", [](#__codelineno-55-38)       "graph_type": "line" [](#__codelineno-55-39)     } [](#__codelineno-55-40)   ] [](#__codelineno-55-41) }`

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

`[](#__codelineno-56-1) { [](#__codelineno-56-2)   "title": "Time Series using Stream Example", [](#__codelineno-56-3)   "widget_type": "timeseries", [](#__codelineno-56-4)   "stream": "rdaf_services_logs", [](#__codelineno-56-5)   "ts_column": "timestamp", [](#__codelineno-56-6)   "max_width": 12, [](#__codelineno-56-7)   "height": 3, [](#__codelineno-56-8)   "min_width": 12, [](#__codelineno-56-9)   "chartProperties": { [](#__codelineno-56-10)     "yAxisLabel": "Count", [](#__codelineno-56-11)     "xAxisLabel": null, [](#__codelineno-56-12)     "legendLocation": "bottom" [](#__codelineno-56-13)   }, [](#__codelineno-56-14)   "interval": "15Min", [](#__codelineno-56-15)   "group_by": [ [](#__codelineno-56-16)     "log_severity" [](#__codelineno-56-17)   ], [](#__codelineno-56-18)   "series_spec": [ [](#__codelineno-56-19)     { [](#__codelineno-56-20)       "column": "log_severity", [](#__codelineno-56-21)       "agg": "value_count", [](#__codelineno-56-22)       "type": "int" [](#__codelineno-56-23)     } [](#__codelineno-56-24)   ] [](#__codelineno-56-25) }`

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/Line_Graphchart.png)

#### ****3.7.1 Line Graph / Timeseries Chart With Fix Time Window****

Below is a sample configuration of Line Graph/Timeseries Chart With Fix Time Window / Widget.

`[](#__codelineno-57-1) { [](#__codelineno-57-2)   "title": "Time Series using Stream Example", [](#__codelineno-57-3)   "widget_type": "timeseries", [](#__codelineno-57-4)   "stream": "rda_microservice_traces", [](#__codelineno-57-5)   "ts_column": "timestamp", [](#__codelineno-57-6)   "max_width": 12, [](#__codelineno-57-7)   "height": 3, [](#__codelineno-57-8)   "min_width": 12, [](#__codelineno-57-9)   "fixTimeWindow": true, [](#__codelineno-57-10)   "chartProperties": { [](#__codelineno-57-11)     "yAxisLabel": "Count", [](#__codelineno-57-12)     "xAxisLabel": null, [](#__codelineno-57-13)     "legendLocation": "bottom" [](#__codelineno-57-14)   }, [](#__codelineno-57-15)   "interval": "auto", [](#__codelineno-57-16)   "group_by": [ [](#__codelineno-57-17)     "request_type" [](#__codelineno-57-18)   ], [](#__codelineno-57-19)   "series_spec": [ [](#__codelineno-57-20)     { [](#__codelineno-57-21)       "column": "request_type", [](#__codelineno-57-22)       "agg": "value_count", [](#__codelineno-57-23)       "type": "int" [](#__codelineno-57-24)     } [](#__codelineno-57-25)   ], [](#__codelineno-57-26)   "widget_id": "121762cf" [](#__codelineno-57-27) }`

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/fixtime_window.png)

**User Selected Duration**

![Dashboard_Line_Graph_chart](https://bot-docs.cloudfabrix.io/images/dashboards/fixtime_userdesired.png)

#### ****3.7.2 Line Graph / Timeseries Chart with Interval and Interval Type****

Below is a sample configuration of Line Graph/Timeseries Chart with Interval and Interval Type

`[](#__codelineno-58-1) { [](#__codelineno-58-2)   "title": "Time Series (Calendar Interval month)", [](#__codelineno-58-3)   "widget_type": "timeseries", [](#__codelineno-58-4)   "stream": "covid19", [](#__codelineno-58-5)   "ts_column": "timestamp", [](#__codelineno-58-6)   "width": 12, [](#__codelineno-58-7)   "height": 6, [](#__codelineno-58-8)   "chartProperties": { [](#__codelineno-58-9)     "yAxisLabel": "Confirmed Count", [](#__codelineno-58-10)     "xAxisLabel": "months", [](#__codelineno-58-11)     "legendLocation": "bottom" [](#__codelineno-58-12)   }, [](#__codelineno-58-13)   "interval": "month", [](#__codelineno-58-14)   "interval_type": "calendar", [](#__codelineno-58-15)   "series_spec": [ [](#__codelineno-58-16)     { [](#__codelineno-58-17)       "column": "Confirmed", [](#__codelineno-58-18)       "agg": "value_count", [](#__codelineno-58-19)       "type": "int" [](#__codelineno-58-20)     } [](#__codelineno-58-21)   ] [](#__codelineno-58-22) }`

![Dashboard_Interval_Type](https://bot-docs.cloudfabrix.io/images/dashboards/interval_type.png)

#### ****3.7.3 Line Graph / Timeseries Chart with Gap Interval****

[Gap Interval - Keep](#__tabbed_9_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Keep / Widget configuration

`[](#__codelineno-59-1) { [](#__codelineno-59-2)   "title": "Time Series (Gap Interval Keep)", [](#__codelineno-59-3)   "widget_type": "timeseries", [](#__codelineno-59-4)   "gap_interval": "keep", [](#__codelineno-59-5)   "stream": "covi19", [](#__codelineno-59-6)   "ts_column": "timestamp", [](#__codelineno-59-7)   "max_width": 12, [](#__codelineno-59-8)   "height": 3, [](#__codelineno-59-9)   "min_width": 12, [](#__codelineno-59-10)   "chartProperties": { [](#__codelineno-59-11)     "yAxisLabel": "Count", [](#__codelineno-59-12)     "xAxisLabel": "Timestamp", [](#__codelineno-59-13)     "legendLocation": "bottom" [](#__codelineno-59-14)   }, [](#__codelineno-59-15)   "interval": "5m", [](#__codelineno-59-16)   "series_spec": [ [](#__codelineno-59-17)     { [](#__codelineno-59-18)       "column": "Confirmed", [](#__codelineno-59-19)       "agg": "sum", [](#__codelineno-59-20)       "type": "int" [](#__codelineno-59-21)     } [](#__codelineno-59-22)   ] [](#__codelineno-59-23) }`

![Dashboard_Keep_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/keep_chart.png)

[Gap Interval - Join](#__tabbed_10_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Join / Widget configuration

`[](#__codelineno-60-1) { [](#__codelineno-60-2)   "title": "Time Series (Gap Interval Join)", [](#__codelineno-60-3)   "widget_type": "timeseries", [](#__codelineno-60-4)   "gap_interval": "join", [](#__codelineno-60-5)   "stream": "covi19", [](#__codelineno-60-6)   "ts_column": "timestamp", [](#__codelineno-60-7)   "max_width": 12, [](#__codelineno-60-8)   "height": 3, [](#__codelineno-60-9)   "min_width": 12, [](#__codelineno-60-10)   "chartProperties": { [](#__codelineno-60-11)     "yAxisLabel": "Count", [](#__codelineno-60-12)     "xAxisLabel": "Timestamp", [](#__codelineno-60-13)     "legendLocation": "bottom" [](#__codelineno-60-14)   }, [](#__codelineno-60-15)   "interval": "5m", [](#__codelineno-60-16)   "series_spec": [ [](#__codelineno-60-17)     { [](#__codelineno-60-18)       "column": "Confirmed", [](#__codelineno-60-19)       "agg": "sum", [](#__codelineno-60-20)       "type": "int" [](#__codelineno-60-21)     } [](#__codelineno-60-22)   ] [](#__codelineno-60-23) }`

![Dashboard_Join_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/join_chart.png)

[Gap Interval - Skip](#__tabbed_11_1)

Below is a sample configuration of Line Graph/Timeseries Chart with Gap Interval - Skip / Widget configuration

`[](#__codelineno-61-1) { [](#__codelineno-61-2)   "title": "Time Series (Gap Interval Skip)", [](#__codelineno-61-3)   "widget_type": "timeseries", [](#__codelineno-61-4)   "gap_interval": "skip", [](#__codelineno-61-5)   "stream": "covi19", [](#__codelineno-61-6)   "ts_column": "timestamp", [](#__codelineno-61-7)   "max_width": 12, [](#__codelineno-61-8)   "height": 3, [](#__codelineno-61-9)   "min_width": 12, [](#__codelineno-61-10)   "chartProperties": { [](#__codelineno-61-11)     "yAxisLabel": "Count", [](#__codelineno-61-12)     "xAxisLabel": "Timestamp", [](#__codelineno-61-13)     "legendLocation": "bottom" [](#__codelineno-61-14)   }, [](#__codelineno-61-15)   "interval": "5m", [](#__codelineno-61-16)   "series_spec": [ [](#__codelineno-61-17)     { [](#__codelineno-61-18)       "column": "Confirmed", [](#__codelineno-61-19)       "agg": "sum", [](#__codelineno-61-20)       "type": "int" [](#__codelineno-61-21)     } [](#__codelineno-61-22)   ] [](#__codelineno-61-23) }`

![Dashboard_Skip_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/skip_chart.png)

#### ****3.7.4 Line Graph / Timeseries Chart with Color Map****

Below is a sample configuration of Line Graph/Timeseries Chart with Color Map / Widget configuration

[Example One](#__tabbed_12_1)

`[](#__codelineno-62-1) { [](#__codelineno-62-2)   "title": "Time Series", [](#__codelineno-62-3)   "widget_type": "timeseries", [](#__codelineno-62-4)   "gap_interval": "keep", [](#__codelineno-62-5)   "stream": "people_custom_timestamp", [](#__codelineno-62-6)   "ts_column": "timestamp", [](#__codelineno-62-7)   "width": 4, [](#__codelineno-62-8)   "height": 4, [](#__codelineno-62-9)   "chartProperties": { [](#__codelineno-62-10)     "yAxisLabel": "Count", [](#__codelineno-62-11)     "xAxisLabel": null, [](#__codelineno-62-12)     "legendLocation": "bottom" [](#__codelineno-62-13)   }, [](#__codelineno-62-14)   "interval": "24h", [](#__codelineno-62-15)   "series_spec": [ [](#__codelineno-62-16)     { [](#__codelineno-62-17)       "column": "name", [](#__codelineno-62-18)       "agg": "value_count", [](#__codelineno-62-19)       "type": "int" [](#__codelineno-62-20)     } [](#__codelineno-62-21)   ], [](#__codelineno-62-22)   "group_by": "city", [](#__codelineno-62-23)   "style": { [](#__codelineno-62-24)     "color-map": { [](#__codelineno-62-25)       "Austin": [ [](#__codelineno-62-26)         "#E91E63", [](#__codelineno-62-27)         "#ffffff" [](#__codelineno-62-28)       ], [](#__codelineno-62-29)       "Portland": [ [](#__codelineno-62-30)         "#FF5722", [](#__codelineno-62-31)         "#ffffff" [](#__codelineno-62-32)       ], [](#__codelineno-62-33)       "San Francisco": [ [](#__codelineno-62-34)         "#FFC107", [](#__codelineno-62-35)         "#ffffff" [](#__codelineno-62-36)       ], [](#__codelineno-62-37)       "Hyderabad": [ [](#__codelineno-62-38)         "#3F51B5", [](#__codelineno-62-39)         "#ffffff" [](#__codelineno-62-40)       ] [](#__codelineno-62-41)     } [](#__codelineno-62-42)   } [](#__codelineno-62-43) }`

![Dashboard_Color_Map](https://bot-docs.cloudfabrix.io/images/dashboards/color_map.png)

[Example Two](#__tabbed_13_1)

**Color Map with Label**

Below is a sample configuration of Line Graph Chart with Color Map with Label / Widget configuration

`[](#__codelineno-63-1) { [](#__codelineno-63-2)   "title": "Time Series (Color-map with label)", [](#__codelineno-63-3)   "widget_type": "timeseries", [](#__codelineno-63-4)   "gap_interval": "keep", [](#__codelineno-63-5)   "stream": "people_custom_timestamp", [](#__codelineno-63-6)   "ts_column": "timestamp", [](#__codelineno-63-7)   "width": 4, [](#__codelineno-63-8)   "height": 4, [](#__codelineno-63-9)   "chartProperties": { [](#__codelineno-63-10)     "yAxisLabel": "Count", [](#__codelineno-63-11)     "xAxisLabel": null, [](#__codelineno-63-12)     "legendLocation": "bottom" [](#__codelineno-63-13)   }, [](#__codelineno-63-14)   "interval": "24h", [](#__codelineno-63-15)   "series_spec": [ [](#__codelineno-63-16)     { [](#__codelineno-63-17)       "column": "name", [](#__codelineno-63-18)       "agg": "value_count", [](#__codelineno-63-19)       "type": "int", [](#__codelineno-63-20)       "label": "City" [](#__codelineno-63-21)     } [](#__codelineno-63-22)   ], [](#__codelineno-63-23)   "group_by": "city", [](#__codelineno-63-24)   "style": { [](#__codelineno-63-25)     "color-map": { [](#__codelineno-63-26)       "City (Portland)": [ [](#__codelineno-63-27)         "#E91E63", [](#__codelineno-63-28)         "#ffffff" [](#__codelineno-63-29)       ], [](#__codelineno-63-30)       "City (San Francisco)": [ [](#__codelineno-63-31)         "#FF5722", [](#__codelineno-63-32)         "#ffffff" [](#__codelineno-63-33)       ], [](#__codelineno-63-34)       "City (Hyderabad)": [ [](#__codelineno-63-35)         "#FFC107", [](#__codelineno-63-36)         "#ffffff" [](#__codelineno-63-37)       ], [](#__codelineno-63-38)       "City (Austin)": [ [](#__codelineno-63-39)         "#3F51B5", [](#__codelineno-63-40)         "#ffffff" [](#__codelineno-63-41)       ] [](#__codelineno-63-42)     } [](#__codelineno-63-43)   } [](#__codelineno-63-44) }`

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

`[](#__codelineno-64-1) { [](#__codelineno-64-2)   "widget_type": "timeseries", [](#__codelineno-64-3)   "title": "Alert Trend", [](#__codelineno-64-4)   "stream": "oia-alerts-stream", [](#__codelineno-64-5)   "min_width": 9, [](#__codelineno-64-6)   "height": 3, [](#__codelineno-64-7)   "max_width": 9, [](#__codelineno-64-8)   "interval": "auto", [](#__codelineno-64-9)   "ts_column": "a_created_ts", [](#__codelineno-64-10)   "fixTimeWindow": true, [](#__codelineno-64-11)   "group_by": [ [](#__codelineno-64-12)     "a_severity" [](#__codelineno-64-13)   ], [](#__codelineno-64-14)   "alert_markers": [{ [](#__codelineno-64-15)     "stream": "oia-alerts-stream", [](#__codelineno-64-16)     "ts_column": "a_created_ts", [](#__codelineno-64-17)     "message_column": "a_message", [](#__codelineno-64-18)     "extra_filter": "a_severity is 'CRITICAL'", [](#__codelineno-64-19)     "severity_column": "a_severity" [](#__codelineno-64-20)   }], [](#__codelineno-64-21)   "series_spec": [ [](#__codelineno-64-22)     { [](#__codelineno-64-23)       "agg": "sum", [](#__codelineno-64-24)       "column": "count_", [](#__codelineno-64-25)       "type": "int", [](#__codelineno-64-26)       "label": "Alert Count" [](#__codelineno-64-27)     } [](#__codelineno-64-28)   ], [](#__codelineno-64-29)   "chartProperties": { [](#__codelineno-64-30)     "yAxisLabel": "Alert Count", [](#__codelineno-64-31)     "xAxisLabel": null, [](#__codelineno-64-32)     "legendLocation": "right" [](#__codelineno-64-33)   } [](#__codelineno-64-34) }`

![Dashboard_Alert_Markers](https://bot-docs.cloudfabrix.io/images/dashboards/alert_markers.png)

#### ****3.7.6 Line Graph / Timeseries Chart with Auto Intervals****

Note

This widget computes aggregation based on Time Range selected (Not based on Data Availability)

Below is a sample configuration of Line Graph / Timeseries Chart with Auto Intervals / Widget configuration

`[](#__codelineno-65-1) { [](#__codelineno-65-2)   "title": "Time Series using Stream Example", [](#__codelineno-65-3)   "widget_type": "timeseries", [](#__codelineno-65-4)   "stream": "company_alerts", [](#__codelineno-65-5)   "ts_column": "timestamp", [](#__codelineno-65-6)   "max_width": 12, [](#__codelineno-65-7)   "height": 7, [](#__codelineno-65-8)   "min_width": 12, [](#__codelineno-65-9)   "chartProperties": { [](#__codelineno-65-10)     "yAxisLabel": "Count", [](#__codelineno-65-11)     "xAxisLabel": null, [](#__codelineno-65-12)     "legendLocation": "bottom" [](#__codelineno-65-13)   }, [](#__codelineno-65-14)   "fixTimeWindow": true, [](#__codelineno-65-15)   "interval": "auto", [](#__codelineno-65-16)   "series_spec": [ [](#__codelineno-65-17)     { [](#__codelineno-65-18)       "column": "count_", [](#__codelineno-65-19)       "agg": "sum", [](#__codelineno-65-20)       "type": "int" [](#__codelineno-65-21)     } [](#__codelineno-65-22)   ] [](#__codelineno-65-23) }`

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

`[](#__codelineno-66-1) { [](#__codelineno-66-2)   "title": "Event Flow Graph", [](#__codelineno-66-3)   "widget_type": "dataflow", [](#__codelineno-66-4)   "chartProperties": { [](#__codelineno-66-5)     "layoutDirection": "tb", [](#__codelineno-66-6)     "userZoomingEnabled": false, [](#__codelineno-66-7)     "hasToolbar": false [](#__codelineno-66-8)   }, [](#__codelineno-66-9)   "output": { [](#__codelineno-66-10)     "formatter": "DescriptiveCountFormatter", [](#__codelineno-66-11)     "stream": "dli-log-stats", [](#__codelineno-66-12)     "extra_filter": "mode is 'processed' and device not in ['ERROR','INFO','WARNING']", [](#__codelineno-66-13)     "ts_column": "timestamp", [](#__codelineno-66-14)     "duration_hours": 720, [](#__codelineno-66-15)     "group_by": [ [](#__codelineno-66-16)       "device" [](#__codelineno-66-17)     ], [](#__codelineno-66-18)     "column": "count", [](#__codelineno-66-19)     "agg": "sum", [](#__codelineno-66-20)     "type": "int" [](#__codelineno-66-21)   }, [](#__codelineno-66-22)   "input": { [](#__codelineno-66-23)     "formatter": "DescriptiveCountFormatter", [](#__codelineno-66-24)     "stream": "dli-log-stats", [](#__codelineno-66-25)     "extra_filter": "mode is 'ingested' and device not in ['ERROR','INFO','WARNING']", [](#__codelineno-66-26)     "ts_column": "timestamp", [](#__codelineno-66-27)     "duration_hours": 720, [](#__codelineno-66-28)     "group_by": [ [](#__codelineno-66-29)       "device" [](#__codelineno-66-30)     ], [](#__codelineno-66-31)     "column": "count", [](#__codelineno-66-32)     "agg": "sum", [](#__codelineno-66-33)     "type": "int", [](#__codelineno-66-34)     "widget_id": "da16c98b" [](#__codelineno-66-35)   }, [](#__codelineno-66-36)   "widget_id": "66b927bc" [](#__codelineno-66-37) }`

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

`[](#__codelineno-67-1) { [](#__codelineno-67-2)   "title": "Ocean", [](#__codelineno-67-3)   "widget_type": "image", [](#__codelineno-67-4)   "max_width": 6, [](#__codelineno-67-5)   "min_width": 4, [](#__codelineno-67-6)   "height": 6, [](#__codelineno-67-7)   "imageUrl": "https://images.unsplash.com/photo-1657883509333-0b1d2ee75853?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=704&q=80", [](#__codelineno-67-8)   "widget_id": "6e8df419" [](#__codelineno-67-9) }`

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

`[](#__codelineno-68-1) { [](#__codelineno-68-2)   "name": "navigator", [](#__codelineno-68-3)   "label": "Navigator", [](#__codelineno-68-4)   "description": "Navigator", [](#__codelineno-68-5)   "enabled": true, [](#__codelineno-68-6)   "dashboard_style": "auto", [](#__codelineno-68-7)   "dashboard_type": "template", [](#__codelineno-68-8)   "short_label": "Stack", [](#__codelineno-68-9)   "context_label_id": "stack_name", [](#__codelineno-68-10)   "dashboard_folder": "Default", [](#__codelineno-68-11)   "version": "23.10.02.1", [](#__codelineno-68-12)   "dashboard_filters": { [](#__codelineno-68-13)     "time_filter": true, [](#__codelineno-68-14)     "default_time_filter_labels": [ [](#__codelineno-68-15)       "Last 1 month" [](#__codelineno-68-16)     ] [](#__codelineno-68-17)   }, [](#__codelineno-68-18)   "template_variables": { [](#__codelineno-68-19)     "CITY": { [](#__codelineno-68-20)       "contextId": [ [](#__codelineno-68-21)         "navigatorSelectionContexts", [](#__codelineno-68-22)         "secondaryListSelection", [](#__codelineno-68-23)         "city" [](#__codelineno-68-24)       ] [](#__codelineno-68-25)     }, [](#__codelineno-68-26)     "NAME": { [](#__codelineno-68-27)       "contextId": [ [](#__codelineno-68-28)         "navigatorSelectionContexts", [](#__codelineno-68-29)         "secondaryListSelection", [](#__codelineno-68-30)         "name" [](#__codelineno-68-31)       ] [](#__codelineno-68-32)     } [](#__codelineno-68-33)   }, [](#__codelineno-68-34)   "navigation_dashboards": { [](#__codelineno-68-35)     "tree_data": { [](#__codelineno-68-36)       "column_name": "city", [](#__codelineno-68-37)       "pstream_name": "main", [](#__codelineno-68-38)       "cfxql_query": "timestamp is after -720d " [](#__codelineno-68-39)     }, [](#__codelineno-68-40)     "tree_detail": { [](#__codelineno-68-41)       "display_column": "name", [](#__codelineno-68-42)       "pstream_name": "main", [](#__codelineno-68-43)       "cfxql_query": "timestamp is after -720d " [](#__codelineno-68-44)     }, [](#__codelineno-68-45)     "showNodeIcon": false, [](#__codelineno-68-46)     "showSearchBox": true [](#__codelineno-68-47)   }, [](#__codelineno-68-48)   "dashboard_sections": [ [](#__codelineno-68-49)     { [](#__codelineno-68-50)       "title": "Node Details", [](#__codelineno-68-51)       "widgets": [ [](#__codelineno-68-52)         { [](#__codelineno-68-53)           "title": "Details", [](#__codelineno-68-54)           "widget_type": "tabular", [](#__codelineno-68-55)           "extra_filter": "(name is '{{NAME}}') and (city is '{{CITY}}')", [](#__codelineno-68-56)           "stream": "main", [](#__codelineno-68-57)           "max_width": 12, [](#__codelineno-68-58)           "height": 8, [](#__codelineno-68-59)           "min_width": 12, [](#__codelineno-68-60)           "widget_id": "cc9a9626" [](#__codelineno-68-61)         } [](#__codelineno-68-62)       ] [](#__codelineno-68-63)     } [](#__codelineno-68-64)   ], [](#__codelineno-68-65)   "saved_time": "2023-11-02T08:25:25.205071" [](#__codelineno-68-66) }`

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

`[](#__codelineno-69-1) { [](#__codelineno-69-2)   "widget_type": "shaded_chart_multisource", [](#__codelineno-69-3)   "title": "Forecasting and Anomaly Detection", [](#__codelineno-69-4)   "show-markers": true, [](#__codelineno-69-5)   "max_width": 12, [](#__codelineno-69-6)   "min_width": 12, [](#__codelineno-69-7)   "height": 8, [](#__codelineno-69-8)   "chartProperties": { [](#__codelineno-69-9)     "yAxisLabel": "Value", [](#__codelineno-69-10)     "xAxisLabel": "Time" [](#__codelineno-69-11)   }, [](#__codelineno-69-12)   "sources": [ [](#__codelineno-69-13)     { [](#__codelineno-69-14)       "type": "train", [](#__codelineno-69-15)       "downsample": false, [](#__codelineno-69-16)       "stream": "regression-train-output", [](#__codelineno-69-17)       "ts_column": "timestamp", [](#__codelineno-69-18)       "baseline_column": "baseline", [](#__codelineno-69-19)       "anomalies_column": "anomalies", [](#__codelineno-69-20)       "predicted_column": "predicted", [](#__codelineno-69-21)       "predicted_anomalies": "predicted_anomalies", [](#__codelineno-69-22)       "upperBound_column": "upperBound", [](#__codelineno-69-23)       "lowerBound_column": "lowerBound", [](#__codelineno-69-24)       "duration_hours": 1000000, [](#__codelineno-69-25)       "synchronized-group": 0 [](#__codelineno-69-26)     }, [](#__codelineno-69-27)     { [](#__codelineno-69-28)       "type": "predict", [](#__codelineno-69-29)       "downsample": false, [](#__codelineno-69-30)       "stream": "regression-live-output", [](#__codelineno-69-31)       "ts_column": "live_timestamp", [](#__codelineno-69-32)       "baseline_column": "baseline", [](#__codelineno-69-33)       "anomalies_column": "anomaly", [](#__codelineno-69-34)       "predicted_column": "predicted", [](#__codelineno-69-35)       "predicted_anomalies": "predicted_anomalies", [](#__codelineno-69-36)       "upperBound_column": "upperBound", [](#__codelineno-69-37)       "lowerBound_column": "lowerBound", [](#__codelineno-69-38)       "duration_hours": 1000000, [](#__codelineno-69-39)       "synchronized-group": 0 [](#__codelineno-69-40)     } [](#__codelineno-69-41)   ], [](#__codelineno-69-42)   "widget_id": "7a134625" [](#__codelineno-69-43) }`

![Dashboard_Shaded_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/shaded_chart.png)

[Example Two](#__tabbed_14_1)

`[](#__codelineno-70-1) { [](#__codelineno-70-2)   "widget_type": "shaded_chart_multisource", [](#__codelineno-70-3)   "title": "Forecasting and Anomaly Detection (Memory Usage - 10.95.125.90)", [](#__codelineno-70-4)   "show-markers": true, [](#__codelineno-70-5)   "max_width": 12, [](#__codelineno-70-6)   "min_width": 12, [](#__codelineno-70-7)   "height": 8, [](#__codelineno-70-8)   "chartProperties": { [](#__codelineno-70-9)     "yAxisLabel": "Memory Usage (bytes)", [](#__codelineno-70-10)     "xAxisLabel": "Time" [](#__codelineno-70-11)   }, [](#__codelineno-70-12)   "sources": [ [](#__codelineno-70-13)     { [](#__codelineno-70-14)       "type": "train", [](#__codelineno-70-15)       "downsample": false, [](#__codelineno-70-16)       "stream": "regression-train-output", [](#__codelineno-70-17)       "extra_filter": "status is 'Success'", [](#__codelineno-70-18)       "ts_column": "timestamp", [](#__codelineno-70-19)       "baseline_column": "baseline", [](#__codelineno-70-20)       "anomalies_column": "anomalies", [](#__codelineno-70-21)       "predicted_column": "predicted", [](#__codelineno-70-22)       "predicted_anomalies": "predicted_anomalies", [](#__codelineno-70-23)       "upperBound_column": "upperBound", [](#__codelineno-70-24)       "lowerBound_column": "lowerBound", [](#__codelineno-70-25)       "duration_hours": 1000000, [](#__codelineno-70-26)       "synchronized-group": 0 [](#__codelineno-70-27)     }, [](#__codelineno-70-28)     { [](#__codelineno-70-29)       "type": "predict", [](#__codelineno-70-30)       "downsample": false, [](#__codelineno-70-31)       "stream": "regression-live-output", [](#__codelineno-70-32)       "extra_filter": "status is 'Success'", [](#__codelineno-70-33)       "ts_column": "live_timestamp", [](#__codelineno-70-34)       "baseline_column": "baseline", [](#__codelineno-70-35)       "anomalies_column": "anomaly", [](#__codelineno-70-36)       "predicted_column": "predicted", [](#__codelineno-70-37)       "predicted_anomalies": "predicted_anomalies", [](#__codelineno-70-38)       "upperBound_column": "upperBound", [](#__codelineno-70-39)       "lowerBound_column": "lowerBound", [](#__codelineno-70-40)       "duration_hours": 1000000, [](#__codelineno-70-41)       "synchronized-group": 0 [](#__codelineno-70-42)     } [](#__codelineno-70-43)   ], [](#__codelineno-70-44)   "widget_id": "7a134625" [](#__codelineno-70-45) }`

![Dashboard_Shaded_Chart](https://bot-docs.cloudfabrix.io/images/dashboards/shaded_chart1.png)

### ****3.12 Label Chart****

This widget can be used as a label Chart inside the dashboard section.

Please refer the below **configuration parameter** table which are used to configure Label Chart widget within the dashboard.

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `label` | yes | Specify the content in the html format ex.heading in `<h1> to <h6>` |
| `widget_type` | yes | Specify the widget\_type as label |

[Example One](#__tabbed_15_1)

`[](#__codelineno-71-1) { [](#__codelineno-71-2)   "widget_type": "label", [](#__codelineno-71-3)   "label": "<div style='text-align:center;width:100%;'><h1><a style='text-decoration:none;color:#0066ff;' target='_blank'> Welcome to RDAF Community </a></h1></div>" [](#__codelineno-71-4) }`

![Label_Widget](https://bot-docs.cloudfabrix.io/images/dashboards/label_widget.png)

[Example Two](#__tabbed_16_1)

`[](#__codelineno-72-1) { [](#__codelineno-72-2)   "widget_type": "label", [](#__codelineno-72-3)   "min_width": 4, [](#__codelineno-72-4)   "height": 3, [](#__codelineno-72-5)   "max_width": 4, [](#__codelineno-72-6)   "sorting": [ [](#__codelineno-72-7)     { [](#__codelineno-72-8)       "endTime": "desc" [](#__codelineno-72-9)     } [](#__codelineno-72-10)   ], [](#__codelineno-72-11)   "label": "{% set all_latest_data = {} %}\r\n{% for latest in latest_end_time %}\r\n    {% set last_updated_time = latest.get(\"label\") %}\r\n    {% set _ = all_latest_data.update({ \"latest\": last_updated_time }) or \"\" %}\r\n{% endfor %}\r\n\r\n<br><br> <center><h4> Last Collected at </h4></center><br><center><h3>{{all_latest_data.get(\"latest\")}}</h3></center>", [](#__codelineno-72-12)   "segments": [ [](#__codelineno-72-13)     { [](#__codelineno-72-14)       "stream": "main", [](#__codelineno-72-15)       "variable": "latest_end_time", [](#__codelineno-72-16)       "ts_column": "timestamp", [](#__codelineno-72-17)       "agg": "value_count", [](#__codelineno-72-18)       "group_by": "endTime", [](#__codelineno-72-19)       "column": "city" [](#__codelineno-72-20)     } [](#__codelineno-72-21)   ] [](#__codelineno-72-22) }`

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

`[](#__codelineno-73-1) { [](#__codelineno-73-2)   "widget_type": "connectivity_chart", [](#__codelineno-73-3)   "title": "People", [](#__codelineno-73-4)   "stream": "main", [](#__codelineno-73-5)   "ts_column": "timestamp", [](#__codelineno-73-6)   "min_width": 12, [](#__codelineno-73-7)   "max_width": 12, [](#__codelineno-73-8)   "height": 8, [](#__codelineno-73-9)   "agg": "sum", [](#__codelineno-73-10)   "agg_column": "count_", [](#__codelineno-73-11)   "columns": [ [](#__codelineno-73-12)     { [](#__codelineno-73-13)       "group_by": "city", [](#__codelineno-73-14)       "label": "For City", [](#__codelineno-73-15)       "color-map": { [](#__codelineno-73-16)         "Portland": [ [](#__codelineno-73-17)           "#ef5350", [](#__codelineno-73-18)           "#ffffff" [](#__codelineno-73-19)         ], [](#__codelineno-73-20)         "San Francisco": [ [](#__codelineno-73-21)           "#FF9800", [](#__codelineno-73-22)           "#ffffff" [](#__codelineno-73-23)         ], [](#__codelineno-73-24)         "Austin": [ [](#__codelineno-73-25)           "#8BC34A", [](#__codelineno-73-26)           "#ffffff" [](#__codelineno-73-27)         ], [](#__codelineno-73-28)         "Hyderabad": [ [](#__codelineno-73-29)           "#1E88E5", [](#__codelineno-73-30)           "#ffffff" [](#__codelineno-73-31)         ] [](#__codelineno-73-32)       } [](#__codelineno-73-33)     }, [](#__codelineno-73-34)     { [](#__codelineno-73-35)       "group_by": "name", [](#__codelineno-73-36)       "label": "For Name", [](#__codelineno-73-37)       "color-map": { [](#__codelineno-73-38)         "James": [ [](#__codelineno-73-39)           "#ef5350", [](#__codelineno-73-40)           "#ffffff" [](#__codelineno-73-41)         ] [](#__codelineno-73-42)       } [](#__codelineno-73-43)     }, [](#__codelineno-73-44)     { [](#__codelineno-73-45)       "group_by": "age", [](#__codelineno-73-46)       "label": "For Age" [](#__codelineno-73-47)     }, [](#__codelineno-73-48)     { [](#__codelineno-73-49)       "group_by": "donation", [](#__codelineno-73-50)       "label": "For Donation" [](#__codelineno-73-51)     } [](#__codelineno-73-52)   ] [](#__codelineno-73-53) }`

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

`[](#__codelineno-74-1) { [](#__codelineno-74-2) "widget_type": "markdown", [](#__codelineno-74-3) "folder": "markdown_syntax", [](#__codelineno-74-4) "objectName": "markdown" [](#__codelineno-74-5) }`

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

`[](#__codelineno-75-1) { [](#__codelineno-75-2)   "name": "covi-library-1", [](#__codelineno-75-3)   "label": "Test Library for Sample Widgets", [](#__codelineno-75-4)   "enabled": "false", [](#__codelineno-75-5)   "description": "Sample library", [](#__codelineno-75-6)   "library": { [](#__codelineno-75-7)     "widgets": { [](#__codelineno-75-8)       "covi_counter": { [](#__codelineno-75-9)         "title": "Deaths", [](#__codelineno-75-10)         "min_width": 6, [](#__codelineno-75-11)         "height": 4, [](#__codelineno-75-12)         "max_width": 6, [](#__codelineno-75-13)         "widget_type": "custom_counter", [](#__codelineno-75-14)         "formatter": "DescriptiveCountFormatter", [](#__codelineno-75-15)         "stream": "covid19", [](#__codelineno-75-16)         "ts_column": "timestamp", [](#__codelineno-75-17)         "duration_hours": 9600, [](#__codelineno-75-18)         "sparkline": { [](#__codelineno-75-19)           "interval": "360h" [](#__codelineno-75-20)         }, [](#__codelineno-75-21)         "style": { [](#__codelineno-75-22)           "color-list": [ [](#__codelineno-75-23)             "#8e24aa" [](#__codelineno-75-24)           ] [](#__codelineno-75-25)         }, [](#__codelineno-75-26)         "column": "Deaths", [](#__codelineno-75-27)         "agg": "sum" [](#__codelineno-75-28)       } [](#__codelineno-75-29)     } [](#__codelineno-75-30)   } [](#__codelineno-75-31) [](#__codelineno-75-32) }`

**Library Being Called from the above Definition**

Below is a sample configuration of Library Being Called from the above Definition / Widget.

`[](#__codelineno-76-1) { [](#__codelineno-76-2)   "name": "covi-library-2", [](#__codelineno-76-3)   "label": "Library Widget Covid", [](#__codelineno-76-4)   "description": "Covid data", [](#__codelineno-76-5)   "enabled": "false", [](#__codelineno-76-6)   "dashboard_type": "dashboard", [](#__codelineno-76-7)   "dashboard_folder": "Default", [](#__codelineno-76-8)   "import": [ [](#__codelineno-76-9)     { [](#__codelineno-76-10)       "from": "covi-library-1", [](#__codelineno-76-11)       "as": "lib1" [](#__codelineno-76-12)     } [](#__codelineno-76-13)   ], [](#__codelineno-76-14)   "dashboard_sections": [ [](#__codelineno-76-15)     { [](#__codelineno-76-16)       "title": "SECTION 1", [](#__codelineno-76-17)       "show_filter": true, [](#__codelineno-76-18)       "widgets": [ [](#__codelineno-76-19)         { [](#__codelineno-76-20)           "extends": "self:covi_count", [](#__codelineno-76-21)           "widget_id": "e1201b84" [](#__codelineno-76-22)         }, [](#__codelineno-76-23)         { [](#__codelineno-76-24)           "extends": "lib1:covi_counter", [](#__codelineno-76-25)           "widget_id": "c3ac1d59" [](#__codelineno-76-26)         } [](#__codelineno-76-27)       ] [](#__codelineno-76-28)     } [](#__codelineno-76-29)   ], [](#__codelineno-76-30)   "library": { [](#__codelineno-76-31)     "widgets": { [](#__codelineno-76-32)       "covi_count": { [](#__codelineno-76-33)         "title": "Confirmed", [](#__codelineno-76-34)         "min_width": 6, [](#__codelineno-76-35)         "height": 4, [](#__codelineno-76-36)         "max_width": 6, [](#__codelineno-76-37)         "widget_type": "custom_counter", [](#__codelineno-76-38)         "formatter": "DescriptiveCountFormatter", [](#__codelineno-76-39)         "stream": "covid19", [](#__codelineno-76-40)         "ts_column": "timestamp", [](#__codelineno-76-41)         "duration_hours": 8990, [](#__codelineno-76-42)         "sparkline": { [](#__codelineno-76-43)           "interval": "360h" [](#__codelineno-76-44)         }, [](#__codelineno-76-45)         "style": { [](#__codelineno-76-46)           "color-list": [ [](#__codelineno-76-47)             "#008000" [](#__codelineno-76-48)           ] [](#__codelineno-76-49)         }, [](#__codelineno-76-50)         "column": "Confirmed", [](#__codelineno-76-51)         "agg": "sum" [](#__codelineno-76-52)       } [](#__codelineno-76-53)     } [](#__codelineno-76-54)   }  [](#__codelineno-76-55) }`

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

`[](#__codelineno-77-1) "stream_query_mapping": { [](#__codelineno-77-2)         "oia-incidents-stream": { [](#__codelineno-77-3)             "timestamp": "i_created_ts", [](#__codelineno-77-4)             "a_severity": null [](#__codelineno-77-5)         }, [](#__codelineno-77-6)         "oia-alerts-stream": { [](#__codelineno-77-7)             "timestamp": "a_created_ts", [](#__codelineno-77-8)             "i_priority_label": null [](#__codelineno-77-9)         } [](#__codelineno-77-10)     }`

Info

By adding above section to any dashboard, it will alter queries sent to OpenSearch based which stream it is querying. If filter contains column "timestamp", replace it with i\_created\_ts If the filter contains a\_severity column skip that specific filter in the query (rest of the conditions will still apply)

[Example Definition](#__tabbed_17_1)

`[](#__codelineno-78-1) { [](#__codelineno-78-2)   "name": "oia-trends----rv", [](#__codelineno-78-3)   "label": "Trends", [](#__codelineno-78-4)   "description": "Trends", [](#__codelineno-78-5)   "version": "23.8.9", [](#__codelineno-78-6)   "enabled": true, [](#__codelineno-78-7)   "debug": true, [](#__codelineno-78-8)   "dashboard_style": "auto", [](#__codelineno-78-9)   "dashboard_type": "template", [](#__codelineno-78-10)   "stream_query_mapping": { [](#__codelineno-78-11)     "oia-incidents-stream": { [](#__codelineno-78-12)       "timestamp": "i_created_ts", [](#__codelineno-78-13)       "a_severity": null [](#__codelineno-78-14)     }, [](#__codelineno-78-15)     "oia-alerts-stream": { [](#__codelineno-78-16)       "timestamp": "a_created_ts", [](#__codelineno-78-17)       "i_priority_label": null [](#__codelineno-78-18)     } [](#__codelineno-78-19)   }, [](#__codelineno-78-20)   "dashboard_filters": { [](#__codelineno-78-21)     "time_filter": true, [](#__codelineno-78-22)     "default_time_filter_non_removable": true, [](#__codelineno-78-23)     "show_default_time_filter": true, [](#__codelineno-78-24)     "additional_datetime_column_filters": [ [](#__codelineno-78-25)       { [](#__codelineno-78-26)         "id": "timestamp", [](#__codelineno-78-27)         "label": "Timestamp" [](#__codelineno-78-28)       } [](#__codelineno-78-29)     ], [](#__codelineno-78-30)     "default_time_filter_labels": [ [](#__codelineno-78-31)       "Last 24 hours" [](#__codelineno-78-32)     ], [](#__codelineno-78-33)     "group_filters": [ [](#__codelineno-78-34)       { [](#__codelineno-78-35)         "stream": "oia-alerts-stream", [](#__codelineno-78-36)         "title": "Source", [](#__codelineno-78-37)         "group_by": [ [](#__codelineno-78-38)           "a_source_systemname" [](#__codelineno-78-39)         ], [](#__codelineno-78-40)         "ts_column": "a_updated_ts", [](#__codelineno-78-41)         "agg": "value_count", [](#__codelineno-78-42)         "column": "a_id", [](#__codelineno-78-43)         "type": "str" [](#__codelineno-78-44)       } [](#__codelineno-78-45)     ] [](#__codelineno-78-46)   }, [](#__codelineno-78-47)   "dashboard_sections": [ [](#__codelineno-78-48)     { [](#__codelineno-78-49)       "title": "Trends", [](#__codelineno-78-50)       "show_filter": true, [](#__codelineno-78-51)       "widgets": [ [](#__codelineno-78-52)         { [](#__codelineno-78-53)           "widget_type": "timeseries", [](#__codelineno-78-54)           "title": "Alert Trend", [](#__codelineno-78-55)           "stream": "oia-alerts-stream", [](#__codelineno-78-56)           "min_width": 9, [](#__codelineno-78-57)           "height": 3, [](#__codelineno-78-58)           "max_width": 9, [](#__codelineno-78-59)           "interval": "auto", [](#__codelineno-78-60)           "ts_column": "a_created_ts", [](#__codelineno-78-61)           "fixTimeWindow": true, [](#__codelineno-78-62)           "group_by": [ [](#__codelineno-78-63)             "a_severity" [](#__codelineno-78-64)           ], [](#__codelineno-78-65)           "alert_markers": [{ [](#__codelineno-78-66)             "stream": "oia-incidents-stream", [](#__codelineno-78-67)             "ts_column": "i_created_ts", [](#__codelineno-78-68)             "message_column": "i_summary", [](#__codelineno-78-69)             "extra_filter": "i_priority_label is 'Critical'", [](#__codelineno-78-70)             "severity_column": "i_priority_label" [](#__codelineno-78-71)           } [](#__codelineno-78-72)           ], [](#__codelineno-78-73)           "series_spec": [ [](#__codelineno-78-74)             { [](#__codelineno-78-75)               "agg": "sum", [](#__codelineno-78-76)               "column": "count_", [](#__codelineno-78-77)               "type": "int", [](#__codelineno-78-78)               "label": "Alert Count" [](#__codelineno-78-79)             } [](#__codelineno-78-80)           ], [](#__codelineno-78-81)           "chartProperties": { [](#__codelineno-78-82)             "yAxisLabel": "Alert Count", [](#__codelineno-78-83)             "xAxisLabel": null, [](#__codelineno-78-84)             "legendLocation": "right", [](#__codelineno-78-85)             "options": { [](#__codelineno-78-86)               "elements": { [](#__codelineno-78-87)                 "line": { [](#__codelineno-78-88)                   "borderWidth": 1 [](#__codelineno-78-89)                 }, [](#__codelineno-78-90)                 "point": { [](#__codelineno-78-91)                   "radius": 0, [](#__codelineno-78-92)                   "hitRadius": 3, [](#__codelineno-78-93)                   "hoverRadius": 2 [](#__codelineno-78-94)                 } [](#__codelineno-78-95)               } [](#__codelineno-78-96)             } [](#__codelineno-78-97)           }, [](#__codelineno-78-98)           "widget_id": "e146eb95" [](#__codelineno-78-99)         }, [](#__codelineno-78-100)         { [](#__codelineno-78-101)           "widget_type": "timeseries multi markers", [](#__codelineno-78-102)           "title": "Incident Trend", [](#__codelineno-78-103)           "stream": "oia-incidents-stream", [](#__codelineno-78-104)           "min_width": 9, [](#__codelineno-78-105)           "height": 3, [](#__codelineno-78-106)           "max_width": 9, [](#__codelineno-78-107)           "interval": "auto", [](#__codelineno-78-108)           "ts_column": "timestamp", [](#__codelineno-78-109)           "fixTimeWindow": true, [](#__codelineno-78-110)           "group_by": [ [](#__codelineno-78-111)             "i_priority_label" [](#__codelineno-78-112)           ], [](#__codelineno-78-113)           "alert_markers": [ [](#__codelineno-78-114)             { [](#__codelineno-78-115)               "stream": "oia-alerts-stream", [](#__codelineno-78-116)               "ts_column": "timestamp", [](#__codelineno-78-117)               "message_column": "a_message", [](#__codelineno-78-118)               "extra_filter": "a_severity is 'CRITICAL'", [](#__codelineno-78-119)               "severity_column": "a_severity" [](#__codelineno-78-120)             } [](#__codelineno-78-121)           ], [](#__codelineno-78-122)           "series_spec": [ [](#__codelineno-78-123)             { [](#__codelineno-78-124)               "agg": "sum", [](#__codelineno-78-125)               "column": "count_", [](#__codelineno-78-126)               "type": "int", [](#__codelineno-78-127)               "label": "Incident Count" [](#__codelineno-78-128)             } [](#__codelineno-78-129)           ], [](#__codelineno-78-130)           "chartProperties": { [](#__codelineno-78-131)             "yAxisLabel": "Incident Count", [](#__codelineno-78-132)             "xAxisLabel": null, [](#__codelineno-78-133)             "legendLocation": "right", [](#__codelineno-78-134)             "options": { [](#__codelineno-78-135)               "elements": { [](#__codelineno-78-136)                 "line": { [](#__codelineno-78-137)                   "borderWidth": 1 [](#__codelineno-78-138)                 }, [](#__codelineno-78-139)                 "point": { [](#__codelineno-78-140)                   "radius": 0, [](#__codelineno-78-141)                   "hitRadius": 3, [](#__codelineno-78-142)                   "hoverRadius": 2 [](#__codelineno-78-143)                 } [](#__codelineno-78-144)               } [](#__codelineno-78-145)             } [](#__codelineno-78-146)           }, [](#__codelineno-78-147)           "widget_id": "17004a8e" [](#__codelineno-78-148)         } [](#__codelineno-78-149)       ] [](#__codelineno-78-150)     } [](#__codelineno-78-151)   ], [](#__codelineno-78-152)   "saved_time": "2023-12-13T04:47:16.762883" [](#__codelineno-78-153) }`

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

`[](#__codelineno-79-1) rdac dashboard generate --stream STREAM –name NAME –publish`

[Example Output](#__tabbed_18_1)

`[](#__codelineno-80-1) rdac dashboard generate --stream covi19 --name dya_covi --publish`

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

`[](#__codelineno-81-1) "template_variables": { [](#__codelineno-81-2)   "CITY": { [](#__codelineno-81-3)     "contextId": [ [](#__codelineno-81-4)       "navigatorSelectionContexts", [](#__codelineno-81-5)       "secondaryListSelection", [](#__codelineno-81-6)       "city" [](#__codelineno-81-7)     ] [](#__codelineno-81-8)   }, [](#__codelineno-81-9)   "NAME": { [](#__codelineno-81-10)     "contextId": [ [](#__codelineno-81-11)       "navigatorSelectionContexts", [](#__codelineno-81-12)       "secondaryListSelection", [](#__codelineno-81-13)       "name" [](#__codelineno-81-14)     ] [](#__codelineno-81-15)   } [](#__codelineno-81-16) }`

Important

Template Variable should be passed only when dashboard type is set to Template

[Calling Template Variable](#__tabbed_19_1)

`[](#__codelineno-82-1) { [](#__codelineno-82-2)   "title": "Details", [](#__codelineno-82-3)   "widget_type": "tabular", [](#__codelineno-82-4)   "extra_filter": "(name is '{{NAME}}') and (city is '{{CITY}}')", [](#__codelineno-82-5)   "stream": "main", [](#__codelineno-82-6)   "max_width": 12, [](#__codelineno-82-7)   "height": 8, [](#__codelineno-82-8)   "min_width": 12, [](#__codelineno-82-9)   "widget_id": "cc9a9626" [](#__codelineno-82-10) }`

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

`[](#__codelineno-83-1) { [](#__codelineno-83-2) "type": "UPDATE_PSTREAM", [](#__codelineno-83-3) "pstreamName": "main", [](#__codelineno-83-4) "operation": "UPDATE", [](#__codelineno-83-5) "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" [](#__codelineno-83-6) }`

[Example for Pipeline Run](#__tabbed_21_1)

`[](#__codelineno-84-1) { [](#__codelineno-84-2) "type": "RUN_PIPELINE", [](#__codelineno-84-3) "pipelineName": "simple_pipeline", [](#__codelineno-84-4) "isSync": true [](#__codelineno-84-5) }`

The pipeline used in the below example is simple\_pipeline, It will get the input from the dashboard to the temp-dataset

The content of the pipeline is as below.

`[](#__codelineno-85-1) @dm:empty      [](#__codelineno-85-2) → @exec:get-input [](#__codelineno-85-3) → @dm:save name=”temp-dataset”`

Below is a sample configuration which performs actions using Dynamic Forms.

`[](#__codelineno-86-1) { [](#__codelineno-86-2)   "name": "Dynamic forms", [](#__codelineno-86-3)   "label": "Dynamic forms", [](#__codelineno-86-4)   "is_template": false, [](#__codelineno-86-5)   "description": "Dynamic forms", [](#__codelineno-86-6)   "version": "24.01.03.1", [](#__codelineno-86-7)   "enabled": true, [](#__codelineno-86-8)   "dashboard_type": "dashboard", [](#__codelineno-86-9)   "dashboard_folder": "Default", [](#__codelineno-86-10)   "dashboard_style": "auto", [](#__codelineno-86-11)   "stream": "main", [](#__codelineno-86-12)   "dashboard_sections": [ [](#__codelineno-86-13)     { [](#__codelineno-86-14)       "title": "Student App", [](#__codelineno-86-15)       "widgets": [ [](#__codelineno-86-16)         { [](#__codelineno-86-17)           "title": "Registration Details", [](#__codelineno-86-18)           "widget_type": "tabular", [](#__codelineno-86-19)           "stream": "main", [](#__codelineno-86-20)           "timebased": false, [](#__codelineno-86-21)           "remote_searchable": true, [](#__codelineno-86-22)           "ts_column": "timestamp", [](#__codelineno-86-23)           "paginated": true, [](#__codelineno-86-24)           "height": 10, [](#__codelineno-86-25)           "min_wdith": 12, [](#__codelineno-86-26)           "columns": { [](#__codelineno-86-27)             "name": { [](#__codelineno-86-28)               "title": "Name", [](#__codelineno-86-29)               "key": true [](#__codelineno-86-30)             }, [](#__codelineno-86-31)             "city": { [](#__codelineno-86-32)               "title": "City", [](#__codelineno-86-33)               "key": true [](#__codelineno-86-34)             }, [](#__codelineno-86-35)             "age": { [](#__codelineno-86-36)               "title": "Age", [](#__codelineno-86-37)               "key": true [](#__codelineno-86-38)             }, [](#__codelineno-86-39)             "Month": { [](#__codelineno-86-40)               "title": "Month", [](#__codelineno-86-41)               "key": true [](#__codelineno-86-42)             }, [](#__codelineno-86-43)             "donations": { [](#__codelineno-86-44)               "title": "Donations", [](#__codelineno-86-45)               "key": true [](#__codelineno-86-46)             }, [](#__codelineno-86-47)             "_RDA_Id": { [](#__codelineno-86-48)               "title": "RDA ID", [](#__codelineno-86-49)               "key": true, [](#__codelineno-86-50)               "visible": false [](#__codelineno-86-51)             } [](#__codelineno-86-52)           }, [](#__codelineno-86-53)           "actions": [ [](#__codelineno-86-54)             { [](#__codelineno-86-55)               "permission": "rda:github:view", [](#__codelineno-86-56)               "title": "Onboard Details", [](#__codelineno-86-57)               "type": "POPUP_FORM", [](#__codelineno-86-58)               "selectionType": "NONE", [](#__codelineno-86-59)               "identifier": "saas-service-action:userdashboard-add-yaml", [](#__codelineno-86-60)               "api-endpoint": { [](#__codelineno-86-61)                 "service-name": "saas-reports", [](#__codelineno-86-62)                 "methodName": "getForm", [](#__codelineno-86-63)                 "stringified-params": true, [](#__codelineno-86-64)                 "parse-output": false, [](#__codelineno-86-65)                 "params": [ [](#__codelineno-86-66)                   { [](#__codelineno-86-67)                     "formId": "rda.saas.dynamic.form", [](#__codelineno-86-68)                     "formDefinition": { [](#__codelineno-86-69)                       "id": "rda.saas.dynamic.form", [](#__codelineno-86-70)                       "refreshRequired": true, [](#__codelineno-86-71)                       "formFieldList": [ [](#__codelineno-86-72)                         { [](#__codelineno-86-73)                           "help": "User Name", [](#__codelineno-86-74)                           "dataType": "string", [](#__codelineno-86-75)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-76)                           "required": true, [](#__codelineno-86-77)                           "editable": true, [](#__codelineno-86-78)                           "label": "User Name", [](#__codelineno-86-79)                           "hidden": false, [](#__codelineno-86-80)                           "fieldId": "name" [](#__codelineno-86-81)                         }, [](#__codelineno-86-82)                         { [](#__codelineno-86-83)                           "help": "City Name", [](#__codelineno-86-84)                           "dataType": "string", [](#__codelineno-86-85)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-86)                           "required": true, [](#__codelineno-86-87)                           "editable": true, [](#__codelineno-86-88)                           "label": "City Name", [](#__codelineno-86-89)                           "hidden": false, [](#__codelineno-86-90)                           "fieldId": "city" [](#__codelineno-86-91)                         }, [](#__codelineno-86-92)                         { [](#__codelineno-86-93)                           "help": "Age", [](#__codelineno-86-94)                           "required": false, [](#__codelineno-86-95)                           "editable": true, [](#__codelineno-86-96)                           "label": "Age", [](#__codelineno-86-97)                           "hidden": false, [](#__codelineno-86-98)                           "fieldId": "age", [](#__codelineno-86-99)                           "dataType": "INT", [](#__codelineno-86-100)                           "controlType": "INT", [](#__codelineno-86-101)                           "defaultValue": false [](#__codelineno-86-102)                         }, [](#__codelineno-86-103)                         { [](#__codelineno-86-104)                           "help": "Month", [](#__codelineno-86-105)                           "required": false, [](#__codelineno-86-106)                           "editable": true, [](#__codelineno-86-107)                           "label": "Month", [](#__codelineno-86-108)                           "hidden": false, [](#__codelineno-86-109)                           "fieldId": "Month", [](#__codelineno-86-110)                           "dataType": "string", [](#__codelineno-86-111)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-112)                           "defaultValue": false [](#__codelineno-86-113)                         }, [](#__codelineno-86-114)                         { [](#__codelineno-86-115)                           "help": "Donations", [](#__codelineno-86-116)                           "required": false, [](#__codelineno-86-117)                           "editable": true, [](#__codelineno-86-118)                           "label": "Donations", [](#__codelineno-86-119)                           "hidden": false, [](#__codelineno-86-120)                           "fieldId": "donations", [](#__codelineno-86-121)                           "dataType": "INT", [](#__codelineno-86-122)                           "controlType": "INT", [](#__codelineno-86-123)                           "defaultValue": false [](#__codelineno-86-124)                         } [](#__codelineno-86-125)                       ] [](#__codelineno-86-126)                     }, [](#__codelineno-86-127)                     "actions": [ [](#__codelineno-86-128)                       { [](#__codelineno-86-129)                         "type": "UPDATE_PSTREAM", [](#__codelineno-86-130)                         "pstreamName": "main" [](#__codelineno-86-131)                       }, [](#__codelineno-86-132)                       { [](#__codelineno-86-133)                         "type": "RUN_PIPELINE", [](#__codelineno-86-134)                         "pipelineName": "simple_pipeline", [](#__codelineno-86-135)                         "isSync": true [](#__codelineno-86-136)                       } [](#__codelineno-86-137)                     ] [](#__codelineno-86-138)                   } [](#__codelineno-86-139)                 ] [](#__codelineno-86-140)               } [](#__codelineno-86-141)             }, [](#__codelineno-86-142)             { [](#__codelineno-86-143)               "permission": "rda:github:view", [](#__codelineno-86-144)               "title": "Edit User", [](#__codelineno-86-145)               "type": "POPUP_FORM", [](#__codelineno-86-146)               "selectionType": "SINGLE", [](#__codelineno-86-147)               "identifier": "saas-service-action:userdashboard-add-yaml", [](#__codelineno-86-148)               "api-endpoint": { [](#__codelineno-86-149)                 "service-name": "saas-reports", [](#__codelineno-86-150)                 "methodName": "getForm", [](#__codelineno-86-151)                 "stringified-params": true, [](#__codelineno-86-152)                 "parse-output": false, [](#__codelineno-86-153)                 "params": [ [](#__codelineno-86-154)                   { [](#__codelineno-86-155)                     "formId": "rda.saas.dynamic.form", [](#__codelineno-86-156)                     "formDefinition": { [](#__codelineno-86-157)                       "id": "rda.saas.dynamic.form", [](#__codelineno-86-158)                       "refreshRequired": true, [](#__codelineno-86-159)                       "formFieldList": [ [](#__codelineno-86-160)                         { [](#__codelineno-86-161)                           "help": "User Name", [](#__codelineno-86-162)                           "dataType": "string", [](#__codelineno-86-163)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-164)                           "required": true, [](#__codelineno-86-165)                           "editable": true, [](#__codelineno-86-166)                           "label": "User Name", [](#__codelineno-86-167)                           "hidden": false, [](#__codelineno-86-168)                           "fieldId": "name" [](#__codelineno-86-169)                         }, [](#__codelineno-86-170)                         { [](#__codelineno-86-171)                           "help": "City Name", [](#__codelineno-86-172)                           "dataType": "string", [](#__codelineno-86-173)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-174)                           "required": true, [](#__codelineno-86-175)                           "editable": true, [](#__codelineno-86-176)                           "label": "City Name", [](#__codelineno-86-177)                           "hidden": false, [](#__codelineno-86-178)                           "fieldId": "city" [](#__codelineno-86-179)                         }, [](#__codelineno-86-180)                         { [](#__codelineno-86-181)                           "help": "Age", [](#__codelineno-86-182)                           "required": false, [](#__codelineno-86-183)                           "editable": true, [](#__codelineno-86-184)                           "label": "Age", [](#__codelineno-86-185)                           "hidden": false, [](#__codelineno-86-186)                           "fieldId": "age", [](#__codelineno-86-187)                           "dataType": "INT", [](#__codelineno-86-188)                           "controlType": "INT", [](#__codelineno-86-189)                           "defaultValue": false [](#__codelineno-86-190)                         }, [](#__codelineno-86-191)                         { [](#__codelineno-86-192)                           "help": "Month", [](#__codelineno-86-193)                           "required": false, [](#__codelineno-86-194)                           "editable": true, [](#__codelineno-86-195)                           "label": "Month", [](#__codelineno-86-196)                           "hidden": false, [](#__codelineno-86-197)                           "fieldId": "Month", [](#__codelineno-86-198)                           "dataType": "string", [](#__codelineno-86-199)                           "controlType": "TEXT_FIELD", [](#__codelineno-86-200)                           "defaultValue": false [](#__codelineno-86-201)                         }, [](#__codelineno-86-202)                         { [](#__codelineno-86-203)                           "help": "Donations", [](#__codelineno-86-204)                           "required": false, [](#__codelineno-86-205)                           "editable": true, [](#__codelineno-86-206)                           "label": "Donations", [](#__codelineno-86-207)                           "hidden": false, [](#__codelineno-86-208)                           "fieldId": "donations", [](#__codelineno-86-209)                           "dataType": "INT", [](#__codelineno-86-210)                           "controlType": "INT", [](#__codelineno-86-211)                           "defaultValue": false [](#__codelineno-86-212)                         } [](#__codelineno-86-213)                       ] [](#__codelineno-86-214)                     }, [](#__codelineno-86-215)                     "actions": [ [](#__codelineno-86-216)                       { [](#__codelineno-86-217)                         "type": "UPDATE_PSTREAM", [](#__codelineno-86-218)                         "pstreamName": "main", [](#__codelineno-86-219)                         "operation": "UPDATE", [](#__codelineno-86-220)                         "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" [](#__codelineno-86-221)                       }, [](#__codelineno-86-222)                       { [](#__codelineno-86-223)                         "type": "RUN_PIPELINE", [](#__codelineno-86-224)                         "pipelineName": "simple_pipeline", [](#__codelineno-86-225)                         "isSync": true [](#__codelineno-86-226)                       } [](#__codelineno-86-227)                     ] [](#__codelineno-86-228)                   } [](#__codelineno-86-229)                 ] [](#__codelineno-86-230)               } [](#__codelineno-86-231)             }, [](#__codelineno-86-232)             { [](#__codelineno-86-233)               "permission": "rda:github:view", [](#__codelineno-86-234)               "title": "Delete User", [](#__codelineno-86-235)               "type": "POPUP_FORM", [](#__codelineno-86-236)               "selectionType": "SINGLE", [](#__codelineno-86-237)               "identifier": "saas-service-action:userdashboard-add-yaml", [](#__codelineno-86-238)               "api-endpoint": { [](#__codelineno-86-239)                 "service-name": "saas-reports", [](#__codelineno-86-240)                 "methodName": "getForm", [](#__codelineno-86-241)                 "stringified-params": true, [](#__codelineno-86-242)                 "parse-output": false, [](#__codelineno-86-243)                 "params": [ [](#__codelineno-86-244)                   { [](#__codelineno-86-245)                     "formId": "rda.saas.dynamic.form", [](#__codelineno-86-246)                     "formActionList": { [](#__codelineno-86-247)                       "formActions": [ [](#__codelineno-86-248)                         { [](#__codelineno-86-249)                           "identifier": "Submit", [](#__codelineno-86-250)                           "actionLabel": "Delete" [](#__codelineno-86-251)                         } [](#__codelineno-86-252)                       ] [](#__codelineno-86-253)                     }, [](#__codelineno-86-254)                     "formDefinition": { [](#__codelineno-86-255)                       "id": "rda.saas.dynamic.form", [](#__codelineno-86-256)                       "refreshRequired": true, [](#__codelineno-86-257)                       "formFieldList": [ [](#__codelineno-86-258)                         { [](#__codelineno-86-259)                           "help": "Do you want to delete the onboarded User?", [](#__codelineno-86-260)                           "dataType": "string", [](#__codelineno-86-261)                           "controlType": "LABEL", [](#__codelineno-86-262)                           "required": false, [](#__codelineno-86-263)                           "editable": false, [](#__codelineno-86-264)                           "label": "Do you want to delete the onboarded User?", [](#__codelineno-86-265)                           "hidden": false, [](#__codelineno-86-266)                           "fieldId": "name" [](#__codelineno-86-267)                         } [](#__codelineno-86-268)                       ] [](#__codelineno-86-269)                     }, [](#__codelineno-86-270)                     "actions": [ [](#__codelineno-86-271)                       { [](#__codelineno-86-272)                         "type": "UPDATE_PSTREAM", [](#__codelineno-86-273)                         "pstreamName": "main", [](#__codelineno-86-274)                         "operation": "DELETE", [](#__codelineno-86-275)                         "cfxql_query": "_RDA_Id is '{{_RDA_Id}}'" [](#__codelineno-86-276)                       }, [](#__codelineno-86-277)                       { [](#__codelineno-86-278)                         "type": "RUN_PIPELINE", [](#__codelineno-86-279)                         "pipelineName": "simple_pipeline", [](#__codelineno-86-280)                         "isSync": true [](#__codelineno-86-281)                       } [](#__codelineno-86-282)                     ] [](#__codelineno-86-283)                   } [](#__codelineno-86-284)                 ] [](#__codelineno-86-285)               } [](#__codelineno-86-286)             } [](#__codelineno-86-287)           ] [](#__codelineno-86-288)         } [](#__codelineno-86-289)       ] [](#__codelineno-86-290)     } [](#__codelineno-86-291)   ] [](#__codelineno-86-292) }`

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

`[](#__codelineno-87-1) { [](#__codelineno-87-2)   "widget_group": "group", [](#__codelineno-87-3)   "min_width": 6, [](#__codelineno-87-4)   "height": 8, [](#__codelineno-87-5)   "max_width": 12, [](#__codelineno-87-6)   "widget_type": "pie_chart", [](#__codelineno-87-7)   "title": "Widget 1", [](#__codelineno-87-8)   "stream": "rdaf_services_logs", [](#__codelineno-87-9)   "extra_filter": "log_severity in ['ERROR', 'DEBUG', 'INFO']", [](#__codelineno-87-10)   "ts_column": "timestamp", [](#__codelineno-87-11)   "column": "_id", [](#__codelineno-87-12)   "agg": "value_count", [](#__codelineno-87-13)   "group_by": [ [](#__codelineno-87-14)     "log_severity" [](#__codelineno-87-15)   ], [](#__codelineno-87-16)   "type": "str" [](#__codelineno-87-17) }`

[Example](#__tabbed_22_1)

`[](#__codelineno-88-1) { [](#__codelineno-88-2)   "name": "Multi_support", [](#__codelineno-88-3)   "label": "Multi Support Widget", [](#__codelineno-88-4)   "description": "GH_2745", [](#__codelineno-88-5)   "version": "24.01.03.1", [](#__codelineno-88-6)   "enabled": true, [](#__codelineno-88-7)   "dashboard_type": "dashboard", [](#__codelineno-88-8)   "dashboard_filters": { [](#__codelineno-88-9)     "time_filter": true [](#__codelineno-88-10)   }, [](#__codelineno-88-11)   "dashboard_folder": "Default", [](#__codelineno-88-12)   "dashboard_sections": [ [](#__codelineno-88-13)     { [](#__codelineno-88-14)       "title": "Student App", [](#__codelineno-88-15)       "show_filter": true, [](#__codelineno-88-16)       "widgets": [ [](#__codelineno-88-17)         { [](#__codelineno-88-18)           "widget_group": "group2", [](#__codelineno-88-19)           "title": "Student city", [](#__codelineno-88-20)           "widget_type": "pie_chart", [](#__codelineno-88-21)           "stream": "main", [](#__codelineno-88-22)           "column": "count_", [](#__codelineno-88-23)           "min_width": 6, [](#__codelineno-88-24)           "group_by": [ [](#__codelineno-88-25)             "city" [](#__codelineno-88-26)           ], [](#__codelineno-88-27)           "type": "int", [](#__codelineno-88-28)           "agg": "value_count", [](#__codelineno-88-29)           "ts_column": "timestamp" [](#__codelineno-88-30)         }, [](#__codelineno-88-31)         { [](#__codelineno-88-32)           "widget_group": "group2", [](#__codelineno-88-33)           "title": "Student name", [](#__codelineno-88-34)           "widget_type": "counter", [](#__codelineno-88-35)           "stream": "main", [](#__codelineno-88-36)           "column": "count_", [](#__codelineno-88-37)           "min_width": 6, [](#__codelineno-88-38)           "group_by": [ [](#__codelineno-88-39)             "name" [](#__codelineno-88-40)           ], [](#__codelineno-88-41)           "type": "int", [](#__codelineno-88-42)           "agg": "value_count", [](#__codelineno-88-43)           "ts_column": "timestamp" [](#__codelineno-88-44)         }, [](#__codelineno-88-45)         { [](#__codelineno-88-46)           "title": "Student donation", [](#__codelineno-88-47)           "label": "Donation", [](#__codelineno-88-48)           "widget_group": "group1", [](#__codelineno-88-49)           "widget_type": "bar_chart", [](#__codelineno-88-50)           "min_width": 6, [](#__codelineno-88-51)           "stream": "main", [](#__codelineno-88-52)           "column": "count_", [](#__codelineno-88-53)           "group_by": [ [](#__codelineno-88-54)             "donation" [](#__codelineno-88-55)           ], [](#__codelineno-88-56)           "type": "int", [](#__codelineno-88-57)           "agg": "value_count", [](#__codelineno-88-58)           "ts_column": "timestamp" [](#__codelineno-88-59)         } [](#__codelineno-88-60)       ] [](#__codelineno-88-61)     } [](#__codelineno-88-62)   ] [](#__codelineno-88-63) }`

[![Multiwidget](https://bot-docs.cloudfabrix.io/images/dashboards/multiwidget.png)](/images/dashboards/multiwidget.png)

[![Multiwidget Student Name](https://bot-docs.cloudfabrix.io/images/dashboards/multiwidget1.png)](/images/dashboards/multiwidget1.png)

\`\`\`

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!