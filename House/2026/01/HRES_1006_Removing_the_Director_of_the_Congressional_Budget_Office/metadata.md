# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1006?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1006
- Title: Removing the Director of the Congressional Budget Office.
- Congress: 119
- Bill type: HRES
- Bill number: 1006
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-03-12T18:59:05Z
- Update date including text: 2026-03-12T18:59:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Budget.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House
- Latest action: 2026-01-15: Submitted in House

## Actions

- 2026-01-15 - IntroReferral: Referred to the House Committee on the Budget.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1006",
    "number": "1006",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Removing the Director of the Congressional Budget Office.",
    "type": "HRES",
    "updateDate": "2026-03-12T18:59:05Z",
    "updateDateIncludingText": "2026-03-12T18:59:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1006ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1006\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Mills submitted the following resolution; which was referred to the Committee on the Budget\nRESOLUTION\nRemoving the Director of the Congressional Budget Office.\nThat effective immediately on the date of the adoption of this resolution, the Director of the Congressional Budget Office is hereby removed pursuant to section 201(a)(4) of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 601(a)(4) ).",
      "versionDate": "2026-01-15",
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
        "name": "Economics and Public Finance",
        "updateDate": "2026-01-16T18:59:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-15",
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
          "measure-id": "id119hres1006",
          "measure-number": "1006",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-15",
          "originChamber": "HOUSE",
          "update-date": "2026-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1006v00",
            "update-date": "2026-03-12"
          },
          "action-date": "2026-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution removes Congressional Budget Office (CBO) Director Phillip Swagel from his position. (Under current law, either chamber of Congress may remove the CBO director with a resolution.)</p>"
        },
        "title": "Removing the Director of the Congressional Budget Office."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1006.xml",
    "summary": {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution removes Congressional Budget Office (CBO) Director Phillip Swagel from his position. (Under current law, either chamber of Congress may remove the CBO director with a resolution.)</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hres1006"
    },
    "title": "Removing the Director of the Congressional Budget Office."
  },
  "summaries": [
    {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution removes Congressional Budget Office (CBO) Director Phillip Swagel from his position. (Under current law, either chamber of Congress may remove the CBO director with a resolution.)</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hres1006"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1006ih.xml"
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
      "title": "Removing the Director of the Congressional Budget Office.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:42Z"
    },
    {
      "title": "Removing the Director of the Congressional Budget Office.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:06:17Z"
    }
  ]
}
```
