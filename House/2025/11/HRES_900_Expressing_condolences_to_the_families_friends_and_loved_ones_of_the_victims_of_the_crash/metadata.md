# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/900?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/900
- Title: Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976.
- Congress: 119
- Bill type: HRES
- Bill number: 900
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-04-06T17:03:15Z
- Update date including text: 2026-04-06T17:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-20 - IntroReferral: Submitted in House
- 2025-11-20 - IntroReferral: Submitted in House
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-20: Submitted in House

## Actions

- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-20 - IntroReferral: Submitted in House
- 2025-11-20 - IntroReferral: Submitted in House
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/900",
    "number": "900",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001220",
        "district": "3",
        "firstName": "Morgan",
        "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
        "lastName": "McGarvey",
        "party": "D",
        "state": "KY"
      }
    ],
    "title": "Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976.",
    "type": "HRES",
    "updateDate": "2026-04-06T17:03:15Z",
    "updateDateIncludingText": "2026-04-06T17:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:24:18Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres900ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 900\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. McGarvey (for himself, Mr. Barr , Mr. Guthrie , Mr. Rogers of Kentucky , Mr. Massie , and Mr. Comer ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976.\nThat the House of Representatives\u2014\n**(1)**\nexpresses heartfelt condolences to the families, friends, and loved ones of the victims of flight 2976;\n**(2)**\nhonors those who lost their lives in this tragedy, including Angela Anderson, Trinadette Trina Chavez, Tony Crain, Captain Dana Diamond, Louisnes Fedon, Kimberly Asa, Carlos Fernandez, John Loucks, John Spray, Jr., Matthew Sweets, First Officer Lee Truitt, Captain Richard Wartenberg, Megan Washburn, and Ella Petty Whorton;\n**(3)**\nconveys its deepest sympathy to the people of Louisville and the Commonwealth of Kentucky; and\n**(4)**\ncommends those heroic first responders and emergency personnel who ran into the fire.",
      "versionDate": "2025-11-20",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-24T17:55:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hres900",
          "measure-number": "900",
          "measure-type": "hres",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres900v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses condolences to the families, friends, and loved ones of the victims of UPS Airlines flight 2976, which crashed in Louisville, Kentucky,\u00a0on November 4, 2025.</p><p>The resolution\u00a0also</p><ul><li>honors those who lost their lives, and</li><li>commends the first responders and emergency personnel.</li></ul>"
        },
        "title": "Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres900.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses condolences to the families, friends, and loved ones of the victims of UPS Airlines flight 2976, which crashed in Louisville, Kentucky,\u00a0on November 4, 2025.</p><p>The resolution\u00a0also</p><ul><li>honors those who lost their lives, and</li><li>commends the first responders and emergency personnel.</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres900"
    },
    "title": "Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976."
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses condolences to the families, friends, and loved ones of the victims of UPS Airlines flight 2976, which crashed in Louisville, Kentucky,\u00a0on November 4, 2025.</p><p>The resolution\u00a0also</p><ul><li>honors those who lost their lives, and</li><li>commends the first responders and emergency personnel.</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres900"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres900ih.xml"
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
      "title": "Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T04:33:29Z"
    },
    {
      "title": "Expressing condolences to the families, friends, and loved ones of the victims of the crash of UPS Airlines flight 2976.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:04:15Z"
    }
  ]
}
```
