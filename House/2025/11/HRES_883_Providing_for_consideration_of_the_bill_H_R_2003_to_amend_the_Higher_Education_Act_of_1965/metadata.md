# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/883
- Title: Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.
- Congress: 119
- Bill type: HRES
- Bill number: 883
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-03-17T15:54:41Z
- Update date including text: 2026-03-17T15:54:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-11-17 - IntroReferral: Submitted in House
- 2025-11-17 - IntroReferral: Submitted in House
- Latest action: 2025-11-17: Submitted in House

## Actions

- 2025-11-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-11-17 - IntroReferral: Submitted in House
- 2025-11-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/883",
    "number": "883",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:54:41Z",
    "updateDateIncludingText": "2026-03-17T15:54:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
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
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres883ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 883\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mrs. Luna submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent. All points of order against consideration of the bill are waived. The bill shall be considered as read. All points of order against provisions in the bill are waived. The previous question shall be considered as ordered on the bill and on any amendment thereto to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Education and Workforce or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H.R. 2003.",
      "versionDate": "2025-11-17",
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
        "name": "Congress",
        "updateDate": "2026-01-16T13:27:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-17",
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
          "measure-id": "id119hres883",
          "measure-number": "883",
          "measure-type": "hres",
          "orig-publish-date": "2025-11-17",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres883v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-11-17",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent."
        },
        "title": "Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres883.xml",
    "summary": {
      "actionDate": "2025-11-17",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres883"
    },
    "title": "Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent."
  },
  "summaries": [
    {
      "actionDate": "2025-11-17",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres883"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres883ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:17Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 2003) to amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:05:26Z"
    }
  ]
}
```
