# References — 논문, 기술 문서, 공개 구현

첫 대회였기 때문에 많은 논문을 체계적으로 비교하지는 못했습니다. 아래 자료는 프로젝트에서 사용한 핵심 방법을 사후에 정확히 설명하고, 다음 연구에서 더 엄밀하게 확장하기 위한 최소 참고자료입니다.

## 1. 참고한 논문

### XLM-RoBERTa

- Conneau et al., [Unsupervised Cross-lingual Representation Learning at Scale](https://aclanthology.org/2020.acl-main.747/), ACL 2020.
- 프로젝트 연결: 한국어·영어·코드 문자열이 혼합된 입력의 Baseline과 Teacher/Student Backbone.

### Knowledge Distillation

- Hinton, Vinyals, Dean, [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531), 2015.
- 프로젝트 연결: 제출이 어려운 Large Teacher의 soft target을 Base Student가 학습.
- 직접 변형: XLM-R 14-class action prediction, `alpha=0.7`, `temperature=2.0`, 이후 FGM·LLRD 결합.

### Text Adversarial Training

- Miyato, Dai, Goodfellow, [Adversarial Training Methods for Semi-Supervised Text Classification](https://arxiv.org/abs/1605.07725), ICLR 2017.
- 프로젝트 연결: 원시 token 대신 embedding 공간에 작은 perturbation을 주는 FGM 적용의 연구적 배경.
- 직접 변형: XLM-R KD Student에 적용하고 `eps=1.0/1.5`를 비교.

### Layer-wise Fine-tuning의 배경

- Howard and Ruder, [Universal Language Model Fine-tuning for Text Classification](https://aclanthology.org/P18-1031/), ACL 2018.
- 프로젝트 연결: 레이어별로 다른 학습률을 사용하는 discriminative fine-tuning의 배경.
- 주의: 이 프로젝트의 Transformer LLRD 구현이 ULMFiT 전체 방법을 재현한 것은 아닙니다.

### Label-noise 후속 연구 후보

- Zhang and Sabuncu, [Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels](https://arxiv.org/abs/1805.07836), NeurIPS 2018.
- Han et al., [Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels](https://arxiv.org/abs/1804.06872), NeurIPS 2018.
- 프로젝트 연결: 이번 대회에서 직접 구현한 방법이 아니라, margin 분석과 FGM 경험을 후속 연구로 확장할 비교 대상.

## 2. 기술 문서

- [Hugging Face XLM-RoBERTa documentation](https://huggingface.co/docs/transformers/model_doc/xlm-roberta)
- [Hugging Face text classification guide](https://huggingface.co/docs/transformers/tasks/sequence_classification)
- [scikit-learn GroupKFold documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)
- [scikit-learn cross-validation guide for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data)

## 3. 공개 구현

- [Hugging Face Transformers](https://github.com/huggingface/transformers): XLM-R sequence classification 인터페이스와 Trainer 생태계 참고.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn): GroupKFold와 평가 도구 참고.
- [Original XLM repository](https://github.com/facebookresearch/XLM): 다국어 사전학습 모델의 원 프로젝트 참고.

## 4. 제안과 직접 기여

실험 방향, 입력 구성, 오류 분석, Teacher/Student 조합, FGM 확장, Ensemble 후보 탐색 등 프로젝트 내 아이디어의 대부분은 제가 제안하고 팀과 함께 검토했습니다. 외부 자료는 원리 이해와 구현 점검에 사용했으며, 공개 구현을 그대로 자신의 독창적 방법으로 표현하지 않습니다.

## 5. 인용 원칙

- 논문에서 직접 얻은 아이디어는 해당 실험 문서에 링크합니다.
- 공식 문서로 확인한 API와 동작은 기술 문서로 분류합니다.
- 공개 코드를 참고했다면 Repository와 참고 범위를 표시합니다.
- 프로젝트에 맞게 바꾼 부분과 원래 방법을 구분합니다.
- 실험 결과는 이 프로젝트의 조건에서 얻은 결과이며 논문의 일반적 결론으로 확대하지 않습니다.
