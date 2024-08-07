import cv2
import face_recognition
import numpy as np

def count_people_in_frame(frame):
    # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Return the number of faces found
    return len(face_locations)

def calculate_heat_density(num_people, room_volume, avg_heat_per_person=100):
    """
    Calculate the heat density inside the room.
    
    :param num_people: Number of people inside the room.
    :param room_volume: Volume of the room in cubic meters.
    :param avg_heat_per_person: Average heat emitted per person in watts.
    :return: Heat density in watts per cubic meter.
    """
    total_heat = num_people * avg_heat_per_person
    heat_density = total_heat / room_volume
    return heat_density

def main():
    # Define room volume in cubic meters (example: 50 cubic meters)
    room_volume = 50

    # Open a connection to the webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture a single frame of video
        ret, frame = video_capture.read()

        # Count the number of people in the frame
        num_people = count_people_in_frame(frame)

        # Calculate heat density
        heat_density = calculate_heat_density(num_people, room_volume)

        # Display the results
        cv2.putText(frame, f'People: {num_people}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f'Heat Density: {heat_density:.2f} W/m^3', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

