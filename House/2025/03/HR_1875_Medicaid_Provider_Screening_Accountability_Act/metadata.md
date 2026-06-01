# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1875
- Title: Medicaid Provider Screening Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1875
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-05-30T23:51:55Z
- Update date including text: 2025-05-30T23:51:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1875",
    "number": "1875",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Medicaid Provider Screening Accountability Act",
    "type": "HR",
    "updateDate": "2025-05-30T23:51:55Z",
    "updateDateIncludingText": "2025-05-30T23:51:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1875ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1875\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Langworthy (for himself, Mr. Morelle , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to require certain additional provider screening under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Medicaid Provider Screening Accountability Act .\n#### 2. Medicaid provider screening requirements\nSection 1902(kk)(1) of the Social Security Act ( 42 U.S.C. 1396a(kk)(1) ) is amended\u2014\n**(1)**\nby striking The State and inserting:\n(A) In general The State ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Additional provider screening Beginning January 1, 2028, as part of the enrollment (or reenrollment or revalidation of enrollment) of a provider or supplier under this title, and not less frequently than monthly during the period that such provider or supplier is so enrolled, the State conducts a check of any database or similar system developed pursuant to section 6401(b)(2) of the Patient Protection and Affordable Care Act to determine whether the Secretary has terminated the participation of such provider or supplier under title XVIII, or whether any other State has terminated the participation of such provider or supplier under such other State\u2019s State plan under this title (or waiver of the plan), or such other State\u2019s State child health plan under title XXI (or waiver of the plan). .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-05-22",
        "actionTime": "06:56:39",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
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
        "name": "Health",
        "updateDate": "2025-03-21T13:41:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
    "originChamber": "House",
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
          "measure-id": "id119hr1875",
          "measure-number": "1875",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1875v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicaid Provider Screening Accountability Act</strong></p><p>This bill requires state Medicaid programs to check, as part of the provider enrollment and reenrollment process, whether providers were terminated from participating in the Medicare program, any other state Medicaid program, or the Children's Health Insurance Program (CHIP) using certain databases (e.g., the Data EXchange system). The bill requires states to continue to check these databases on at least a monthly basis after providers are enrolled.</p>"
        },
        "title": "Medicaid Provider Screening Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1875.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Provider Screening Accountability Act</strong></p><p>This bill requires state Medicaid programs to check, as part of the provider enrollment and reenrollment process, whether providers were terminated from participating in the Medicare program, any other state Medicaid program, or the Children's Health Insurance Program (CHIP) using certain databases (e.g., the Data EXchange system). The bill requires states to continue to check these databases on at least a monthly basis after providers are enrolled.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr1875"
    },
    "title": "Medicaid Provider Screening Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Provider Screening Accountability Act</strong></p><p>This bill requires state Medicaid programs to check, as part of the provider enrollment and reenrollment process, whether providers were terminated from participating in the Medicare program, any other state Medicaid program, or the Children's Health Insurance Program (CHIP) using certain databases (e.g., the Data EXchange system). The bill requires states to continue to check these databases on at least a monthly basis after providers are enrolled.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr1875"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1875ih.xml"
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
      "title": "Medicaid Provider Screening Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Provider Screening Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to require certain additional provider screening under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:22Z"
    }
  ]
}
```
