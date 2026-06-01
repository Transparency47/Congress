# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1012
- Title: Spent Fuel Prioritization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1012
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-07-30T12:51:54Z
- Update date including text: 2025-07-30T12:51:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1012",
    "number": "1012",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Spent Fuel Prioritization Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-30T12:51:54Z",
    "updateDateIncludingText": "2025-07-30T12:51:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1012ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1012\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Levin (for himself, Mr. Issa , Mrs. Kim , Mr. Fitzpatrick , Mr. Lawler , and Mr. Peters ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Nuclear Waste Policy Act of 1982 to prioritize the acceptance of high-level radioactive waste or spent nuclear fuel from certain civilian nuclear power reactors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Spent Fuel Prioritization Act of 2025 .\n#### 2. Acceptance priority for high-level radioactive waste and spent nuclear fuel\nSection 302(a) of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10222(a) ) is amended by adding at the end the following:\n(7) In determining the order in which the Secretary will accept high-level radioactive waste or spent nuclear fuel for disposal or storage, the Secretary shall prioritize high-level radioactive waste or spent nuclear fuel from a civilian nuclear power reactor based on the operating status of the civilian nuclear power reactor, the population of the area in which the civilian nuclear power reactor is located, the earthquake hazard of the area in which the civilian nuclear power reactor is located, and national security risk related to the continued storage of high-level radioactive waste or spent nuclear fuel in the area in which the civilian nuclear power reactor is located, giving highest priority to a civilian nuclear power reactor that is\u2014 (A) decommissioned or decommissioning; (B) located in an area, as determined by the Secretary, the population of which is the largest; (C) located in an area with the highest hazard of an earthquake, as indicated by the Seismic Hazard Maps published by the Director of the United States Geological Survey pursuant to section 5(b)(3)(J) of the Earthquake Hazards Reduction Act of 1977; and (D) located in an area, as determined by the Secretary (in consultation with the Secretary of Defense and the Secretary of Homeland Security), where the continued storage of high-level radioactive waste or spent nuclear fuel poses a significant national security concern. .",
      "versionDate": "2025-02-05",
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
        "updateDate": "2025-03-10T11:16:41Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1012ih.xml"
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
      "title": "Spent Fuel Prioritization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:54Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Spent Fuel Prioritization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Nuclear Waste Policy Act of 1982 to prioritize the acceptance of high-level radioactive waste or spent nuclear fuel from certain civilian nuclear power reactors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:16Z"
    }
  ]
}
```
