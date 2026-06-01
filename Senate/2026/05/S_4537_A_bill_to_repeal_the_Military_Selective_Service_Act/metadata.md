# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4537?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4537
- Title: A bill to repeal the Military Selective Service Act.
- Congress: 119
- Bill type: S
- Bill number: 4537
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-28T22:29:32Z
- Update date including text: 2026-05-28T22:29:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4537",
    "number": "4537",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A bill to repeal the Military Selective Service Act.",
    "type": "S",
    "updateDate": "2026-05-28T22:29:32Z",
    "updateDateIncludingText": "2026-05-28T22:29:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T17:10:31Z",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "KY"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4537is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4537\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Wyden (for himself, Mr. Paul , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo repeal the Military Selective Service Act.\n#### 1. Repeal of Military Selective Service Act\n##### (a) Repeal\nThe Military Selective Service Act ( 50 U.S.C. 3801 et seq. ) is repealed.\n##### (b) Transfers in connection with repeal\nNotwithstanding the proviso in section 10(a)(4) of the Military Selective Service Act ( 50 U.S.C. 3809(a)(4) ), the Office of Selective Service Records shall not be reestablished upon the repeal of the Act. Not later than 180 days after the date of the enactment of this Act, the assets, contracts, property, and records held by the Selective Service System, and the unexpended balances of any appropriations available to the Selective Service System, shall be transferred to the Administrator of General Services upon the repeal of the Act. The Director of the Office of Personnel Management shall assist officers and employees of the Selective Service System to transfer to other positions in the executive branch.\n##### (c) Effect on existing sanctions\n**(1)**\nNotwithstanding any other provision of law, a person may not be denied a right, privilege, benefit, or employment position under Federal law on the grounds that the person failed to present himself for and submit to registration under section 3 of the Military Selective Service Act ( 50 U.S.C. 3802 ), before the repeal of that Act by subsection (a).\n**(2)**\nA State, political subdivision of a State, or political authority of two or more States may not enact or enforce a law, regulation, or other provision having the force and effect of law to penalize or deny any privilege or benefit to a person who failed to present himself for and submit to registration under section 3 of the Military Selective Service Act ( 50 U.S.C. 3802 ), before the repeal of that Act by subsection (a). In this section, State means a State, the District of Columbia, and a territory or possession of the United States.\n**(3)**\nFailing to present oneself for and submit to registration under section 3 of the Military Selective Service Act ( 50 U.S.C. 3802 ), before the repeal of that Act by subsection (a), shall not be reason for any entity of the U.S. Government to determine that a person lacks good moral character or is unsuited for any privilege or benefit.\n##### (d) Conscientious objectors\nNothing contained in this Act shall be construed to undermine or diminish the rights of conscientious objectors under laws and regulations of the United States.",
      "versionDate": "2026-05-14",
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
        "updateDate": "2026-05-28T22:29:32Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4537is.xml"
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
      "title": "A bill to repeal the Military Selective Service Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T03:03:23Z"
    },
    {
      "title": "A bill to repeal the Military Selective Service Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T10:56:30Z"
    }
  ]
}
```
