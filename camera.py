import cv2
import time
import pandas as pd


#class holds all necessary functions to record using Open CV video capture
class Camera():

    def __init__(self, car, image_file_path, csv_file_path, camera_id = 0):

        #dictionary to hold all steering and throttle data
        self.data = {'Timestamp': [], 'Steering' : [], 'Throttle' : []}

        self.car = car
        self.camera_id = camera_id

        #creates an Open CV video capture object
        self.camera = cv2.VideoCapture(camera_id) #pass 0 if only one camera connected otherwise pass the ID of camera
        self.recording = False
        self.image_file_path = image_file_path
        self.csv_file_path = csv_file_path

    #function to start recording and save camera frames along with timestamps
    def start_recording(self):

        #opens camera to begin recording
        self.camera.open(self.camera_id)
        self.recording = True

        print("Now Recording")
        while self.recording:

            success, frame = self.camera.read() #returns true to success if frame was captured correctly
            throttle, steering = self.car.get_data()
            timestamp = time.time()

            if success:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
                cv2.imwrite(filename='{}{}.jpg'.format(self.image_file_path, timestamp), img=frame)
                self.data['Timestamp'].append(timestamp)
                self.data['Steering'].append(steering)
                self.data['Throttle'].append(throttle)
                
        dataframe = pd.DataFrame(self.data)
        dataframe.to_csv(csv_file_path)
        self.data['Timestamp'].clear()
        self.data['Steering'].clear()
        self.data['Throttle'].clear()
        print('Stopped Recording')

    def stop_recording(self):
        self.recording = False
