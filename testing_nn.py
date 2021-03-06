import logging
from nnpredict.nnpredict import NNpredict
from nnpredict.models import LinearModel, NNModel


lg = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':

    pheno_file = 'data/sim_1000G_chr10.txt'
    train_plink = 'data/split_test/SampleMajor_train'
    dev_plink = 'data/split_test/SampleMajor_dev'

    train_plink = 'data/sample_major/1kg/sim_1000G_chr10_SampleMajor_train'
    dev_plink = 'data/sample_major/1kg/sim_1000G_chr10_SampleMajor_dev'

    ld_block_file = 'data/sim_1000G_chr10.ld_blocks.pickel'
    monster = NNpredict(train_plink, dev_plink, pheno_file)
    config_ln = {'ld_blocks': ld_block_file}
    config_nn = {'layers': [10]}
    #config_nn = {'layers': []}

    monster.run_model(epochs=200,
                      batch_size=100,
                      l_rate=0.0001,
                      penal=0.01,
                      pheno_name='V1',
                      tb_name='sample_majorMode',
                      in_model=LinearModel, ld_blocks=ld_block_file)

    # monster.run_model(epochs=400,
    #                   batch_size=100,
    #                   l_rate=0.001,
    #                   penal=0.01,
    #                   keep=0.2,
    #                   pheno_name='V1',
    #                   tb_name='sample_majorMode',
    #                   in_model=NNModel, **config_nn)
