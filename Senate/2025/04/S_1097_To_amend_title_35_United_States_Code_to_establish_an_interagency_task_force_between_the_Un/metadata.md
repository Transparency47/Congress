# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1097?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1097
- Title: Interagency Patent Coordination and Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1097
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2025-12-05T21:51:50Z
- Update date including text: 2025-12-05T21:51:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1804-1805)
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 41.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1804-1805)
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 41.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1097",
    "number": "1097",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Interagency Patent Coordination and Improvement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:51:50Z",
    "updateDateIncludingText": "2025-12-05T21:51:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 41.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S1804-1805)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
        "item": [
          {
            "date": "2025-04-10T20:23:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-24T22:04:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DE"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1097is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1097\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Durbin (for himself, Mr. Tillis , Mr. Grassley , Mr. Coons , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to establish an interagency task force between the United States Patent and Trademark Office and the Food and Drug Administration for purposes of sharing information and providing technical assistance with respect to patents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the \u201c Interagency Patent Coordination and Improvement Act of 2025 \u201d.",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1097rs.xml",
      "text": "II\nCalendar No. 41\n119th CONGRESS\n1st Session\nS. 1097\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Durbin (for himself, Mr. Tillis , Mr. Grassley , Mr. Coons , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo amend title 35, United States Code, to establish an interagency task force between the United States Patent and Trademark Office and the Food and Drug Administration for purposes of sharing information and providing technical assistance with respect to patents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the \u201c Interagency Patent Coordination and Improvement Act of 2025 \u201d.",
      "versionDate": "2025-04-10",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4570",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Interagency Patent Coordination and Improvement Act of 2025",
      "type": "HR"
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
            "name": "Administrative remedies",
            "updateDate": "2025-04-08T14:59:28Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2025-04-08T14:59:28Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-08T14:59:28Z"
          },
          {
            "name": "Food and Drug Administration (FDA)",
            "updateDate": "2025-04-08T14:59:28Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-04-08T14:59:28Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-04-08T14:59:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-04-03T17:16:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119s1097",
          "measure-number": "1097",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1097v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Interagency Patent Coordination and Improvement Act of 2025</strong></p><p>This bill establishes the Interagency Task Force on Patents to support coordination and communication between the U.S. Patent and Trademark Office (USPTO) and the Food and Drug Administration (FDA) on activities relating to patents for human drugs and biological products.</p><p>The task force's duties shall include sharing information about (1) the processes of each agency, including how each agency evaluates applications (e.g., patent applications at the USPTO and new drug applications at the FDA); and (2) new approvals of patents, human drugs, biological products, and new technologies. The task force must also establish a process that requires (1) the USPTO to request from the FDA information relating to certain patent applications to help patent examiners carry out their duties, (2) the FDA to provide such information to the USPTO, and (3) the USPTO to assist the FDA in its ministerial role of listing patents.</p>"
        },
        "title": "Interagency Patent Coordination and Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1097.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interagency Patent Coordination and Improvement Act of 2025</strong></p><p>This bill establishes the Interagency Task Force on Patents to support coordination and communication between the U.S. Patent and Trademark Office (USPTO) and the Food and Drug Administration (FDA) on activities relating to patents for human drugs and biological products.</p><p>The task force's duties shall include sharing information about (1) the processes of each agency, including how each agency evaluates applications (e.g., patent applications at the USPTO and new drug applications at the FDA); and (2) new approvals of patents, human drugs, biological products, and new technologies. The task force must also establish a process that requires (1) the USPTO to request from the FDA information relating to certain patent applications to help patent examiners carry out their duties, (2) the FDA to provide such information to the USPTO, and (3) the USPTO to assist the FDA in its ministerial role of listing patents.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s1097"
    },
    "title": "Interagency Patent Coordination and Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interagency Patent Coordination and Improvement Act of 2025</strong></p><p>This bill establishes the Interagency Task Force on Patents to support coordination and communication between the U.S. Patent and Trademark Office (USPTO) and the Food and Drug Administration (FDA) on activities relating to patents for human drugs and biological products.</p><p>The task force's duties shall include sharing information about (1) the processes of each agency, including how each agency evaluates applications (e.g., patent applications at the USPTO and new drug applications at the FDA); and (2) new approvals of patents, human drugs, biological products, and new technologies. The task force must also establish a process that requires (1) the USPTO to request from the FDA information relating to certain patent applications to help patent examiners carry out their duties, (2) the FDA to provide such information to the USPTO, and (3) the USPTO to assist the FDA in its ministerial role of listing patents.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s1097"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1097is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1097rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Interagency Patent Coordination and Improvement Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "title": "Interagency Patent Coordination and Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Interagency Patent Coordination and Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 35, United States Code, to establish an interagency task force between the United States Patent and Trademark Office and the Food and Drug Administration for purposes of sharing information and providing technical assistance with respect to patents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:47Z"
    }
  ]
}
```
