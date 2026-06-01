# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/389
- Title: Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.
- Congress: 119
- Bill type: HRES
- Bill number: 389
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2026-05-21T14:54:04Z
- Update date including text: 2026-05-21T14:54:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-06 - IntroReferral: Submitted in House
- 2025-05-06 - IntroReferral: Submitted in House
- Latest action: 2025-05-06: Submitted in House

## Actions

- 2025-05-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-06 - IntroReferral: Submitted in House
- 2025-05-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/389",
    "number": "389",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000295",
        "district": "14",
        "firstName": "David",
        "fullName": "Rep. Joyce, David P. [R-OH-14]",
        "lastName": "Joyce",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
    "type": "HRES",
    "updateDate": "2026-05-21T14:54:04Z",
    "updateDateIncludingText": "2026-05-21T14:54:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:03:35Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "OR"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "VA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres389ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 389\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mr. Joyce of Ohio (for himself, Ms. Bonamici , Mrs. Kiggans of Virginia , and Ms. Underwood ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of National Nurses Week, as founded by the American Nurses Association;\n**(2)**\nrecognizes the significant contributions of nurses to the health care system of the United States; and\n**(3)**\nencourages the people of the United States to observe National Nurses Week with appropriate recognition, ceremonies, activities, and programs to demonstrate the importance of nurses to the everyday lives of patients.",
      "versionDate": "2025-05-06",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2175)"
      },
      "number": "709",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2026.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1264",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the goals and ideals of \"National Nurses Week\", to be observed from May 6 through May 12, 2026.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2778)"
      },
      "number": "206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
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
        "name": "Health",
        "updateDate": "2025-05-20T13:54:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
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
          "measure-id": "id119hres389",
          "measure-number": "389",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres389v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the goals and ideals of National Nurses Week.</p>"
        },
        "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres389.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the goals and ideals of National Nurses Week.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres389"
    },
    "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025."
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the goals and ideals of National Nurses Week.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres389"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres389ih.xml"
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
      "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T08:18:28Z"
    },
    {
      "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T08:05:56Z"
    }
  ]
}
```
