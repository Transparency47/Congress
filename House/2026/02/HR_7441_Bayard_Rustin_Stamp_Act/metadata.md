# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7441
- Title: Bayard Rustin Stamp Act
- Congress: 119
- Bill type: HR
- Bill number: 7441
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-14T08:07:57Z
- Update date including text: 2026-05-14T08:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E114-115)
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E114-115)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7441",
    "number": "7441",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Bayard Rustin Stamp Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:57Z",
    "updateDateIncludingText": "2026-05-14T08:07:57Z"
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E114-115)",
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
          "date": "2026-02-09T17:00:25Z",
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NJ"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7441ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7441\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Ms. Norton (for herself and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the Postmaster General to issue a forever stamp depicting Bayard Rustin, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bayard Rustin Stamp Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nBayard Rustin was born on March 17, 1912, and was raised by his grandparents in West Chester, Pennsylvania. From a young age, Rustin learned to prioritize the values of nonviolence and peacekeeping from his grandparents\u2019 Quaker faith, and would continue to build these values in his life as a civil rights movement leader.\n**(2)**\nRustin attended City College of New York, where he joined a progressive club that aimed to remedy racial issues during turbulent times. His time with the club was short lived, but it inspired him to join the Fellowship of Reconciliation, an organization that became a champion for labor rights, equality, and world peace.\n**(3)**\nHis time with the Fellowship of Reconciliation prompted Rustin to become a leader in the 1947 Journey to Reconciliation , an event where White and Black people across the South rode buses together to challenge segregation laws, a precursor to the Freedom Rides.\n**(4)**\nRustin was an advisor in Martin Luther King, Jr.\u2019s inner circle as he advocated pacifism and nonviolence for achieving equal treatment for African-Americans.\n**(5)**\nRustin used his brilliant strategic handling of the use of aggressive, peaceful action in the civil rights movement and throughout his life as an activist.\n**(6)**\nHis most important role was as the chief organizer of the March on Washington for Jobs and Freedom in 1963, the largest demonstration ever organized at the time, in which a quarter of a million people turned out to demand civil rights for African-Americans.\n**(7)**\nIn the years after the civil rights movement, Rustin used his background as a gay man to inspire others to advocate for and to achieve LGBTQ+ rights.\n**(8)**\nRustin remained a strategist and public speaker for workers\u2019 rights movements, including co-founding the A. Philip Randolph Institute for Black trade union members.\n**(9)**\nRustin committed to promoting social good and advocating for the disenfranchised until his death in 1987.\n#### 3. Bayard Rustin stamp\n##### (a) In general\nIn order to honor the life and work of Bayard Rustin, a leader in the civil rights movement, the Postmaster General shall provide for the issuance of a forever stamp suitable for that purpose that depicts Bayard Rustin.\n##### (b) Definition of definitive stamp\nFor the purposes of this Act, the term forever stamp means a definitive stamp that\u2014\n**(1)**\nmeets the postage required for first-class mail up to one ounce in weight; and\n**(2)**\nretains full validity for that purpose even if the rate of that postage is later increased.\n##### (c) Effective date\nThe stamp described in subsection (a) shall be issued as soon as practicable after the date of the enactment of this Act.",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-18T16:01:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7441ih.xml"
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
      "title": "Bayard Rustin Stamp Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bayard Rustin Stamp Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Postmaster General to issue a forever stamp depicting Bayard Rustin, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T04:18:24Z"
    }
  ]
}
```
