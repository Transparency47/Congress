# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/392
- Title: Expressing support for the designation of May as "National Bladder Cancer Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 392
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2026-04-07T20:35:10Z
- Update date including text: 2026-04-07T20:35:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/392",
    "number": "392",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Expressing support for the designation of May as \"National Bladder Cancer Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-04-07T20:35:10Z",
    "updateDateIncludingText": "2026-04-07T20:35:10Z"
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
          "date": "2025-05-06T14:00:45Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
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
      "sponsorshipDate": "2025-05-06",
      "state": "PA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "GA"
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
      "sponsorshipDate": "2025-05-06",
      "state": "AL"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "AL"
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
      "sponsorshipDate": "2025-05-06",
      "state": "DC"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres392ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 392\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mr. Murphy (for himself, Mr. Davis of North Carolina , Mr. Fitzpatrick , Mr. Tonko , Mr. David Scott of Georgia , Ms. Sewell , Ms. Barrag\u00e1n , Mr. Aderholt , Ms. Norton , and Mr. Connolly ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May as National Bladder Cancer Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Bladder Cancer Awareness Month ;\n**(2)**\nsupports the goals and ideals of National Bladder Cancer Awareness Month ; and\n**(3)**\ncalls on the people of the United States, interested groups, the research community, and affected persons to\u2014\n**(A)**\npromote awareness of bladder cancer and foster understanding of the impact of the disease on patients, their families, caregivers, and their community;\n**(B)**\ntake an active role in the fight to end bladder cancer; and\n**(C)**\nobserve National Bladder Cancer Awareness Month with appropriate ceremonies and activities.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-05-20T13:51:12Z"
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
          "measure-id": "id119hres392",
          "measure-number": "392",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres392v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Bladder Cancer Awareness Month.</p>"
        },
        "title": "Expressing support for the designation of May as \"National Bladder Cancer Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres392.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Bladder Cancer Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres392"
    },
    "title": "Expressing support for the designation of May as \"National Bladder Cancer Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Bladder Cancer Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres392"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres392ih.xml"
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
      "title": "Expressing support for the designation of May as \"National Bladder Cancer Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T08:18:20Z"
    },
    {
      "title": "Expressing support for the designation of May as \"National Bladder Cancer Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T08:05:54Z"
    }
  ]
}
```
