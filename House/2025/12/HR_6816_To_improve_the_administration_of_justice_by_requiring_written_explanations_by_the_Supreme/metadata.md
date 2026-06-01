# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6816?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6816
- Title: Shadow Docket Sunlight Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6816
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-21T05:04:02Z
- Update date including text: 2026-01-21T05:04:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6816",
    "number": "6816",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Shadow Docket Sunlight Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-21T05:04:02Z",
    "updateDateIncludingText": "2026-01-21T05:04:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6816ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6816\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Ross (for herself, Mr. Raskin , Mr. Johnson of Georgia , Ms. Scanlon , and Mr. Correa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo improve the administration of justice by requiring written explanations by the Supreme Court of its decisions and the disclosure of votes by justices in cases within the appellate jurisdiction of the Supreme Court that involve preliminary injunctive relief, and other purposes.\n#### 1. Short title\nThis Act may be cited as the Shadow Docket Sunlight Act of 2025 .\n#### 2. Supreme Court written explanations and disclosure of voting in cases involving preliminary injunctive relief\n##### (a) In general\nChapter 155 of title 28, United States Code, is amended by adding at the end the following:\n2285. Written explanations and disclosure of voting in Supreme Court cases involving preliminary injunctive relief (a) Definitions In this section\u2014 (1) the term Supreme Court means the Supreme Court of the United States, including any individual justice or set of justices when acting on behalf of the Supreme Court of the United States; and (2) the term Supreme Court\u2019s appellate jurisdiction means all cases within the jurisdiction of the Supreme Court other than those within the original jurisdiction of the Supreme Court. (b) Requirement (1) Written explanation and vote disclosure In any case within the Supreme Court\u2019s appellate jurisdiction, the Supreme Court may not issue any order granting, denying, or vacating preliminary injunctive relief or granting, denying, or vacating a stay of preliminary injunctive relief unless the Supreme Court publishes a written explanation of reasons supporting such order and indicates in writing how each participating justice voted regarding such order. (2) Contents for orders granting, denying, or vacating preliminary injunctive relief The written explanation required under paragraph (1) for an order granting, denying, or vacating preliminary injunctive relief shall include an evaluation of the following criteria: (A) Whether an applicant seeking preliminary injunctive relief is likely to succeed on the merits. (B) Whether an applicant seeking preliminary injunctive relief is likely to suffer irreparable harm absent such relief. (C) Whether the balance of equities tips in the favor of an applicant seeking preliminary injunctive relief. (D) Whether preliminary injunctive relief is in the public interest. (3) Contents for orders granting, denying, or vacating a stay of preliminary injunctive relief The written explanation required under paragraph (1) for an order granting, denying, or vacating a stay of preliminary injunctive relief shall include an evaluation of the following criteria: (A) Whether the stay applicant has made a strong showing of the likelihood of success on the merits. (B) Whether the stay applicant will be irreparably injured absent a stay. (C) Whether issuance of the stay will substantially injure the other parties interested in the proceeding. (D) Whether a stay is in the public interest. (4) Multiple opinions The written explanation required under paragraph (1) may be made in 1 or more opinions representing a majority of justices participating in a decision, without regard to whether a majority of the justices participating in a decision publish the same written explanation. (5) Administrative and scheduling orders excluded The requirements of this subsection shall not apply to orders granting or denying applications that relate only to administrative or scheduling matters or petitions for certiorari and that do not grant, deny, or vacate preliminary injunctive relief or grant, deny, or vacate a stay of preliminary injunctive relief. (c) Limitations and inclusions In implementing this section, the following shall apply: (1) Nothing in this section shall be construed to modify the substantive standards applied by any court in deciding any case. (2) Nothing in this section shall be construed to modify the jurisdiction of the Supreme Court under any other law. (3) This section shall apply with respect to orders issued in connection with a claim under chapter 5 or 7 of title 5. .\n##### (b) Conforming amendment\nThe table of sections for chapter 155 of title 28, United States Code, is amended by adding at the end the following:\n2285. Written explanations and disclosure of voting in Supreme Court cases involving preliminary injunctive relief. .\n#### 3. Reports\n##### (a) In general\nNot later than April 1 of the first year that begins more than 180 days after the date of enactment of this Act, and April 1 of every second year thereafter, the Director of the Federal Judicial Center shall submit to Congress a report\u2014\n**(1)**\nassessing the extent of compliance or noncompliance with the requirements of section 2285 of title 28, United States Code, as added by section 2 of this Act; and\n**(2)**\nproviding any recommendations of the Director regarding ways to improve compliance with such section 2285.\n##### (b) Additional time\nFor the first report required under subsection (a), the Director of the Federal Judicial Center may submit the report after the date described in that subsection if the Director identifies in writing to Congress the amount of additional time needed for completion of the report.\n#### 4. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any particular person or circumstance is held invalid, the remaining provisions of this Act and the amendments made by this Act, and the application of such remaining provisions and amendments to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-12-17",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3533",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shadow Docket Sunlight Act of 2025",
      "type": "S"
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
        "name": "Law",
        "updateDate": "2025-12-19T15:47:45Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6816ih.xml"
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
      "title": "Shadow Docket Sunlight Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shadow Docket Sunlight Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T10:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the administration of justice by requiring written explanations by the Supreme Court of its decisions and the disclosure of votes by justices in cases within the appellate jurisdiction of the Supreme Court that involve preliminary injunctive relief, and other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T10:03:45Z"
    }
  ]
}
```
