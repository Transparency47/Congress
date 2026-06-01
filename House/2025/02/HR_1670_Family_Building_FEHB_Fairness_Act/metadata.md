# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1670
- Title: Family Building FEHB Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 1670
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-12-06T07:00:17Z
- Update date including text: 2025-12-06T07:00:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-16 17:16:45 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1670, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-16 17:16:45 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1670, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1670",
    "number": "1670",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Family Building FEHB Fairness Act",
    "type": "HR",
    "updateDate": "2025-12-06T07:00:17Z",
    "updateDateIncludingText": "2025-12-06T07:00:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2025-09-16",
      "actionTime": "17:16:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1670, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1670ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1670\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Connolly (for himself, Ms. Norton , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require Federal employee health benefit plans to include assisted reproductive treatment benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family Building FEHB Fairness Act .\n#### 2. Fertility treatment benefits\n##### (a) In general\nSection 8904 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by adding at the end the following new subparagraph:\n(G) Fertility treatment benefits. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(ii)**\nby inserting after subparagraph (E) the following new subparagraph:\n(F) Fertility treatment benefits. ; and\n**(2)**\nby adding at the end the following new subsection:\n(c) In this section, the term fertility treatment means\u2014 (1) preservation of human oocytes, sperm, or embryos for later reproductive use; (2) artificial insemination, including intravaginal insemination, intracervical insemination, and intrauterine insemination; (3) assisted reproductive technology, including in vitro fertilization and other treatments or procedures in which reproductive genetic material, such as oocytes, sperm, fertilized eggs, and embryos, are handled, when clinically appropriate; (4) genetic testing of embryos; (5) medications prescribed or obtained over-the-counter, as indicated for fertility; (6) gamete donation; and (7) such other information, referrals, treatments, procedures, medications, laboratory services, technologies, and services relating to fertility as the Director of the Office of Personnel Management, in coordination with the Secretary of Health and Human Services, determines appropriate. .\n##### (b) Effective date\nThe amendments made by this Act shall take effect on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "797",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Family Building FEHB Fairness Act",
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
            "name": "Family planning and birth control",
            "updateDate": "2025-09-02T17:47:15Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-09-02T17:47:11Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-09-02T17:47:19Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-09-02T17:47:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-28T11:19:56Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1670ih.xml"
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
      "title": "Family Building FEHB Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Family Building FEHB Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Federal employee health benefit plans to include assisted reproductive treatment benefits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:43Z"
    }
  ]
}
```
