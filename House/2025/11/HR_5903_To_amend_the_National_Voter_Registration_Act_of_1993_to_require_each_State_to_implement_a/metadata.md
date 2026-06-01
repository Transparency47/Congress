# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5903
- Title: PROVE Act
- Congress: 119
- Bill type: HR
- Bill number: 5903
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-05-12T08:05:42Z
- Update date including text: 2026-05-12T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5903",
    "number": "5903",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "PROVE Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:42Z",
    "updateDateIncludingText": "2026-05-12T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "DC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "OR"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NY"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "GA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5903ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5903\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Beyer introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the National Voter Registration Act of 1993 to require each State to implement a process under which individuals who are 16 years of age may apply to register to vote in elections for Federal office in the State, to direct the Election Assistance Commission to make grants to States to increase the involvement of minors in public election activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pre-Registration Of Voters Everywhere Act or the PROVE Act .\n#### 2. Pre-registration of minors for voting in Federal elections\n##### (a) Requiring Implementation of Process\nThe National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ) is amended by inserting after section 8 the following new section:\n8A. Pre-registration process for minors (a) Requiring Implementation of Pre-Registration Process Each State shall implement a process under which\u2014 (1) an individual who is a resident of the State may apply to register to vote in elections for Federal office in the State at any time after the individual turns 16 years of age; and (2) if the individual is not 18 years of age or older at the time the individual applies under paragraph (1) but would be eligible to vote in such elections if the individual were 18 years of age, the State shall ensure that the individual is registered to vote in elections for Federal office in the State that are held on or after the date on which the individual turns 18 years of age. (b) Permitting Availability of Process for Younger Individuals A State may, at its option, make the process implemented under subsection (a) available to individuals who are younger than 16 years of age. .\n##### (b) Effective Date\nThe amendment made by subsection (a) shall take effect upon the expiration of the 90-day period that begins on the date of the enactment of this Act.\n#### 3. Grants to States for activities to encourage involvement of minors in election activities\n##### (a) Grants\n**(1) In general**\nThe Election Assistance Commission (hereafter in this section referred to as the Commission ) shall make grants to eligible States to enable such States to carry out a plan to increase the involvement of individuals under 18 years of age in public election activities in the State.\n**(2) Contents of plans**\nA State\u2019s plan under this subsection shall include\u2014\n**(A)**\nmethods to promote the use of the pre-registration process implemented under section 8A of the National Voter Registration Act of 1993 (as added by section 2(a));\n**(B)**\nmodifications to the curriculum of secondary schools in the State to promote civic engagement; and\n**(C)**\nsuch other activities to encourage the involvement of young people in the electoral process as the State considers appropriate.\n##### (b) Eligibility\nA State is eligible to receive a grant under this section if the State submits to the Commission, at such time and in such form as the Commission may require, an application containing\u2014\n**(1)**\na description of the State\u2019s plan under subsection (a);\n**(2)**\na description of the performance measures and targets the State will use to determine its success in carrying out the plan; and\n**(3)**\nsuch other information and assurances as the Commission may require.\n##### (c) Period of Grant; Report\n**(1) Period of grant**\nA State receiving a grant under this section shall use the funds provided by the grant over a 2-year period agreed to between the State and the Commission.\n**(2) Report**\nNot later than 6 months after the end of the 2-year period agreed to under paragraph (1), the State shall submit to the Commission a report on the activities the State carried out with the funds provided by the grant, and shall include in the report an analysis of the extent to which the State met the performance measures and targets included in its application under subsection (b)(2).\n##### (d) State Defined\nIn this section, the term State means each of the several States and the District of Columbia.\n##### (e) Authorization of Appropriations\nThere are authorized to be appropriated for grants under this section $25,000,000, to remain available until expended.",
      "versionDate": "2025-11-04",
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
        "updateDate": "2025-12-08T22:02:44Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5903ih.xml"
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
      "title": "PROVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pre-Registration Of Voters Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Voter Registration Act of 1993 to require each State to implement a process under which individuals who are 16 years of age may apply to register to vote in elections for Federal office in the State, to direct the Election Assistance Commission to make grants to States to increase the involvement of minors in public election activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T10:33:23Z"
    }
  ]
}
```
