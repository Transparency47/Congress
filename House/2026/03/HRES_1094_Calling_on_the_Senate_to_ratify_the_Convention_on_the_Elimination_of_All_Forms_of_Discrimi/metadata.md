# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1094?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1094
- Title: Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.
- Congress: 119
- Bill type: HRES
- Bill number: 1094
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-04-27T14:16:12Z
- Update date including text: 2026-04-27T14:16:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-02 - IntroReferral: Submitted in House
- 2026-03-02 - IntroReferral: Submitted in House
- Latest action: 2026-03-02: Submitted in House

## Actions

- 2026-03-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-02 - IntroReferral: Submitted in House
- 2026-03-02 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1094",
    "number": "1094",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.",
    "type": "HRES",
    "updateDate": "2026-04-27T14:16:12Z",
    "updateDateIncludingText": "2026-04-27T14:16:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:00:15Z",
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
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "FL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1094ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1094\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Ms. Norton (for herself, Ms. Wilson of Florida , and Mrs. Dingell ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCalling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.\nThat the House of Representatives calls upon the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.",
      "versionDate": "2026-03-02",
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
        "updateDate": "2026-03-05T00:27:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-02",
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
          "measure-id": "id119hres1094",
          "measure-number": "1094",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-02",
          "originChamber": "HOUSE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1094v00",
            "update-date": "2026-04-27"
          },
          "action-date": "2026-03-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution calls on the Senate to ratify the UN Convention on the Elimination of All Forms of Discrimination Against Women, also known as CEDAW.</p>"
        },
        "title": "Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1094.xml",
    "summary": {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution calls on the Senate to ratify the UN Convention on the Elimination of All Forms of Discrimination Against Women, also known as CEDAW.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hres1094"
    },
    "title": "Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women."
  },
  "summaries": [
    {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution calls on the Senate to ratify the UN Convention on the Elimination of All Forms of Discrimination Against Women, also known as CEDAW.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hres1094"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1094ih.xml"
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
      "title": "Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T09:18:30Z"
    },
    {
      "title": "Calling on the Senate to ratify the Convention on the Elimination of All Forms of Discrimination Against Women.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T09:05:24Z"
    }
  ]
}
```
