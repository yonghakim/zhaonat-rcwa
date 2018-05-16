import numpy as np
import cmath

'''
need to modify these function so that each block can accept arbitrarily sized square matrices
'''

def dict_to_matrix(S_dict):
    '''
    converts dictionary form of scattering matrix to a np.matrix
    :param S_dict:
    :return:
    '''
    return np.block([[S_dict['S11'], S_dict['S12']],[S_dict['S21'], S_dict['S22']]]);


def RedhefferStar(SA,SB): #SA and SB are both 2x2 block matrices;
    '''
    RedhefferStar for arbitrarily sized 2x2 block matrices for RCWA
    :param SA: dictionary containing the four sub-blocks
    :param SB: dictionary containing the four sub-blocks,
    keys are 'S11', 'S12', 'S21', 'S22'
    :return:
    '''

    assert type(SA) == dict, 'not dict'
    assert type(SB) == dict, 'not dict'

    # once we break every thing like this, we should still have matrices
    SA_11 = SA['S11']; SA_12 = SA['S12']; SA_21 = SA['S21']; SA_22 = SA['S22'];
    SB_11 = SB['S11']; SB_12 = SB['S12']; SB_21 = SB['S21']; SB_22 = SB['S22'];
    N = len(SA_11) #SA_11 should be square so length is fine
    I = np.matrix(np.identity(N));

    D = np.linalg.inv(I-SB_11*SA_22);
    F = np.linalg.inv(I-SA_22*SB_11);

    SAB_11 = SA_11 + SA_12*D*SB_11*SA_21;
    SAB_12 = SA_12*D*SB_12;
    SAB_21 = SB_21*F*SA_21;
    SAB_22 = SB_22 + SB_21*F*SA_22*SB_12;

    SAB = np.block([[SAB_11, SAB_12],[SAB_21, SAB_22]])
    SAB_dict = {'S11': SAB_11, 'S22': SAB_22,  'S12': SAB_12,  'S21': SAB_21};

    return SAB, SAB_dict;

