# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/127
- Title: A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 127
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2025-12-05T21:54:46Z
- Update date including text: 2025-12-05T21:54:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1781)
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1781)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/127",
    "number": "127",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.",
    "type": "SRES",
    "updateDate": "2025-12-05T21:54:46Z",
    "updateDateIncludingText": "2025-12-05T21:54:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S1781)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-14T16:57:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres127is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 127\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Peters (for himself and Ms. Slotkin ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nHonoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.\nThat the Senate\u2014\n**(1)**\nhonors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary;\n**(2)**\ncommends the thousands of men and women who have worked and trained at Selfridge Air National Guard Base;\n**(3)**\nreinforces the commitment of the Armed Forces to Selfridge Air National Guard Base as a facility that is key to the national security of United States;\n**(4)**\nencourages continued cooperation and dialogue with the Department of Defense in support of Selfridge Air National Guard Base; and\n**(5)**\nacknowledges the ongoing investments of the State of Michigan in its defense assets and workforce and continued contributions to the defense of the United States.",
      "versionDate": "2025-03-14",
      "versionType": "IS"
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "223",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T20:57:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
    "originChamber": "Senate",
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
          "measure-id": "id119sres127",
          "measure-number": "127",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-14",
          "originChamber": "SENATE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres127v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>"
        },
        "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres127.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119sres127"
    },
    "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119sres127"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres127is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:32Z"
    },
    {
      "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T10:56:22Z"
    }
  ]
}
```
