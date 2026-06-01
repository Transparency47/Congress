# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/362
- Title: Expressing support for the designation of April 30, 2025, as "National Adult Hepatitis B Vaccination Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 362
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-04-07T19:57:11Z
- Update date including text: 2026-04-07T19:57:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-30 - IntroReferral: Submitted in House
- 2025-04-30 - IntroReferral: Submitted in House
- Latest action: 2025-04-30: Submitted in House

## Actions

- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-30 - IntroReferral: Submitted in House
- 2025-04-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/362",
    "number": "362",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000288",
        "district": "4",
        "firstName": "Henry",
        "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
        "lastName": "Johnson",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Expressing support for the designation of April 30, 2025, as \"National Adult Hepatitis B Vaccination Awareness Day\".",
    "type": "HRES",
    "updateDate": "2026-04-07T19:57:11Z",
    "updateDateIncludingText": "2026-04-07T19:57:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-30T14:00:40Z",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "HI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres362ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 362\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Johnson of Georgia (for himself, Ms. Vel\u00e1zquez , Ms. Williams of Georgia , Ms. Norton , Ms. Tokuda , Ms. Sewell , and Ms. Chu ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of April 30, 2025, as National Adult Hepatitis B Vaccination Awareness Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Adult Hepatitis B Vaccination Awareness Day ;\n**(2)**\nrecognizes the importance of providing support and encouragement\u2014\n**(A)**\nfor all adults aged 18 and older to be tested for hepatitis B at least once in their lifetime in accordance with recommendations;\n**(B)**\nfor individuals susceptible to infection to be vaccinated against hepatitis B; and\n**(C)**\nfor individuals diagnosed with hepatitis B to be linked to appropriate care; and\n**(3)**\nin order to reduce the number of new hepatitis B infections and hepatitis B-related deaths, encourages a commitment to\u2014\n**(A)**\nincreasing adult hepatitis B vaccination rates;\n**(B)**\nmaintaining childhood hepatitis B vaccination rates; and\n**(C)**\npromoting provider and community awareness of adult hepatitis B vaccination.",
      "versionDate": "2025-04-30",
      "versionType": "IH"
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
        "updateDate": "2025-05-19T17:00:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119hres362",
          "measure-number": "362",
          "measure-type": "hres",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres362v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Adult Hepatitis B Vaccination Awareness Day.</p>"
        },
        "title": "Expressing support for the designation of April 30, 2025, as \"National Adult Hepatitis B Vaccination Awareness Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres362.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Adult Hepatitis B Vaccination Awareness Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres362"
    },
    "title": "Expressing support for the designation of April 30, 2025, as \"National Adult Hepatitis B Vaccination Awareness Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Adult Hepatitis B Vaccination Awareness Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres362"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres362ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of April 30, 2025, as \"National Adult Hepatitis B Vaccination Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-01T08:48:17Z"
    },
    {
      "title": "Expressing support for the designation of April 30, 2025, as \"National Adult Hepatitis B Vaccination Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T08:06:14Z"
    }
  ]
}
```
