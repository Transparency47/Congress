# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4220
- Title: Veterans Health Administration Novel Therapeutics Preparedness Act
- Congress: 119
- Bill type: S
- Bill number: 4220
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-30T11:03:21Z
- Update date including text: 2026-04-30T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4220",
    "number": "4220",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Veterans Health Administration Novel Therapeutics Preparedness Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:21Z",
    "updateDateIncludingText": "2026-04-30T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
        "item": [
          {
            "date": "2026-04-29T21:37:46Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-26T16:41:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4220is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4220\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Sheehy (for himself, Mr. Gallego , Ms. Duckworth , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish within the Veterans Health Administration an Office of Novel Therapeutics, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Health Administration Novel Therapeutics Preparedness Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEmerging therapeutic interventions, including certain psychedelic-assisted therapies under evaluation by the Food and Drug Administration as of the date of the enactment of this Act, may significantly alter the treatment landscape for post-traumatic stress disorder, depression, and other mental health conditions affecting veterans.\n**(2)**\nThe administration of certain emerging therapies may require intensive clinical engagement, interdisciplinary teams, dedicated clinical space, structured preparation, and post-treatment integration that differ substantially from traditional outpatient mental health services.\n**(3)**\nThe Department of Veterans Affairs is uniquely positioned to deliver integrated, veteran-centered care that combines medical, mental health, and peer support services within a single system of care.\n**(4)**\nAbsent centralized governance and implementation planning, the Department may face delays, safety risks, or inconsistent access following regulatory approval of such therapies.\n**(5)**\nEstablishing a dedicated Office of Novel Therapeutics will ensure that the Department is prepared to responsibly evaluate, research, and implement emerging treatment modalities consistent with patient safety and evidence-based practice.\n#### 3. Establishment of Office of Novel Therapeutics within Veterans Health Administration\n##### (a) Establishment\n**(1) In general**\nChapter 73 of title 38, United States Code, is amended by adding at the end the following new subchapter:\nVI Novel Therapeutics 7391. Definitions In this subchapter: (1) Center of excellence The term center of excellence means a medical center of the Department designated under section 7394 of this title as a center of excellence for novel therapeutics to advance research, training, and implementation of emerging therapeutic interventions. (2) Emerging therapeutic intervention The term emerging therapeutic intervention means a pharmacological, biological, or other therapeutic modality under evaluation or review by the Food and Drug Administration. 7392. Office of Novel Therapeutics (a) Establishment There is established within the Veterans Health Administration, under the Office of the Under Secretary for Health, an Office of Novel Therapeutics (in this section referred to as the Office ). (b) Director The head of the Office shall be the Director of the Office of Novel Therapeutics, who shall be appointed by the Under Secretary for Health and who shall\u2014 (1) possess demonstrated expertise in clinical research and implementation science; and (2) report directly to the Under Secretary for Health. (c) Coordinating authority The Office shall serve as the primary coordinating authority within the Veterans Health Administration for matters relating to emerging and novel therapeutic interventions. (d) Duties The Office shall\u2014 (1) develop and oversee national policy, guidance, and clinical standards for the evaluation, research, and potential implementation by the Veterans Health Administration of emerging and novel therapeutic interventions for mental health conditions affecting veterans; (2) develop a national clinical model for the administration of intensive therapeutic interventions, including structured preparation, monitored administration, and post-administration integration; (3) develop guidance regarding patient eligibility and candidacy for emerging therapeutic interventions, ensuring that utilization management or step therapy requirements do not unduly restrict access where clinically appropriate; (4) develop implementation-readiness plans for therapies that may receive approval from the Food and Drug Administration, including\u2014 (A) facility infrastructure requirements; (B) interdisciplinary team composition standards; (C) allocation of protected clinical time necessary to safely administer intensive therapeutic interventions, including full session and integration requirements; (D) patient safety and adverse event monitoring and response protocols; and (E) integration with suicide prevention, post-traumatic stress disorder, and substance use disorder programs; (5) conduct a workforce-readiness assessment to identify clinicians and peer support specialists with prior training or certification relevant to emerging therapeutic interventions and gaps in training, supervision, and clinical capacity necessary to support safe and effective implementation of such interventions; (6) establish national training and credentialing standards for clinicians administering novel therapeutics; (7) develop a standardized, competency-based training framework for clinicians and peer support specialists participating in emerging therapeutic interventions, including preparation, monitored administration, integration, safety monitoring, interdisciplinary collaboration, and culturally competent care; (8) distinguish between research protocols and clinical implementation standards to ensure that patient care models are not constrained solely by sponsor-driven research design; (9) coordinate with the Office of Research and Development\u2014 (A) to align research priorities with implementation-readiness needs; (B) to recommend specialized review pathways for research involving emerging therapeutic interventions; and (C) to develop standards for allocation of protected research time for clinicians participating in research involving emerging therapeutic interventions, including clarification that patients seen under approved research protocols shall be counted toward standard clinical productivity metrics; (10) develop guidance to ensure continuity of care, including\u2014 (A) post-administration integration services; (B) incorporation of peer support specialists; and (C) coordination with community-based organizations for aftercare support as appropriate; (11) identify not fewer than one medical center in each Veterans Integrated Service Network to develop infrastructure and workforce-readiness for emerging therapeutic models; and (12) establish criteria for the designation of centers of excellence and oversee compliance with national standards. 7393. Clinical Implementation Program for Emerging Therapeutics (a) Establishment The Secretary, acting through the Office of Novel Therapeutics, shall establish a Clinical Implementation Program for Emerging Therapeutics (in this section referred to as the Program ) to evaluate the effectiveness, feasibility, safety, and scalability of emerging therapeutic interventions within the Department. (b) Purpose The Program shall\u2014 (1) utilize effectiveness-implementation hybrid models to evaluate both clinical outcomes and real-world implementation factors with respect to emerging therapeutic interventions; (2) test and refine care delivery models, including patient eligibility criteria, safety protocols, interdisciplinary team models, and post-administration integration services; (3) generate real-world evidence to inform potential systemwide adoption; and (4) assess workforce, infrastructure, cost, and operational requirements necessary for broader implementation. (c) Covered conditions In carrying out the Program, the Secretary may prioritize one or more brain or mental health conditions affecting veterans, including\u2014 (1) post-traumatic stress disorder; (2) treatment-resistant depression; (3) substance use disorders; (4) suicidality; (5) traumatic brain injury; (6) repetitive low-level blast exposure; (7) chronic pain; (8) co-occurring conditions; and (9) other clinically appropriate conditions as determined appropriate by the Secretary. (d) Site selection The Secretary may conduct the Program at\u2014 (1) one or more centers of excellence; and (2) such other medical centers as the Secretary determines appropriate. 7394. Centers of excellence for novel therapeutics (a) Designation The Secretary may designate one or more medical centers of the Department as centers of excellence for novel therapeutics. (b) Functions Each center of excellence designated under subsection (a) shall\u2014 (1) serve as a national leader in research, clinical training, and implementation of emerging therapeutic interventions; (2) develop and disseminate best practices and clinical standards across the Veterans Health Administration; (3) provide technical assistance and training to other medical centers of the Department; (4) integrate interdisciplinary care models, including peer support and post-administration integration services; (5) incorporate veteran advisory input into program development; and (6) coordinate with academic affiliates and external research partners, as appropriate. (c) Coordination Centers of excellence designated under subsection (a) shall operate in coordination with, and under standards established by, the Office of Novel Therapeutics. 7395. Veteran Advisory Committee on Novel Therapeutics (a) Establishment The Secretary shall establish a Veteran Advisory Committee on Novel Therapeutics (in this section referred to as the Committee ) to advise the Office of Novel Therapeutics. (b) Membership The Secretary shall select the members of the Committee, which shall include the following: (1) Veterans with lived experience of mental health treatment furnished by the Department. (2) Veterans who have participated in clinical research involving emerging therapeutic interventions, as applicable. (3) Family members or caregivers of veterans described in paragraph (1) or (2). (4) Representatives from academic institutions affiliated with the Department with expertise in clinical research, behavioral health, or emerging therapeutic interventions. (5) Subject matter experts as determined appropriate by the Secretary. (c) Duties With respect to the use of novel therapeutics, the Committee shall provide input on\u2014 (1) patient safety considerations; (2) informed consent practices; (3) implementation and access barriers; and (4) patient-centered care design. 7396. Interagency coordination In carrying out this subchapter, the Secretary shall coordinate with the Secretary of Health and Human Services, the Commissioner of Food and Drugs, the Administrator of the Centers for Medicare & Medicaid Services, the Secretary of Defense, and the Administrator of the Drug Enforcement Administration to support\u2014 (1) regulatory readiness; (2) development of reimbursement and billing pathways; (3) scheduling and rescheduling considerations, as appropriate; and (4) shared data infrastructure for monitoring safety, quality, and outcomes. 7397. Annual report Not less frequently than annually, the Secretary shall submit to Congress a report describing\u2014 (1) research activities of the Department relating to emerging therapeutic interventions; (2) clinical outcomes and patient-reported outcomes under the Clinical Implementation Program for Emerging Therapeutics under section 7393 of this title; (3) safety events and adverse outcomes; (4) workforce readiness and training capacity; (5) implementation barriers, including staffing, procurement, and infrastructure needs; and (6) recommendations for legislative or administrative action relating to novel therapeutics. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 73 of such title is amended by adding at the end the following:\nSUBCHAPTER VI\u2014Novel Therapeutics Sec. 7391. Definitions. 7392. Office of Novel Therapeutics. 7393. Clinical Implementation Program for Emerging Therapeutics. 7394. Centers of excellence for novel therapeutics. 7395. Veteran Advisory Committee on Novel Therapeutics. 7396. Interagency coordination. 7397. Annual report. .\n##### (b) National preparedness and implementation strategy\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a national preparedness and implementation strategy of the Veterans Health Administration for emerging mental health therapeutics, including\u2014\n**(1)**\nworkforce capacity assessments;\n**(2)**\nfacility modification needs;\n**(3)**\nprojected timelines for phased implementation; and\n**(4)**\nbarriers to implementation.",
      "versionDate": "2026-03-26",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-15T01:42:38Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4220is.xml"
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
      "title": "Veterans Health Administration Novel Therapeutics Preparedness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Health Administration Novel Therapeutics Preparedness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish within the Veterans Health Administration an Office of Novel Therapeutics, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:23Z"
    }
  ]
}
```
