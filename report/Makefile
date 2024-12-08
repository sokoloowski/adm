ifndef OUTPUT_FILE_SUFFIX
OUTPUT_FILE_SUFFIX := latest
endif

ifndef OUTPUT_PATH
OUTPUT_PATH := out
endif

ifndef DOCKER_CMD
DOCKER_CMD := docker run -it --rm -v .:/data -u 1000:1000
endif

ifndef PANDOC_CMD
PANDOC_CMD := ${DOCKER_CMD} pandocker:latest
endif

ifndef LATEXMK_CMD
LATEXMK_CMD := ${DOCKER_CMD} --entrypoint latexmk pandocker:latest
endif

pdf:
	echo "" > from-doi.bib
	pandoc -N --standalone --lua-filter diagram-generator.lua --lua-filter doi2cite.lua -F pandoc-crossref src/*.md -o output.tex --biblatex
	latexmk -pdf
	mkdir -p ${OUTPUT_PATH}
	mv output.pdf ${OUTPUT_PATH}/pp-rai-${OUTPUT_FILE_SUFFIX}.pdf
	cp ${OUTPUT_PATH}/pp-rai-${OUTPUT_FILE_SUFFIX}.pdf ${OUTPUT_PATH}/preview.pdf
	rm -f output.*

docker-pdf:
	echo "" > from-doi.bib
	${PANDOC_CMD} -N --standalone --lua-filter diagram-generator.lua --lua-filter doi2cite.lua -F pandoc-crossref src/*.md -o output.tex --biblatex
	${LATEXMK_CMD} -pdf
	mkdir -p ${OUTPUT_PATH}
	mv output.pdf ${OUTPUT_PATH}/pp-rai-${OUTPUT_FILE_SUFFIX}.pdf
	cp ${OUTPUT_PATH}/pp-rai-${OUTPUT_FILE_SUFFIX}.pdf ${OUTPUT_PATH}/preview.pdf
	rm -f output.*
