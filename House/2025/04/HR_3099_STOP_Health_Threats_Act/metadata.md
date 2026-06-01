# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3099
- Title: STOP Health Threats Act
- Congress: 119
- Bill type: HR
- Bill number: 3099
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-09-27T08:06:09Z
- Update date including text: 2025-09-27T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3099",
    "number": "3099",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "STOP Health Threats Act",
    "type": "HR",
    "updateDate": "2025-09-27T08:06:09Z",
    "updateDateIncludingText": "2025-09-27T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-30T21:14:15Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3099ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3099\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Costa (for himself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Health and Human Services to make grants to local governments for the training of local law enforcement officers on public health threats arising from violations of building codes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safety Training for Officers on Public Health Threats Act or the STOP Health Threats Act .\n#### 2. Grants to train local enforcement officers on public health threats\n##### (a) In general\nThe Secretary of Health and Human Services, in consultation with the Secretary of Housing and Urban Development and the heads of other relevant agencies engaged in regulating building codes determined necessary by the Secretary of Health and Human Services, shall award grants to local governments for the training of local enforcement officers on public health threats arising from violations of building codes.\n##### (b) Use of funds\nA local government receiving a grant under this section shall use the grant to\u2014\n**(1)**\ndevelop and implement a training program for local enforcement officers on recognizing and responding to public health threats described in subsection (a);\n**(2)**\npartner with other local governments to collaborate on such training;\n**(3)**\nin carrying out paragraphs (1) and (2), coordinate with\u2014\n**(A)**\nrelevant offices and agencies of the Federal, State, and local government, such as a public health department; or\n**(B)**\nnongovernmental organizations with issue area expertise; and\n**(4)**\ncarry out any other activities deemed appropriate by the Secretary for training described in subsection (a).\n##### (c) Application\nTo seek a grant under subsection (a), a local government shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to applicants based on\u2014\n**(1)**\ntheir capacity to provide the training described in subsection (a); and\n**(2)**\nprioritizing areas where threats have been identified.\n##### (e) Definition\nIn this section, the term enforcement officers means those carrying out enforcement activities and implement relevant consensus-based codes, specifications, and standards that establish minimum acceptable criteria for the design, construction, and maintenance of residential structures and facilities.",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-21T11:08:26Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3099ih.xml"
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
      "title": "STOP Health Threats Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Health Threats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safety Training for Officers on Public Health Threats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to make grants to local governments for the training of local law enforcement officers on public health threats arising from violations of building codes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T06:18:32Z"
    }
  ]
}
```
