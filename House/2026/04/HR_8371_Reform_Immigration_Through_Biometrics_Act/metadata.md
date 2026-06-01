# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8371
- Title: Reform Immigration Through Biometrics Act
- Congress: 119
- Bill type: HR
- Bill number: 8371
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-16T08:07:29Z
- Update date including text: 2026-05-16T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8371",
    "number": "8371",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Reform Immigration Through Biometrics Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:29Z",
    "updateDateIncludingText": "2026-05-16T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-21T19:44:47Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-20T16:00:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8371ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8371\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Donalds introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo evaluate U.S. Customs and Border Protection\u2019s implementation of an integrated biometric entry and exit data system in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reform Immigration Through Biometrics Act .\n#### 2. Evaluation of CBP\u2019s implementation of an integrated biometric entry and exit data system\n##### (a) Evaluation\n**(1) In general**\nNot later than 180 days after the date of the enactment of this section, the Secretary of Homeland Security shall submit to the Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate a report on the status of efforts to implement an integrated entry and exit data system in accordance with section 110 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1365a ; in this section referred to as the System ).\n**(2) Contents**\nThe report required under paragraph (1) shall include information relating to the following with respect to the System:\n**(A)**\nThe impact on arrival and departure wait times.\n**(B)**\nAn evaluation of audits conducted on devices procured by the private sector.\n**(C)**\nAn evaluation of prior and ongoing consultation with the private sector.\n**(D)**\nMilestones and metrics of success that have occurred already, and whether such milestones and metrics should be updated to successfully carry out the congressional directive to establish the System.\n**(E)**\nRisks and mitigation strategies to address such risks.\n**(F)**\nThe effects of the System on the following:\n**(i)**\nLegitimate travel and trade.\n**(ii)**\nCombating terrorism.\n**(iii)**\nIdentifying visa holders who violate the terms of their visas.\n**(3) Requirement**\nThe Secretary of Homeland Security shall ensure that the collection of biometric data under the System shall cause the least possible disruption to the movement of people or cargo in air, sea, or land transportation while fulfilling the goals of improving counterterrorism efforts and identifying visa holders who violate the terms of their visas.\n##### (b) Data matching assessment\n**(1) in general**\nNot later than 180 days after the date of the enactment of this section, the Secretary of Homeland Security shall submit to the Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate a report on how the System is currently matching biometric information for an individual, regardless of nationality, citizenship, or immigration status, who is departing the United States against biometric data previously provided to the United States Government by such individual for the purposes of international travel.\n**(2) Prohibition**\nThe report required under paragraph (1) shall not include any information relating to citizens of the United States, except to describe the privacy protections for such citizens with regard to facial recognition.\n##### (c) Further evaluations\nNot later than 180 days after the date of the enactment of this section, the Secretary of Homeland Security shall submit to the Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate a report on whether the sharing of biographic data provided to the Department of Homeland Security by the Canadian Border Services Agency pursuant to the 2011 Beyond the Border agreement has occurred, and the impacts of such data sharing agreement.\n##### (d) Other biometric initiatives\nNothing in this section may be construed as limiting the authority of the Secretary of Homeland Security to collect biometric information in circumstances other than as specified in this section.\n##### (e) Savings clause\nNothing in this section may prohibit the collection of user fees permitted by section 13031 of the Consolidated Omnibus Budget Reconciliation Act of 1985 ( 19 U.S.C. 58c ).",
      "versionDate": "2026-04-20",
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
        "name": "Immigration",
        "updateDate": "2026-04-28T15:40:46Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8371ih.xml"
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
      "title": "Reform Immigration Through Biometrics Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reform Immigration Through Biometrics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To evaluate U.S. Customs and Border Protection's implementation of an integrated biometric entry and exit data system in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:29Z"
    }
  ]
}
```
