# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8203
- Title: Workforce Recovery and Resilience Act
- Congress: 119
- Bill type: HR
- Bill number: 8203
- Origin chamber: House
- Introduced date: 2026-04-06
- Update date: 2026-05-01T12:42:01Z
- Update date including text: 2026-05-01T12:42:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-06: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-06: Introduced in House

## Actions

- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-06",
    "latestAction": {
      "actionDate": "2026-04-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8203",
    "number": "8203",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Workforce Recovery and Resilience Act",
    "type": "HR",
    "updateDate": "2026-05-01T12:42:01Z",
    "updateDateIncludingText": "2026-05-01T12:42:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-06",
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
      "actionDate": "2026-04-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-06",
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
          "date": "2026-04-06T14:01:30Z",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8203ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8203\nIN THE HOUSE OF REPRESENTATIVES\nApril 6, 2026 Mr. Mackenzie (for himself and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to provide to States and local areas information on the best practices for addressing the effects that substance use disorder has on the workforce, and to provide local areas with grants to provide training activities related to the treatment and prevention of substance use disorder.\n#### 1. Short title\nThis Act may be cited as the Workforce Recovery and Resilience Act .\n#### 2. Technical assistance\nSection 168 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3223 ) is amended by adding at the end the following:\n(d) Communities impacted by substance use disorders The Secretary shall, as part of the activities described in subsection (c)(2), evaluate and disseminate to States and local areas information regarding evidence-based and promising practices for addressing the economic and workforce impacts associated with high rates of substance use disorders, which information shall\u2014 (1) be updated annually to reflect the most recent and available research; and (2) include information\u2014 (A) shared by States and local areas regarding effective practices for addressing such impacts; and (B) on how to apply for any funding that may be available under section 170(b)(1)(E). .\n#### 3. National dislocated worker grants\nSection 170 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3225 ) is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D)(ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) to an entity described in subsection (c)(1)(B) to provide employment and training activities related to the prevention and treatment of substance use disorders, including addiction treatment, mental health treatment, and pain management, in an area that, as a result of widespread substance use, addiction, and overdoses, has higher-than-average demand for such activities that exceeds the availability of State and local resources to provide such activities. ; and\n**(2)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(B)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively; and\n**(C)**\nby inserting after subparagraph (B) the following:\n(C) Substance use related grants In order to be eligible to receive employment and training assistance under a national dislocated worker grant awarded pursuant to subsection (b)(1)(E), an individual shall be\u2014 (i) a dislocated worker; (ii) a long-term unemployed individual; (iii) an individual who is unemployed or significantly underemployed as a result of widespread substance use in the area; or (iv) an individual who is employed or seeking employment in a health care profession involved in the prevention and treatment of substance use disorders, including such professions that provide addiction treatment, mental health treatment, or pain management. .",
      "versionDate": "2026-04-06",
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
        "actionDate": "2026-04-21",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 14."
      },
      "number": "8210",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A Stronger Workforce for America Act of 2026",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-30T20:50:25Z"
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
      "date": "2026-04-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8203ih.xml"
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
      "title": "Workforce Recovery and Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Workforce Recovery and Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Workforce Innovation and Opportunity Act to provide to States and local areas information on the best practices for addressing the effects that substance use disorder has on the workforce, and to provide local areas with grants to provide training activities related to the treatment and prevention of substance use disorder.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T04:48:24Z"
    }
  ]
}
```
