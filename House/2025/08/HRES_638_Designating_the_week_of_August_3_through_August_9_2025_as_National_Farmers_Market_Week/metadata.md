# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/638
- Title: Designating the week of August 3 through August 9, 2025, as "National Farmers Market Week".
- Congress: 119
- Bill type: HRES
- Bill number: 638
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-01-21T09:05:33Z
- Update date including text: 2026-01-21T09:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-08-05 - IntroReferral: Submitted in House
- 2025-08-05 - IntroReferral: Submitted in House
- Latest action: 2025-08-05: Submitted in House

## Actions

- 2025-08-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-08-05 - IntroReferral: Submitted in House
- 2025-08-05 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/638",
    "number": "638",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Designating the week of August 3 through August 9, 2025, as \"National Farmers Market Week\".",
    "type": "HRES",
    "updateDate": "2026-01-21T09:05:33Z",
    "updateDateIncludingText": "2026-01-21T09:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:01:00Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-08-05",
      "state": "HI"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OH"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NC"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "KS"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NC"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres638ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 638\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Valadao (for himself, Mr. Bishop , Ms. Tokuda , Ms. Brown , Mrs. Hayes , Ms. Budzinski , Mr. Davis of North Carolina , Ms. Davids of Kansas , Mr. Costa , Ms. Adams , and Ms. Underwood ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nDesignating the week of August 3 through August 9, 2025, as National Farmers Market Week .\nThat Congress\u2014\n**(1)**\nsupports the designation of National Farmers Market Week ; and\n**(2)**\nrecognizes the vital role that farmers markets play in bringing communities together and in supporting the livelihoods of millions of people in the United States, from farmers and food producers to consumers.",
      "versionDate": "2025-08-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Agricultural marketing and promotion",
            "updateDate": "2025-09-09T18:55:22Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-09-09T18:55:22Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-09-09T18:55:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-09-17T19:37:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-05",
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
          "measure-id": "id119hres638",
          "measure-number": "638",
          "measure-type": "hres",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2025-09-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres638v00",
            "update-date": "2025-09-18"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Farmers Market Week. The resolution also recognizes the vital role that farmers markets play in bringing communities together and in supporting the livelihoods of millions of people in the United States.</p>"
        },
        "title": "Designating the week of August 3 through August 9, 2025, as \"National Farmers Market Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres638.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Farmers Market Week. The resolution also recognizes the vital role that farmers markets play in bringing communities together and in supporting the livelihoods of millions of people in the United States.</p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119hres638"
    },
    "title": "Designating the week of August 3 through August 9, 2025, as \"National Farmers Market Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Farmers Market Week. The resolution also recognizes the vital role that farmers markets play in bringing communities together and in supporting the livelihoods of millions of people in the United States.</p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119hres638"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres638ih.xml"
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
      "title": "Designating the week of August 3 through August 9, 2025, as \"National Farmers Market Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T08:19:03Z"
    },
    {
      "title": "Designating the week of August 3 through August 9, 2025, as \"National Farmers Market Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T08:05:46Z"
    }
  ]
}
```
