# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1205
- Title: Safe Shelters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1205
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-05-02T14:53:37Z
- Update date including text: 2025-05-02T14:53:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1205",
    "number": "1205",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Safe Shelters Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-02T14:53:37Z",
    "updateDateIncludingText": "2025-05-02T14:53:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:16:32Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-11T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "CO"
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
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NJ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1205ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1205\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Ms. Mace (for herself, Ms. Boebert , Mr. Weber of Texas , Mr. Van Drew , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit certain sex offenders from entering or using the services of certain emergency shelters, to authorize the Administrator of the Federal Emergency Management Agency to designate emergency shelters for such sex offenders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Shelters Act of 2025 .\n#### 2. Emergency shelters for sex offenders\n##### (a) Prohibition on use of undesignated shelters\n**(1) In general**\nExcept for the purpose of seeking information on designated shelters, a covered sex offender may not enter or use the services of an undesignated shelter.\n**(2) Notification**\nA covered sex offender who enters an undesignated shelter shall, immediately upon entering such shelter, notify any individual operating such shelter that such offender is required to register on the National Sex Offender Registry.\n**(3) Provision of information**\nUpon receiving a notification from a covered sex offender under paragraph (2), the individual so notified shall inform such offender of\u2014\n**(A)**\nany designated shelter; and\n**(B)**\nthe prohibition in paragraph (1).\n**(4) Penalty**\nWhoever, in or affecting interstate commerce, being a covered sex offender, knowingly fails to comply with paragraph (1) or (2) shall be fined under title 18, United States Code, imprisoned not more than 5 years, or both.\n**(5) Effective date**\nThis subsection shall take effect 180 days after the date of enactment of this Act.\n##### (b) Designated shelters for sex offenders\n**(1) In general**\nThe Administrator of the Federal Emergency Management Agency may, as necessary, designate a Federal building or Federal prison from the lists created pursuant to paragraph (2) as a designated shelter for the duration, as determined by the Administrator, of a disaster described in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(2) Lists of buildings and prisons**\nNot later than 180 days after the date of enactment of this Act and on an ongoing basis thereafter, the Administrator of the General Services Administration and Director of the Bureau of Prisons shall each make available to the Administrator of the Federal Emergency Management Agency a list of available Federal buildings or Federal prisons, as appropriate, that the Administrator of the Federal Emergency Management Agency may designate pursuant to paragraph (1).\n**(3) Distribution of information**\nThe Administrator of the Federal Emergency Management Agency shall make available to each individual operating an undesignated shelter information on each designated shelter.\n##### (c) Definitions\nIn this section:\n**(1) Covered sex offender**\nThe term covered sex offender means a sex offender who is required to register on the National Sex Offender Registry under section 113 of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20913 ).\n**(2) Designated shelter**\nThe term designated shelter means an emergency shelter that is designated for use under this section by covered sex offenders only.\n**(3) Emergency shelter**\nThe term emergency shelter means a shelter run by the Federal Emergency Management Agency or a State or local government in response to a disaster described in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(4) National Sex Offender Registry**\nThe term National Sex Offender Registry means the national database established under section 119 of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20921 ).\n**(5) Sex offender**\nThe term sex offender has the meaning given such term in section 111 of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20911 ).\n**(6) Undesignated shelter**\nThe term undesignated shelter means an emergency shelter other than a designated shelter.",
      "versionDate": "2025-02-11",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-05-02T14:53:25Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-05-02T14:53:31Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-02T14:53:37Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2025-05-02T14:53:13Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-05-02T14:53:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-12T18:26:01Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1205ih.xml"
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
      "title": "Safe Shelters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Shelters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit certain sex offenders from entering or using the services of certain emergency shelters, to authorize the Administrator of the Federal Emergency Management Agency to designate emergency shelters for such sex offenders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T04:18:48Z"
    }
  ]
}
```
