# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3697?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3697
- Title: RAVES Reporting Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3697
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2025-07-16T14:38:19Z
- Update date including text: 2025-07-16T14:38:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3697",
    "number": "3697",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "RAVES Reporting Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-16T14:38:19Z",
    "updateDateIncludingText": "2025-07-16T14:38:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3697ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3697\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. David Scott of Georgia introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to conduct a study, and publish guidance, on the conversion of rural abandoned factories, space centers, and military bases into space-related manufacturing facilities and space complexes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural American Vitalization in Extraterrestrial Space Reporting Act of 2025 or the RAVES Reporting Act of 2025 .\n#### 2. Study and guidance on conversion of rural, abandoned factories into space-related manufacturing facilities\n##### (a) Study\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense, acting through the Office of Local Defense Community Cooperation, and in consultation with the Office of Space Affairs of the Department of State and the Small Business Development Center of the Small Business Administration, shall conduct a study, and publish guidance, on the conversion of abandoned factories, space centers, and military bases in rural areas into space-related manufacturing facilities and space complexes.\n##### (b) Elements\nThe study and guidance required under subsection (a) shall include information relating to the following:\n**(1)**\nOn average and by State, the cost of conversions of abandoned factories, and space centers, and abandoned military bases in rural areas into space-related manufacturing facilities and space complexes.\n**(2)**\nGreatest needs for terrestrial space manufacturing.\n**(3)**\nEnvironmental and sustainability concerns relating to such conversions.\n**(4)**\nImpact on local economies of region in which such conversions are carried out.\n**(5)**\nTechnical skills and relevant education needed for construction workers, engineers, scientists, and other elements of the workforce relating to such conversions, as well as for the operation of such facilities.\n**(6)**\nPotential for collaboration with local community colleges relating to such conversions.\n**(7)**\nEffects of artificial intelligence on workforce development relating to such conversions.\n**(8)**\nThe number of factories and military bases in rural areas abandoned as of 2025.\n**(9)**\nPotential for development within rural communities relating to such conversions.\n**(10)**\nViable sources of potential funding or incentives for private sector entities for such conversions.\n**(11)**\nPotential national security implications relating to such conversions, in particular with regard to United States adversaries and the Space Command.\n**(12)**\nAn estimate of the time required to complete such conversions.\n**(13)**\nInput from private and public entities that have collaborated or currently collaborate with the National Aeronautics and Space Administration (NASA) regarding space manufacturing.\n**(14)**\nAn analysis undertaken in consultation with outside experts in the aerospace field on the current state of the aerospace industry in rural areas of the United States, including a description of best practices relating to such conversions.\n##### (c) Submission to Congress\nThe Secretary of Defense shall submit to Congress the study and guidance required under subsection (a).\n##### (d) Definitions\nIn this section:\n**(1) Abandoned**\nThe term abandoned means out of use or underutilized for at least five years, with no apparent plans to restart production or repurpose for other uses.\n**(2) Factory**\nThe term factory means an industrial facility for manufacturing goods or parts.\n**(3) Rural area**\nThe term rural area , with respect to an abandoned factory, space center, or military base, means such a factory, center, or base, as the case may be, that is located in any area other than\u2014\n**(A)**\na city or town that has a population of greater than 50,000 inhabitants; or\n**(B)**\nany urbanized area contiguous and adjacent to a city or town described in subparagraph (A).\n**(4) Space complex**\nThe term space complex means a group of buildings designed for the purpose of building spacecraft, instruments, or technologies to study space, or testing or launching such devices.",
      "versionDate": "2025-06-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T14:38:18Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3697ih.xml"
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
      "title": "RAVES Reporting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RAVES Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural American Vitalization in Extraterrestrial Space Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Defense to conduct a study, and publish guidance, on the conversion of rural abandoned factories, space centers, and military bases into space-related manufacturing facilities and space complexes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:19Z"
    }
  ]
}
```
