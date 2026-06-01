# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4864?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4864
- Title: Ethanol for America Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4864
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-04-06T12:43:25Z
- Update date including text: 2026-04-06T12:43:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4864",
    "number": "4864",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Ethanol for America Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T12:43:25Z",
    "updateDateIncludingText": "2026-04-06T12:43:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:07:00Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "SD"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "KS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "KS"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4864ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4864\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Smith of Nebraska (for himself, Ms. Budzinski , Mr. Johnson of South Dakota , Mr. Mann , Mr. Schmidt , Mr. Flood , Mr. Feenstra , and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Environmental Protection Agency to finalize a proposed rule with respect to E15 fuel dispenser labeling and compatibility with underground storage tanks with modifications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ethanol for America Act of 2025 .\n#### 2. Finalization of proposed rule required\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Proposed rule**\nThe term proposed rule means the proposed rule of the Administrator entitled E15 Fuel Dispenser Labeling and Compatibility with Underground Storage Tanks (86 Fed. Reg. 5094 (January 19, 2021)).\n##### (b) Finalization required\nNot later than 90 days after the date of enactment of this Act, the Administrator shall finalize the proposed rule in accordance with this section.\n##### (c) E15 labeling requirements\nIn finalizing the proposed rule pursuant to subsection (b) with respect to E15 labeling, the Administrator shall finalize the first co-proposal described in the proposed rule.\n##### (d) E15 compatibility with underground storage tanks\n**(1) E15 compatibility**\nIn finalizing the proposed rule pursuant to subsection (b) with respect to the compatibility of underground storage tanks with fuel blends with up to 15 percent ethanol, the Administrator shall ensure that\u2014\n**(A)**\nexisting underground storage tank systems are deemed to be compliant with fuel blends with up to 15 percent ethanol, regardless of whether the owners or operators of those systems are able to locate installation or compatibility documentation for those systems;\n**(B)**\nsteel and fiberglass underground storage tanks manufactured after July 2005 and all fiberglass reinforced plastic piping are considered compatible with fuel blends of up to 15 percent ethanol; and\n**(C)**\nif owners or operators of underground storage tank systems can demonstrate the compatibility of certain components of those systems (such as gaskets or seals) with fuel blends with up to 15 percent ethanol, those owners or operators are not required to replace other equipment to achieve full system compatibility.\n**(2) Future storage flexibility**\nFor purposes of ensuring that gasoline and diesel underground storage tank systems have future flexibility in fuel storage, the Administrator, in finalizing the proposed rule pursuant to subsection (b), shall require owners and operators of underground storage tank systems that store motor fuel for on-road vehicles to ensure that those systems and the components of those systems, including components such as pipe dopes and sealants, that are installed or replaced after the effective date of the proposed rule are compatible with fuel blends with up to 100 percent ethanol, regardless of the types of fuel blends currently being stored in those systems.",
      "versionDate": "2025-08-01",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-31",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2591",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ethanol for America Act of 2025",
      "type": "S"
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-06T12:43:24Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4864ih.xml"
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
      "title": "Ethanol for America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ethanol for America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Environmental Protection Agency to finalize a proposed rule with respect to E15 fuel dispenser labeling and compatibility with underground storage tanks with modifications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:32Z"
    }
  ]
}
```
