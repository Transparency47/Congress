# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3401?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3401
- Title: Retreaded Tire Jobs, Supply Chain Security and Sustainability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3401
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-03-18T08:06:44Z
- Update date including text: 2026-03-18T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3401",
    "number": "3401",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Retreaded Tire Jobs, Supply Chain Security and Sustainability Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T08:06:44Z",
    "updateDateIncludingText": "2026-03-18T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-14T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "OH"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-07-07",
      "state": "KS"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NC"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3401ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3401\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. LaHood (for himself and Mrs. Sykes ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish the retreaded tire credit, to require Federal agencies to consider the use of retreaded tires, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Retreaded Tire Jobs, Supply Chain Security and Sustainability Act of 2025 .\n#### 2. Credit for certain retreaded tires\n##### (a) In general\nPart IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end of subpart D the following new section:\n45BB. Retreaded tire credit (a) In general For purposes of section 38, the retreaded tire credit for any taxable year is an amount equal to the sum of the credit amounts determined under subsection (b) with respect to the taxpayer for the taxable year. (b) Per tire amount There shall be a credit equal to so much of the qualified tire retreading expenses of the taxpayer as do not exceed the lesser of\u2014 (1) 30 percent of the amount paid or incurred by the taxpayer to purchase qualified retreaded tires placed in service during the taxable year, or (2) the product of $30 multiplied by the number of qualified retreaded tires placed in service by the taxpayer during the taxable year. (c) Qualified retreaded tire The term qualified retreaded tire means a retreaded tire\u2014 (1) retreaded in the United States, and (2) purchased by the taxpayer in the United States. (d) Regulations and guidance The Secretary shall issue such regulations and guidance as the Secretary determines necessary to carry out the purposes of this section. (e) Termination No credit shall be determined under this section with respect to qualified retreaded tires placed in service after December 31, 2028. .\n##### (b) Credit allowed as part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41), and by adding at the end the following new paragraph:\n(42) the retreaded tire credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Retreaded tire credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to tires placed in service after December 31, 2025.\n#### 3. Use of retreaded tires for Federal fleets\n##### (a) Requirement\nIn any case in which a retreaded tire is available on the General Services Administration tire schedule in the size, load range, and tread designation desired, the head of an agency shall order such tire instead of a new, not retread-able tire.\n##### (b) FAR revision\nNot later than 1 year after the date of the enactment of this Act, the Federal Acquisition Regulation shall be updated to include the requirements of this section.\n##### (c) Agency defined\nThe term agency has the meaning given the term executive agency in section 133 of title 41, United States Code.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2790",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Resilient Tire Supply and Jobs Act",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:34:55Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3401ih.xml"
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
      "title": "Retreaded Tire Jobs, Supply Chain Security and Sustainability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retreaded Tire Jobs, Supply Chain Security and Sustainability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish the retreaded tire credit, to require Federal agencies to consider the use of retreaded tires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:25Z"
    }
  ]
}
```
