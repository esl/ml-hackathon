
ASSETS_DIR = assets
URLS_DIR = $(ASSETS_DIR)/urls
CATEGORIES = $(notdir $(wildcard $(URLS_DIR)/*))
IMAGES_DIR = $(ASSETS_DIR)/images
IMAGES_DIRS = $(addprefix $(IMAGES_DIR)/,$(CATEGORIES))
TF_DIR = $(ASSETS_DIR)/tf
RETRAINED_GRAPH = $(TF_DIR)/retrained_graph.pb
LABELS_FILE = $(TF_DIR)/retrained_labels.txt

all: $(IMAGES_DIRS) $(RETRAINED_GRAPH)

$(IMAGES_DIRS): URLS_FILE = $(CURDIR)/$(URLS_DIR)/$(notdir $@)
$(IMAGES_DIRS):
	mkdir -p $@
	(cd $@ && cat $(URLS_FILE) | xargs -I{} -P10 curl -OLs {})

$(RETRAINED_GRAPH):
	python bin/retrain.py \
	    --bottleneck_dir=$(TF_DIR)/bottlenecks \
	    --how_many_training_steps=500 \
	    --model_dir=$(TF_DIR)/models \
	    --summaries_dir=$(TF_DIR)/training_summaries/inception_v3 \
	    --output_graph=$@ \
	    --output_labels=$(LABELS_FILE) \
	    --image_dir=$(IMAGES_DIR)

label_image:
	python bin/label_image.py \
	    --graph=$(RETRAINED_GRAPH) \
	    --image=$(IMAGE_PATH) \
	    --input_layer=Placeholder \
	    --output_layer=final_result \
	    --labels $(LABELS_FILE)

.PHONY: all
