# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6026
- Title: To direct the Secretary of Veterans Affairs and the Secretary of Education to submit a report on the availability, accessibility, and affordability of childcare for veteran families.
- Congress: 119
- Bill type: HR
- Bill number: 6026
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-24T09:05:20Z
- Update date including text: 2025-12-24T09:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6026",
    "number": "6026",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To direct the Secretary of Veterans Affairs and the Secretary of Education to submit a report on the availability, accessibility, and affordability of childcare for veteran families.",
    "type": "HR",
    "updateDate": "2025-12-24T09:05:20Z",
    "updateDateIncludingText": "2025-12-24T09:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:30:05Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-12T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "IA"
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
      "sponsorshipDate": "2025-12-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6026ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6026\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Gottheimer (for himself and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Veterans Affairs and the Secretary of Education to submit a report on the availability, accessibility, and affordability of childcare for veteran families.\n#### 1. Department of Veterans Affairs and Department of Education joint report on childcare for veteran families\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans and the Secretary of Education shall submit to Congress a joint report on the availability, accessability, and affordability of childcare for veteran families. Such report shall include\u2014\n**(1)**\nan assessment of childcare options available to veteran families as of the date of the submission of the report;\n**(2)**\nan identification of gaps in childcare options for veteran families; and\n**(3)**\nan evaluation of barriers to childcare for veteran families, including\u2014\n**(A)**\ncost;\n**(B)**\ngeographic distance; and\n**(C)**\neligibility criteria.\n##### (b) Veteran family defined\nIn this section, the term veteran family has the meaning given such term in section 2044 of title 38, United States Code.",
      "versionDate": "2025-11-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:22:59Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6026ih.xml"
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
      "title": "To direct the Secretary of Veterans Affairs and the Secretary of Education to submit a report on the availability, accessibility, and affordability of childcare for veteran families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T10:18:24Z"
    },
    {
      "title": "To direct the Secretary of Veterans Affairs and the Secretary of Education to submit a report on the availability, accessibility, and affordability of childcare for veteran families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:05:30Z"
    }
  ]
}
```
