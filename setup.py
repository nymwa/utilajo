import setuptools

setuptools.setup(
        name = 'utilajo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
                'tqdm',
                'sentencepiece',
                'pyyaml',
            ],
        entry_points = {
            'console_scripts':[
                'progress = utilajo.progress:main',

                # preprocess
                'glui = utilajo.preproc.glui:main',
                'remove-identical = utilajo.preproc.remove_identical:remove_identical',
                'renversi = utilajo.preproc.renversi:main',
                'space-normalize = utilajo.preproc.space_normalize:main',
                'superspecimeni = utilajo.preproc.superspecimeni:main',
                'tondi = utilajo.preproc.tondi:main',

                # preprocess de
                'beta-to-eszett = utilajo.preproc.de.beta_to_eszett:main',
                'fm-grundkiewicz-filter = utilajo.preproc.de.grundkiewicz_filter:main',

                # preprocess fi
                'split-titles = utilajo.preproc.fi.split_titles:main',

                # preprocess spacy
                'en-tokenize = utilajo.preproc.spacy.tokenize:en',
                'de-tokenize = utilajo.preproc.spacy.tokenize:de',

                # postprocess
                'indeksi = utilajo.postproc.indeksi:main',
                'hazardi = utilajo.postproc.hazardi:main',
                'kunigi = utilajo.postproc.kunigi:main',
                'kuntrunki = utilajo.postproc.kuntrunki:main',
                'nltk-detokenize = utilajo.postproc.nltk_detokenize:main',
                'trunki = utilajo.postproc.trunki:main',

                # erg
                'target-jsonize = utilajo.erg.target_jsonize:main',

                # fasttext
                'ambidetekti = utilajo.fasttext.ambidetekti:main',
                'detekti = utilajo.fasttext.detekti:main',

                # m2
                'm22src = utilajo.m22src:m2_to_src',
                'm22trg = utilajo.m22trg:m2_to_trg',

                # check-fairseq-vocab
                'compare-vocab = utilajo.check_fairseq_vocab:main',

                # generate
                '2yaml = utilajo.generate.conv_to_yaml:main',
                'yaml2tsv = utilajo.generate.yaml_to_tsv:main',
                'r2l2tsv = utilajo.generate.r2l_to_tsv:main',
                'merge-r2l = utilajo.generate.merge_r2l:main',
                'select-best = utilajo.generate.select_best:main',

                # mlm
                'mlm-scoring = utilajo.mlm.mlm_scoring:main',

                # entag
                'gec-tag = utilajo.entag:gec',
                'de-gec-tag = utilajo.entag:de',
                'en-gec-tag = utilajo.entag:en',
                'd2e-tag = utilajo.entag:d2e',
                'e2d-tag = utilajo.entag:e2d',

                # stat
                'char-stat = utilajo.stat.char:main',
                'sent-stat = utilajo.stat.sent:main',
                ]},)

