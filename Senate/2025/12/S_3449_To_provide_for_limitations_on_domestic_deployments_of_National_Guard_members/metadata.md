# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3449
- Title: NOTICE Act
- Congress: 119
- Bill type: S
- Bill number: 3449
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-06T19:42:58Z
- Update date including text: 2026-01-06T19:42:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3449",
    "number": "3449",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "NOTICE Act",
    "type": "S",
    "updateDate": "2026-01-06T19:42:58Z",
    "updateDateIncludingText": "2026-01-06T19:42:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T19:02:44Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "HI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MD"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3449is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3449\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Booker (for himself, Mr. Blumenthal , Ms. Hirono , Mr. Van Hollen , Ms. Slotkin , Mr. Padilla , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for limitations on domestic deployments of National Guard members.\n#### 1. Short title\nThis Act may be cited as the Notification of Troop Involvement and Congressional Engagement Act or the NOTICE Act .\n#### 2. Limitations on domestic deployments of National Guard members\nSection 12406 of title 10, United States Code, is amended\u2014\n**(1)**\nby striking Whenever and inserting (a) In general .\u2014Whenever ; and\n**(2)**\nby adding at the end the following new subsections:\n(b) Notification requirement (1) Not later than 24 hours before calling into Federal service members and units of the National Guard of any State under subsection (a), the President shall notify Congress of the planned deployment. (2) The notice required under paragraph (1) shall assert a good-faith claim for federalizing the National Guard and describe with specificity\u2014 (A) (i) the invasion, including the United States territory, the foreign power, and the act or acts of the foreign power that constitute an invasion necessitating the use of authority pursuant to subsection (a)(1); (ii) the rebellion against the authority of the Government of the United States, including the place and time of the rebellion, the person, persons, or group engaged in the rebellion, and the activities of those engaged in the rebellion necessitating the use of authority pursuant to subsection (a)(2); or (iii) the laws of the United States which the President is unable to execute, the reasons that regular forces are unable to execute the law, and, where the President is taking such action without the consent of the Governor of the State, evidence of the Governor\u2019s inability or refusal to provide for the safety and welfare of the public, or the Governor\u2019s refusal to obey a court order, or other active steps the Governor has taken to obstruct the President from faithfully executing the law; (B) the geographical area where the National Guard will be called to and the duration of the federalization of the National Guard; (C) the training received by the National Guard unit or units expected to be deployed and interacting with civilian populations, including restrictions under section 1385 of title 18; and (D) the chain of command the National Guard unit or units will be placed under and their requirements to communicate with state and local forces. (c) Notification requirement for longer deployments (1) If a deployment under this section lasts longer than 48 hours, the President shall notify Congress of the continued deployment in writing and provide subsequent updates every 72 hours thereafter. (2) The notice required under paragraph (1) shall assert a good-faith claim for the continued deployment of the National Guard and describe with specificity the conditions described under subsection (b)(2), including any changes to the conditions since the prior notice. .",
      "versionDate": "2025-12-11",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T19:42:58Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3449is.xml"
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
      "title": "NOTICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NOTICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Notification of Troop Involvement and Congressional Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for limitations on domestic deployments of National Guard members.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:34Z"
    }
  ]
}
```
