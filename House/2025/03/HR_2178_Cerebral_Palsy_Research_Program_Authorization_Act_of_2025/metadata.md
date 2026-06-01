# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2178
- Title: Cerebral Palsy Research Program Authorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2178
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-04-24T08:07:14Z
- Update date including text: 2026-04-24T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2178",
    "number": "2178",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Cerebral Palsy Research Program Authorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:14Z",
    "updateDateIncludingText": "2026-04-24T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:05:30Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MO"
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
      "sponsorshipDate": "2025-03-18",
      "state": "DC"
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
      "sponsorshipDate": "2025-03-21",
      "state": "GA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NJ"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "AL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2178ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2178\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Cohen (for himself, Mr. Fitzpatrick , Mr. Cleaver , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to carry out a program of research related to cerebral palsy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cerebral Palsy Research Program Authorization Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCerebral palsy is the most common lifelong motor impairment in children, affecting more than 1,000,000 Americans, 1 in 345 children, and over 17,000,000 people worldwide.\n**(2)**\nIn the United States, more than 10,000 babies are diagnosed with cerebral palsy each year.\n**(3)**\nCerebral palsy is a broad group of disorders disrupting a person\u2019s ability to move, sit, stand, walk, talk, and use their hands.\n**(4)**\nIn more than 80 percent of cases, the cause of cerebral palsy is unknown.\n**(5)**\nSeventy-five percent of individuals with cerebral palsy also have 1 or more additional developmental disabilities including epilepsy, intellectual disabilities, communication problems, learning and attention disorders, chronic pain, autism, hearing disorders, and visual impairments or blindness.\n**(6)**\nChildren with cerebral palsy are more likely to die from the flu and related viruses, including COVID\u201319, than children without neurologic disorders.\n**(7)**\nThere is no consensus of best practices for a person with cerebral palsy at the time of diagnosis or through the lifespan.\n**(8)**\nIt is estimated that the lifetime care and medical costs for all people with cerebral palsy who were born in 2000 alone will total more than $13,500,000,000. The loss of productivity and lost wages of the individual with cerebral palsy and their family members is more than $35,000,000,000.\n**(9)**\nAlthough there is not yet a known cure for many types of cerebral palsy, we know that treatment breakthroughs and the prevention of many types of cerebral palsy is possible.\n#### 3. Cerebral palsy research\nTitle III of the Public Health Service Act is amended by inserting after section 317C of such Act ( 42 U.S.C. 247b\u20134 ) the following new section:\n317C\u20131. Cerebral palsy research (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, and in consultation with other Federal agencies and partners, shall carry out (directly or through grants or contracts) a program of research related to cerebral palsy, including\u2014 (1) research on\u2014 (A) the most promising avenues of cerebral palsy diagnosis and treatment; (B) factors that may mitigate the prevalence of cerebral palsy; and (C) the health care and societal costs of cerebral palsy; (2) public health surveillance; and (3) other research that the Director of the Centers for Disease Control and Prevention determines to be appropriate to provide education and training for health professionals and the general public for purposes of diagnosing, treating, and explaining the causes, prevalence, and lifelong effects of cerebral palsy. (b) Technical assistance The Secretary may (directly or through grants or contracts) provide technical assistance to public and nonprofit private entities in furtherance of research under this section. (c) Evaluations The Secretary shall (directly or through grants or contracts) provide for the evaluation of activities under subsection (a) in order to determine the extent to which such activities have been effective, including evaluation of the effects of such activities on various demographic populations. (d) Authorization of appropriations To carry out this section, there is authorized to be appropriated $5,000,000 for each of fiscal years 2026 through 2031. .",
      "versionDate": "2025-03-18",
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
        "name": "Health",
        "updateDate": "2025-03-31T16:26:37Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2178ih.xml"
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
      "title": "Cerebral Palsy Research Program Authorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cerebral Palsy Research Program Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to carry out a program of research related to cerebral palsy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:48:38Z"
    }
  ]
}
```
