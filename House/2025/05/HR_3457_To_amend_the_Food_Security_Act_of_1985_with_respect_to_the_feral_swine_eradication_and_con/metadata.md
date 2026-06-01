# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3457
- Title: To amend the Food Security Act of 1985 with respect to the feral swine eradication and control program, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3457
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-08-27T08:05:37Z
- Update date including text: 2025-08-27T08:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3457",
    "number": "3457",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "To amend the Food Security Act of 1985 with respect to the feral swine eradication and control program, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:37Z",
    "updateDateIncludingText": "2025-08-27T08:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-17",
      "state": "AL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3457ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3457\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Moore of Alabama (for himself, Ms. Crockett , and Mr. Jackson of Texas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 with respect to the feral swine eradication and control program, and for other purposes.\n#### 1. Feral swine eradication and control program\n##### (a) Feral swine eradication and control program\nChapter 5 of subtitle D of the Food Security Act of 1985 ( 16 U.S.C. 3839bb et seq. ) is amended by inserting after section 1240M the following:\n1240N. Feral swine eradication and control program (a) In general The Secretary shall establish a feral swine eradication and control program (in this section referred to as the program ) to respond to the threat feral swine pose to agriculture, native ecosystems, and human and animal health. (b) Duties of the Secretary In carrying out the program, the Secretary shall\u2014 (1) study and assess the nature and extent of damage to the threatened areas caused by feral swine; (2) develop methods to eradicate or control feral swine in the threatened areas; (3) develop methods to restore damage caused by feral swine; and (4) provide financial assistance to agricultural producers in threatened areas. (c) Assistance The Secretary may provide financial assistance to agricultural producers under the program to implement methods to\u2014 (1) eradicate or control feral swine in the threatened areas; and (2) restore damage caused by feral swine. (d) Coordination The Secretary shall ensure that the Natural Resources Conservation Service and the Animal and Plant Health Inspection Service coordinate for purposes of this section through State technical committees established under section 1261(a). (e) Contracts with land-Grant colleges and universities (1) In general The Secretary shall direct the Natural Resources Conservation Service and the Animal and Plant Health Inspection Service to enter into a contract with 1 or more land-grant colleges or universities to carry out activities under the program. (2) Eligible land-grant colleges and universities A land-grant college or university is eligible to enter into a contract under paragraph (1) if such college or university\u2014 (A) has developed and implemented a system of evaluating damages from feral swine and the effectiveness of control and eradication efforts; (B) shows evidence of a strong working relationship with the Animal and Plant Health Inspection Service, Wildlife Services; and (C) has maintained a State-funded, non-Federal Wildlife Services program that has in place an active cooperative agreement with the Animal and Plant Health Inspection Service, Wildlife Services. (3) Role of land-grant college or university A land-grant college or university that enters into a contract under paragraph (1) shall provide educational support and assistance with control and eradication efforts under the program by\u2014 (A) identifying, and carrying out research on, novel methods of feral swine control and eradication and land remediation; (B) assisting the Secretary in identifying threatened areas; (C) coordinating and collaborating with field staff, programmatic staff, and research staff within the Natural Resources Conservation Service and the Animal and Plant Health Inspection Service; and (D) consulting with the Secretary on the establishment of goals and plans for research to be carried out under the program. (f) Cost Sharing (1) Federal share The Federal share of the costs of activities under the program may not exceed 75 percent of the total costs of such activities. (2) In-kind contributions The non-Federal share of the costs of activities under the program may be provided in the form of in-kind contributions of materials or services. (g) Definitions In this section: (1) Land-grant college or university The term land-grant college or university has the meaning given the term land-grant colleges and universities in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 ). (2) Threatened area The term threatened area means an area of a State in which feral swine have been identified as a threat to agriculture, native ecosystems, or human and animal health, as determined by the Secretary. (h) Funding (1) Mandatory funding Of the funds made available under section 1241(a)(3)(A), the Secretary shall use to carry out this section $150,000,000 for the period of fiscal years 2026 through 2030. (2) Distribution of funds Of the funds made available under paragraph (1)\u2014 (A) 40 percent shall be allocated to the Natural Resources Conservation Service to carry out the program, including the provision of financial assistance to producers for on-farm trapping and technology related to capturing and confining feral swine; and (B) 60 percent shall be allocated to the Animal and Plant Health Inspection Service to carry out the program, including the use of established, and testing of innovative, population reduction methods. (3) Limitation on administrative expenses Not more than 10 percent of funds made available under this section may be used for administrative expenses of the program. .\n##### (b) Repeal\nSection 2408 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 8351 note) is repealed.\n##### (c) Clerical amendment\nThe table of contents in section 1(b) of the Agriculture Improvement Act of 2018 is amended by striking the item relating to section 2408.",
      "versionDate": "2025-05-15",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-10T22:54:57Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3457ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 with respect to the feral swine eradication and control program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:15Z"
    },
    {
      "title": "To amend the Food Security Act of 1985 with respect to the feral swine eradication and control program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T08:06:28Z"
    }
  ]
}
```
