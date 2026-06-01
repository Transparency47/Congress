# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1619?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1619
- Title: Post-Disaster Assistance Online Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 1619
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-12-05T06:26:04Z
- Update date including text: 2025-12-05T06:26:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1619",
    "number": "1619",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Post-Disaster Assistance Online Accountability Act",
    "type": "S",
    "updateDate": "2025-12-05T06:26:04Z",
    "updateDateIncludingText": "2025-12-05T06:26:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T17:17:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1619is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1619\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Lankford (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide for an online repository for certain reporting requirements for recipients of Federal disaster assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Post-Disaster Assistance Online Accountability Act .\n#### 2. Subpage for transparency of disaster assistance\n##### (a) Establishment of repository for reporting requirements\nThe Director of the Office of Management and Budget, in consultation with the Secretary of the Treasury and the head of each covered Federal agency, shall establish a subpage within the website established under section 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) to publish the information required to be made available to the public under this section.\n##### (b) Submission of information by Federal agencies\nNot later than 30 days after the end of a calendar quarter, the head of each covered Federal agency that made disaster assistance available to an eligible recipient during such quarter shall, in coordination with the Director of the Office of Management and Budget, make available to the public on the subpage established under subsection (a) the information described in subsection (c), and ensure that any data asset of the covered Federal agency is machine readable.\n##### (c) Information required\nThe information described in this subsection is, with respect to disaster assistance provided by a covered Federal agency\u2014\n**(1)**\nthe total amount of disaster assistance provided by the covered Federal agency during such quarter;\n**(2)**\nthe amount of disaster assistance provided by the covered Federal agency that was expended or obligated to projects or activities; and\n**(3)**\na detailed list of all projects or activities for which disaster assistance dispersed by the agency was expended, obligated, or used, including\u2014\n**(A)**\nthe name of the project or activity;\n**(B)**\na description of the project or activity;\n**(C)**\nan evaluation of the completion status of the project or activity;\n**(D)**\nany award identification number assigned to the project;\n**(E)**\nthe Catalog for Disaster Assistance number assigned by the Federal Emergency Management Agency;\n**(F)**\nthe location of the project, including ZIP Codes; and\n**(G)**\nany reporting requirement information being collected by a covered Federal agency with respect to that covered Federal agency\u2019s disaster assistance.\n##### (d) Guidance\nThe head of each covered Federal agency, in coordination with the Director of the Office of Management and Budget and the Secretary of the Treasury, shall issue such guidance as is necessary to meet the requirements of this Act.\n##### (e) Agreement with private entity\nThe Director of the Office of Management and Budget, if necessary for purposes of transparency, may enter into an agreement with a private entity, including a nonprofit organization, to develop the subpage required under this section.\n#### 3. Definitions\nIn this Act, the following definitions apply:\n**(1) Covered Federal agency**\nThe term covered Federal agency means\u2014\n**(A)**\nany agency providing assistance under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. );\n**(B)**\nthe Small Business Administration; and\n**(C)**\nthe Department of Housing and Urban Development.\n**(2) Disaster assistance**\nThe term disaster assistance means any funds that are made available by the Federal Government in response to a specified natural disaster, including\u2014\n**(A)**\nany assistance provided by the Administrator of the Small Business Administration as a result of a disaster declared under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) );\n**(B)**\nany assistance provided by the Secretary of Housing and Urban Development for activities authorized under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ) related to disaster relief, long-term recovery, restoration of infrastructure and housing, and economic revitalization in the most impacted and distressed areas resulting from a major disaster declared pursuant to the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. );\n**(C)**\nflood insurance coverage provided under the National Flood Insurance Program pursuant to the National Flood Insurance Act of 1968 ( 42 U.S.C. 4001 et seq. ); and\n**(D)**\nany assistance provided under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n**(3) Eligible recipient**\nThe term eligible recipient \u2014\n**(A)**\nmeans any entity that receives disaster assistance directly from the Federal Government (including disaster assistance received through a grant, loan, or contract), other than an individual; and\n**(B)**\nincludes a State that receives disaster assistance.\n**(4) Specified natural disaster**\nThe term specified natural disaster means\u2014\n**(A)**\na fire on public or private forest land or grassland described in section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 );\n**(B)**\na major disaster declared by the President under section 401 of such Act ( 42 U.S.C. 5170 );\n**(C)**\nan emergency declared by the President under section 501 of such Act ( 42 U.S.C. 5191 ); and\n**(D)**\nany other natural disaster for which a disaster declaration is made by the Federal Government.",
      "versionDate": "2025-05-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-15",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "153",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Post-Disaster Assistance Online Accountability Act",
      "type": "HR"
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
        "updateDate": "2025-06-09T14:50:21Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1619is.xml"
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
      "title": "Post-Disaster Assistance Online Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Post-Disaster Assistance Online Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for an online repository for certain reporting requirements for recipients of Federal disaster assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:26Z"
    }
  ]
}
```
