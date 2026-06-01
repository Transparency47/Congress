# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2062?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2062
- Title: To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2062
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-04-30T08:06:45Z
- Update date including text: 2026-04-30T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2062",
    "number": "2062",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:45Z",
    "updateDateIncludingText": "2026-04-30T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:04:00Z",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MO"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MD"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2062ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2062\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Kelly of Pennsylvania (for himself, Mr. Murphy , and Mr. Smith of New Jersey ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.\n#### 1. Treatment of health care sharing ministries as a medical expense and not as insurance\n##### (a) Treatment as a medical expense\nSection 213(d)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by adding at the end the following new subparagraph:\n(E) for membership in a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof), including\u2014 (i) the sharing of medical expenses with respect to such ministry, and (ii) the payment of administrative fees of such ministry. .\n##### (b) Health care sharing ministry not treated as a health plan or insurance\n**(1) In general**\nChapter 79 of such Code is amended by inserting after section 7702B the following new section:\n7702C. Treatment of health care sharing ministries For purposes of this title, a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof) shall not be treated as a health plan or as insurance. .\n**(2) Clerical amendment**\nThe table of sections for chapter 79 of such Code is amended by inserting after the item relating to section 7702B the following new item:\nSec. 7702C. Treatment of health care sharing ministries. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "653",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
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
        "updateDate": "2025-05-08T19:36:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2062",
          "measure-number": "2062",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2062v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2062.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr2062"
    },
    "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr2062"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2062ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:32Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T08:07:19Z"
    }
  ]
}
```
