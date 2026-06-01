# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/748
- Title: A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 748
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-02-04T05:06:22Z
- Update date including text: 2026-02-04T05:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-03-05 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.
- 2025-10-14 - Committee: Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.
- 2025-10-14 - Committee: Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.
- 2025-10-14 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 188.
- 2025-12-15 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8747-8748; text: CR S8748)
- 2025-12-15 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Floor: Message on Senate action sent to the House.
- 2025-12-16 12:04:14 - Floor: Received in the House.
- 2025-12-16 12:21:34 - Floor: Held at the desk.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-03-05 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.
- 2025-10-14 - Committee: Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.
- 2025-10-14 - Committee: Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.
- 2025-10-14 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 188.
- 2025-12-15 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8747-8748; text: CR S8748)
- 2025-12-15 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Floor: Message on Senate action sent to the House.
- 2025-12-16 12:04:14 - Floor: Received in the House.
- 2025-12-16 12:21:34 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/748",
    "number": "748",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.",
    "type": "S",
    "updateDate": "2026-02-04T05:06:22Z",
    "updateDateIncludingText": "2026-02-04T05:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-16",
      "actionTime": "12:21:34",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-16",
      "actionTime": "12:04:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8747-8748; text: CR S8748)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 188.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Indian Affairs. Reported by Senator Murkowski without amendment. With written report No. 119-79.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
            "date": "2025-10-14T19:58:17Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-05T19:30:46Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-26T18:39:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 748\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.\n#### 1. Lytton Rancheria of California land reaffirmation\n##### (a) In general\nNotwithstanding any other provision of law, the Lytton Rancheria of California is subject to the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 984, chapter 576; 25 U.S.C. 5101 et seq. ), and the Secretary of the Interior may acquire and take into trust land for the benefit of the Lytton Rancheria of California pursuant to section 5 of that Act ( 25 U.S.C. 5108 ).\n##### (b) Land To Be made part of the reservation\nLand taken into trust pursuant to subsection (a) shall be\u2014\n**(1)**\npart of the reservation of the Lytton Rancheria of California; and\n**(2)**\nadministered in accordance with the laws and regulations generally applicable to property held in trust by the United States for an Indian Tribe.",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748rs.xml",
      "text": "II\nCalendar No. 188\n119th CONGRESS\n1st Session\nS. 748\n[Report No. 119\u201379]\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nOctober 14, 2025 Reported by Ms. Murkowski , without amendment\nA BILL\nTo reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.\n#### 1. Lytton Rancheria of California land reaffirmation\n##### (a) In general\nNotwithstanding any other provision of law, the Lytton Rancheria of California is subject to the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 984, chapter 576; 25 U.S.C. 5101 et seq. ), and the Secretary of the Interior may acquire and take into trust land for the benefit of the Lytton Rancheria of California pursuant to section 5 of that Act ( 25 U.S.C. 5108 ).\n##### (b) Land To Be made part of the reservation\nLand taken into trust pursuant to subsection (a) shall be\u2014\n**(1)**\npart of the reservation of the Lytton Rancheria of California; and\n**(2)**\nadministered in accordance with the laws and regulations generally applicable to property held in trust by the United States for an Indian Tribe.",
      "versionDate": "2025-10-14",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 748\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.\n#### 1. Lytton Rancheria of California land reaffirmation\n##### (a) In general\nNotwithstanding any other provision of law, the Lytton Rancheria of California is subject to the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 984, chapter 576; 25 U.S.C. 5101 et seq. ), and the Secretary of the Interior may acquire and take into trust land for the benefit of the Lytton Rancheria of California pursuant to section 5 of that Act ( 25 U.S.C. 5108 ).\n##### (b) Land To Be made part of the reservation\nLand taken into trust pursuant to subsection (a) shall be\u2014\n**(1)**\npart of the reservation of the Lytton Rancheria of California; and\n**(2)**\nadministered in accordance with the laws and regulations generally applicable to property held in trust by the United States for an Indian Tribe.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "California",
            "updateDate": "2025-06-25T18:30:33Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-06-25T18:30:33Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-06-25T18:30:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-24T18:57:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s748",
          "measure-number": "748",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s748v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill applies the Indian Reorganization Act (IRA) to the Lytton Rancheria of California. Additionally, the bill authorizes the Department of the Interior to acquire and take land into trust for the benefit of the tribe under the IRA. Land taken into trust shall be part of the tribe's reservation.</p><p>A 2009 Supreme Court case, <em>Carcieri v. Salazar</em>, decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Lytton Rancheria of California, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) authorizes\u00a0Interior to take land into trust for the benefit of the tribe.</p>"
        },
        "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s748.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill applies the Indian Reorganization Act (IRA) to the Lytton Rancheria of California. Additionally, the bill authorizes the Department of the Interior to acquire and take land into trust for the benefit of the tribe under the IRA. Land taken into trust shall be part of the tribe's reservation.</p><p>A 2009 Supreme Court case, <em>Carcieri v. Salazar</em>, decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Lytton Rancheria of California, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) authorizes\u00a0Interior to take land into trust for the benefit of the tribe.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s748"
    },
    "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill applies the Indian Reorganization Act (IRA) to the Lytton Rancheria of California. Additionally, the bill authorizes the Department of the Interior to acquire and take land into trust for the benefit of the tribe under the IRA. Land taken into trust shall be part of the tribe's reservation.</p><p>A 2009 Supreme Court case, <em>Carcieri v. Salazar</em>, decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Lytton Rancheria of California, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) authorizes\u00a0Interior to take land into trust for the benefit of the tribe.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s748"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s748es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T15:18:43Z"
    },
    {
      "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Lytton Rancheria of California, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-27T11:56:21Z"
    }
  ]
}
```
