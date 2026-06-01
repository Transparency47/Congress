# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8245
- Title: GRACIE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8245
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-23T08:07:05Z
- Update date including text: 2026-04-23T08:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8245",
    "number": "8245",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "GRACIE Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:05Z",
    "updateDateIncludingText": "2026-04-23T08:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:33:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "UT"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "UT"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8245ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8245\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mrs. Wagner (for herself, Ms. Stefanik , Mr. Moskowitz , Mr. Moore of Utah , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo support State efforts to record all child welfare interviews.\n#### 1. Short title\nThis Act may be cited as the Generate Recordings of All Child protective Interviews Everywhere Act or the GRACIE Act of 2026 .\n#### 2. Child protective service interview recording grants\n##### (a) Grants\nThe Associate Commissioner may award grants to States for the purpose of assisting State agencies responsible for conducting child welfare interviews in recording and retaining all child welfare interviews conducted by such State agencies.\n##### (b) Application\nA State seeking a grant under this section shall submit an application to the Associate Commissioner at such time and in such manner as the Associate Commissioner may require. Such application shall include\u2014\n**(1)**\nthe State\u2019s lead agency for the grant program and that agency\u2019s current requirements involving the recording and retention of child welfare interviews;\n**(2)**\nthe challenges the State faces in developing, implementing, and monitoring requirements involving the recording and retention of child welfare interviews; and\n**(3)**\na description of how the State plans to use funds for activities described in subsection (c).\n##### (c) Use of funds\n**(1) In general**\nAmounts received under a grant under this section shall be used exclusively for costs directly associated with conducting and retaining for 5 years the recording of all child welfare interviews by a State agency responsible for conducting child welfare interviews, including initial interviews conducted during a family assessment to the extent practicable.\n**(2) Recording requirement**\nA State receiving a grant under this section shall have a statute, ordinance, policy, or practice requiring all child welfare interviews conducted by the State agency responsible for conducting child welfare interviews to be recorded through electronic audio recording, body camera video, or any other reasonable means of recording.\n**(3) Retention requirement**\nA State receiving a grant under this section shall have a statute, ordinance, policy, or practice requiring the recordings described in paragraph (2) to be retained and stored for not less than 5 years in a manner consistent with the protocols established by the State for such recordings, which shall include that\u2014\n**(A)**\na copy of such recording\u2014\n**(i)**\nsubject to clause (ii), may only be released to appropriate government agencies investigating an allegation or prosecuting an offense relating to an allegation; and\n**(ii)**\nupon request by a caregiver or guardian in connection with a judicial proceeding, shall be made available to the caregiver or guardian, unless the court orders otherwise;\n**(B)**\na penalty is imposed for a violation of the limitation described in subparagraph (A); and\n**(C)**\nthe retention systems of the State agency responsible for conducting child welfare interviews securely manage the storage and distribution of such a recording with access controls and role-based permission management.\n##### (d) Accountability\n**(1) Records**\nA State that receives a grant under this section shall maintain such records as the Associate Commissioner may require to facilitate an effective audit relating to the receipt of the grant, the use of amounts from the grant, or outsourcing activities.\n**(2) Access**\nFor the purpose of conducting audits and examinations, the Associate Commissioner shall have access to any book, document, or record of the State agency that receives a grant under this section if the Associate Commissioner determines that the book, document, or record relates to\u2014\n**(A)**\nthe receipt of the grant; or\n**(B)**\nthe use of amounts from the grant.\n##### (e) Definitions\nIn this section:\n**(1) Associate Commissioner**\nThe term Associate Commissioner means the Associate Commissioner of the Children\u2019s Bureau of the Office of the Administration for Children and Families of the Department of Health and Human Services.\n**(2) Child welfare interview**\nThe term child welfare interview means a documented interview with any relevant parties, including a child or an adult, conducted by a State agency responsible for conducting child welfare interviews in order to elicit information regarding concerns of abuse of a child, neglect of a child, or other crimes against a child.\n**(3) State**\nThe term State means\u2014\n**(A)**\neach of the several States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico; and\n**(D)**\nany territory or possession of the United States.\n##### (f) Funding and sunset\nFor each of fiscal years 2026 through 2031, the Associate Commissioner shall use not more than $30,000,000 of the amounts appropriated to carry out subpart 1 of part B of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. ) to carry out this section.",
      "versionDate": "2026-04-09",
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
        "name": "Families",
        "updateDate": "2026-04-14T19:58:56Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8245ih.xml"
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
      "title": "GRACIE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRACIE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Generate Recordings of All Child protective Interviews Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To support State efforts to record all child welfare interviews.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T08:18:42Z"
    }
  ]
}
```
