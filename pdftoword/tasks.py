# from time import sleep

# @shared_task(bind=True)
# def go_to_sleep(self, duration):
#     progress_recoder= Progress_Recoder(self)
#     for i in range(5):
#         sleep(duration)
#         progress_recoder.set_progress(i+1,5,f'on iteration{i}')
#     return "Done"
