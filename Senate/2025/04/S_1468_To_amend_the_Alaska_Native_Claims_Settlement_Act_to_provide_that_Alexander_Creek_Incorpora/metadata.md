# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1468
- Title: A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1468
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1468",
    "number": "1468",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T19:33:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:34Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1468is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1468\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Sullivan introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes.\n#### 1. Alexander Creek recognition\nThe Alaska Native Claims Settlement Act ( 43 U.S.C. 1601 et seq. ) is amended by adding at the end the following:\n43. Alexander Creek recognition (a) Definitions In this section: (1) Alexander Creek, Incorporated The term Alexander Creek, Incorporated means Alexander Creek, Incorporated, the entity organized and recognized\u2014 (A) on the day before the date of enactment of this section, as a Group Corporation; and (B) effective beginning on the date of enactment of this section, as a Village Corporation. (2) Alexander Creek village The term Alexander Creek village means the community\u2014 (A) located in T. 15 N., R. 7 W., Seward Meridian, in the State; and (B) recognized as a Native village under subsection (b)(2). (3) Region The term Region means Cook Inlet Region, Incorporated, the appropriate Regional Corporation for Alexander Creek, Incorporated, under section 14(h). (b) Recognition of Alexander Creek Notwithstanding section 1432(d) of the Alaska National Interest Lands Conservation Act ( Public Law 96\u2013487 ; 94 Stat. 2543) and the deadline described in section 11(b)(3), subject to the requirements of this section\u2014 (1) Alexander Creek, Incorporated, is recognized as a Village Corporation pursuant to this Act; and (2) Alexander Creek village shall be recognized as a Native village, notwithstanding any other provision of this Act. (c) Organization of Alexander Creek, Incorporated As soon as practicable after the date of enactment of this section, Alexander Creek, Incorporated, shall submit to the Secretary\u2014 (1) any amendments to the State corporate charter of Alexander Creek, Incorporated, necessary to convert Alexander Creek, Incorporated, from a Group Corporation to a Village Corporation; and (2) if necessary, any amendments to the State corporate charter or governing business documents of Alexander Creek, Incorporated, that fulfill the terms of the agreement described in subsection (d). (d) Agreement (1) Negotiations Not later than 30 days after the date of enactment of this section, the Secretary shall offer to enter into negotiations with Alexander Creek, Incorporated, for the purposes of fairly and equitably settling\u2014 (A) the aboriginal land claims of Alexander Creek, Incorporated; and (B) any other claims of Alexander Creek, Incorporated, against the United States. (2) Condition As a condition of recognition as a Village Corporation under this Act, Alexander Creek, Incorporated, shall enter into an agreement with the Secretary to achieve the purposes described in paragraph (1) by not later than 13 months after the date of enactment of this section. (3) Parity To the maximum extent practicable, the agreement under this subsection shall achieve parity, with respect to approximate value, with similar agreements of other Village Corporations. (4) Treatment for Federal property purposes (A) Coordination with GSA The Secretary shall coordinate with the Administrator of General Services with respect to any surplus property to be transferred to Alexander Creek, Incorporated, pursuant to the agreement under this subsection. (B) Status as a State and State agency Notwithstanding paragraphs (2) and (3) of section 549(a) of title 40, United States Code, Alexander Creek, Incorporated, shall be considered to be a State and a State agency under that section for purposes of the agreement under this subsection. (C) Surplus property Notwithstanding any other provision of law, Alexander Creek, Incorporated, shall be eligible to receive real property declared to be surplus under section 1303 of title 40, United States Code, for purposes of the agreement under this subsection. (e) Shareholder participation (1) In general Alexander Creek, Incorporated, shall notify each member of Alexander Creek village that\u2014 (A) effective beginning on the date of enactment of this section, the members shall cease to receive benefits from the Region as at-large shareholders pursuant to section 7(m); and (B) all future resource payments from the Region shall be retained by Alexander Creek, Incorporated, pursuant to section 7(j). (2) Liability The Region shall not be liable under any State, Federal, or local law, or under State or Federal common law, for damages arising out of or relating to the cessation of payments to members of Alexander Creek village under paragraph (1)(A). (f) Construction relating to land entitlements (1) In general Except as provided in this section with respect to Alexander Creek, Incorporated, nothing in this section modifies or amends any land conveyance entitlements or conveyance agreement between\u2014 (A) the Region and Village Corporations other than Alexander Creek, Incorporated; (B) the Region and the Federal Government; and (C) any party described in subparagraph (A) or (B) and the State. (2) Current Alexander Creek, Incorporated, land Nothing in this section reduces the land entitlement of Alexander Creek, Incorporated, as a Group Corporation before the date of enactment of this section, including any land selected by and conveyed to Alexander Creek, Incorporated, before that date of enactment. .",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
            "name": "Alaska",
            "updateDate": "2025-12-12T20:02:30Z"
          },
          {
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2025-12-12T19:50:06Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-12-12T20:02:45Z"
          },
          {
            "name": "Small towns",
            "updateDate": "2025-12-12T20:02:17Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-12T19:50:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-27T15:49:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1468",
          "measure-number": "1468",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1468v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill recognizes Alexander Creek, Incorporated, as an Alaska Native village corporation, subject to certain conditions,\u00a0and Alexander Creek village as an Alaska Native village.</p> <p>Alexander Creek, Incorporated, must submit to the Department of the Interior any amendments to its state corporate charter that are necessary to convert from a group corporation to a village corporation.</p> <p>The bill requires Interior to offer to enter into negotiations with Alexander Creek, Incorporated, to settle aboriginal land claims and any other claims against the United States. As a condition of recognition as a village corporation, Alexander Creek, Incorporated must enter into such an agreement with Interior no later than 13 months after this bill's enactment.</p> <p>Alexander Creek, Incorporated, must notify its members that (1) they will cease to receive benefits from Cook Inlet Region, Incorporated, individually as at-large shareholders, and (2) all future resource payments shall be retained by Alexander Creek, Incorporated.</p>"
        },
        "title": "A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1468.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill recognizes Alexander Creek, Incorporated, as an Alaska Native village corporation, subject to certain conditions,\u00a0and Alexander Creek village as an Alaska Native village.</p> <p>Alexander Creek, Incorporated, must submit to the Department of the Interior any amendments to its state corporate charter that are necessary to convert from a group corporation to a village corporation.</p> <p>The bill requires Interior to offer to enter into negotiations with Alexander Creek, Incorporated, to settle aboriginal land claims and any other claims against the United States. As a condition of recognition as a village corporation, Alexander Creek, Incorporated must enter into such an agreement with Interior no later than 13 months after this bill's enactment.</p> <p>Alexander Creek, Incorporated, must notify its members that (1) they will cease to receive benefits from Cook Inlet Region, Incorporated, individually as at-large shareholders, and (2) all future resource payments shall be retained by Alexander Creek, Incorporated.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1468"
    },
    "title": "A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill recognizes Alexander Creek, Incorporated, as an Alaska Native village corporation, subject to certain conditions,\u00a0and Alexander Creek village as an Alaska Native village.</p> <p>Alexander Creek, Incorporated, must submit to the Department of the Interior any amendments to its state corporate charter that are necessary to convert from a group corporation to a village corporation.</p> <p>The bill requires Interior to offer to enter into negotiations with Alexander Creek, Incorporated, to settle aboriginal land claims and any other claims against the United States. As a condition of recognition as a village corporation, Alexander Creek, Incorporated must enter into such an agreement with Interior no later than 13 months after this bill's enactment.</p> <p>Alexander Creek, Incorporated, must notify its members that (1) they will cease to receive benefits from Cook Inlet Region, Incorporated, individually as at-large shareholders, and (2) all future resource payments shall be retained by Alexander Creek, Incorporated.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1468"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1468is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "title": "A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:28Z"
    },
    {
      "title": "A bill to amend the Alaska Native Claims Settlement Act to provide that Alexander Creek, Incorporated, is recognized as a Village Corporation under that Act, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:56:25Z"
    }
  ]
}
```
