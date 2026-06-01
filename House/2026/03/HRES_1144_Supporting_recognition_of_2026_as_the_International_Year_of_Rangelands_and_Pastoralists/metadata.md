# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1144
- Title: Supporting recognition of 2026 as the "International Year of Rangelands and Pastoralists".
- Congress: 119
- Bill type: HRES
- Bill number: 1144
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-06T12:59:31Z
- Update date including text: 2026-04-06T12:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House
- Latest action: 2026-03-27: Submitted in House

## Actions

- 2026-03-27 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1144",
    "number": "1144",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001228",
        "district": "2",
        "firstName": "Celeste",
        "fullName": "Rep. Maloy, Celeste [R-UT-2]",
        "lastName": "Maloy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\".",
    "type": "HRES",
    "updateDate": "2026-04-06T12:59:31Z",
    "updateDateIncludingText": "2026-04-06T12:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:33:45Z",
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
          "date": "2026-03-28T01:33:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "KS"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "MP"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "ID"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "WY"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1144ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1144\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Ms. Maloy (for herself, Mr. Costa , Mr. Mann , Mr. Evans of Colorado , Ms. King-Hinds , Mr. Fulcher , Ms. Hageman , and Mr. Grothman ) submitted the following resolution; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nSupporting recognition of 2026 as the International Year of Rangelands and Pastoralists .\nThat the House of Representatives\u2014\n**(1)**\nsupports recognizing the International Year of Rangelands and Pastoralists ;\n**(2)**\nrecognizes the economic, social, and ecological importance of rangelands and the ranchers, farmers, land managers, pastoralists, and partners who have been caretakers of the American rangelands for generations; and\n**(3)**\nencourages Federal agencies, universities, and organizations across the country to engage in activities that promote education, research, and outreach related to rangeland management.",
      "versionDate": "2026-03-27",
      "versionType": "IH"
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
        "actionDate": "2026-03-17",
        "text": "Referred to the Committee on Energy and Natural Resources. (text: CR S1093-1094)"
      },
      "number": "645",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "type": "SRES"
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
        "updateDate": "2026-03-30T17:36:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-27",
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
          "measure-id": "id119hres1144",
          "measure-number": "1144",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1144v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports\u00a0recognizing the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>"
        },
        "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1144.xml",
    "summary": {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports\u00a0recognizing the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres1144"
    },
    "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\"."
  },
  "summaries": [
    {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports\u00a0recognizing the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres1144"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1144ih.xml"
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
      "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:22Z"
    },
    {
      "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T08:06:22Z"
    }
  ]
}
```
