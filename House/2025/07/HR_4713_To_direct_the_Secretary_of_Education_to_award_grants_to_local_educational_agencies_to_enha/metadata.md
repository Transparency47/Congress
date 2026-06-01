# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4713
- Title: Safe Schools and Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4713
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-09-16T17:50:44Z
- Update date including text: 2025-09-16T17:50:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4713",
    "number": "4713",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Safe Schools and Communities Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-16T17:50:44Z",
    "updateDateIncludingText": "2025-09-16T17:50:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:13:25Z",
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
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4713ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4713\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Nunn of Iowa (for himself and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to award grants to local educational agencies to enhance school and community safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Schools and Communities Act of 2025 .\n#### 2. Grant program for training\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall award, on a competitive basis, grants to local educational agencies to carry out the activities described in subsection (c).\n##### (b) Application\nA local educational agency desiring a grant under this section shall submit to the Secretary an application at such time, in such form, and containing such information as the Secretary may require.\n##### (c) Grant uses\nA local educational agency that receives a grant under this section shall use such grant funds to\u2014\n**(1)**\nprovide, to school personnel who work at elementary schools and secondary schools served by such agency and who are in contact with students on at least a weekly basis, training on\u2014\n**(A)**\nhuman trafficking risk factors, indicators, and protocols;\n**(B)**\nfentanyl and drug abuse prevention;\n**(C)**\nstrategies to prevent, intervene, and reduce participation of students in gang activity; and\n**(D)**\nlocal and community resources for the prevention and intervention described in subparagraphs (B) and (C).\n**(2)**\ncover the costs of providing such training, including with respect to instructor and program fees, training supplies, and educational materials; and\n**(3)**\nimplement\u2014\n**(A)**\nspecialized human trafficking curriculum;\n**(B)**\nfentanyl and drug abuse prevention instruction or materials; or\n**(C)**\ngang education and prevention programs.\n##### (d) ESEA terms\nThe terms elementary school , local educational agency , secondary school , and Secretary have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n##### (e) Funding\nSection 4103(a)(3) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7113(a)(3) ) is amended\u2014\n**(1)**\nby striking technical assistance and inserting\n(A) technical assistance ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(B) awarding grants under the Safe Schools and Communities Act of 2025 . .",
      "versionDate": "2025-07-23",
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
        "name": "Education",
        "updateDate": "2025-09-16T17:50:44Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4713ih.xml"
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
      "title": "Safe Schools and Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Schools and Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to award grants to local educational agencies to enhance school and community safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:49:02Z"
    }
  ]
}
```
