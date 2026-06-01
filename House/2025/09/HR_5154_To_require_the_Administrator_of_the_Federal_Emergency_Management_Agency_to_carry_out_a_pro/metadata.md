# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5154
- Title: REACT Act
- Congress: 119
- Bill type: HR
- Bill number: 5154
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-10-07T08:05:44Z
- Update date including text: 2025-10-07T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-05 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-05 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5154",
    "number": "5154",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "REACT Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:44Z",
    "updateDateIncludingText": "2025-10-07T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-05",
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
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-05T21:39:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5154ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5154\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Mullin (for himself, Ms. Pelosi , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Administrator of the Federal Emergency Management Agency to carry out a program to provide technical and financial assistance to State, local, and Tribal authorities to conduct testing of emergency alert and warning systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Resilient Emergency Alert Communications and Training Act or the REACT Act .\n#### 2. Support for emergency alerting systems\n##### (a) In general\nThe Administrator of the Federal Emergency Management Agency shall carry out a program to provide technical and financial assistance to State, local, and Tribal authorities to conduct periodic field training, end-to-end testing, and community-based exercises of emergency alert and warning systems, which shall be in addition to support provided under any existing program.\n##### (b) Requirements\nThe technical and financial assistance provided under subsection (a) shall include\u2014\n**(1)**\nfunding and training for community-based exercises, including organized live testing at the local level;\n**(2)**\nassistance with establishing a clear delineation of roles, responsibilities, and standard operating procedures within the emergency alert and warning chain of authorization, including across local, Tribal, State, and Federal authorities;\n**(3)**\ndeveloping and publishing templates for emergency alert and warning messages, in accordance with evidence-based scientific research, that\u2014\n**(A)**\nmay include message completeness requirements; and\n**(B)**\nbuild upon existing training materials;\n**(4)**\ntraining on best practices for crafting, disseminating, and assessing the effectiveness of emergency alert and warning messages, provided across different platforms and jurisdictions;\n**(5)**\ndevelopment of standardized metrics to assess the effectiveness of emergency alert and warning systems;\n**(6)**\ntesting of technology and infrastructure for emergency alert and warning systems, including multimodal capabilities, to ensure such systems are working effectively and in coordination with one another;\n**(7)**\ntechnical assistance for the development of public education campaigns that explain how emergency alert and warning systems work, actions by individuals required to ensure they receive alerts and warnings, and how individuals and communities should respond; and\n**(8)**\nreview of, and recommendations for, local policy and standard operating procedures regarding the use of emergency alert and warning systems.\n##### (c) Operational plan\nNot later than 1 year after the date of enactment of this Act, the Administrator, in consultation with State, local, and Tribal authorities, shall develop and submit to Congress a plan for carrying out the program under this section. Such plan shall contain anticipated costs and metrics to assess the effectiveness of such training, testing, and exercises.\n##### (d) Report\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Administrator shall submit to Congress a report on the field training, end-to-end testing, community-based exercises, and public education supported under this section and such report shall contain\u2014\n**(1)**\nfor each Alerting Authority under the Integrated Public Alert and Warning System and for each State, local, or Tribal authority receiving assistance under this section that is not an established Alerting Authority\u2014\n**(A)**\nwhether the authority has conducted field training, end-to-end testing, community-based exercises, and public education relating to the emergency alert and warning systems of such authority;\n**(B)**\nthe frequency and scope of the activities described in subparagraph (A);\n**(C)**\nwhether the authority has established sufficient standard operating procedures regarding the use of its emergency alert and warning systems;\n**(D)**\na description of the percentage of individuals or regions covered by its emergency alert and warning systems;\n**(E)**\na description of the methods used to obtain public participation and feedback, and their results, during and after such activities; and\n**(F)**\na description of opt-out rates for emergency alert and warning systems during and after such activities;\n**(2)**\nan assessment of the effectiveness of such field training, end-to-end testing, and community-based exercises as measured by the metrics contained in the plan required under subsection (c); and\n**(3)**\nany recommendations for updating such plan.\n##### (e) Sunset\nThe authority provided under this section shall terminate on the date that is 10 years after the date of enactment of this Act.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section $30,000,000 for each of fiscal years 2025 through 2035.\n##### (g) Rule of construction\nNothing in this section may be construed to require State, local and Tribal authorities to be mandated to use any particular emergency alert and warning system.\n##### (h) Emergency alert and warning system defined\nIn this section, the term emergency alert and warning system means any system used by a State, local, or Tribal authority to warn the public about emergencies or natural hazards, including such systems that operate through the Integrated Public Alert and Warning System.",
      "versionDate": "2025-09-04",
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
        "updateDate": "2025-09-17T20:08:16Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5154ih.xml"
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
      "title": "REACT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REACT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Resilient Emergency Alert Communications and Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Federal Emergency Management Agency to carry out a program to provide technical and financial assistance to State, local, and Tribal authorities to conduct testing of emergency alert and warning systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:21Z"
    }
  ]
}
```
