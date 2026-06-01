# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8132
- Title: Bonneville Power Leadership Recruitment Act
- Congress: 119
- Bill type: HR
- Bill number: 8132
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-28T08:05:47Z
- Update date including text: 2026-04-28T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8132",
    "number": "8132",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "Bonneville Power Leadership Recruitment Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:47Z",
    "updateDateIncludingText": "2026-04-28T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:33:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "ID"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "NV"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8132ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8132\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Bentz (for himself, Mr. Simpson , and Mr. Amodei of Nevada ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo adjust the compensation of the Administrator of the Bonneville Power Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bonneville Power Leadership Recruitment Act .\n#### 2. Bonneville Power Administrator compensation\n##### (a) Rate of pay\nBeginning in the first pay period beginning on or after the date that is 6 months after the date of the enactment of this Act, the annual rate of basic pay\u2014\n**(1)**\nfor the Administrator of the Bonneville Power Administration (referred to in this section as the Administrator ) shall be set at a level determined by the Secretary of Energy (referred to in this section as the Secretary ) to be comparable to chief executives of consumer-owned utilities in the Western Interconnection; and\n**(2)**\nfor employees of the Bonneville Power Administration, including members of the Senior Executive Service (as defined in section 2101a of title 5, United States Code), shall be set at a level determined by the Secretary to be comparable to compensation for similar positions at consumer-owned utilities in the Western Interconnection.\n##### (b) Additional considerations\nThe determination of the Secretary with respect to the annual rate of basic pay under subsection (a) shall\u2014\n**(1)**\nbe based on an annual survey of the prevailing compensation for similar positions in consumer-owned utilities in the Western Interconnection;\n**(2)**\nbe consistent with the approved annual general and administrative budget of the Administrator, encourage the widest diversified use of electric power at the lowest possible rates to consumers consistent with sound business principles, and be cognizant of the need for deep experience, strategic vision, intelligence, and accountability;\n**(3)**\nwith respect to pay for employees of the Bonneville Power Administration, take into account education, experience, level of responsibility, geographic differences, and retention and recruitment needs; and\n**(4)**\nprovide that the individual total compensation of the Administrator and employees of the Bonneville Power Administration shall be comparable to and competitive with similar positions among consumer-owned utilities in the Western Interconnection.\n##### (c) Conforming amendment\nSection 5316 of title 5, United States Code, is amended by striking Administrator, Bonneville Power Administration, Department of the Interior. .",
      "versionDate": "2026-03-27",
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
        "name": "Energy",
        "updateDate": "2026-04-14T13:58:37Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8132ih.xml"
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
      "title": "Bonneville Power Leadership Recruitment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bonneville Power Leadership Recruitment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To adjust the compensation of the Administrator of the Bonneville Power Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:36Z"
    }
  ]
}
```
