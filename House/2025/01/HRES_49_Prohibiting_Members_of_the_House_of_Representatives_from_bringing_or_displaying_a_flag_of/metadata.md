# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/49?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/49
- Title: Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 49
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-02-28T20:51:00Z
- Update date including text: 2025-02-28T20:51:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-16 - Committee: Submitted in House
- 2025-01-16 - IntroReferral: Submitted in House
- Latest action: 2025-01-16: Submitted in House

## Actions

- 2025-01-16 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-16 - Committee: Submitted in House
- 2025-01-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/49",
    "number": "49",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-02-28T20:51:00Z",
    "updateDateIncludingText": "2025-02-28T20:51:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OH"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres49ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 49\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mrs. Cammack (for herself, Mr. Higgins of Louisiana , Mr. Bost , Ms. Malliotakis , Ms. Hageman , Mr. Babin , Mr. Miller of Ohio , Mr. Collins , Mrs. Luna , Ms. Lee of Florida , Mr. Van Orden , Mr. Langworthy , and Mrs. Bice ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProhibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes.\n#### 1. Prohibition with respect to flag of a foreign nation on the floor of the House\n##### (a) Prohibition\n**(1) In general**\nDuring a session of the House of Representatives, a Member, Delegate, or Resident Commissioner may not bring or display on the floor of the House any flag of a foreign nation.\n**(2) Application**\nExcept as provided under subsection (b) , the prohibition under subsection (a) shall apply to a flag of a foreign nation regardless of the size of the flag.\n##### (b) Exception\nThe prohibition under subsection (a) shall not apply\u2014\n**(1)**\nto a flag of a foreign nation worn as a lapel pin by a Member, Delegate, or Resident Commissioner; or\n**(2)**\nto a depiction of a flag of a foreign nation used as part of an exhibit by a Member, Delegate, or Resident Commissioner during a speech or debate under the Rules of the House of Representatives.\n##### (c) Enforcement\nThe Sergeant-at-Arms of the House of Representatives is charged with the enforcement of the prohibition under subsection (a) .",
      "versionDate": "2025-01-16",
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
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-22T14:47:45Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-22T14:47:56Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2025-01-22T14:48:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-21T12:58:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hres49",
          "measure-number": "49",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres49v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution prohibits a Member, Delegate, or Resident Commissioner from bringing or displaying any flag of a foreign nation on the House floor while it is in session. However, the prohibition does not apply to a Member wearing a flag of a foreign nation as a lapel pin or using a depiction of such a flag as part of an exhibit during a speech or debate under House rules.</p>"
        },
        "title": "Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres49.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution prohibits a Member, Delegate, or Resident Commissioner from bringing or displaying any flag of a foreign nation on the House floor while it is in session. However, the prohibition does not apply to a Member wearing a flag of a foreign nation as a lapel pin or using a depiction of such a flag as part of an exhibit during a speech or debate under House rules.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hres49"
    },
    "title": "Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution prohibits a Member, Delegate, or Resident Commissioner from bringing or displaying any flag of a foreign nation on the House floor while it is in session. However, the prohibition does not apply to a Member wearing a flag of a foreign nation as a lapel pin or using a depiction of such a flag as part of an exhibit during a speech or debate under House rules.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hres49"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres49ih.xml"
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
      "title": "Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:18:22Z"
    },
    {
      "title": "Prohibiting Members of the House of Representatives from bringing or displaying a flag of a foreign nation on the floor of the House, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:49Z"
    }
  ]
}
```
