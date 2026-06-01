# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/111
- Title: Expressing support for blockchain technology and digital assets.
- Congress: 119
- Bill type: HRES
- Bill number: 111
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-07-28T15:31:52Z
- Update date including text: 2025-07-28T15:31:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - Committee: Submitted in House
- Latest action: 2025-02-05: Submitted in House

## Actions

- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-05 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/111",
    "number": "111",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Expressing support for blockchain technology and digital assets.",
    "type": "HRES",
    "updateDate": "2025-07-28T15:31:52Z",
    "updateDateIncludingText": "2025-07-28T15:31:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Financial Services, and Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-05T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-05T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-05T15:02:30Z",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "WI"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres111ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 111\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Johnson of South Dakota (for himself, Mr. Steil , Mr. Davis of North Carolina , and Mr. Torres of New York ) submitted the following resolution; which was referred to the Committee on Energy and Commerce , and in addition to the Committees on Financial Services , and Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for blockchain technology and digital assets.\nThat it is the sense of the House of Representatives that\u2014\n**(1)**\nthe United States should seek to prioritize understanding the potential opportunities of the next generation of the internet;\n**(2)**\nthe United States should seek to foster advances in technology to improve our financial system and create more fair and equitable access to financial services for everyday Americans;\n**(3)**\nthe United States must support the development of digital assets and the underlying technology in the United States or risk the shifting of the development of such assets and technology outside of the United States, to less regulated countries;\n**(4)**\nthe United States should strive to be a global leader in the development and adoption of digital assets and blockchain technology;\n**(5)**\nCongress should enact a functional framework tailored to the specific risks of different digital asset-related activities and unique benefits of distributed ledger technology, distributed networks, and decentralized systems; and\n**(6)**\nconsumers and market participants will benefit from a framework for digital assets consistent with longstanding investor protections in securities and commodities markets, yet tailored to the unique benefits and risks of the digital asset ecosystem.",
      "versionDate": "2025-02-05",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-14T13:51:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hres111",
          "measure-number": "111",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres111v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses the sense that the United States should strive to be a global leader in the development and adoption of digital assets and blockchain technology.\u00a0</p>"
        },
        "title": "Expressing support for blockchain technology and digital assets."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres111.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense that the United States should strive to be a global leader in the development and adoption of digital assets and blockchain technology.\u00a0</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hres111"
    },
    "title": "Expressing support for blockchain technology and digital assets."
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense that the United States should strive to be a global leader in the development and adoption of digital assets and blockchain technology.\u00a0</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hres111"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres111ih.xml"
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
      "title": "Expressing support for blockchain technology and digital assets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T12:33:18Z"
    },
    {
      "title": "Expressing support for blockchain technology and digital assets.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T09:06:29Z"
    }
  ]
}
```
