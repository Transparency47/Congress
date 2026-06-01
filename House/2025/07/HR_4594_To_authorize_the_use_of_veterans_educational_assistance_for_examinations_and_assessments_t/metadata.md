# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4594
- Title: Military Learning for Credit Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4594
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2026-03-27T08:06:49Z
- Update date including text: 2026-03-27T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4594",
    "number": "4594",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000604",
        "district": "2",
        "firstName": "Maggie",
        "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
        "lastName": "Goodlander",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Military Learning for Credit Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:49Z",
    "updateDateIncludingText": "2026-03-27T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-07-22",
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
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:04:00Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NH"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AZ"
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
      "sponsorshipDate": "2025-08-08",
      "state": "PA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "MI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4594ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4594\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Ms. Goodlander (for herself, Ms. Stefanik , Mr. Pappas , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo authorize the use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Learning for Credit Act of 2025 .\n#### 2. Authority for use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning\n##### (a) In general\nAn individual who is entitled to veterans educational assistance may use such assistance to cover the costs of covered examinations and assessments to receive credit toward degrees awarded by institutions of higher learning for approved programs of education.\n##### (b) Veterans educational assistance\nFor purposes of this section, veterans educational assistance is educational assistance available to veterans and other eligible individuals under the provisions of law as follows:\n**(1)**\nChapters 30, 32, 33, 34, and 35 of title 38, United States Code.\n**(2)**\nAny other provision of law providing educational assistance to a veteran, or to another individual in connection with the service of a veteran in the Armed Forces.\n##### (c) Limitation on amount usable\nThe total amount of veterans educational assistance that may be used for the costs of a covered examination or assessment under subsection (a) may not exceed the lesser of\u2014\n**(1)**\nthe amount charged for the examination or assessment by the entity administering the examination or assessment; or\n**(2)**\n$500.\n##### (d) Charge against entitlement\n**(1) In general**\nThe number of months (or fraction thereof) of entitlement charged an individual under the applicable provision of law specified in subsection (b) for use of veterans educational assistance for costs of covered examinations and assessments under this section shall be equal to the quotient obtained by dividing\u2014\n**(A)**\nthe cost of the examination or assessment (as determined pursuant to subsection (c)); by\n**(B)**\nthe monthly rate of veterans educational assistance to which the individual is entitled under such provision of law at the time of the examination or assessment.\n**(2) Rule of construction**\nA charge against entitlement to educational assistance under a law administered by the Secretary of Veterans Affairs in order to receive assistance under this section shall not be construed to affect entitlement to educational assistance under a law administered by the Secretary of Defense, including entitlement to educational assistance under the Department of Defense Tuition Assistance Program.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe term approved program of education means a program of education approved for use of veterans educational assistance pursuant to chapter 35 or 36 of title 38, United States Code, or another applicable provision of law.\n**(2)**\nThe term covered examinations and assessments means the following:\n**(A)**\nA DANTES Subject Standardized Test Program (DSST) examination.\n**(B)**\nA College Level Examination Program (CLEP) examination.\n**(C)**\nThe National Career Readiness Certificate examination.\n**(D)**\nAny other examination of a similar nature to an exam specified in subparagraph (A), (B), or (C) specified by the Secretary of Veterans Affairs for purposes of this section.\n**(E)**\nAn assessment by an institution of higher learning of a portfolio or written narrative by a student with supporting documentation that demonstrates prior military training or learning.\n**(3)**\nThe term institution of higher learning has the meaning given such term in section 3452(f) of title 38, United States Code.",
      "versionDate": "2025-07-22",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-18",
        "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "2328",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Military Learning for Credit Act of 2025",
      "type": "S"
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
            "name": "Higher education",
            "updateDate": "2026-01-09T16:22:41Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-01-09T16:22:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-01T15:17:15Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4594ih.xml"
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
      "title": "Military Learning for Credit Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military Learning for Credit Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:24Z"
    }
  ]
}
```
