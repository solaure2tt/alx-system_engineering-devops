# 0x18. Webstack monitoring
===========================================

## Task 0: Sign up for Datadog and install datadog-agent 

    Sign up for Datadog - Please make sure you are using the US website of Datagog (https://app.datadoghq.com)
    Use the US1 region
    Install datadog-agent on web-01
    Create an application key
    Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
    Your server web-01 should be visible in Datadog under the host name XX-web-01
        You can validate it by using this API
        If needed, you will need to update the hostname of your server

## Task 1: Monitor some metrics 
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.

## Task 2:  Create a dashboard 
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

    Create a new dashboard
    Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
    Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API
