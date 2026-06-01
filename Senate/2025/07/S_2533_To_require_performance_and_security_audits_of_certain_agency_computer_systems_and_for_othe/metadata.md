# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2533
- Title: Pick Up After Your DOGE Act
- Congress: 119
- Bill type: S
- Bill number: 2533
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-09-17T22:00:35Z
- Update date including text: 2025-09-17T22:00:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2533",
    "number": "2533",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Pick Up After Your DOGE Act",
    "type": "S",
    "updateDate": "2025-09-17T22:00:35Z",
    "updateDateIncludingText": "2025-09-17T22:00:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T15:12:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2533is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2533\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Whitehouse (for himself, Mr. Wyden , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require performance and security audits of certain agency computer systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pick Up After Your DOGE Act .\n#### 2. Definition\nIn this Act, the term appropriate congressional committee means any committee with jurisdiction over an agency that is the subject of an audit under this Act.\n#### 3. United States DOGE service access to data\nNot later than 30 days after the date of enactment of this Act, the Administrator of the United States DOGE Service shall submit to the appropriate congressional committees and the Comptroller General of the United States a full accounting of all Federal agencies where agency DOGE teams, as defined in Executive Order 14158 (90 Fed. Reg. 8441; relating to establishing and implementing the President's Department of Government Efficiency), or individuals acting on behalf of, or at the instruction of, the United States DOGE Service or agency DOGE teams, accessed Federal agency computer systems, networks, data, or information.\n#### 4. Comptroller General studies\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the Comptroller General of the United States shall commence a comprehensive audit of Federal agency computer systems and networks accessed by the United States DOGE Service, the U.S. DOGE Service Temporary Organization, or any employees or volunteers affiliated with those agencies, or, if applicable, associated agency DOGE teams, to identify security vulnerabilities or bugs in software installed, created, or modified by the United States DOGE Service, the U.S. DOGE Service Temporary Organization, or any employees or volunteers affiliated with those agencies, or, if applicable, associated agency DOGE teams.\n##### (b) Priority review\nIn conducting the audits described in subsection (a), the Comptroller General shall give priority to reviews of the systems, networks, and databases of the Social Security Administration, the Department of Health and Human Services and the Centers for Medicare & Medicaid Services, and the Department of the Treasury and the Internal Revenue Service.\n##### (c) Initial Audit Results\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall submit to the appropriate congressional committees and agency heads a report or reports describing the results of the comprehensive systems audits performed under subsection (a) for the Social Security Administration, the Department of Health and Human Services and the Centers for Medicare & Medicaid Services, and the Department of the Treasury and the Internal Revenue Service, including recommendations for legislation and administrative action as the Comptroller General determines appropriate.\n##### (d) Final audit results\nNot later than 2 years after the date of enactment of this Act, the Comptroller General shall submit to the appropriate congressional committees and agency heads a report or reports describing the results of the comprehensive systems audits performed under subsection (a) for other Federal agencies selected for review by the Comptroller General, in consultation with the appropriate congressional committees, including recommendations for legislation and administrative actions as the Comptroller General determines appropriate.\n##### (e) Agency action\nNot later than 90 days after receipt of an audit report by an agency head under subsections (c) or (d), the agency head shall\u2014\n**(1)**\nfix any vulnerabilities or bugs identified in the report; and\n**(2)**\nsubmit to the appropriate committee of jurisdiction a report on the status of those vulnerabilities or bugs.",
      "versionDate": "2025-07-30",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T22:00:35Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2533is.xml"
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
      "title": "Pick Up After Your DOGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pick Up After Your DOGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require performance and security audits of certain agency computer systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T04:48:19Z"
    }
  ]
}
```
