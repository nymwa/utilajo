import setuptools

setuptools.setup(
        name = 'utilajo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
                'fasttext',
                'tqdm',
                'sentencepiece',
                'pyyaml',
            ],
        entry_points = {
            'console_scripts':[
                'progress = utilajo.progress:main',

                # filter
                'punct-end = utilajo.filter.punct_end:main',
                'clean-ctrl = utilajo.filter.clean_ctrl:main',

                # preprocess
                'glui = utilajo.preproc.glui:main',
                'remove-identical = utilajo.preproc.remove_identical:remove_identical',
                'renversi = utilajo.preproc.renversi:main',
                'space-normalize = utilajo.preproc.space_normalize:main',
                'unicode-normalize = utilajo.preproc.unicode_normalize:main',
                'superspecimeni = utilajo.preproc.superspecimeni:main',
                'tondi = utilajo.preproc.tondi:main',
                'chartondi = utilajo.preproc.chartondi:main',
                'ambitondi = utilajo.preproc.ambitondi:main',
                'ambichartondi = utilajo.preproc.ambichartondi:main',
                'purigi = utilajo.preproc.purigi:main',
                'malgrandigi = utilajo.preproc.malgrandigi:main',
                'senliterigi = utilajo.preproc.senliterigi:main',
                'ambisenliterigi = utilajo.preproc.ambisenliterigi:main',
                'miksi = utilajo.preproc.miksi:main',
                'vicigi = utilajo.preproc.vicigi:main',
                'unuvicigi = utilajo.preproc.unuvicigi:main',
                'forripeti = utilajo.preproc.forripeti:main',

                # preprocess wmt
                'preproc-iwslt = utilajo.preproc.wmt.iwslt:main',
                'preproc-tatoeba = utilajo.preproc.wmt.tatoeba:main',
                'preproc-europarl = utilajo.preproc.wmt.europarl:main',
                'preproc-rapid = utilajo.preproc.wmt.rapid:main',
                'preproc-bicleaner = utilajo.preproc.wmt.bicleaner:main',

                # preprocess de
                'beta-to-eszett = utilajo.preproc.de.beta_to_eszett:main',
                'fm-grundkiewicz-filter = utilajo.preproc.de.grundkiewicz_filter:main',

                # preprocess fi
                'split-titles = utilajo.preproc.fi.split_titles:main',

                # preprocess spacy
                'en-tokenize = utilajo.preproc.spacy.tokenize:en',
                'de-tokenize = utilajo.preproc.spacy.tokenize:de',
                'fr-tokenize = utilajo.preproc.spacy.tokenize:fr',
                'ja-tokenize = utilajo.preproc.spacy.tokenize:ja',
                'zh-tokenize = utilajo.preproc.spacy.tokenize:zh',

                # postprocess
                'indeksi = utilajo.postproc.indeksi:main',
                'hazardi = utilajo.postproc.hazardi:main',
                'kunigi = utilajo.postproc.kunigi:main',
                'kunigi2 = utilajo.postproc.kunigi2:main',
                'kuntrunki = utilajo.postproc.kuntrunki:main',
                'nltk-detokenize = utilajo.postproc.nltk_detokenize:main',
                'trunki = utilajo.postproc.trunki:main',
                'remove-space = utilajo.postproc.remove_space:main',
                'laulonge = utilajo.postproc.laulonge:main',
                'selekti = utilajo.postproc.selekti:main',

                # erg
                'target-jsonize = utilajo.erg.target_jsonize:main',

                # fasttext
                'ambidetekti = utilajo.fasttext.ambidetekti:main',
                'detekti = utilajo.fasttext.detekti:main',

                # m2
                'm22src = utilajo.m2.m22src:m2_to_src',
                'm22trg = utilajo.m2.m22trg:m2_to_trg',

                # moses
                'krampo-grandigi = utilajo.moses.krampo:grandigi_main',
                'krampo-malgrandigi = utilajo.moses.krampo:malgrandigi_main',
                'krampo-deigi = utilajo.moses.deigi:deigi_main',

                # compare-fairseq-vocab
                'compare-vocab = utilajo.compare_fairseq_vocab:main',

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
                'unk-stat = utilajo.stat.unk:main',
                ]},)

