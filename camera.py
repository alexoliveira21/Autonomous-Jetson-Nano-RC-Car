import cv2
import time
import pandas as pd
import threading


#class holds all necessary functions to record using Open CV video capture
class Camera():

    def __init__(self, car, image_file_path, csv_file_path, camera_id = 0):

        print("Initializing Camera..")

        #dictionary to hold all steering and throttle data
        self.data = {'Timestamp': [], 'Steering' : [], 'Throttle' : []}
        self.start_time = time.time()
        self.car = car
        self.camera_id = camera_id

        #creates an Open CV video capture object
        self.camera = cv2.VideoCapture(camera_id) #pass 0 if only one camera connected otherwise pass the ID of camera

        self.recording = False
        self.image_file_path = image_file_path
        self.csv_file_path = csv_file_path
        self.camera.open(self.camera_id)
        #opens camera to begin recording
        self.camera.open(self.camera_id)


    def capture_frame(self):
        while True:
            if self.camera.isOpened == False:
                self.camera.open(self.camera_id)

            success, frame = self.camera.read() #returns true to success if frame was captured correctly
            throttle, steering = self.car.get_data()
            timestamp = time.time()

            if success:
                #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
                frame = cvtColor(frame, cv2.BayerGR2BGR)
                cv2.imwrite(filename='{}{}'.format(self.image_file_path, timestamp), img=frame)
                self.data['Timestamp'].append(timestamp)
                self.data['Steering'].append(steering)
                self.data['Throttle'].append(throttle)

    def save_data(self):

        dataframe = pd.DataFrame(self.data)
        dataframe.to_csv(self.csv_file_path + str(self.start_time))
        self.data['Timestamp'].clear()
        self.data['Steering'].clear()
        self.data['Throttle'].clear()
        print('Stopped Recording')


    #function to start recording and save camera frames along with timestamps
    def start_recording(self):

        #opens camera to begin recording
        self.camera.open(self.camera_id)
        self.recording = True

        print("Now Recording")
        while self.recording:
            cv2.waitKey(100)
            success, frame = self.camera.read() #returns true to success if frame was captured correctly
            print(frame)
            throttle, steering = self.car.get_data()
            timestamp = time.time()

            if success:
                #frame = cv2.cvtColor(frame, cv2.BayerBG2BGR)
                cv2.imwrite('{}{}.jpg'.format(self.image_file_path, timestamp), frame)
                self.data['Timestamp'].append(timestamp)
                self.data['Steering'].append(steering)
                self.data['Throttle'].append(throttle)

    def start(self):
        video_thread = threading.Thread(target = self.start_recording)
        video_thread.start()

    def stop_recording(self):
        self.recording = False
