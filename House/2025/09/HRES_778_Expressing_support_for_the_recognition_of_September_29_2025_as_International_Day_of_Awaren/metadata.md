# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/778?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/778
- Title: Expressing support for the recognition of September 29, 2025, as "International Day of Awareness of Food Loss and Waste".
- Congress: 119
- Bill type: HRES
- Bill number: 778
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-06T13:01:30Z
- Update date including text: 2026-04-06T13:01:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House
- Latest action: 2025-09-30: Submitted in House

## Actions

- 2025-09-30 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/778",
    "number": "778",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the recognition of September 29, 2025, as \"International Day of Awareness of Food Loss and Waste\".",
    "type": "HRES",
    "updateDate": "2026-04-06T13:01:30Z",
    "updateDateIncludingText": "2026-04-06T13:01:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "ME"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-30",
      "state": "DC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres778ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 778\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Lawler (for himself, Ms. Pingree , Mr. LaLota , Ms. Norton , Mr. Gottheimer , Mr. Beyer , and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nExpressing support for the recognition of September 29, 2025, as International Day of Awareness of Food Loss and Waste .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the recognition of International Day of Awareness of Food Loss and Waste ; and\n**(2)**\nacknowledges the importance of the implementation of food waste prevention methods.",
      "versionDate": "2025-09-30",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-12-02T20:35:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hres778",
          "measure-number": "778",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres778v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the recognition of International Day of Awareness of Food Loss and Waste.</p>"
        },
        "title": "Expressing support for the recognition of September 29, 2025, as \"International Day of Awareness of Food Loss and Waste\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres778.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the recognition of International Day of Awareness of Food Loss and Waste.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres778"
    },
    "title": "Expressing support for the recognition of September 29, 2025, as \"International Day of Awareness of Food Loss and Waste\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the recognition of International Day of Awareness of Food Loss and Waste.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres778"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres778ih.xml"
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
      "title": "Expressing support for the recognition of September 29, 2025, as \"International Day of Awareness of Food Loss and Waste\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:18:25Z"
    },
    {
      "title": "Expressing support for the recognition of September 29, 2025, as \"International Day of Awareness of Food Loss and Waste\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:05:31Z"
    }
  ]
}
```
