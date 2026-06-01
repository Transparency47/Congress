# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/505
- Title: Recognizing June 12, 2025, as this year's observance of "Philippines Independence Day" to honor the 127th anniversary of the independence of the Philippines.
- Congress: 119
- Bill type: HRES
- Bill number: 505
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2026-03-30T15:51:54Z
- Update date including text: 2026-03-30T15:51:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H2648)
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House
- Latest action: 2025-06-11: Submitted in House

## Actions

- 2025-06-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H2648)
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/505",
    "number": "505",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Recognizing June 12, 2025, as this year's observance of \"Philippines Independence Day\" to honor the 127th anniversary of the independence of the Philippines.",
    "type": "HRES",
    "updateDate": "2026-03-30T15:51:54Z",
    "updateDateIncludingText": "2026-03-30T15:51:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2648)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MP"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "AS"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "IN"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres505ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 505\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Moylan (for himself, Mr. Scott of Virginia , Mrs. Kim , Mr. Case , Ms. King-Hinds , and Mrs. Radewagen ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing June 12, 2025, as this year\u2019s observance of Philippines Independence Day to honor the 127th anniversary of the independence of the Philippines.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the historic significance of the 127th anniversary of the sovereign and independent country of the Philippines on June 12, 1898;\n**(2)**\nreaffirms the bonds of friendship and cooperation which have existed between the United States and the Philippines and commits to strengthening those bonds;\n**(3)**\nreaffirms its support for the Philippines to defend its internal security from terrorism;\n**(4)**\nreaffirms its enduring support for the Philippines;\n**(5)**\nrecognizes the courage and bravery of the Filipino and Filipino American servicemen and servicewomen who have fought alongside and in the United States Armed Forces; and\n**(6)**\nsupports the recognition of \u201cPhilippines Independence Day\u201d.",
      "versionDate": "2025-06-11",
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
        "name": "International Affairs",
        "updateDate": "2025-07-17T20:33:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-11",
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
          "measure-id": "id119hres505",
          "measure-number": "505",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres505v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the historic significance of the 127th anniversary of the Philippines' sovereignty and independence.</p><p>The resolution also (1) reaffirms the bonds of friendship and cooperation between the United States and the Philippines, (2) recognizes the courage and bravery of Filipino and Filipino American\u00a0servicemembers who have fought alongside and in the U.S. armed forces, and (3) supports the recognition of Philippines Independence Day.</p>"
        },
        "title": "Recognizing June 12, 2025, as this year's observance of \"Philippines Independence Day\" to honor the 127th anniversary of the independence of the Philippines."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres505.xml",
    "summary": {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the historic significance of the 127th anniversary of the Philippines' sovereignty and independence.</p><p>The resolution also (1) reaffirms the bonds of friendship and cooperation between the United States and the Philippines, (2) recognizes the courage and bravery of Filipino and Filipino American\u00a0servicemembers who have fought alongside and in the U.S. armed forces, and (3) supports the recognition of Philippines Independence Day.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hres505"
    },
    "title": "Recognizing June 12, 2025, as this year's observance of \"Philippines Independence Day\" to honor the 127th anniversary of the independence of the Philippines."
  },
  "summaries": [
    {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the historic significance of the 127th anniversary of the Philippines' sovereignty and independence.</p><p>The resolution also (1) reaffirms the bonds of friendship and cooperation between the United States and the Philippines, (2) recognizes the courage and bravery of Filipino and Filipino American\u00a0servicemembers who have fought alongside and in the U.S. armed forces, and (3) supports the recognition of Philippines Independence Day.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hres505"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres505ih.xml"
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
      "title": "Recognizing June 12, 2025, as this year's observance of \"Philippines Independence Day\" to honor the 127th anniversary of the independence of the Philippines.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T09:03:42Z"
    },
    {
      "title": "Recognizing June 12, 2025, as this year's observance of \"Philippines Independence Day\" to honor the 127th anniversary of the independence of the Philippines.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:06:42Z"
    }
  ]
}
```
