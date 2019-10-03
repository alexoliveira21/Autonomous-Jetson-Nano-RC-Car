import cv2

#class holds all necessary functions to record using Open CV video capture
class Camera():

    def __init__(self, image_file_path, camera_id = 0):

        self.camera_id = camera_id
        #creates an Open CV video capture object
        self.camera = cv2.VideoCapture(camera_id) #pass 0 if only one camera connected otherwise pass the ID of camera
        self.recording = False

    #function to start recording and save camera frames along with timestamps
    def start_recording(self):

        self.camera.open(self.camera_id)
        self.recording = True
        while recording:

            if self.camera.isOpened() == False:
                self.camera.open()

            success, frame = self.camera.read() #returns true to success if frame was captured correctly

            if success:
                cv2.imwrite(filename='')
