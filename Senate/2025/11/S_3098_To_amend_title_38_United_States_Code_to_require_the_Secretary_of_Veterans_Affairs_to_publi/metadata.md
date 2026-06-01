# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3098
- Title: Presumptive CLARITY Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3098
- Origin chamber: Senate
- Introduced date: 2025-11-04
- Update date: 2026-05-06T16:21:08Z
- Update date including text: 2026-05-06T16:21:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in Senate
- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-11-04: Introduced in Senate

## Actions

- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3098",
    "number": "3098",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Presumptive CLARITY Act of 2025",
    "type": "S",
    "updateDate": "2026-05-06T16:21:08Z",
    "updateDateIncludingText": "2026-05-06T16:21:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-04",
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
            "date": "2026-04-29T21:37:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-04T20:12:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3098is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3098\nIN THE SENATE OF THE UNITED STATES\nNovember 4, 2025 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to publish information about conditions and cohorts the Department of Veterans Affairs is considering for purposes of establishing or removing presumptions of service connection regarding toxic exposure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Presumptive Clear Legal Assessment and Review of Illnesses from Toxic exposure Yields Act of 2025 or the Presumptive CLARITY Act of 2025 .\n#### 2. Requiring public transparency in process of determinations relating to presumptions of service connection regarding toxic exposure\n##### (a) In general\nSubchapter I of chapter 11 of title 38, United States Code, is amended by adding at the end the following new section:\n1105. Public transparency regarding presumptions of service connection regarding toxic exposure (a) Publication required The Secretary shall establish and maintain on a publicly accessible website of the Department a list of conditions and cohorts that the Department is considering for purposes of establishing or removing a presumption of service connection based on toxic exposure. (b) Contents Publication under subsection (a) shall include the following: (1) An overview of the process for the establishment or removal described in subsection (a), including the steps and goals for time of completion for each step. (2) For each condition and cohort for which the Department is considering establishing or removing as described in subsection (a), the following: (A) The status of the condition or cohort in the process being carried out by the Department for such establishment or removal. (B) The actions taken by the Department regarding notice and opportunity for public comment on the establishment or removal, including instructions on how the public can submit comments and recommendations. .\n##### (b) Commencement of publication\nThe Secretary of Veterans Affairs shall ensure that publication required by section 1105 of such title, as added by subsection (a), commences on or before the date that is 180 days after the date of the enactment of this Act.\n##### (c) Clerical amendment\nThe table of sections at the beginning of chapter 11 of such title is amended by inserting after the item relating to section 1104 the following new item:\n1105. Public transparency regarding presumptions of service connection regarding toxic exposure. .",
      "versionDate": "2025-11-04",
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
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2026-05-06T16:19:38Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-06T16:21:07Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-06T16:20:52Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-05-06T16:19:26Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-05-06T16:20:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:43:07Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3098is.xml"
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
      "title": "Presumptive CLARITY Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Presumptive CLARITY Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Presumptive Clear Legal Assessment and Review of Illnesses from Toxic exposure Yields Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to require the Secretary of Veterans Affairs to publish information about conditions and cohorts the Department of Veterans Affairs is considering for purposes of establishing or removing presumptions of service connection regarding toxic exposure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:25Z"
    }
  ]
}
```
