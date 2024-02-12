import multiprocessing
import camera_module
import dht11_module
import hx711_module
import adxl345_module

def main():
    # Erstellen Sie Prozesse für jedes Modul
    camera_process = multiprocessing.Process(target=camera_module.run_camera_module)
    dht11_process = multiprocessing.Process(target=dht11_module.run_dht11_module)
    hx711_process = multiprocessing.Process(target=hx711_module.run_hx711_module)
    adxl345_process = multiprocessing.Process(target=adxl345_module.run_adxl345_module)

    # Starten Sie die Prozesse
    camera_process.start()
    dht11_process.start()
    hx711_process.start()
    adxl345_process.start()

    # Warten Sie auf die Prozesse, um zu beenden
    camera_process.join()
    dht11_process.join()
    hx711_process.join()
    adxl345_process.join()

if __name__ == "__main__":
    main()
