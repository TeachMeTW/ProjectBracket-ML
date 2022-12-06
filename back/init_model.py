import os
import wget
import tensorflow as tf
import object_detection
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

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

VERIFICATION_SCRIPT = os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')


def create_dirs():

    for path in paths.values():
        if not os.path.exists(path):
            os.system('mkdir {}'.format(path))

    if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
        os.system('git clone https://github.com/tensorflow/models {}'.format(paths['APIMODEL_PATH']))


    # For mac
    # Having issues with this
    if os.name=='posix':  
        os.system('brew install protobuf-c')
        os.system('cd back/assets/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python -m pip install . ')
        os.system('python {}'.format(VERIFICATION_SCRIPT))
        
    # For windows
    if os.name=='nt':
        url="https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip"
        wget.download(url)
        os.system('move protoc-3.15.6-win64.zip {}'.format(paths['PROTOC_PATH']))
        os.system('cd {} && tar -xf protoc-3.15.6-win64.zip'.format(paths['PROTOC_PATH']))
        os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(paths['PROTOC_PATH'], 'bin'))   
        os.system('cd back/assets/models/research && protoc object_detection/protos/*.proto --python_out=. && copy object_detection\\packages\\tf2\\setup.py setup.py && python setup.py build && python setup.py install')
        os.system('cd back/assets/models/research/slim && pip install -e . ')
        
    

    if os.name =='posix':
        os.system('wget {}'.format(PRETRAINED_URL))
        os.sytem('mv {} {}'.format((PRETRAINED_MODEL_NAME+'.tar.gz'),paths['PRETRAINED_MODEL_PATH']))
        os.system('cd {} && tar -zxvf {}'.format(paths['PRETRAINED_MODEL_PATH'],(PRETRAINED_MODEL_NAME+'.tar.gz')))
    if os.name == 'nt':
        wget.download(PRETRAINED_URL)
        os.system('move {} {}'.format((PRETRAINED_MODEL_NAME+'.tar.gz'),(paths['PRETRAINED_MODEL_PATH'])))
        os.system('cd {} && tar -zxvf {}'.format((paths['PRETRAINED_MODEL_PATH']),(PRETRAINED_MODEL_NAME+'.tar.gz')))
        
    
    
    os.system('python {}'.format(VERIFICATION_SCRIPT))   
    
# Create label Map    

def create_labels():
    labels = [{'name':'airpods', 'id':1},
            {'name':'book', 'id':2},
            {'name':'bottle', 'id':3},
            {'name':'carbonmonitor', 'id':4},
            {'name':'cat', 'id':5},
            {'name':'maskedface', 'id':6},
            {'name':'masked', 'id':6},
            {'name':'microphone', 'id':7},
            {'name':'multimeter', 'id':8},
            {'name':'pencil', 'id':9},
            {'name':'phone', 'id':10},
            {'name':'face', 'id':11},
            {'name':'watch', 'id':12},
            {'name':'keyboard', 'id':13},
            {'name':'glasses', 'id':14}
            ]

    with open(files['LABELMAP'], 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')
            
    # TF RECORD

    if not os.path.exists(files['TF_RECORD_SCRIPT']):
        os.system('git clone https://github.com/nicknochnack/GenerateTFRecord {}'.format(paths['SCRIPTS_PATH']))
        
    os.system('python {} -x {} -l {} -o {}'.format((files['TF_RECORD_SCRIPT']),(os.path.join(paths['IMAGE_PATH'], 'train')),(files['LABELMAP']),(os.path.join(paths['ANNOTATION_PATH'], 'train.record'))))
    os.system('python {} -x {} -l {} -o {}'.format((files['TF_RECORD_SCRIPT']),(os.path.join(paths['IMAGE_PATH'], 'test')),(files['LABELMAP']),(os.path.join(paths['ANNOTATION_PATH'], 'test.record'))))

    # Copy model to training

    if os.name =='posix':
        os.system('cp {} {}'.format((os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'pipeline.config')),(os.path.join(paths['CHECKPOINT_PATH']))))
    if os.name == 'nt':
        os.system('copy {} {}'.format((os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'pipeline.config')),(os.path.join(paths['CHECKPOINT_PATH']))))
        
        
    # Config update 

    config = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])

    config

    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    with tf.io.gfile.GFile(files['PIPELINE_CONFIG'], "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)  
        
    pipeline_config.model.ssd.num_classes = len(labels)
    pipeline_config.train_config.batch_size = 4
    pipeline_config.train_config.fine_tune_checkpoint = os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'checkpoint', 'ckpt-0')
    pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
    pipeline_config.train_input_reader.label_map_path= files['LABELMAP']
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATION_PATH'], 'train.record')]
    pipeline_config.eval_input_reader[0].label_map_path = files['LABELMAP']
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATION_PATH'], 'test.record')]

    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile(files['PIPELINE_CONFIG'], "wb") as f:                                                                                                                                                                                                                     
        f.write(config_text)   
        
TRAINING_SCRIPT = os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection', 'model_main_tf2.py')
command = "python {} --model_dir={} --pipeline_config_path={} --num_train_steps=2000".format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],files['PIPELINE_CONFIG'])
#os.system(command)
print(command)




# Evaluate
command = "python {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}".format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],files['PIPELINE_CONFIG'], paths['CHECKPOINT_PATH'])
print(command)

if __name__ == "__main__":
    create_dirs()
    create_labels()