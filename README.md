[HOW TO USE]

1) 프로젝트 백서 요약 시

- **project_summarization.ipynb 참고**

- sources/SOURCE_completed_project_contents.txt 에 신규 프로젝트 백서의 주제, 진행 프로세스 긁어서 붙여넣기

- project_summarization.ipynb 코드 돌리기

- sources/SOURCE_summarized_project.txt 파일에서 생성된 프로젝트 요약 텍스트 확인

- (필요 시) 기업 규모와 도메인은 아직까지는 수동으로 입력했지만 perplexity api로 기업 정보 끌어올 수 있으면 이 정보도 추가할 수 있을 듯



2) 커스텀 메일 생성 시

- **proposal_automation.ipynb 참고**

- **INPUT.yaml에 이하 4가지 정보를 기입해주세요!!!**

- INPUT.yaml: 기업명(필수), 기업홈페이지링크(선택, 그러나 첨부할 시 정보의 질 향상), 제안대상자명(선택, 기제 안할 시 이후 제안서에 '담당자님'이라는 워딩으로 들어감), 제안대상자 직책(선택)**

- proposal_automation.ipynb 코드 돌리기

- sources/SOURCE_target_company_information.txt에 타겟 기업 관련 정보가 들어있을겁니다. 굳이 확인할 필요는 X

- outputs/{기업명}_completed_proposal_letter.txt 파일에서 생성된 제안문 확인
   
