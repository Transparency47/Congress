# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3564
- Title: NIH Clinical Trial Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 3564
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-01-22T15:35:48Z
- Update date including text: 2026-01-22T15:35:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3564",
    "number": "3564",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "NIH Clinical Trial Integrity Act",
    "type": "S",
    "updateDate": "2026-01-22T15:35:48Z",
    "updateDateIncludingText": "2026-01-22T15:35:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-12-18T17:38:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "ME"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3564is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3564\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Kim (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Director of the National Institutes of Health, to take certain steps to increase clinical trial diversity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NIH Clinical Trial Integrity Act .\n#### 2. Diversity goals for clinical trials funded by the National Institutes of Health\n##### (a) Applications\nBeginning on the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the National Institutes of Health (referred to in this section as the Secretary ), shall require that a research organization or entity funded by the National Institutes of Health (referred to in this section as an NIH-funded research organization or entity ) seeking to conduct a clinical trial investigating a drug or device (as those terms are defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )) or a biological product (as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) )) that is funded by the National Institutes of Health or a behavioral intervention, the protocol for which is approved by the National Institutes of Health, submit an application (or renewal thereof) for such funding or approval that includes\u2014\n**(1)**\nclear and measurable goals for the recruitment and retention of participants that reflect\u2014\n**(A)**\nthe race, ethnicity, age, and sex of patients with the disease or condition being investigated; or\n**(B)**\nas scientifically or ethically justified and appropriate, the race, ethnicity, age, and sex of the general population of the United States if the prevalence of the disease or condition is not known;\n**(2)**\na rationale for the goals specified under paragraph (1) that specifies\u2014\n**(A)**\nhow investigators will determine the number of participants for each population category that reflect the population groups specified in paragraph (1); or\n**(B)**\nstrategies that will be used to enroll and retain participants across the different race, ethnicity, age, and sex categories;\n**(3)**\na detailed plan for how the clinical trial will achieve the goals specified under paragraph (1) that specifies\u2014\n**(A)**\nthe requirements for researchers, in conducting the trial, to analyze the population groups specified in paragraph (1) separately; and\n**(B)**\nhow the trial will recruit a study population that is\u2014\n**(i)**\nscientifically and ethically appropriate in terms of the scientific objectives and proposed study design; and\n**(ii)**\nin sufficient numbers to obtain clinically and statistically meaningful determinations of the safety and effectiveness of the drug, device, or behavioral intervention being studied in the respective race, ethnicity, age, and sex groups; and\n**(4)**\nthe NIH-funded research organization or entity\u2019s plan for implementing, or an explanation of why the NIH-funded research organization or entity cannot implement, alternative clinical trial follow-up requirements that are less burdensome for trial participants, such as\u2014\n**(A)**\nrequiring fewer follow-up visits;\n**(B)**\nallowing phone follow-up or home visits by appropriately qualified staff (in lieu of in-person visits by patients);\n**(C)**\nallowing for online follow-up options;\n**(D)**\npermitting the patient\u2019s primary care provider to perform some of the follow-up visit requirements;\n**(E)**\nallowing for evening and weekend hours for required follow-up visits;\n**(F)**\nallowing virtual or telemedicine visits;\n**(G)**\nuse of wearable technology to record key health parameters; and\n**(H)**\nuse of alternate labs or imaging centers, which may be closer to the residence of the patients participating in the trial.\n##### (b) Terms\n**(1) In general**\nAs a condition on the receipt of funding through the National Institutes of Health, as described in subsection (a), with respect to a clinical trial, the NIH-funded research organization or entity of the clinical trial shall agree to terms requiring that\u2014\n**(A)**\nthe aggregate demographic information of trial participants be shared on an annual basis with the Secretary while participant recruitment and data collection in such trial is ongoing, and that such information is provided with respect to\u2014\n**(i)**\nunderrepresented populations, including populations grouped by race, ethnicity, age, and sex; and\n**(ii)**\nsuch populations that reflect the prevalence of the disease or condition that is the subject of the clinical trial involved (as available and as appropriate to the scientific objective for the study, as determined by the Director of the National Institutes of Health);\n**(B)**\nthe NIH-funded research organization or entity submits to the program officer and grants management specialist of the specific institute, center, or office of the National Institutes of Health, annually or as frequently as such officer or specialist determines necessary, the retention rate of participants in the clinical trial, disaggregated by race, ethnicity, age, and sex;\n**(C)**\nthe clinical trial researchers complete education and training programs on diversity in clinical trials; and\n**(D)**\nat the conclusion of the trial, the sponsor submits to the Secretary the number of participants in the trial, disaggregated by race, ethnicity, age, and sex.\n**(2) Privacy protections**\nAny data shared under paragraph (1) may not include any individually identifiable information or protected health information with respect to clinical trial participants and shall only be disclosed to the extent allowed under Federal privacy laws and by National Institutes of Health policy.\n##### (c) Exception\nIn lieu of submitting an application under subsection (a) and documentation of goals as required by paragraph (1) of such subsection, an applicant may provide reasoning for why the recruitment of each of the population groups specified in paragraph (1) of subsection (a) is not necessary and why such recruitment is not scientifically justified or possible.\n#### 3. Eliminating cost barriers\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the National Institutes of Health, shall conduct and complete a study on\u2014\n**(1)**\nthe need for review of human subject regulations specified in part 46 of title 45, Code of Federal Regulations (or successor regulations), and related guidance;\n**(2)**\nthe modernization of such regulations and guidance to establish updated guidelines for reimbursement of out-of-pocket expenses of human subjects, compensation of human subjects for time spent participating in the clinical trial, and incentives for recruitment of human subjects; and\n**(3)**\nthe need for updated safe harbor rules under section 1001.952 of title 42, Code of Federal Regulations (or successor regulations), and section 1128B of the Social Security Act (commonly referred to as the Federal Anti-Kickback Statute ( 42 U.S.C. 1320a\u20137b )) with respect to the assistance provided under this section.\n#### 4. Public awareness and education campaign\n##### (a) National campaign\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in consultation with the stakeholders specified in subsection (e), shall carry out a national campaign to increase the awareness and knowledge of individuals in the United States, including health care professionals, patients, and others, with respect to the need for diverse clinical trials among the demographic groups identified pursuant to section 2(a)(1).\n##### (b) Requirements\nThe national campaign conducted under this section shall include\u2014\n**(1)**\n**(A)**\nthe development and distribution of written educational materials;\n**(B)**\nthe development and placing of public service announcements that are intended to encourage individuals who are members of the demographic groups identified pursuant to section 2(b)(1)(A)(i) to seek to participate in clinical trials; and\n**(C)**\nthe development of curricula for health care professionals on\u2014\n**(i)**\nhow to participate in clinical trials as an investigator; and\n**(ii)**\nhow such professionals can enroll patients in trials;\n**(2)**\nsuch efforts as are reasonable and necessary to ensure meaningful access by consumers with limited English proficiency; and\n**(3)**\nthe development and distribution of best practices and training for recruiting underrepresented study populations, including a method for sharing such best practices among clinical trial sponsors, providers, community-based organizations who assist with recruitment, and with the public.\n##### (c) Health disparities\nIn developing the national campaign under subsection (a), the Secretary shall recognize and address\u2014\n**(1)**\nhealth disparities among individuals who are members of the population groups specified in section 2(b)(1)(A) with respect to access to care and participation in clinical trials; and\n**(2)**\nany barriers in access to care and participation in clinical trials that are specific to individuals who are members of such groups.\n##### (d) Grants\nThe Secretary shall establish a program to award grants to nonprofit private entities (including community-based organizations and faith communities, institutions of higher education eligible to receive funds under section 371 of the Higher Education Act of 1965 ( 20 U.S.C. 1067q ), national organizations that serve underrepresented populations, and community pharmacies) to enable such entities\u2014\n**(1)**\nto test alternative outreach and education strategies to increase the awareness and knowledge of individuals in the United States, with respect to the need for diverse clinical trials that reflect the race, ethnicity, age, and sex of patients with the disease or condition being investigated; and\n**(2)**\nto cover administrative costs of such entities in assisting in diversifying clinical trials subject to section 2.\n##### (e) Stakeholders specified\nThe stakeholders specified in this subsection are the following:\n**(1)**\nRepresentatives of the Food and Drug Administration, the Health Resources and Services Administration, the Office on Minority Health of the Department of Health and Human Services, the Centers for Disease Control and Prevention, and the National Institutes of Health.\n**(2)**\nCommunity-based resources and advocates.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2029.\n#### 5. Definition\nIn this Act, the term clinical trial means a research study in which one or more human subjects are prospectively assigned to one or more interventions (which may include placebo or other control) to evaluate the effects of those interventions on health-related biomedical or behavioral outcomes.",
      "versionDate": "2025-12-18",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-22T15:35:48Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3564is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NIH Clinical Trial Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NIH Clinical Trial Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services, acting through the Director of the National Institutes of Health, to take certain steps to increase clinical trial diversity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:17Z"
    }
  ]
}
```
