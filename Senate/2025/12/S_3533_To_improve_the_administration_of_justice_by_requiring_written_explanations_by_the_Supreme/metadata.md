# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3533
- Title: Shadow Docket Sunlight Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3533
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3533",
    "number": "3533",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Shadow Docket Sunlight Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
            "date": "2025-12-17T19:24:02Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-17T19:24:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3533is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3533\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Blumenthal (for himself, Mr. Booker , Mr. Durbin , Ms. Klobuchar , Mr. Padilla , Mr. Reed , Mr. Sanders , Mr. Schiff , Mr. Schumer , Ms. Smith , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo improve the administration of justice by requiring written explanations by the Supreme Court of its decisions and the disclosure of votes by justices in cases within the appellate jurisdiction of the Supreme Court that involve preliminary injunctive relief, and other purposes.\n#### 1. Short title\nThis Act may be cited as the Shadow Docket Sunlight Act of 2025 .\n#### 2. Supreme Court written explanations and disclosure of voting in cases involving preliminary injunctive relief\n##### (a) In general\nChapter 155 of title 28, United States Code, is amended by adding at the end the following:\n2285. Written explanations and disclosure of voting in Supreme Court cases involving preliminary injunctive relief (a) Definitions In this section\u2014 (1) the term Supreme Court means the Supreme Court of the United States, including any individual justice or set of justices when acting on behalf of the Supreme Court of the United States; and (2) the term Supreme Court\u2019s appellate jurisdiction means all cases within the jurisdiction of the Supreme Court other than those within the original jurisdiction of the Supreme Court. (b) Requirement (1) Written explanation and vote disclosure In any case within the Supreme Court\u2019s appellate jurisdiction, the Supreme Court may not issue any order granting, denying, or vacating preliminary injunctive relief or granting, denying, or vacating a stay of preliminary injunctive relief unless the Supreme Court publishes a written explanation of reasons supporting such order and indicates in writing how each participating justice voted regarding such order. (2) Contents for orders granting, denying, or vacating preliminary injunctive relief The written explanation required under paragraph (1) for an order granting, denying, or vacating preliminary injunctive relief shall include an evaluation of the following criteria: (A) Whether an applicant seeking preliminary injunctive relief is likely to succeed on the merits. (B) Whether an applicant seeking preliminary injunctive relief is likely to suffer irreparable harm absent such relief. (C) Whether the balance of equities tips in the favor of an applicant seeking preliminary injunctive relief. (D) Whether preliminary injunctive relief is in the public interest. (3) Contents for orders granting, denying, or vacating a stay of preliminary injunctive relief The written explanation required under paragraph (1) for an order granting, denying, or vacating a stay of preliminary injunctive relief shall include an evaluation of the following criteria: (A) Whether the stay applicant has made a strong showing of the likelihood of success on the merits. (B) Whether the stay applicant will be irreparably injured absent a stay. (C) Whether issuance of the stay will substantially injure the other parties interested in the proceeding. (D) Whether a stay is in the public interest. (4) Multiple opinions The written explanation required under paragraph (1) may be made in 1 or more opinions representing a majority of justices participating in a decision, without regard to whether a majority of the justices participating in a decision publish the same written explanation. (5) Administrative and scheduling orders excluded The requirements of this subsection shall not apply to orders granting or denying applications that relate only to administrative or scheduling matters or petitions for certiorari and that do not grant, deny, or vacate preliminary injunctive relief or grant, deny, or vacate a stay of preliminary injunctive relief. (c) Limitations and inclusions In implementing this section, the following shall apply: (1) Nothing in this section shall be construed to modify the substantive standards applied by any court in deciding any case. (2) Nothing in this section shall be construed to modify the jurisdiction of the Supreme Court under any other law. (3) This section shall apply with respect to orders issued in connection with a claim under chapter 5 or 7 of title 5. .\n##### (b) Conforming amendment\nThe table of sections for chapter 155 of title 28, United States Code, is amended by adding at the end the following:\n2285. Written explanations and disclosure of voting in Supreme Court cases involving preliminary injunctive relief. .\n#### 3. Reports\n##### (a) In general\nNot later than April 1 of the first year that begins more than 180 days after the date of enactment of this Act, and April 1 of every second year thereafter, the Director of the Federal Judicial Center shall submit to Congress a report\u2014\n**(1)**\nassessing the extent of compliance or noncompliance with the requirements of section 2285 of title 28, United States Code, as added by section 2 of this Act; and\n**(2)**\nproviding any recommendations of the Director regarding ways to improve compliance with such section 2285.\n##### (b) Additional time\nFor the first report required under subsection (a), the Director of the Federal Judicial Center may submit the report after the date described in that subsection if the Director identifies in writing to Congress the amount of additional time needed for completion of the report.\n#### 4. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any particular person or circumstance is held invalid, the remaining provisions of this Act and the amendments made by this Act, and the application of such remaining provisions and amendments to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-12-17",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6816",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shadow Docket Sunlight Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-01-14T16:22:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3533is.xml"
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
      "title": "Shadow Docket Sunlight Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shadow Docket Sunlight Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the administration of justice by requiring written explanations by the Supreme Court of its decisions and the disclosure of votes by justices in cases within the appellate jurisdiction of the Supreme Court that involve preliminary injunctive relief, and other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:48:21Z"
    }
  ]
}
```
