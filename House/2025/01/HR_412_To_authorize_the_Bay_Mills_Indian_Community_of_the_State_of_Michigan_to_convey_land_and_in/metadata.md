# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/412
- Title: To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe.
- Congress: 119
- Bill type: HR
- Bill number: 412
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-04-16T19:59:23Z
- Update date including text: 2025-04-16T19:59:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-29 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-02-05 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-29 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-02-05 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/412",
    "number": "412",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe.",
    "type": "HR",
    "updateDate": "2025-04-16T19:59:23Z",
    "updateDateIncludingText": "2025-04-16T19:59:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-02-05T21:16:44Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-01-29T21:06:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr412ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 412\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Bergman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe.\n#### 1. Land and interests of the Bay Mills Indian Community of Michigan\n##### (a) In General\nSubject to subsections (b) and (c), notwithstanding any other provision of law (including regulations), the Bay Mills Indian Community of Michigan (including any agent or instrumentality of the Tribe) (referred to in this section as the Tribe ), may transfer, lease, encumber, or otherwise convey, without further authorization or approval, all or any part of the Tribe\u2019s interest in any real property that is not held in trust by the United States for the benefit of the Tribe.\n##### (b) Effect of section\nNothing in this section is intended to authorize the Tribe to transfer, lease, encumber, or otherwise convey, any lands, or any interest in any lands, that are held in trust by the United States for the benefit of the Tribe.\n##### (c) Liability\nThe United States shall not be held liable to any party (including the Tribe or any agent or instrumentality of the Tribe) for any term of, or any loss resulting from the term of any transfer, lease, encumbrance, or conveyance of land made pursuant to this Act unless the United States or an agent or instrumentality of the United States is a party to the transaction or the United States would be liable pursuant to any other provision of law. This subsection shall not apply to land transferred or conveyed by the Tribe to the United States to be held in trust for the benefit of the Tribe.",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-04-14T17:58:05Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-04-14T17:58:11Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2025-04-14T17:57:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-04-09T20:08:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr412",
          "measure-number": "412",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr412v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill allows the Bay Mills Indian Community of Michigan to transfer, lease, encumber, or otherwise convey its real property that is not held in trust by the United States. The United States shall not be held liable for any loss resulting from a transfer of real property by the tribe.</p>"
        },
        "title": "To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr412.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill allows the Bay Mills Indian Community of Michigan to transfer, lease, encumber, or otherwise convey its real property that is not held in trust by the United States. The United States shall not be held liable for any loss resulting from a transfer of real property by the tribe.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hr412"
    },
    "title": "To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe."
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill allows the Bay Mills Indian Community of Michigan to transfer, lease, encumber, or otherwise convey its real property that is not held in trust by the United States. The United States shall not be held liable for any loss resulting from a transfer of real property by the tribe.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hr412"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr412ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:24Z"
    },
    {
      "title": "To authorize the Bay Mills Indian Community of the State of Michigan to convey land and interests in land owned by the Tribe.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-16T09:06:12Z"
    }
  ]
}
```
