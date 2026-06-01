# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4408?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4408
- Title: UNITY Act
- Congress: 119
- Bill type: HR
- Bill number: 4408
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-09-11T08:06:34Z
- Update date including text: 2025-09-11T08:06:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4408",
    "number": "4408",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "UNITY Act",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:34Z",
    "updateDateIncludingText": "2025-09-11T08:06:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-16T17:01:53Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4408ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4408\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. King-Hinds introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo study the effectiveness of disaster response and recovery in noncontiguous communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Understanding Noncontiguous Infrastructure and Threats Year-round Act or the UNITY Act .\n#### 2. Improving disaster workforce retention in noncontiguous communities\n##### (a) In general\nThe Administrator of the Federal Emergency Management Agency shall conduct a study on the effectiveness of practices of the Agency relating to hiring, recruitment, and retention in noncontiguous communities by soliciting feedback from staff in such communities.\n##### (b) Contents\nIn conducting the study under subsection (a), the Administrator shall\u2014\n**(1)**\nevaluate the recruitment strategies of the Agency and efforts of the Agency to broaden the pool of qualified local candidates;\n**(2)**\nprioritize input from communities in which there are the most severe staffing shortages; and\n**(3)**\nidentify specific steps that the Agency can take to improve opportunities for staff in noncontiguous communities.\n##### (c) Briefing\nNot later than 6 months after the date of enactment of this Act, the Administrator shall brief the Committee on Transportation and Infrastructure and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate on the results of the study conducted under subsection (a).\n##### (d) Policies\nThe Administrator shall take such actions as are necessary to revise any policies, guidance, or regulations of the Agency to address the disaster workforce challenges in noncontiguous communities identified in the study conducted under subsection (a).\n#### 3. GAO review of disaster response and recovery in noncontiguous communities\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study on the effectiveness of disaster response and recovery practices in noncontiguous communities, with a particular focus on recovery efforts relating to damage caused by Super Typhoon Yutu, and compare such practices with the disaster response and recovery practices in contiguous communities.\n##### (b) Contents\nIn conducting the study under subsection (a), the Comptroller General shall\u2014\n**(1)**\nanalyze ongoing recovery efforts from disasters that have impacted noncontiguous communities;\n**(2)**\nanalyze the level of coordination between the Federal Departments and Agencies tasked with disaster response and recovery;\n**(3)**\nassess how effectively Federal agencies coordinate with State emergency management offices;\n**(4)**\nassess the effectiveness of the Area offices and Regional Advisory Councils of the Agency in assisting noncontiguous communities; and\n**(5)**\nmake recommendations on how to improve the disaster response and recovery outcomes in noncontiguous communities.\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Transportation and Infrastructure and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the study conducted under subsection (a).\n#### 4. Preliminary damage assessment pilot program\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall establish a pilot program to implement new technology in carrying out a preliminary damage assessment in a noncontiguous community in which a major disaster has been declared under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ).\n##### (b) Priority\nIn carrying out the pilot program established under subsection (a), the Administrator shall ensure that the most geographically remote noncontiguous communities are prioritized.\n##### (c) Briefing\nNot later than 3 years after the date of enactment of this Act, the Administrator shall brief the Committee on Transportation and Infrastructure and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate on the implementation of the pilot program established under subsection (a).\n##### (d) Sunset\nThe pilot program established under subsection (a) shall terminate on September 30, 2030.",
      "versionDate": "2025-07-15",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-30T22:08:14Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4408ih.xml"
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
      "title": "UNITY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UNITY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Understanding Noncontiguous Infrastructure and Threats Year-round Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study the effectiveness of disaster response and recovery in noncontiguous communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:28Z"
    }
  ]
}
```
