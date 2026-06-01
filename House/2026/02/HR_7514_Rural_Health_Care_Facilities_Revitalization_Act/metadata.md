# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7514
- Title: Rural Health Care Facilities Revitalization Act
- Congress: 119
- Bill type: HR
- Bill number: 7514
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-02-27T20:04:43Z
- Update date including text: 2026-02-27T20:04:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7514",
    "number": "7514",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Rural Health Care Facilities Revitalization Act",
    "type": "HR",
    "updateDate": "2026-02-27T20:04:43Z",
    "updateDateIncludingText": "2026-02-27T20:04:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "MI"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "HI"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7514ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7514\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Ms. Salinas (for herself, Mr. Moolenaar , Ms. Tokuda , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo authorize rural health facilities to use certain Federal agricultural credit assistance for the purpose of refinancing debt obligations, updating necessary services, technology, and equipment, and supporting ancillary needs.\n#### 1. Short title\nThis Act may be cited as the Rural Health Care Facilities Revitalization Act .\n#### 2. Assistance for distressed rural health care facilities\n##### (a) In general\nSubtitle A of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922\u20131936c ) is amended by adding at the end the following:\n310J. Assistance for distressed rural health care facilities (a) In general A health care facility, including a hospital, behavioral health facility, health care clinic (including a mobile health care clinic), home health agency, and long-term care facility, in a rural area may use assistance provided under section 306(a) for a community facility, or under section 310B, to\u2014 (1) refinance a debt obligation; (2) update a telehealth, equipment, or online database; or (3) support ancillary needs, including operating expenses and reserve funds. (b) Limitations A facility may use assistance pursuant to subsection (a) only if doing so would\u2014 (1) help preserve access to a health service in a rural community; (2) meaningfully improve the financial position of the facility; and (3) otherwise meet the financial feasibility and security adequacy requirements of the Rural Development Agency. (c) Waiver In the case of an application from a facility referred to in subsection (a) of this section for assistance under section 306(a) for a community facility, or under section 310B, the Secretary may waive the requirement of section 302(a)(1)(D) if the facility that is insolvent or located in a persistent poverty area, socially vulnerable community (as determined by the Secretary), or distressed area (as determined by the Secretary). (d) Definitions In this section: (1) Persistent poverty area The term persistent poverty area means an area with a poverty rate of 20 percent or more for 4 consecutive time periods, approximately 10 years apart, spanning approximately 30 years. (2) Rural area The term rural area means an area with a population of 50,000 or fewer inhabitants that is not an urbanized area adjacent or contiguous to a city with a population of more than 50,000 inhabitants. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect 6 months after the date of the enactment of this Act.",
      "versionDate": "2026-02-11",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-27T20:04:43Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7514ih.xml"
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
      "title": "Rural Health Care Facilities Revitalization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Health Care Facilities Revitalization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize rural health facilities to use certain Federal agricultural credit assistance for the purpose of refinancing debt obligations, updating necessary services, technology, and equipment, and supporting ancillary needs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:28Z"
    }
  ]
}
```
