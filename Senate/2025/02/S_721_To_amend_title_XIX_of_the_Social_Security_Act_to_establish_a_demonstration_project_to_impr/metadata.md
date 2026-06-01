# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/721?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/721
- Title: Sickle Cell Disease Comprehensive Care Act
- Congress: 119
- Bill type: S
- Bill number: 721
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:07:27Z
- Update date including text: 2025-12-05T22:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/721",
    "number": "721",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Sickle Cell Disease Comprehensive Care Act",
    "type": "S",
    "updateDate": "2025-12-05T22:07:27Z",
    "updateDateIncludingText": "2025-12-05T22:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T19:42:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "SC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "LA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s721is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 721\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Booker (for himself and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to establish a demonstration project to improve outpatient clinical care for individuals with sickle cell disease.\n#### 1. Short title\nThis Act may be cited as the Sickle Cell Disease Comprehensive Care Act .\n#### 2. Enabling State Medicaid programs to provide care through health homes to individuals with sickle cell disease\nSection 1945 of the Social Security Act ( 42 U.S.C. 1396w\u20134 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting (and, beginning January 1, 2026, to eligible individuals with sickle cell disease (as defined in subsection (c)(5))) after chronic conditions ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by inserting and each eligible individual with sickle cell disease after chronic conditions ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) Special rule relating to sickle cell disease health homes (A) In general Beginning January 1, 2026, the Secretary may approve a State plan amendment under this section that is designed to provide health home services primarily to eligible individuals with sickle cell disease (in this section referred to as a sickle cell disease-focused State plan amendment ). (B) Requirement to provide dental and vision services In the case of a sickle cell disease-focused State plan amendment approved by the Secretary on or after January 1, 2026, a State shall ensure the provision of dental and vision services to eligible individuals with sickle cell disease who are enrolled in such health home. Such requirement shall apply irrespective of existing requirements related to comparability or whether or not the State provides dental or vision services to other Medicaid beneficiaries. (C) Report requirements (i) In general In the case of a State with a sickle cell disease-focused State plan amendment, such State shall, at the end of the first 8 fiscal year quarters that such State plan amendment is in effect, submit to the Secretary a report on the following, with respect to eligible individuals with sickle cell disease provided health home services under such State plan amendment: (I) The quality of health care provided to such individuals, with a focus on outcomes relevant to the recovery of each such individual. (II) The access of such individuals to health care. (III) The total expenditures of such individuals for health care. (ii) Applicable measures For purposes of the report required under this subparagraph, the Secretary shall specify all applicable measures for determining quality of health care provided to eligible individuals with sickle cell disease, access to health care by such individuals, and expenditures on health care by such individuals. (D) Best practices Not later than June 30, 2026, the Secretary shall make publicly available on the website of the Centers for Medicare & Medicaid Services best practices for designing and implementing a sickle cell disease-focused State plan amendment, based on clinical practice guidelines for sickle cell disease developed by medical specialty societies and in consultation with sickle cell disease providers and patient advocacy organizations. (E) Definitions For purposes of this section: (i) Eligible individual with sickle cell disease The term eligible individual with sickle cell disease means, with respect to a State, an individual who satisfies all of the following: (I) The individual is eligible for medical assistance under the State plan or under a waiver of such plan. (II) The individual has sickle cell disease. (III) The individual may or may not have previously received health home services under any other State plan amendment approved for the State under this section by the Secretary. (ii) Sickle cell disease The term sickle cell disease means an inherited blood disorder affecting red blood cells that occurs when an individual has inherited a sickle cell gene from each parent, as identified by a newborn screening or other genetic test. ; and\n**(3)**\nin subsection (h)(5), by inserting or a health home for eligible individuals with sickle cell disease after chronic conditions .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-09-08",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5178",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sickle Cell Disease Comprehensive Care Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Blood and blood diseases",
            "updateDate": "2025-07-24T14:26:13Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-24T14:26:38Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-24T14:26:32Z"
          },
          {
            "name": "Hearing, speech, and vision care",
            "updateDate": "2025-07-24T14:26:26Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-07-24T14:26:09Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-24T14:26:43Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-24T14:26:16Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-24T14:26:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T17:42:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s721",
          "measure-number": "721",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s721v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>"
        },
        "title": "Sickle Cell Disease Comprehensive Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s721.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s721"
    },
    "title": "Sickle Cell Disease Comprehensive Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sickle Cell Disease Comprehensive Care Act</strong></p><p>This bill allows state Medicaid programs to establish health homes to provide coordinated care for individuals with sickle-cell disease. (Under current law, state Medicaid programs may establish health homes to provide coordinated care for individuals with specified chronic conditions.) States must ensure that such care includes dental and vision services.</p><p>The Centers for Medicare & Medicaid Services must issue best practices for states on how to design and implement such health homes.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s721"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s721is.xml"
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
      "title": "Sickle Cell Disease Comprehensive Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sickle Cell Disease Comprehensive Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to establish a demonstration project to improve outpatient clinical care for individuals with sickle cell disease.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:04Z"
    }
  ]
}
```
