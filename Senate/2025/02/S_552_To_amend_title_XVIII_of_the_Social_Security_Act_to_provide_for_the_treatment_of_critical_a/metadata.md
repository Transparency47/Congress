# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/552
- Title: CRITICAL Act
- Congress: 119
- Bill type: S
- Bill number: 552
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-07-07T15:02:40Z
- Update date including text: 2025-07-07T15:02:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/552",
    "number": "552",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "CRITICAL Act",
    "type": "S",
    "updateDate": "2025-07-07T15:02:40Z",
    "updateDateIncludingText": "2025-07-07T15:02:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T21:44:10Z",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s552is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 552\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Sullivan (for himself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for the treatment of critical access hospital services furnished by a critical access hospital located in a noncontiguous State.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Reimbursement Initiative Targeting Investment and Care in rural Locations or the CRITICAL Act .\n#### 2. Treatment of critical access hospitals located in a noncontiguous State\n##### (a) Inpatient critical access hospital services\nSection 1814(l)(1) of the Social Security Act ( 42 U.S.C. 1395f(l)(1) ) is amended by inserting (or, in the case of inpatient critical access hospital services furnished on or after January 1, 2026, by a critical access hospital that is located in a noncontiguous State, 105 percent) after 101 percent .\n##### (b) Outpatient critical access hospital services\nSection 1834(g)(1) of the Social Security Act ( 42 U.S.C. 1395m(g)(1) ) is amended by inserting (or, in the case of outpatient critical access hospital services furnished on or after January 1, 2026, by a critical access hospital that is located in a noncontiguous State, 105 percent) after 101 percent .\n##### (c) Ambulance services\nSection 1834(l)(8) of the Social Security Act ( 42 U.S.C. 1395m(l)(8) ) is amended by inserting (or, in the case of ambulance services furnished on or after January 1, 2026, by a critical access hospital that is located in a noncontiguous State or by an entity that is owned and operated by a critical access hospital that is located in a noncontiguous State, 105 percent) after 101 percent .\n##### (d) Skilled nursing facility services\nSection 1883(a)(3) of the Social Security Act ( 42 U.S.C. 1395tt(a)(3) ) is amended by inserting (or, in the case of covered skilled nursing facility services furnished on or after January 1, 2026, under an agreement under this section by a critical access hospital that is located in a noncontiguous State, 105 percent) after 101 percent .",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in Senate"
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
            "name": "Alaska",
            "updateDate": "2025-07-07T15:02:02Z"
          },
          {
            "name": "Hawaii",
            "updateDate": "2025-07-07T15:02:06Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-07-07T15:02:11Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-07T15:02:40Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-07-07T15:02:21Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-07-07T15:02:16Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-07-07T15:02:27Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-07T15:01:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:44:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s552",
          "measure-number": "552",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s552v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Comprehensive Reimbursement Initiative Targeting Investment and Care in rural Locations or the CRITICAL Act</strong></p><p>This bill increases the Medicare payment rate by 4% for services provided by critical access hospitals in Alaska and Hawaii.</p>"
        },
        "title": "CRITICAL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s552.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Comprehensive Reimbursement Initiative Targeting Investment and Care in rural Locations or the CRITICAL Act</strong></p><p>This bill increases the Medicare payment rate by 4% for services provided by critical access hospitals in Alaska and Hawaii.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s552"
    },
    "title": "CRITICAL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Comprehensive Reimbursement Initiative Targeting Investment and Care in rural Locations or the CRITICAL Act</strong></p><p>This bill increases the Medicare payment rate by 4% for services provided by critical access hospitals in Alaska and Hawaii.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s552"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s552is.xml"
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
      "title": "CRITICAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CRITICAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive Reimbursement Initiative Targeting Investment and Care in rural Locations",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for the treatment of critical access hospital services furnished by a critical access hospital located in a noncontiguous State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:52Z"
    }
  ]
}
```
