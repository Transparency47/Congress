# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1162
- Title: Medicaid Primary Care Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1162
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2026-01-21T09:05:19Z
- Update date including text: 2026-01-21T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1162",
    "number": "1162",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Medicaid Primary Care Improvement Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:19Z",
    "updateDateIncludingText": "2026-01-21T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:02:40Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CO"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MO"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1162ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1162\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Crenshaw (for himself, Ms. Schrier , Mr. Smucker , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo facilitate direct primary care arrangements under Medicaid.\n#### 1. Short title\nThis Act may be cited as the Medicaid Primary Care Improvement Act .\n#### 2. Clarifying that certain payment arrangements are allowable under the medicaid program\n##### (a) Rule of construction\nNothing in title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) shall be construed as prohibiting a State, under its State plan (or waiver of such plan) under such title (including through a medicaid managed care organization (as defined in section 1903(m)(1)(A) of such Act)), from providing medical assistance consisting of primary care services through a direct primary care arrangement with a health care provider, including as part of a value-based care arrangement established by the State. For purposes of the preceding sentence, the term direct primary care arrangement means, with respect to any individual, an arrangement under which such individual is provided medical assistance consisting solely of primary care services provided by primary care practitioners, if the sole compensation for such care is a fixed periodic fee.\n##### (b) Guidance\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall\u2014\n**(1)**\nconvene at least one virtual open door meeting to seek input from stakeholders, including primary care providers who practice under the direct primary care model, state Medicaid agencies, and Medicaid managed care organizations; and\n**(2)**\ntaking into account such input, issue guidance to States on how a State may implement direct primary care arrangements (as defined in subsection (a)) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).\n##### (c) Report\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report containing\u2014\n**(1)**\nan analysis of the extent to which States are contracting with independent physicians, independent physician practices, and primary care practices for purposes of furnishing medical assistance under State plans (or waivers of such plans) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ); and\n**(2)**\nan analysis of quality of care and cost of care furnished to individuals enrolled under such title where such care is paid for under a direct primary care arrangement (as defined in subsection (a)) through a medicaid managed care organization (as so defined).\n##### (d) Rule of construction\nNothing in this section shall be construed to alter statutory requirements under the State plan (or waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for cost-sharing requirements or be construed to limit medical assistance solely to those provided under a direct primary care arrangement.",
      "versionDate": "2025-02-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-24T16:19:48Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-24T16:19:48Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-04-24T16:19:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-14T12:47:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1162",
          "measure-number": "1162",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1162v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Medicaid Primary Care Improvement Act</b></p><p>This bill specifies that state Medicaid programs are authorized to provide primary care services through direct primary care arrangements (i.e., arrangements in which primary care providers receive a fixed periodic fee for their services).</p> <p>The Centers for Medicare & Medicaid Services must (1) convene at least one virtual stakeholder meeting and issue related guidance on how state Medicaid programs may implement direct primary care arrangements, and (2) report on the extent to which state Medicaid programs contract with independent providers and on the quality and cost of care under direct primary care arrangements that are offered through Medicaid managed care organizations.</p>"
        },
        "title": "Medicaid Primary Care Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1162.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicaid Primary Care Improvement Act</b></p><p>This bill specifies that state Medicaid programs are authorized to provide primary care services through direct primary care arrangements (i.e., arrangements in which primary care providers receive a fixed periodic fee for their services).</p> <p>The Centers for Medicare & Medicaid Services must (1) convene at least one virtual stakeholder meeting and issue related guidance on how state Medicaid programs may implement direct primary care arrangements, and (2) report on the extent to which state Medicaid programs contract with independent providers and on the quality and cost of care under direct primary care arrangements that are offered through Medicaid managed care organizations.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr1162"
    },
    "title": "Medicaid Primary Care Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicaid Primary Care Improvement Act</b></p><p>This bill specifies that state Medicaid programs are authorized to provide primary care services through direct primary care arrangements (i.e., arrangements in which primary care providers receive a fixed periodic fee for their services).</p> <p>The Centers for Medicare & Medicaid Services must (1) convene at least one virtual stakeholder meeting and issue related guidance on how state Medicaid programs may implement direct primary care arrangements, and (2) report on the extent to which state Medicaid programs contract with independent providers and on the quality and cost of care under direct primary care arrangements that are offered through Medicaid managed care organizations.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr1162"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1162ih.xml"
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
      "title": "Medicaid Primary Care Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Primary Care Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To facilitate direct primary care arrangements under Medicaid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:03Z"
    }
  ]
}
```
