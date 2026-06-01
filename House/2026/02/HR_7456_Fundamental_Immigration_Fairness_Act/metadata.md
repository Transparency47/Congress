# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7456
- Title: Fundamental Immigration Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 7456
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-19T16:52:58Z
- Update date including text: 2026-02-19T16:52:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7456",
    "number": "7456",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Fundamental Immigration Fairness Act",
    "type": "HR",
    "updateDate": "2026-02-19T16:52:58Z",
    "updateDateIncludingText": "2026-02-19T16:52:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7456ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7456\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mrs. Watson Coleman (for herself, Mr. Pocan , and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit the authority of the Secretary of Homeland Security to detain aliens of good moral character, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fundamental Immigration Fairness Act .\n#### 2. Limitation on detention of aliens of good moral character\n##### (a) In general\nExcept as provided in subsection (b), the Secretary of Homeland Security may not take into custody an alien, prior to the entry of an order of removal against the alien, who is arriving at or departing from\u2014\n**(1)**\nany field office of the Department of Homeland Security; or\n**(2)**\nany facility of the Executive Office for Immigration Review.\n##### (b) Exception\nSubsection (a) shall not apply in the case of an alien who is not of good moral character, as determined by an immigration judge, in accordance with section 101(f) of the Immigration and Nationality Act ( 8 U.S.C. 1101(f) ).\n##### (c) Clarification\nSection 101(f) of the Immigration and Nationality Act is amended by adding at the end the following: A determination that an alien is not of good moral character may not be based solely on the alien\u2019s unlawful presence in or unlawful entry into the United States. .\n##### (d) Definitions\nIn this section, the terms have the meanings given such terms in the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n#### 3. No public display of parties to immigration proceedings\nThe Attorney General may not display the name of any party (other than the United States) to an immigration proceeding outside the room in which the proceeding is taking place or is to take place, or any other location in a facility of the Executive Office for Immigration Review that can be accessed by the public.",
      "versionDate": "2026-02-09",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-02-19T16:52:58Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7456ih.xml"
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
      "title": "Fundamental Immigration Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T06:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fundamental Immigration Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the authority of the Secretary of Homeland Security to detain aliens of good moral character, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T06:48:25Z"
    }
  ]
}
```
