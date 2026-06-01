# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8710?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8710
- Title: National Defense Data Resilience Act
- Congress: 119
- Bill type: HR
- Bill number: 8710
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-13T21:21:14Z
- Update date including text: 2026-05-13T21:21:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8710",
    "number": "8710",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "National Defense Data Resilience Act",
    "type": "HR",
    "updateDate": "2026-05-13T21:21:14Z",
    "updateDateIncludingText": "2026-05-13T21:21:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-05-07T13:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8710ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8710\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Subramanyam (for himself and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to require the Secretary of Defense to implement resilient capabilities to recover critical Department of Defense data in the event such data is lost, degraded, or destroyed, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Defense Data Resilience Act .\n#### 2. Data recovery requirements and strategy\n##### (a) Data recovery requirements\nChapter 19 of title 10, United States Code, is amended by inserting after section 391b the following new section:\n391c. Data recovery requirements (a) Mandatory recovery time objectives (1) The Secretary of Defense shall, with respect to each element of the Department of Defense, carry out the following: (A) Designate data as one of the following types, as applicable: (i) Critical data. (ii) Important data. (iii) Necessary data. (B) Not later than 180 days after the date of the enactment of this section, establish mandatory recovery time objectives for data so designated as critical data. (C) Not later than 270 days after the date of the enactment of this section, establish mandatory recovery time objectives for data so designated as important data or necessary data. (2) Each recovery time objective established under paragraph (1) shall satisfy the following requirements: (A) Be based upon the type of data to which such objective applies, including with respect to threat exposure. (B) Be updated in response to intelligence on evolving threats from state and non-state actors, including the People\u2019s Republic of China. (3) Not later than one year after the date of the enactment of this section and annually thereafter, the Secretary of Defense shall, for each element of the Department of Defense, submit to the congressional defense committees an auditable recovery certification report that includes information relating to the following: (A) Each recovery time objective that is established under paragraph (1) and applies to such element. (B) Whether such objective satisfies the requirements listed in paragraph (2). (b) Data recovery capability requirements (1) Not later than 180 days after the date of the enactment of this section, the Secretary of Defense shall, for data designated as critical data pursuant to subparagraph (A) of subsection (a)(1), field data recovery capabilities that satisfy the following requirements: (A) Prioritize providing critical services in support of national defense. (B) Include the following: (i) Immutable backups that satisfy the following requirements: (I) Preserve logically separated copies of data. (II) Are selectively segmented or isolated from external networks by means of software, firewalls, or other controls. (ii) Continuous monitoring of backup environments to detect tampering, insider threats, and malicious corruption. (iii) Annual recovery exercises that simulate sophisticated nation-state cyberattacks designed to cripple data systems. (iv) Audits in which external or internal independent groups mimic tactics, techniques, and procedures of cyberattacks to assess and validate the ability of each element of the Department of Defense to carry out the objectives established under such subsection with respect to realistic threat conditions. (2) Not later than 270 days after the date of the enactment of this section, the Secretary of Defense shall, for data designated as important data or necessary data pursuant to subsection (a)(1)(A), field data recovery capabilities described in paragraph (1). (c) Approved technology standards In fielding a data recovery capability under subsection (b), the Secretary of Defense may not adopt technology unless the following requirements are satisfied: (1) Such technology is listed in an inventory of the Department of Defense for certified cybersecurity and data protection technology. (2) If such technology is technology for recovering or repairing damaged or lost data, such technology provides for the following: (A) Immutable storage. (B) Robust recovery capabilities. (C) Full audit trails. (D) Continuous monitoring for data integrity and anomalous activity. (d) Definitions In this section: (1) The term critical data means data, so vital to the United States, that the incapacity or destruction of such data would have a debilitating impact on security, national economic security, national public health or safety, or any combination thereof. (2) The term data recovery capability means a technology, process, or governance framework to ensure rapid, secure, and verifiable recovery after a destructive cyberattack. (3) The term important data means data that is important to the United States and the incapacity or destruction of such data would have a significant impact on security, national economic security, national public health or safety, or any combination thereof. (4) The term necessary data means data, the incapacity or destruction of which would have a measurable impact on security, national economic security, national public health or safety, or any combination thereof. (5) The term recovery time objective means the maximum allowable time the Secretary of Defense determines necessary to restore critical functions and data following a cyberattack. .\n##### (b) Clerical amendment\nThe table of sections for chapter 19 of title 10, United States Code, is amended by inserting after the item relating to section 391b the following new item:\n391c. Data recovery requirements. .\n##### (c) Data recovery strategy\n**(1)**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the congressional defense committees a data recovery strategy for the Department of Defense that includes information relating to the following:\n**(A)**\nRecovery time objectives for such strategy.\n**(B)**\nThe technology necessary for such objectives.\n**(C)**\nOversight processes with respect to such strategy.\n**(D)**\nThe funds necessary to carry out such strategy.\n**(2)**\nThe strategy under paragraph (1) shall be submitted in unclassified form, but may contain a classified annex.\n**(3)**\nIn this subsection, the term recovery time objective means the maximum allowable time the Secretary of Defense determines necessary to restore critical functions and data following a cyberattack.",
      "versionDate": "2026-05-07",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-05-13T21:21:14Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8710ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "National Defense Data Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T07:38:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Defense Data Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T07:38:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to require the Secretary of Defense to implement resilient capabilities to recover critical Department of Defense data in the event such data is lost, degraded, or destroyed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T07:33:43Z"
    }
  ]
}
```
