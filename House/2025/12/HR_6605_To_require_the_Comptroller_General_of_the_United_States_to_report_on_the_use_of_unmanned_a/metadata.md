# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6605
- Title: Secure Our Skies Drone Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6605
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-02-03T09:05:47Z
- Update date including text: 2026-02-03T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6605",
    "number": "6605",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Secure Our Skies Drone Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:47Z",
    "updateDateIncludingText": "2026-02-03T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:34:41Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
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
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6605ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6605\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Vasquez (for himself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Comptroller General of the United States to report on the use of unmanned aircraft systems and on systems developed to counter such unmanned aircraft systems by Federal, State, local, and Tribal agencies.\n#### 1. Short title\nThis Act may be cited as the Secure Our Skies Drone Safety Act of 2025 .\n#### 2. Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall complete a study, and submit to Congress a report thereon, on the use of unmanned aircraft systems (hereinafter in this Act referred to as UAS ) and on systems developed to counter such unmanned aircraft systems by Federal, State, local, and Tribal agencies. Such report shall include the following:\n**(1)**\nRecommendations for the following:\n**(A)**\nWhat, if any, legal authorities and what policies need to be changed to improve the ability of such agencies to successfully counter threats from such UAS.\n**(B)**\nWhat actions need to be taken to bolster the capabilities of the United States and its allies to manufacture UAS and to simplify the procurement process for UAS.\n**(2)**\nInformation about the following:\n**(A)**\nThe number of UAS deployed by Federal, State, local, and Tribal law enforcement agencies as of the date of the report.\n**(B)**\nFor State, local, and Tribal agencies, the number of UAS purchased from entities operating within an adversarial nation (including any countries included on the list set forth in section 791.4 of title 15 of the Code of Federal Regulations).\n**(C)**\nHow many UAS are domestically produced.\n**(D)**\nAny cost restrictions that prevent law enforcement agencies from expanding the use of UAS produced in the United States or a nation other than one referred to in subparagraph (B).\n**(E)**\nHow frequently UAS are used and for what purposes.\n**(F)**\nWhether the operators of UAS are trained or certified in any way.\n**(G)**\nWhat authorities, policies, or protocols govern the use of UAS.\n**(H)**\nWhat privacy protections or expectations are there regarding the use of UAS.\n**(I)**\nWhat countermeasures or strategies exist to counter UAS, and to what extent is there a training or certification in their use.",
      "versionDate": "2025-12-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-07T17:48:30Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6605ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to report on the use of unmanned aircraft systems and on systems developed to counter such unmanned aircraft systems by Federal, State, local, and Tribal agencies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:25Z"
    },
    {
      "title": "Secure Our Skies Drone Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Our Skies Drone Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```
