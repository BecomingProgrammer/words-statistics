#coding=gbk
import en

otherwordlist = []
def simplify_word(a):
    
    try:#�����Ƿ�Ϊ����,������򷵻�
        en.is_verb(en.verb.present(a))
        return en.verb.present(a)
    except:#����������
        pass
    
    #�����Ƿ�������
    if en.is_noun(en.noun.singular(a)):
        return en.noun.singular(a)
    
    #����Ѿ������ж�������,����,���ݴ�,����,����
    if en.is_noun(a) or en.is_verb(a) or en.is_adjective(a) or en.is_adverb(a) or en.is_connective(a):
        return a
        
    
    
    
    otherwordlist.append(a)
    return a

    

