import argparse
import yaml
import datetime
import time
import sys
import pipeline_factory
import os
import subprocess
from string import Template
import errno

parser = argparse.ArgumentParser()
parser.add_argument('-c','--config')
parser.add_argument('--components_dir')
parser.add_argument('--num_jobs')
parser.add_argument('--num_pipelines')
parser.add_argument('--drmaa')
parser.add_argument('--run_id', default=None)
parser.add_argument('--outdir',default=os.getcwd())
args = parser.parse_args()


def load_yaml():
	yaml_dict = yaml.load(open(args.config))

	sample_ids = yaml_dict['__SAMPLES__'].keys()

	return sample_ids

def generate_run_id():
    if args.run_id:
        return args.run_id
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def run(cmd, ret = False):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                            stderr = subprocess.PIPE, shell = True)
    
    print 'Running Command: '+cmd

    cmdout, cmderr = proc.communicate()
    
    print cmdout 
    if ret:
        return cmdout, cmderr
    if not cmderr == '':
        print cmdout
        #raise Exception(cmderr)

def generate_interval_files(sample_ids, run_id, pipeline_name):
	for sample in sample_ids:
		print 'Processing sample: '+sample
		path = os.path.join(args.outdir,run_id,sample+'_'+pipeline_name,'outputs')
		interval_file1 = os.path.join(path, 'TASK_SPLIT_PAIRED_FASTQ_split_fq_paired_interval.txt')
		mkdir_p(path)
                if os.path.exists(interval_file1):
                    print 'file exists: '+interval_file1
                    continue
		print 'creating interval file: '+interval_file1
		intfile_writer = open(interval_file1, 'w')
		for i in xrange(5):
			intfile_writer.write(str(i)+'\n')
 
                interval_file = os.path.join(path, 'TASK_SPLIT_UNPAIRED_FASTQ_split_fq_unpaired_interval.txt')
                mkdir_p(path)
                if os.path.exists(interval_file):
                    print 'file exists: '+interval_file
                    continue
                print 'creating interval file: '+interval_file
                intfile_writer = open(interval_file, 'w')
                for i in xrange(5):
                        intfile_writer.write(str(i)+'\n')


def init_pipeline(pipeline_name,conf_file):
	cmd = [sys.executable, os.path.join(os.path.dirname(pipeline_factory.__file__),'factory.py') , '--working_dir', args.outdir,
	       'init_pipeline', '-c', conf_file, '-p', pipeline_name]
	cmd = ' '.join(cmd)
	print 'MY INIT CMD: ' +cmd
	run(cmd)

def run_pipeline(pipeline_name, run_id):
	cmd = [sys.executable, args.outdir+pipeline_name+'.py', '--working_dir', args.outdir, '--factory_dir', os.path.dirname(pipeline_factory.__file__), 
			'--components_dir', args.components_dir, '--num_jobs', args.num_jobs, '--num_pipelines', args.num_pipelines,
			'--run_id', run_id, '--drmaa_library_path', args.drmaa]
	cmd = ' '.join(cmd)

	cmdout, cmderr = run(cmd, ret = True)

        if 'breakpoint' in cmdout:
            print 'cmdout: '+cmdout
            return
        if 'Job Completed' in cmderr:
            print 'cmdout: '+cmdout
            print 'cmderr:'+cmderr
            return
        if 'qmaster' in cmderr:
            print 'cmderr:'+cmderr
            return
        if 'KeyboardInterrupt' in cmderr:
            print 'cmderr:'+cmderr
            return
        if 'error' or 'warning' in cmderr:
            print 'cmdout: '+cmdout
            raise Exception(cmderr)

        print 'cmdout: '+cmdout
        print 'cmderr: '+cmderr

def update_yaml(pipeline_name, run_id):
    yaml_dict = yaml.load(open(args.config))

    for mysample in yaml_dict["__SAMPLES__"].keys():
	interval_filepath = os.path.join(args.outdir,run_id,mysample+'_'+pipeline_name,'outputs')
	yaml_dict["__SAMPLES__"][mysample]["interval_pairedfq"]= os.path.join(interval_filepath, 'TASK_SPLIT_PAIRED_FASTQ_split_fq_paired_interval.txt')
	yaml_dict["__SAMPLES__"][mysample]["interval_unpairedfq"]= os.path.join(interval_filepath, 'TASK_SPLIT_UNPAIRED_FASTQ_split_fq_unpaired_interval.txt')

    #with open(args.config,"w") as f:
#	yaml.dump(yaml_dict,f)

#    yaml_dict = yaml.load(open(args.config))
#    template = open(args.config)

    with open(updated_yaml_name,"w") as f:
        yaml.dump(yaml_dict,f)

    yaml_dict = yaml.load(open(updated_yaml_name))
    template = open(updated_yaml_name)

    output = []

    myenv_ids = ["$run_id","$sample_id"]
    myenv_names = ["$pipeline_name","$pipeline_working_dir","$run_id","$sample_id"]	
    print "UPDATING YAML.... pipeline_name: " + pipeline_name
    print "UPDATING YAML.... CWD: " + args.outdir
    print "UPDATING YAML.... RUN_ID: " + run_id
    for line in template:
	if not any(e in line for e in myenv_names):
        	line = Template(line).substitute(CWD=args.outdir,
                                         PIPELINE_NAME=pipeline_name,
        				 RUN_ID=run_id)
	output.append(line)

    #outfile_stream = open(args.config,'w')
    outfile_stream = open(updated_yaml_name,'w')
    for line in output:
        outfile_stream.write(line)
    outfile_stream.close()


pipeline_name = os.path.basename(args.config).replace('.yaml','')
updated_yaml_name = args.config.replace('.yaml','')+ "_updated.yaml"
print "New yaml file is at : " + updated_yaml_name
sample_ids = load_yaml()
run_id = generate_run_id()
generate_interval_files(sample_ids, run_id, pipeline_name)
update_yaml(pipeline_name,run_id)
init_pipeline(pipeline_name,updated_yaml_name) #init_pipeline(pipeline_name,args.config)
run_pipeline(pipeline_name, run_id)

#if the pipeline finishes without error (no exception) then the interval file will be populated, so rerun
init_pipeline(pipeline_name, updated_yaml_name)
run_pipeline(pipeline_name, run_id)

