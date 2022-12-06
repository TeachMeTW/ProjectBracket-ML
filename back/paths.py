import os


MODEL_NAME = 'ssd_mobilenet_fpn_lite'
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    
    
    'WORKSPACE_PATH': os.path.join('back'),
    'SCRIPTS_PATH': os.path.join('back','assets','scripts'),
    'APIMODEL_PATH': os.path.join('back', 'assets','models'),
    'ANNOTATION_PATH': os.path.join('back', 'assets', 'unsorted','labels'),
    'IMAGE_PATH': os.path.join('back', 'assets', 'unsorted','images'),
    'MODEL_PATH': os.path.join('back', 'assets', 'unsorted','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('back', 'assets', 'unsorted','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('back', 'assets', 'unsorted','models',MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('back', 'assets', 'unsorted','models',MODEL_NAME, 'export'), 
    'TFJS_PATH':os.path.join('back', 'assets', 'unsorted','models',MODEL_NAME, 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('back', 'assets', 'unsorted','models',MODEL_NAME, 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('back','protoc')
    
}


files = {
    'PIPELINE_CONFIG':os.path.join('back', 'assets', 'unsorted','models', MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}
