from docker_2.celery import app

@app.task
def export_calibration_report(a,b):
    return a+b


# result = export_calibration_report.delay(4, 6)

# # Wait for the task to complete and get the result
# print("Task result:", result.get())
