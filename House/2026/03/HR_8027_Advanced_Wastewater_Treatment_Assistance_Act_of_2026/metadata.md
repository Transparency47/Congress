# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8027
- Title: Advanced Wastewater Treatment Assistance Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8027
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-21T08:08:05Z
- Update date including text: 2026-05-21T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8027",
    "number": "8027",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Advanced Wastewater Treatment Assistance Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:05Z",
    "updateDateIncludingText": "2026-05-21T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8027ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8027\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Ms. Stevens (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish a grant program for advanced wastewater treatment projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advanced Wastewater Treatment Assistance Act of 2026 .\n#### 2. Advanced wastewater treatment projects\n##### (a) In general\nThe Administrator of the Environmental Protection Agency shall establish a program to provide a grant to each State in accordance with the formula established pursuant to subsection (b) for advanced wastewater treatment projects.\n##### (b) Grant allotment\nThe Administrator shall establish a formula to determine the amount allotted to each State under this section.\n##### (c) Administrative costs\n**(1) Administrator**\nThe Administrator may use not more than 1 percent of the amounts made available to carry out this section to administer the grant program established under this section.\n**(2) State**\nEach State may use not more than 1 percent of a grant provided under this section for administrative costs.\n##### (d) Cost sharing\n**(1) In general**\nSubject to paragraph (2), the non-Federal share of the cost of an advanced wastewater treatment project carried out under this section shall be at least 50 percent.\n**(2) Disadvantaged communities**\nThe non-Federal share required under paragraph (1) shall not apply to an advanced wastewater treatment project that serves a qualified disadvantaged community.\n##### (e) Set aside\nOf the amounts made available to carry out this section, not less than 49 percent shall be used for advanced wastewater treatment projects that\u2014\n**(1)**\nserve qualified disadvantaged communities;\n**(2)**\nare operated by a rural, small, or tribal publicly owned treatment works and provide either a direct or indirect benefit to a qualified disadvantaged community; and\n**(3)**\nare operated by a public regional water provider that serves 2 or more qualified disadvantaged communities with a combined population of more than 100,000.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $1,000,000,000 for fiscal years 2026 through 2030, to remain available until expended.\n##### (g) Definitions\nIn this section:\n**(1) Advanced wastewater treatment project**\nThe term advanced wastewater treatment project means a project or activity for advanced wastewater treatment (as defined by the Administrator) that is eligible for assistance under section 603(c) of the Federal Water Pollution Control Act ( 33 U.S.C. 1383(c) ).\n**(2) Qualified disadvantaged community**\nThe term qualified disadvantaged community means a municipality or intermunicipal, interstate, or State agency described in section 603(i)(1)(A) of the Federal Water Pollution Control Act ( 33 U.S.C. 1383(i)(1)(A) ).\n**(3) State**\nThe term State has the meaning given such term in section 502(3) of the Federal Water Pollution Control Act ( 33 U.S.C. 1362 ).\n#### 3. Study on efficacy of advanced wastewater treatment technologies\n##### (a) In general\nThe Administrator of the Environmental Protection Agency, in consultation with the Director of the National Institute of Standards and Technology, shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to conduct a comprehensive study on the efficacy of advanced wastewater treatment technologies in capturing emerging contaminants, including nanomaterials and perfluoroalkyl and polyfluoroalkyl substances.\n##### (b) Reports\n**(1) Interim report**\nNot later than 3 years after the date of enactment of this Act, the National Academies shall make publicly available an interim report on the study conducted under subsection (a).\n**(2) Final report**\nNot later than 5 years after the date of enactment of this Act, the National Academies shall make publicly available a final report the study conducted under subsection (a).",
      "versionDate": "2026-03-19",
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
        "name": "Water Resources Development",
        "updateDate": "2026-04-13T21:30:26Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8027ih.xml"
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
      "title": "Advanced Wastewater Treatment Assistance Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advanced Wastewater Treatment Assistance Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program for advanced wastewater treatment projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:38Z"
    }
  ]
}
```
