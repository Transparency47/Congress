# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/60?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/60
- Title: Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 60
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-03-12T08:06:52Z
- Update date including text: 2025-03-12T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House
- Latest action: 2025-01-23: Submitted in House

## Actions

- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/60",
    "number": "60",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.",
    "type": "HRES",
    "updateDate": "2025-03-12T08:06:52Z",
    "updateDateIncludingText": "2025-03-12T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "DC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "WI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres60ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 60\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Brownley (for herself and Ms. Norton ) submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nExpressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.\nThat the House of Representatives supports the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.",
      "versionDate": "2025-01-23",
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
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-06T15:25:09Z"
          },
          {
            "name": "Minority employment",
            "updateDate": "2025-02-06T15:25:20Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-02-06T15:25:25Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2025-02-06T15:25:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-01-27T22:52:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hres60",
          "measure-number": "60",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres60v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the naming of new or undedicated Department of Veterans Affairs facilities after women veterans and minority veterans to reflect the diversity of all who have served in the Armed Forces.</p>"
        },
        "title": "Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres60.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the naming of new or undedicated Department of Veterans Affairs facilities after women veterans and minority veterans to reflect the diversity of all who have served in the Armed Forces.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hres60"
    },
    "title": "Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the naming of new or undedicated Department of Veterans Affairs facilities after women veterans and minority veterans to reflect the diversity of all who have served in the Armed Forces.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hres60"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres60ih.xml"
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
      "title": "Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-24T09:18:21Z"
    },
    {
      "title": "Expressing the support of the House of Representatives for the naming of new or undedicated facilities of the Department of Veterans Affairs after women veterans and minority veterans in order to reflect the diversity of all who have served in the Armed Forces of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:31Z"
    }
  ]
}
```
