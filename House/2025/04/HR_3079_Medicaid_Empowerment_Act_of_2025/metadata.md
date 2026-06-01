# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3079
- Title: Medicaid Empowerment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3079
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2026-05-15T17:23:10Z
- Update date including text: 2026-05-15T17:23:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3079",
    "number": "3079",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Medicaid Empowerment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-15T17:23:10Z",
    "updateDateIncludingText": "2026-05-15T17:23:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:05:00Z",
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3079ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3079\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mr. Rulli (for himself, Mr. Veasey , and Mr. Carey ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to extend renewal periods for certain home and community-based services waivers and State plan amendments under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Medicaid Empowerment Act of 2025 .\n#### 2. Extending renewal periods for certain home and community-based services waivers and State plan amendments under Medicaid\nSection 1915 of the Social Security Act ( 42 U.S.C. 1396n ) is amended\u2014\n**(1)**\nin subsection (c)(3), by inserting (or, with respect to extensions of waivers beginning on or after the date of the enactment of the Medicaid Empowerment Act of 2025, 10-year periods) after five-year periods ;\n**(2)**\nin subsection (h)(2), by inserting (or, with respect to extensions of waivers under subsection (c) beginning on or after the date of the enactment of the Medicaid Empowerment Act of 2025, 10-year periods) after 5-year periods ; and\n**(3)**\nin subsection (i)(7)(C), by inserting (or, with respect to renewals of elections beginning on or after the date of the enactment of the Medicaid Empowerment Act of 2025, 10-year terms) after 5-year terms .",
      "versionDate": "2025-04-29",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-20T14:41:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
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
          "measure-id": "id119hr3079",
          "measure-number": "3079",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-29",
          "originChamber": "HOUSE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3079v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicaid Empowerment Act of 2025</strong></p><p>This bill allows state Medicaid programs to renew home- and community-based services waivers (also known as Section 1915(c) waivers) in 10-year periods. Currently, these waivers may be extended in five-year periods; waivers allow state Medicaid programs to cover long-term care services that are provided in home or community settings rather than in institutional settings.</p>"
        },
        "title": "Medicaid Empowerment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3079.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Empowerment Act of 2025</strong></p><p>This bill allows state Medicaid programs to renew home- and community-based services waivers (also known as Section 1915(c) waivers) in 10-year periods. Currently, these waivers may be extended in five-year periods; waivers allow state Medicaid programs to cover long-term care services that are provided in home or community settings rather than in institutional settings.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr3079"
    },
    "title": "Medicaid Empowerment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Empowerment Act of 2025</strong></p><p>This bill allows state Medicaid programs to renew home- and community-based services waivers (also known as Section 1915(c) waivers) in 10-year periods. Currently, these waivers may be extended in five-year periods; waivers allow state Medicaid programs to cover long-term care services that are provided in home or community settings rather than in institutional settings.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr3079"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3079ih.xml"
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
      "title": "Medicaid Empowerment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Empowerment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to extend renewal periods for certain home and community-based services waivers and State plan amendments under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:42Z"
    }
  ]
}
```
