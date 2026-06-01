# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2309?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2309
- Title: Medicare and Medicaid Fraud Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 2309
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2026-02-18T09:05:44Z
- Update date including text: 2026-02-18T09:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2309",
    "number": "2309",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Medicare and Medicaid Fraud Prevention Act",
    "type": "HR",
    "updateDate": "2026-02-18T09:05:44Z",
    "updateDateIncludingText": "2026-02-18T09:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:02:00Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
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
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "UT"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2309ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2309\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Peters (for himself, Mr. Evans of Colorado , Mr. Suozzi , Ms. Malliotakis , and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to require certain additional provider screening under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Medicare and Medicaid Fraud Prevention Act .\n#### 2. Medicaid provider screening requirements\nSection 1902(kk)(1) of the Social Security Act ( 42 U.S.C. 1396a(kk)(1) ) is amended\u2014\n**(1)**\nby striking The State and inserting:\n(A) In general The State ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Additional provider screening Beginning January 1, 2027, as part of the enrollment (or revalidation of enrollment) of a provider or supplier under this title, and not less frequently than quarterly during the period that such provider or supplier is so enrolled, the State conducts a check of the Death Master File (as such term is defined in section 203(d) of the Bipartisan Budget Act of 2013) to determine whether such provider or supplier is deceased. .",
      "versionDate": "2025-03-24",
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
        "name": "Health",
        "updateDate": "2025-04-03T17:14:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119hr2309",
          "measure-number": "2309",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-24",
          "originChamber": "HOUSE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2309v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicare and Medicaid Fraud Prevention Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs check, as part of the provider enrollment and reenrollment process, whether providers are deceased through the Social Security Administration's Death Master File. The bill requires states to continue to check this database on at least a quarterly basis after providers are enrolled.</p>"
        },
        "title": "Medicare and Medicaid Fraud Prevention Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2309.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare and Medicaid Fraud Prevention Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs check, as part of the provider enrollment and reenrollment process, whether providers are deceased through the Social Security Administration's Death Master File. The bill requires states to continue to check this database on at least a quarterly basis after providers are enrolled.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr2309"
    },
    "title": "Medicare and Medicaid Fraud Prevention Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare and Medicaid Fraud Prevention Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs check, as part of the provider enrollment and reenrollment process, whether providers are deceased through the Social Security Administration's Death Master File. The bill requires states to continue to check this database on at least a quarterly basis after providers are enrolled.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr2309"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2309ih.xml"
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
      "title": "Medicare and Medicaid Fraud Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare and Medicaid Fraud Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to require certain additional provider screening under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:45Z"
    }
  ]
}
```
