# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/172
- Title: Raising awareness for the sarcoma cancer chordoma.
- Congress: 119
- Bill type: HRES
- Bill number: 172
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-07T20:36:15Z
- Update date including text: 2026-04-07T20:36:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-27 - Committee: Submitted in House
- Latest action: 2025-02-27: Submitted in House

## Actions

- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-27 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/172",
    "number": "172",
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
    "title": "Raising awareness for the sarcoma cancer chordoma.",
    "type": "HRES",
    "updateDate": "2026-04-07T20:36:15Z",
    "updateDateIncludingText": "2026-04-07T20:36:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:10:45Z",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
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
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres172ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 172\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Johnson of Georgia (for himself, Mrs. McBath , Ms. Wilson of Florida , Ms. Vel\u00e1zquez , and Ms. Norton ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRaising awareness for the sarcoma cancer chordoma.\nThat it is the sense of the House of Representatives that chordoma patients and families need increased funding and support for\u2014\n**(1)**\naccurate and early diagnosis;\n**(2)**\nthe development of new treatments, diagnostics, and cures;\n**(3)**\nfewer hurdles between research and new treatments; and\n**(4)**\npatient-centric approaches to drug discovery and development.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2026-02-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1081",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "type": "HRES"
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
        "updateDate": "2025-03-03T16:33:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hres172",
          "measure-number": "172",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres172v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses the sense of the House of Representatives of the need for increased funding and support for diagnosis, treatments, and cures for chordoma (a bone cancer of the skull and spine).</p>"
        },
        "title": "Raising awareness for the sarcoma cancer chordoma."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres172.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense of the House of Representatives of the need for increased funding and support for diagnosis, treatments, and cures for chordoma (a bone cancer of the skull and spine).</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres172"
    },
    "title": "Raising awareness for the sarcoma cancer chordoma."
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses the sense of the House of Representatives of the need for increased funding and support for diagnosis, treatments, and cures for chordoma (a bone cancer of the skull and spine).</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres172"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres172ih.xml"
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
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:18:27Z"
    },
    {
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:05:51Z"
    }
  ]
}
```
