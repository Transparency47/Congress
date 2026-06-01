# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/818?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/818
- Title: Abandoned Well Remediation Research and Development Act
- Congress: 119
- Bill type: S
- Bill number: 818
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/818",
    "number": "818",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Lujan, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Abandoned Well Remediation Research and Development Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-03T21:22:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s818is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 818\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Luj\u00e1n (for himself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to require the Secretary of Energy to establish an abandoned wells research, development, and demonstration program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Abandoned Well Remediation Research and Development Act .\n#### 2. Abandoned well remediation research and development\n##### (a) In general\nTitle VI of division D of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 1080) is amended by adding at the end the following:\n40602. Abandoned wells research, development, and demonstration program (a) Definition of abandoned well In this section, the term abandoned well means a well originally drilled in connection with oil and gas operations that\u2014 (1) is not being used; (2) has not been plugged; and (3) has no anticipated use in oil and gas operations. (b) Establishment Not later than 120 days after the date of enactment of the Abandoned Well Remediation Research and Development Act , the Secretary, in coordination with relevant Federal and State agencies and entities, shall establish a research, development, and demonstration program to improve\u2014 (1) data collection on the location of abandoned wells; (2) the plugging, remediation, reclamation, and repurposing of abandoned wells; and (3) strategies to mitigate potential environmental impacts of documented and undocumented abandoned wells. (c) Activities Research, development, and demonstration activities carried out under the program established under subsection (b) shall include activities to improve\u2014 (1) remote sensor capabilities, light detection and ranging (referred to in this section as LiDAR ) capabilities, optical gas imaging, magnetic survey technology, and any other technologies relevant to the efficient identification of abandoned wells; (2) understanding of how certain parameters of abandoned wells affect methane emission rates of the wells, including parameters such as well age, well depth, geology, construction, case material, and geographic region; (3) the efficiency and cost-efficacy of processes for plugging, remediating, reclaiming, and repurposing abandoned wells, including\u2014 (A) improvement of processes and technologies for the unique challenges associated with plugging remote abandoned wells; (B) use of low carbon, lightweight cement or use of alternative materials and additives for plugging purposes; and (C) repurposing of abandoned wells for alternative uses, including geothermal power production or carbon capture, utilization, and storage; and (4) understanding of the impacts of abandoned wells on groundwater quality and contamination. (d) Coordination In carrying out the program established under subsection (b), the Secretary shall ensure coordination of activities carried out under the program with\u2014 (1) institutions of higher education; (2) the National Laboratories; and (3) the private sector. (e) Authorization of appropriations There are authorized to be appropriated to carry out this section\u2014 (1) $30,000,000 for fiscal year 2026; (2) $31,250,000 for fiscal year 2027; (3) $32,500,000 for fiscal year 2028; (4) $33,750,000 for fiscal year 2029; and (5) $35,000,000 for fiscal year 2030. .\n##### (b) Clerical amendment\nThe table of contents for the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 437) is amended by inserting after the item relating to section 40601 the following:\nSec. 40602. Abandoned wells research, development, and demonstration program. .",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-03-28T11:27:38Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s818is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Abandoned Well Remediation Research and Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Abandoned Well Remediation Research and Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Infrastructure Investment and Jobs Act to require the Secretary of Energy to establish an abandoned wells research, development, and demonstration program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:30Z"
    }
  ]
}
```
